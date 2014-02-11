#!/bin/sh

# Argument validation from http://stackoverflow.com/questions/699576/validating-parameters-to-a-bash-script
die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"


while [ "true" ]
do
    echo "[INFO] Wait $1 seconds for next backup. Start sleeping now..."
    sleep $1
    echo $(python -c "from time import strftime;print '[INFO] Automatically starting backup at %s...' % strftime('%Y-%m-%d %H:%M:%S')")
    (cd . && ./immediate_backup.py)
    echo "[INFO] Backup finished."
done
