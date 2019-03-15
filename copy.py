import shutil
import os
files=os.listdir('C:\\Program Files (x86)\\Jenkins\workspace\\maven_git_pipeline\\target')
if files.endswith('.war'):
    shutil.copy(files,'C:\\Program Files\\Apache Software Foundation\\Tomcat 8.0\\webapps')
    print("done manikanta")
