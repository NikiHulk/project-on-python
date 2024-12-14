# tests/TossCoinTests.py

from unittest.mock import patch
from src.assistant.TossCoin import TossCoin


# Тестирование правильности работы подбрасывания монеты
@patch('src.assistant.TossCoin.speak')
@patch('src.assistant.TossCoin.random.choice')
def test_toss_coin(mock_random_choice, mock_speak):
    """Тестируем метод toss_coin."""

    # Настроим mock, чтобы random.choice всегда возвращал "орел"
    mock_random_choice.return_value = "орел"

    # Создаем объект класса
    coin_tosser = TossCoin()

    # Подбрасываем монету 1 раз
    coin_tosser.toss_coin(1)

    # Проверка, что random.choice был вызван 1 раз
    mock_random_choice.assert_called_once_with(["орел", "решка"])

    # Проверка, что speak была вызвана с правильным сообщением
    mock_speak.assert_called_once_with("Монета подброшена, вам выпал орел")


# Тестирование подбрасывания нескольких монет
@patch('src.assistant.TossCoin.speak')
@patch('src.assistant.TossCoin.random.choice')
def test_multiple_tosses(mock_random_choice, mock_speak):
    """Тестируем метод toss_coin с несколькими подбрасываниями."""

    # Настроим mock, чтобы random.choice чередовал "орел" и "решка"
    mock_random_choice.side_effect = ["орел", "решка", "орел"]

    # Создаем объект класса
    coin_tosser = TossCoin()

    # Подбрасываем монету 3 раза
    coin_tosser.toss_coin(3)

    # Проверка, что random.choice был вызван 3 раза
    mock_random_choice.assert_any_call(["орел", "решка"])

    # Проверка, что speak была вызвана 3 раза с правильными результатами
    mock_speak.assert_any_call("Монета подброшена, вам выпал орел")
    mock_speak.assert_any_call("Монета подброшена, вам выпала решка")
    mock_speak.assert_any_call("Монета подброшена, вам выпал орел")
