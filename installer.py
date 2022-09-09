#clone git repo into .overwatch
#install node deps
#install py deps
import os
import sys
import subprocess
if __name__ == "__main__":
    path = os.getcwd()
    subprocess.run(['git', 'clone', 'https://github.com/giannicrivello/overwatch.git'])
    os.chdir('overwatch')
    subprocess.run(['npm', 'i', 'package.json'])
    os.chdir('../')
    sys.exit()
