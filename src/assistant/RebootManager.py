import os
from platform import system


class RebootManager:

    """
    Класс для управления перезагрузкой или завершением работы системы.
    """

    # TODO -> модуль speech
    def rebootManager(restart):

        """
        Перезагружает систему или завершает работу в зависимости от переданного параметра.

        Аргументы:
        restart (bool): Если True, система будет перезагружена через 5 секунд.
                         Если False, программа завершит свою работу.

        Возвращает:
        None
        """

        if restart == True:
            os.system("shutdown /r /t 5")
        else:
            exit()


if __name__ == "__main__":
    reboot = RebootManager()
    reboot.rebootManager()
