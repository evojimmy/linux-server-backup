#!/bin/sh

start() {
    echo "Starting routine backup: "

    instance=$(getinstance)
    if [ -z $instance ]; then
        touch $LOGFILE
        echo "================================" >> $LOGFILE
        echo $(python -c "from time import strftime;print '[INFO] Starting background routine at %s' % strftime('%Y-%m-%d %H:%M:%S')") >> $LOGFILE
        DAYS=`python -c "import config;d=config.ROUTINE_DAYS if 'ROUTINE_DAYS' in config.__dict__ else 7;print d"`
        SECONDS=`echo "${DAYS} * 24 * 60 * 60" | bc`
        nohup $WORKER ${SECONDS} >> $LOGFILE 2>&1 &
        echo "done. PID: $!"
    else
        echo "Background routine has already been started. PID: $instance"
        echo "Please check $LOGFILE for latest message."
    fi
}

stop() {
    echo $(python -c "from time import strftime;print '[INFO] Stopping background routine at %s' % strftime('%Y-%m-%d %H:%M:%S')") >> $LOGFILE
    instance=$(getinstance)
    if [ ! -z $instance ]; then
        echo "Stopping routine backup. PID: $instance"
        kill -9 $instance || true;
    else
        echo "Stopped."
    fi
}

status() {
    instance=$(getinstance)
    if [ ! -z $instance ]; then
        echo "Running. PID: $instance"
    else
        echo "Stopped."
    fi
}

usage() {
    N=$(basename "$0")
    echo "Usage: $N {start|stop|status|restart}" >&2
    exit 1
}

getinstance() {
    for pid in `ps | grep routine_worker | cut -f2 -d ' '`; do
        if [ ! -z $(isauthentic $pid) ]; then
            echo $pid;
            exit;
        fi
    done
}

isauthentic() {
    pid=$1
    cmdline=`cat /proc/$pid/cmdline | tr "\0" "\n" | grep "$WORKER"`
    if [ ! -z $cmdline ]; then
        echo $pid;
    fi
}


# set global envs

DIR=$(python -c "import os; print os.path.dirname(os.path.realpath('$0'))")
cd $DIR
#echo $DIR

WORKER="$DIR/scripts/routine_worker.sh"
#echo $WORKER

LOGFILE="$DIR/routine_backup.log"
#echo $LOGFILE

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
