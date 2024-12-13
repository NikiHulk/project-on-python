import os
from platform import system


class RebootManager:
    """
    Класс для управления перезагрузкой системы.
    Этот класс предоставляет метод для перезагрузки операционной системы.
    В текущей реализации он поддерживает только Windows,  нуждается в расширении для других ОС.
    """

    # TODO -> модуль speech
    def rebootManager(restart):
        """
        Перезагружает систему или завершает программу.
        Args:
            restart (bool, optional): Флаг, указывающий, следует ли перезагрузить систему.
        Если True (по умолчанию), система перезагружается; иначе программа завершается.
        """

        if restart == True:
            os.system("shutdown /r /t 5")
        else:
            exit()


if __name__ == "__main__":
    reboot = RebootManager()
    reboot.rebootManager()
