import os
import sh
from django.core.management import BaseCommand

import kronos

@kronos.register('0 * * * *')
def task1():
    pass


def test1(self, *args, **options):
    print('________________________________________')
    filepath = 'dir_temp'
        #
    if os.path.isdir(
            filepath):  ## Создали дериктори
        print('Есть директория: dir_temp')
    else:
        os.mkdir(filepath)
        sh.git.clone('https://gitea.radium.group/radium/project-configuration', filepath)


import subprocess
# import datetime
import gzip
from django.core.management.base import BaseCommand


# execute_backup()
#
# FILE_NAME = 'some_file_name.sql'
# ARCHIVE_NAME = 'some_archive_name.gz'
# REPO_NAME    = 'some_repo_name'
# GIT_USER = 'some_git_username' # You'll need to change this in .netrc as well.
# MYSQL_USER   = 'some_mysql_user'
# MYSQL_PASS   = 'some_mysql_pass'
# DATABASE_TO_DUMP = 'SomeDatabase' # You can use --all-databases but be careful with it! It will dump everything!.

# def dump_dbs_to_gzip():
#     # Dump arguments.
#     args = [
#         'mysqldump', '-u', MYSQL_USER, '-p%s' % (MYSQL_PASS),
#         '--add-drop-database',
#         DATABASE_TO_DUMP,
#     ]
#     # Dump to file.
#     dump_file = open(FILE_NAME, 'w')
#     mysqldump_process = subprocess.Popen(args, stdout=dump_file)
#     retcode = mysqldump_process.wait()
#     dump_file.close()
#     if retcode > 0:
#         print('Back-up error')
#     # Compress.
#     sql_file = open(FILE_NAME, 'r')
#     gz_file = gzip.open(ARCHIVE_NAME, 'wb')
#     gz_file.writelines(sql_file)
#     gz_file.close()
#     sql_file.close()
#     # Delete the original file.
#     sh.rm('-f', FILE_NAME)

def clone_repo():
    # Set the repository location.
    repo_origin = 'https://%s@bitbucket.org/%s/%s.git' % (GIT_USER, GIT_USER, REPO_NAME)

    # Clone the repository in the /tmp folder.
    sh.cd('/tmp')
    sh.rm('-rf', REPO_NAME)
    sh.git.clone(repo_origin)
    sh.cd(REPO_NAME)


def commit_and_push():
    # Commit and push.
    sh.git.add('.')
    sh.git.commit(m=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    sh.git.push('origin', 'master')
    sh.cd('..')
    sh.rm('-rf', REPO_NAME)


def execute_backup():
    clone_repo()
    dump_dbs_to_gzip()
    commit_and_push()


if __name__ == "__main__":
    execute_backup()
