import hashlib
import os
import shutil
import time
from tqdm import tqdm
import sh
from celery import shared_task
from django.core.management import BaseCommand
a = False
b = False
c = False


@shared_task()
def task1():
    global a
    print('____________________1____________________')
    a = True

@shared_task()
def task2():
    global b
    print('_____________________2___________________')
    b = True

@shared_task()
def task3():
    global c
    print('_____________________3___________________')
    c = True

@shared_task()
def task4():
    global a
    global b
    global c
    while a and b and c:
        print('_________________ Stage1 _____ Sozdaem Direktoriu:  dir_temp i cloniruem tuda  __________________')
        filepath = 'dir_temp'
        filepath1 = 'dir_temp/nitpick/all.toml'
        filepath2 = 'result.txt'

        if os.path.isdir(
                filepath):  ## Создали дериктори
            print('Есть директория: dir_temp')
        else:
            os.mkdir(filepath)
            time.sleep(1)
            print('Клонируем из репозитория')
            sh.git.clone('https://gitea.radium.group/radium/project-configuration', filepath)
        #     #############################
        #
        # print('_________________ Stage2 _______________________')  # sha256 dir_temp/nitpick/all.toml
        print('Собираем хэши всех файлов хед-директория в список Result, который переносим в ткст файл result.txt')
        #
        # import hashlib
        #
        # # m = hashlib.sha256()
        # #
        # # m.update(b"Nobody inspects")
        # #
        # # m.update(b" the spammish repetition")
        # #
        # # m.digest()
        # # b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
        # #
        # # m.hexdigest()
        # #############################3
        # import io, hashlib, hmac
        #
        # # with open(hashlib.__file__, "rb") as f:
        # # digest = hashlib.file_digest(f, "sha256")
        # # digest.hexdigest()
        # with open(filepath1, "rb") as f:
        #     content = f.read()
        #     sha256 = hashlib.sha256()
        #     sha256.update(content)
        #     print('Result1 of stage2:')
        #     print(f'{sha256.name}, {sha256.hexdigest()}')
        # ############################## Stage 3 ###################  soberem vse files iz filepath1='dir_temp/nitpick/ s hashem v spisok Result'
        Result = []
        path = next(os.walk(filepath))[1][0]  ###Dostaem name of head directory in filepath
        # print(path)

        walker = os.walk(filepath)
        # print('===============', walker)
        # for walk in walker:
        #     print('======================')
        #     print(walk)
        for folder, sub_folder, files in walker:## Worker красоту не поддерживает, если через коммандный файл запускать, то можно обернуть tqdm()
            # time.sleep(1)
            for file in files:
                file_path = os.path.join(folder, file)
                file_hash = hashlib.sha256(open(file_path, 'rb').read()).hexdigest()
                Result.append(file_hash)

            # print(Result)
            with open(filepath2, 'w+') as f:
                for i in Result:
                    f.write(i + '\n')

        ################################### Stage3 Deleting ######################
        print(
            "Через 12 секунд удалим временную папку и все в ней, останется только result.txt файл в корневом директории с хэшами файлов.................")
        time.sleep(12)  ##Cherez 120 sec udalyaem
        # rm_r(filepath)
        print(
            "Удаляем временную папку и все в ней, останется только result.txt файл в корневом директории с хэшами файлов.................")
        if not os.path.exists(filepath):
            return
        if os.path.isfile(filepath) or os.path.islink(filepath):
            os.unlink(filepath)
        else:
            shutil.rmtree(filepath)
        a = False
        b = False
        c = False


