import unittest
from RebootManager import RebootManager


class TestRebootManager(unittest.TestCase):
    def test_reboot_command(self):
        result = RebootManager.rebootManager(restart=True, test_mode=True)
        self.assertEqual(result, "shutdown /r /t 5")

    def test_exit_command(self):
        result = RebootManager.rebootManager(restart=False, test_mode=True)
        self.assertEqual(result, "exit")


if __name__ == "__main__":
    unittest.main()
