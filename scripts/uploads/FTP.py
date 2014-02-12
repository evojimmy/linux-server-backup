def do(addr, user, password, source_directory, target_directory='/'):
    logs = []
    logs.append("[INFO] Uploading to %s ..." % addr)
    import os
    lftp_cmd = """
open -u %(user)s,%(password)s %(addr)s
mirror -R %(source)s %(target)s
""" % {'addr': addr, 'user': user, 'password': password,
       'source': source_directory, 'target': target_directory}
    with open("/tmp/lftp_script", "w") as f:
        f.write(lftp_cmd)
    os.system("lftp -f /tmp/lftp_script")
    os.system("rm -f /tmp/lftp_script")
    logs.append("[INFO] ... done.")
    return '\n'.join(logs)
