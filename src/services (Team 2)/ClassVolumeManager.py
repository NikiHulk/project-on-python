import comtypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeManager:
    def __init__(self):
        self.volume = self.GetVolumeController()

    def GetVolumeController(self):
        """Получает контроллер громкости."""
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            return comtypes.cast(interface, IAudioEndpointVolume)
        except Exception as e:
            print(f"Ошибка при получении контроллера громкости: {e}")
            return None

    def AdjustVolume(self, adjustment):  #adjustment - число (положительное - увеличить, отрицательное - уменьшить)
        """Регулирует громкость."""
        if self.volume:
            current_volume = self.GetVolume()
            new_volume = max(0, min(current_volume + adjustment, 100))
            self.SetVolume(new_volume)
        else:
            print("Контроллер громкости недоступен.")

    def GetVolume(self):
        """Возвращает текущий уровень громкости (0-100)."""
        if self.volume:
            return int(self.volume.GetMasterVolumeLevelScalar()*100)
        else:
            return None

    def SetVolume(self, level):
        """Устанавливает уровень громкости (0-100)."""
        if self.volume:
            self.volume.SetMasterVolumeLevelScalar(level/100, None)
        else:
            print("Контроллер громкости недоступен.")

    def mute(self):
        """Включает/выключает звук."""
        if self.volume:
            is_muted = self.volume.GetMute()
            self.volume.SetMute(not is_muted, None)
        else:
            print("Контроллер громкости недоступен.")

    def IsMuted(self):
        """Возвращает True, если звук отключен, иначе False."""
        if self.volume:
            return self.volume.GetMute()
        else:
            return None
