import os
import platform


class RebootManager:
    """
    Класс для управления перезагрузкой системы.

    Этот класс предоставляет метод для перезагрузки операционной системы.
    В текущей реализации поддерживаются операционные системы Windows, Linux и macOS.
    """

    @staticmethod
    def reboot_manager(restart=True):
        """
        Перезагружает систему или завершает программу в зависимости от операционной системы.

        В зависимости от флага `restart`, метод либо перезагружает систему, либо завершает программу.
        Если операционная система не поддерживается (не Windows, Linux или macOS), возникает ошибка.

        Args:
            restart (bool, optional): Флаг, указывающий, следует ли перезагружать систему.
                                      Если True (по умолчанию), система перезагружается.
                                      Если False, программа завершится.

        Raises:
            EnvironmentError: Если операционная система не поддерживается (не Windows, Linux или macOS).
        """
        # Получаем название операционной системы
        system_name = platform.system()

        # Перезагрузка для Windows
        if system_name == "Windows":
            if restart:
                os.system("shutdown /r /t 5")  # Перезагрузка с задержкой 5 секунд
            else:
                exit()

        # Перезагрузка для Linux и macOS (Darwin для macOS)
        elif system_name == "Linux" or system_name == "Darwin":
            if restart:
                os.system("sudo shutdown -r now")  # Для Linux и macOS перезагрузка
            else:
                exit()

        # Если операционная система не поддерживается
        else:
            raise EnvironmentError(f"Поддержка для этой операционной системы ({system_name}) не реализована.")


# Запуск перезагрузки системы при исполнении скрипта
if __name__ == "__main__":
    reboot = RebootManager()
    reboot.reboot_manager(restart=True)
