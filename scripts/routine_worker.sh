#!/bin/sh

# Argument validation from http://stackoverflow.com/questions/699576/validating-parameters-to-a-bash-script
die () {
    echo >&2 "$@"
    exit 1
}

[ "$#" -eq 1 ] || die "1 argument required, $# provided"


while [ "true" ]
do
    echo $(python -c "from time import strftime;print '[SITEBAK-INFO] Wait $1 seconds for next backup. Start sleeping at %s...' % strftime('%Y-%m-%d %H:%M:%S')")
    sleep $1
    echo "[SITEBAK-INFO] Finish sleeping."
    echo $(python -c "from time import strftime;print '[SITEBAK-INFO] Backup automatically starts at %s' % strftime('%Y-%m-%d %H:%M:%S')")
    (cd . && ./immediate_backup.py)
    echo $(python -c "from time import strftime;print '[SITEBAK-INFO] Backup finishes at %s' % strftime('%Y-%m-%d %H:%M:%S')")
done
