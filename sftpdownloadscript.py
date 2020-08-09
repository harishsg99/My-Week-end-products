import pysftp as sftp
import sys
hostname=sys.argv[1]
username=sys.argv[2]
password=sys.argv[3]
remotepath1=sys.argv[4]
localpath1=sys.argv[5]
def sftpExample():
	try:
		s = sftp.Connection(hostname,username,password)
        s.get(remotepath1,localpath1, preserve_mtime=True)
        s.close()
    except Exception, e:
		print str(e)

sftpExample()
