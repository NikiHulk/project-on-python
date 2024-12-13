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

        В зависимости от флага `restart`, метод может либо выключить систему с задержкой,
        либо завершить программу.

        Args:
            restart (bool): Флаг, указывающий, следует ли выключить систему.
                             Если True, система будет выключена; если False, программа завершится.

        Raises:
            OSError: Если операционная система не поддерживается для выключения, например, Linux или macOS.
            OSError: Если операционная система неизвестна.

        Example:
            shutdownManager(True)  # Выключить систему.
            shutdownManager(False)  # Завершить программу.
        """

        platform = system().lower()  # Получаем имя операционной системы в нижнем регистре

        if platform == 'windows':
            if restart:
                os.system("shutdown /s /t 5")  # Выключение Windows с задержкой 5 секунд
            else:
                exit()  # Завершаем программу

        elif platform == 'linux' or platform == 'darwin':
            raise OSError(f"Операционная система {platform} не поддерживается для выключения.")

        else:
            raise OSError("Неподдерживаемая операционная система.")
