import paramiko
import os
import scp
import sys
pwd=str(sys.argv[1])
hosts=str(sys.argv[2])
instance=str(sys.argv[3])
version=str(sys.argv[4])
package_path=os.getcwd()
#package_path=str(sys.argv[5])
pt=str(os.path.join("{}".format(package_path),"target","{}.war".format(version)))
#pt=str(C:\\Program Files (x86)\\Jenkins\\workspace\\folder1\\end2end\\target\\sivamani.war)
ssh=paramiko.SSHClient()
                
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
def ftp(path):
    sftp=ssh.open_sftp()
    sftp.put(path,"/home/mani/tomcat/packages/")
    sftp.close()

for host in hosts.split(","):
    print("conecting to {}".format(host))
    ssh.connect(hostname=host,username="mani",password=pwd)
    ftp(pt)
    stdin,stdout,stderr=ssh.exec_command("sh /home/mani/tomcat/scripts/deploy.sh {} {}".format(instance,version),get_pty=True)
    print(''.join(stdout.readlines()))
