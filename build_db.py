import subprocess
import urllib.request
import os

def main():
    urllib.request.urlretrieve('https://raw.githubusercontent.com/theypsilon/DB-Template_MiSTer/main/.github/build_db.py', '/tmp/build_db.py')
    result = subprocess.run(['python3', '/tmp/build_db.py', '-d'], env=os.environ.copy())
    return result.returncode

if __name__ == '__main__':
    exit(main())
