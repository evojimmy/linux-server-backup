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
            log.append('[SITEBAK-WARN] Ignore non-existing path: %s' % f)

    cmd = 'tar -%scf %s%s%s.tar%s %s' % (tar_param, outpath, os.sep, name, compress_type, ' '.join(files))
    try:
        subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError as e:
        log.append('[SITEBAK-ERR] %s' % str(e))

    log.append('')
    return '\n'.join(log)