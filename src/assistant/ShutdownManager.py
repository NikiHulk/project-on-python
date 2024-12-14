import os
from platform import system


class ShutdownManager:

    """
    Класс для управления выключением или перезагрузкой системы.
    """


    # TODO -> модуль speech
    def shutdownManager(restart):

        """
        Осуществляет выключение или перезагрузку системы в зависимости от аргумента.

        Аргументы:
        restart (bool): Если True, выполняется перезагрузка системы, если False — завершение работы.

        Возвращает:
        None
        """

        if restart == True:
            os.system("shutdown /s /t 5")
        else:
            exit()


if __name__ == "__main__":
    reboot = ShutdownManager()
    reboot.shutdownManager()
