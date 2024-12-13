import unittest
from unittest.mock import patch
from src import RebootManager


class TestRebootManager(unittest.TestCase):

    @patch('os.system')
    def test_reboot_windows(self, mock_system):
        """Тестируем перезагрузку на Windows."""
        with patch('platform.system', return_value='Windows'):
            # Проверяем перезагрузку
            RebootManager.reboot_manager(restart=True)
            mock_system.assert_called_once_with("shutdown /r /t 5")

    @patch('os.system')
    def test_shutdown_windows(self, mock_system):
        """Тестируем завершение программы на Windows."""
        with patch('platform.system', return_value='Windows'):
            # Проверяем завершение программы
            with self.assertRaises(SystemExit):  # Ожидаем исключение SystemExit
                RebootManager.reboot_manager(restart=False)

    @patch('os.system')
    def test_reboot_linux(self, mock_system):
        """Тестируем перезагрузку на Linux."""
        with patch('platform.system', return_value='Linux'):
            # Проверяем перезагрузку
            RebootManager.reboot_manager(restart=True)
            mock_system.assert_called_once_with("sudo shutdown -r now")

    @patch('os.system')
    def test_shutdown_linux(self, mock_system):
        """Тестируем завершение программы на Linux."""
        with patch('platform.system', return_value='Linux'):
            # Проверяем завершение программы
            with self.assertRaises(SystemExit):  # Ожидаем исключение SystemExit
                RebootManager.reboot_manager(restart=False)

    @patch('os.system')
    def test_reboot_mac(self, mock_system):
        """Тестируем перезагрузку на macOS."""
        with patch('platform.system', return_value='Darwin'):
            # Проверяем перезагрузку
            RebootManager.reboot_manager(restart=True)
            mock_system.assert_called_once_with("sudo shutdown -r now")

    @patch('os.system')
    def test_shutdown_mac(self, mock_system):
        """Тестируем завершение программы на macOS."""
        with patch('platform.system', return_value='Darwin'):
            # Проверяем завершение программы
            with self.assertRaises(SystemExit):  # Ожидаем исключение SystemExit
                RebootManager.reboot_manager(restart=False)

    @patch('os.system')
    def test_unsupported_os(self, mock_system):
        """Тестируем, что происходит при использовании неподдерживаемой ОС."""
        with patch('platform.system', return_value='UnsupportedOS'):
            with self.assertRaises(EnvironmentError):
                RebootManager.reboot_manager(restart=True)
            mock_system.assert_not_called()


if __name__ == '__main__':
    unittest.main()
