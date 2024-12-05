import os
from platform import system


class RebootManager:
    " --- ( код зависящий от части speech {передача в переменную restart кодового слова да/нет} )"

    # TODO -> модуль speech

    restart = True

    def rebootManager(restart):
        if restart == True:
            os.system("shutdown /s /t 5")
        else:
            exit()