import os
from platform import system


class ShutdownManager:
    """
    Класс для управления выключением системы.

    Этот класс предоставляет метод для выключения операционной системы.
    В текущей реализации он поддерживает только Windows,  нуждается в расширении для других ОС.
    """

    # TODO -> модуль speech
    def shutdownManager(restart):
        """
        Выключает систему или завершает программу.

        Args:
            shutdown (bool, optional): Флаг, указывающий, следует ли выключить систему.
        Если True (по умолчанию), система выключается; иначе программа завершается.
        """

        if restart == True:
            os.system("shutdown /s /t 5")
        else:
            exit()


if __name__ == "__main__":
    reboot = ShutdownManager()
    reboot.shutdownManager()
