# Импортируем нужные функции из ProcessingVoiceInput
from src.assistant.ProcessingVoiceInput import listenForWakeWord

# Точка входа в программу
if __name__ == "__main__":
    listenForWakeWord()  # Запуск прослушивания ключевого слова
