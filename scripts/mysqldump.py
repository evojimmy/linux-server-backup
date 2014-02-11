# Actual work that dumps MySQL database
def do(user, password, outpath):
    log = []

    cmd = 'mysqldump -u%s -p%s --all-databases > /tmp/mysql.sql' % (user, password)
    import subprocess, os
    try:
        subprocess.check_output(cmd, shell=True)
        cmd = 'tar -jcf %s -C /tmp ./mysql.sql' % (outpath + os.sep + 'mysql.tar.bz2') # bz2 saves bytes
        subprocess.check_output(cmd, shell=True)
        subprocess.check_output('rm /tmp/mysql.sql', shell=True)
    except subprocess.CalledProcessError as e:
        log.append('[SITEBAK-ERR] %s' % str(e))
    log.append('')
    return '\n'.join(log)