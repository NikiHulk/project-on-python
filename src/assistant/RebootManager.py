import os
from platform import system


class RebootManager:
    # TODO -> модуль speech
    def rebootManager(restart):
        if restart == True:
            os.system("shutdown /r /t 5")
        else:
            exit()


if __name__ == "__main__":
    reboot = RebootManager()
    reboot.rebootManager()
