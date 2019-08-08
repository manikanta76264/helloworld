import paramiko
import scp
import sys
pwd=str(sys.argv[1])
hosts=str(sys.argv[2])
instance=str(sys.argv[3])
version=str(sys.argv[4])
package_path=str(sys.argv[5])
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def ftp(path):
	sftp=ssh.open_sftp()
	sftp.put(path "/home/mani/tomcat/packages/")
	sftp.close()

for host in hosts.split(","):
	print("conecting to {}".format(host))
	ssh.connect(hostname=host,username="mani",password=pwd)
	ftp(package_path)
    stdin,stdout,stderr=ssh.exec_command("sh /home/mani/tomcat/scripts/deploy.sh {} {}".format(instance,version),get_pty=True)
    print(''.join(stdout.readlines()))