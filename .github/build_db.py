import subprocess
import urllib.request
import os
import sys

def main():
    print('Building database...')

    dryrun = False
    if len(sys.argv) >= 2 and sys.argv[1] == '-d':
        print('Dry run')
        dryrun = True

    db_id = os.getenv('GITHUB_REPOSITORY', 'theypsilon/test')

    if not dryrun:
        subprocess.run(['git', 'config', '--global', 'user.email', 'theypsilon@gmail.com'], check=True)
        subprocess.run(['git', 'config', '--global', 'user.name', 'The CI/CD Bot'], check=True)
        
        cleanup_build_py(db_id)

    urllib.request.urlretrieve('https://raw.githubusercontent.com/MiSTer-devel/Distribution_MiSTer/develop/.github/calculate_db.py', '/tmp/distribution_calculate_db.py')

    db_url = f'https://raw.githubusercontent.com/{db_id}/db/db.json.zip'
    base_files_url = f'https://raw.githubusercontent.com/{db_id}/%s/'

    calculate_env = {
        'DB_ID': db_id,
        'DB_URL': db_url,
        'DB_ZIP_NAME': 'db.json.zip',
        'DB_JSON_NAME': 'db.json',
        'BASE_FILES_URL': base_files_url,
        'LATEST_ZIP_URL': '',
        'CHECK_CHANGED': 'false'
    }

    print('Calculating database with environment:')
    print(calculate_env)

    result = subprocess.run(['python3', '/tmp/distribution_calculate_db.py', '-d'], env=calculate_env)
    if result.returncode != 0:
        print('Error: Failed to build database')
        return 1

    if not dryrun:
        print('Pushing database...')
        subprocess.run(['git', 'checkout', '--orphan','db'], check=True)
        subprocess.run(['git', 'reset'], check=True)
        subprocess.run(['git', 'add', 'db.json.zip'], check=True)
        subprocess.run(['git', 'commit', '-m','Creating database'], check=True)
        subprocess.run(['git', 'push', '--force','origin', 'db'], check=True)

    return 0

def cleanup_build_py(db_id):  
    if db_id.lower().strip() == 'theypsilon/db-template_mister':
        print('Skipping cleanup_build_py')
        return

    needs_commit = False
    if os.path.exists('build_db.py'):
        subprocess.run(['git', 'rm', 'build_db.py'], check=True)
        needs_commit = True

    if os.path.exists('.github/build_db.py'):
        subprocess.run(['git', 'rm', '.github/build_db.py'], check=True)
        needs_commit = True

    if needs_commit:
        subprocess.run(['git', 'commit', '-m','BOT: Cleaning build_db.py'], check=True)
        subprocess.run(['git', 'push'], check=True)

if __name__ == '__main__':
    exit(main())
