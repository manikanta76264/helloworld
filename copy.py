import shutil
import os
fil=os.listdir('C:\\Program Files (x86)\\Jenkins\workspace\\maven_git_pipeline\\target')
if fil endswith('*.war'):
    shutil.copy(fil,'C:\\Program Files\\Apache Software Foundation\\Tomcat 8.0\\webapps')
    print("done manikanta")
