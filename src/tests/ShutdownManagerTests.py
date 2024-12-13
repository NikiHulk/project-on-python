import unittest
from unittest.mock import patch
from platform import system
from assistant.ShutdownManager import ShutdownManager

class TestShutdownManager(unittest.TestCase):

    @patch('platform.system', return_value='Linux')
    def test_shutdown_linux(self, mock_system):
        """Тестируем выключение на Linux."""
        with self.assertRaises(OSError):
            ShutdownManager.shutdownManager(restart=True)

    @patch('platform.system', return_value='Darwin')
    def test_shutdown_mac(self, mock_system):
        """Тестируем выключение на macOS."""
        with self.assertRaises(OSError):
            ShutdownManager.shutdownManager(restart=False)

    @patch('platform.system', return_value='UnsupportedOS')
    def test_shutdown_unsupported_os(self, mock_system):
        """Тестируем, что происходит при использовании неподдерживаемой ОС."""
        with self.assertRaises(OSError):
            ShutdownManager.shutdownManager(restart=True)

    @patch('platform.system', return_value='Windows')
    @patch('os.system')
    def test_shutdown_windows(self, mock_system, mock_os_system):
        """Тестируем выключение на Windows."""
        ShutdownManager.shutdownManager(restart=True)
        mock_os_system.assert_called_with("shutdown /s /t 5")

if __name__ == '__main__':
    unittest.main()
