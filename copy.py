import shutil
import os
files=os.listdir('C:\\Program Files (x86)\\Jenkins\workspace\\maven_git_pipeline\\target')
for source in files:
    if source=='*.war':
        shutil.copy(source,'C:\\Program Files\\Apache Software Foundation\\Tomcat 8.0\\webapps')
        print("done manikanta")
