#!/bin/sh

start() {
    echo "Starting routine backup: "
    if [ ! -f /tmp/routine_backup.pid ]; then
        touch routine_backup.log
        echo "================================" >> routine_backup.log
        echo $(python -c "from time import strftime;print '[INFO] Starting background routine at %s' % strftime('%Y-%m-%d %H:%M:%S')") >> ./routine_backup.log
        DAYS=`python -c "import config;d=config.ROUTINE_DAYS if 'ROUTINE_DAYS' in config.__dict__ else 7;print d"`
        SECONDS=`echo "${DAYS} * 24 * 60 * 60" | bc`
        nohup ./scripts/routine_worker.sh ${SECONDS} >> ./routine_backup.log 2>&1 &
        echo $! > /tmp/routine_backup.pid
        echo "done."
    else
        echo "Background routine has already been started."
        echo "Please check routine_backup.log for latest message."
    fi
}

stop() {
    echo $(python -c "from time import strftime;print '[INFO] Stopping background routine at %s' % strftime('%Y-%m-%d %H:%M:%S')") >> ./routine_backup.log
    echo "Stopping routine backup: "
    kill -9 `cat /tmp/routine_backup.pid` || true
    rm -f /tmp/routine_backup.pid
    echo "done."
}

status() {
    if [ -f /tmp/routine_backup.pid ]; then
        echo "Running. PID: `cat /tmp/routine_backup.pid`"
        echo ""
        echo "Latest logs:"
        tail -n 10 routine_backup.log
    else
        echo "Stopped."
    fi
}

usage() {
    N=$(basename "$0")
    echo "Usage: $N {start|stop|status|restart}" >&2
    exit 1
}

cd $(python -c "import os; print os.path.dirname(os.path.realpath('$0'))")

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    status)
        status
        ;;
    restart)
        stop
        start
        ;;
    *)
        usage
        ;;
esac

exit 0
