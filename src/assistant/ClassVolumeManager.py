import comtypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume

class VolumeManager:
    """
    Класс для управления громкостью системы.
    Атрибуты:
        volume (IAudioEndpointVolume): Объект для управления громкостью.  Может быть None, если не удалось получить контроллер.
    Методы:
            GetVolumeController(): Получает контроллер громкости системы.
            AdjustVolume(adjustment): Регулирует громкость на заданное значение.
            GetVolume(): Возвращает текущий уровень громкости (0-100).
            SetVolume(level): Устанавливает уровень громкости (0-100).
            mute(): Включает/выключает беззвучный режим.
            IsMuted(): Возвращает True, если звук отключен, иначе False.
    """

    def __init__(self):
        self.volume = self.GetVolumeController()

    def GetVolumeController(self):
        """Получает контроллер громкости.
        Returns:
            IAudioEndpointVolume: Объект для управления громкостью, или None при ошибке.
        """
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            return comtypes.cast(interface, IAudioEndpointVolume)
        except Exception as e:
            print(f"Ошибка при получении контроллера громкости: {e}")
            return None

    def AdjustVolume(self, adjustment):  #adjustment - число (положительное - увеличить, отрицательное - уменьшить)
        """Регулирует громкость системы.
        Args:
            adjustment (int): Значение регулировки громкости. Положительное значение увеличивает громкость, отрицательное уменьшает.
        Returns:
            None.
        """
        if self.volume:
            current_volume = self.GetVolume()
            new_volume = max(0, min(current_volume + adjustment, 100))
            self.SetVolume(new_volume)
        else:
            print("Контроллер громкости недоступен.")

    def GetVolume(self):
        """Возвращает текущий уровень громкости (0-100).
        Returns:
            int: Текущий уровень громкости, или None, если контроллер громкости недоступен.
        """
        if self.volume:
            return int(self.volume.GetMasterVolumeLevelScalar()*100)
        else:
            return None

    def SetVolume(self, level):
        """Устанавливает уровень громкости (0-100).
        Args:
            level (int): Уровень громкости (0-100).

        Returns:
            None.
        """
        if self.volume:
            self.volume.SetMasterVolumeLevelScalar(level/100, None)
        else:
            print("Контроллер громкости недоступен.")

    def mute(self):
        """Включает/выключает звук.
        Returns:
            None.
        """
        if self.volume:
            is_muted = self.volume.GetMute()
            self.volume.SetMute(not is_muted, None)
        else:
            print("Контроллер громкости недоступен.")

    def IsMuted(self):
        """Возвращает True, если звук отключен, иначе False.
        Returns:
            bool: True, если звук отключен, False - в противном случае, или None, если контроллер громкости недоступен.
        """
        if self.volume:
            return self.volume.GetMute()
        else:
            return None
