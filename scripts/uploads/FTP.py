def do(addr, user, password, source_directory, target_directory='/', additional_cmd=''):
    logs = []
    logs.append("[INFO] Uploading to %s ..." % addr)
    import os
    source_directory = source_directory.rstrip(os.sep)
    target = target_directory.rstrip('/') + '/' + os.path.basename(source_directory)
    lftp_cmd = """
%(additional_cmd)s
open -u %(user)s,%(password)s %(addr)s
mirror -R %(source)s %(target)s
""" % {'addr': addr, 'user': user, 'password': password,
       'source': source_directory, 'target': target,
       'additional_cmd': additional_cmd }
    with open("/tmp/lftp_script", "w") as f:
        f.write(lftp_cmd)
    os.system("lftp -f /tmp/lftp_script")
    os.system("rm -f /tmp/lftp_script")
    logs.append("[INFO] ... done.")
    return '\n'.join(logs)
