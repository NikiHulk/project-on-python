import comtypes
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume

class VolumeManager:

    """
    Класс для управления громкостью системы.

    Этот класс предоставляет методы для регулировки громкости, получения текущего уровня громкости,
    установки нужного уровня громкости, а также включения/выключения звука.

    Методы:
        GetVolumeController(): Возвращает объект контроллера громкости.
        AdjustVolume(adjustment): Регулирует громкость на заданное значение (положительное - увеличить, отрицательное - уменьшить).
        GetVolume(): Возвращает текущий уровень громкости в процентах (0-100).
        SetVolume(level): Устанавливает уровень громкости в процентах (0-100).
        mute(): Включает или выключает звук.
        IsMuted(): Проверяет, выключен ли звук, возвращает True если звук выключен, иначе False.
    """

    def __init__(self):

        """
        Конструктор для инициализации объекта VolumeManager.
        При инициализации автоматически получает контроллер громкости.
        """

        self.volume = self.GetVolumeController()

    def GetVolumeController(self):

        """
        Получает и возвращает контроллер громкости для системных динамиков.

        Возвращает:
            IAudioEndpointVolume: Контроллер громкости.

        Исключения:
            Если не удается получить контроллер громкости, выводится сообщение об ошибке.
        """

        """Получает контроллер громкости."""
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            return comtypes.cast(interface, IAudioEndpointVolume)
        except Exception as e:
            print(f"Ошибка при получении контроллера громкости: {e}")
            return None

    def AdjustVolume(self, adjustment):  #adjustment - число (положительное - увеличить, отрицательное - уменьшить)

        """
        Регулирует громкость на заданное количество.

        Аргументы:
            adjustment (int): Положительное число для увеличения громкости, отрицательное для уменьшения.

        Если контроллер громкости доступен, изменяет текущий уровень громкости.
        Если контроллер недоступен, выводит сообщение об ошибке.
        """

        """Регулирует громкость."""
        if self.volume:
            current_volume = self.GetVolume()
            new_volume = max(0, min(current_volume + adjustment, 100))
            self.SetVolume(new_volume)
        else:
            print("Контроллер громкости недоступен.")

    def GetVolume(self):

        """
        Возвращает текущий уровень громкости в процентах.

        Возвращает:
            int: Уровень громкости в процентах (0-100).
            None: Если контроллер громкости недоступен.
        """

        """Возвращает текущий уровень громкости (0-100)."""
        if self.volume:
            return int(self.volume.GetMasterVolumeLevelScalar()*100)
        else:
            return None

    def SetVolume(self, level):

        """
        Устанавливает уровень громкости.

        Аргументы:
            level (int): Новый уровень громкости (0-100).

        Если контроллер громкости доступен, устанавливает новый уровень громкости.
        Если контроллер недоступен, выводит сообщение об ошибке.
        """

        """Устанавливает уровень громкости (0-100)."""
        if self.volume:
            self.volume.SetMasterVolumeLevelScalar(level/100, None)
        else:
            print("Контроллер громкости недоступен.")

    def mute(self):

        """
        Включает или выключает звук.

        Если контроллер громкости доступен, изменяет состояние звука (включение/выключение).
        Если контроллер недоступен, выводит сообщение об ошибке.
        """

        """Включает/выключает звук."""
        if self.volume:
            is_muted = self.volume.GetMute()
            self.volume.SetMute(not is_muted, None)
        else:
            print("Контроллер громкости недоступен.")

    def IsMuted(self):

        """
        Проверяет, выключен ли звук.

        Возвращает:
            bool: True, если звук выключен; False, если звук включен.
            None: Если контроллер громкости недоступен.
        """

        """Возвращает True, если звук отключен, иначе False."""
        if self.volume:
            return self.volume.GetMute()
        else:
            return None
