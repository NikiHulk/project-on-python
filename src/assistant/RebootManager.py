import os
import platform


class RebootManager:
    """
    Класс для управления перезагрузкой системы.
    Этот класс предоставляет метод для перезагрузки операционной системы.
    В текущей реализации он поддерживает Windows, Linux и macOS.
    """

    @staticmethod
    def reboot_manager(restart=True):
        """
        Перезагружает систему или завершает программу в зависимости от операционной системы.

        Args:
            restart (bool, optional): Флаг, указывающий, следует ли перезагружать систему.
            Если True (по умолчанию), система перезагружается; иначе программа завершается.
        """

        system_name = platform.system()

        if system_name == "Windows":
            if restart:
                os.system("shutdown /r /t 5")  # Перезагрузка с задержкой 5 секунд
            else:
                exit()

        elif system_name == "Linux" or system_name == "Darwin":  # macOS использует "Darwin"
            if restart:
                os.system("sudo shutdown -r now")  # Для Linux и macOS перезагрузка
            else:
                exit()

        else:
            raise EnvironmentError(f"Поддержка для этой операционной системы ({system_name}) не реализована.")


if __name__ == "__main__":
    reboot = RebootManager()
    reboot.reboot_manager(restart=True)
