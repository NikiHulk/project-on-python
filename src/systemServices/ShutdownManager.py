import os
from platform import system


class ShutdownManager:
    # TODO -> модуль speech
    def shutdownManager(restart):
        if restart == True:
            os.system("shutdown /s /t 5")
        else:
            exit()


if __name__ == "__main__":
    reboot = ShutdownManager()
    reboot.shutdownManager()
