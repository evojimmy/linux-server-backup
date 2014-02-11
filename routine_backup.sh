#!/bin/sh

start() {
    echo "Starting routine backup: "
    if [ ! -f /tmp/routine_backup.pid ]; then
        touch ./routine_backup.log
        echo $(python -c "from time import strftime;print '[SITEBAK-INFO] Starting routine backup at %s' % strftime('%Y-%m-%d %H:%M:%S')") >> ./routine_backup.log
        DAYS=`python -c "import config;d=config.ROUTINE_DAYS if 'ROUTINE_DAYS' in config.__dict__ else 7;print d"`
        SECONDS=`echo "${DAYS} * 24 * 60 * 60" | bc`
        #echo ${SECONDS}
        nohup ./scripts/routine_worker.sh ${SECONDS} >> ./routine_backup.log 2>&1 &
        echo $! > /tmp/routine_backup.pid
        echo "done."
    else
        echo "Routine backup has already started. Please check routine_backup.log for current status."
    fi
}

stop() {
    echo "Stopping routine backup: "
    kill -9 `cat /tmp/routine_backup.pid` || true
    rm -f /tmp/routine_backup.pid
    echo "done."
    echo $(python -c "from time import strftime;print '[SITEBAK-INFO] Stopped routine backup at %s' % strftime('%Y-%m-%d %H:%M:%S')") >> ./routine_backup.log
}

usage() {
    N=$(basename "$0")
    echo "Usage: $N {start|stop}" >&2
    exit 1
}

cd $(python -c "import os; print os.path.dirname(os.path.realpath('$0'))")

case "$1" in
    # If arg `start` is given, start daemon.
    start)
        start
        ;;
    stop)
        stop
        ;;
    *)
        usage
        ;;
esac

exit 0
