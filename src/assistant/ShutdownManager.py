import os
from platform import system


class ShutdownManager:
    """
    Класс для управления выключением системы.

    Этот класс предоставляет метод для выключения операционной системы.
    В текущей реализации он поддерживает только Windows, нуждается в расширении для других ОС.
    """

    def shutdownManager(restart):
        """
        Выключает систему или завершает программу.

        Args:
            restart (bool): Флаг, указывающий, следует ли выключить систему.
            Если True, система выключается; иначе программа завершится.
        """

        platform = system().lower()  # Получаем имя операционной системы в нижнем регистре

        if platform == 'windows':
            if restart:
                os.system("shutdown /s /t 5")
            else:
                exit()

        elif platform == 'linux' or platform == 'darwin':
            raise OSError(f"Операционная система {platform} не поддерживается для выключения.")

        else:
            raise OSError("Неподдерживаемая операционная система.")
