# create using tar
import os, subprocess

def do(filelist, outpath, name, compress_type=''):
    log = []
    if compress_type == '':
        tar_param = ''
    elif compress_type == 'gz':
        tar_param = 'z'
    elif compress_type == 'bz2':
        tar_param = 'j'
    if compress_type != '':
        compress_type = '.' + compress_type

    files = []
    for f in filelist:
        if os.path.exists(f):
            files.append(f)
        else:
            log.append('[WARN] Ignore non-existing path: %s' % f)

    cmd = 'tar -%scf %s%s%s.tar%s %s' % (tar_param, outpath, os.sep, name, compress_type, ' '.join(files))

    status = os.system(cmd)
    if status != 0:
        log.append('[ERROR] errno=%s when executing %s' % (status, cmd))
    #try:
    #    subprocess.check_output(cmd, shell=True)
    #except subprocess.CalledProcessError as e:
    #    log.append('[ERROR] %s' % str(e))

    return '\n'.join(log)
