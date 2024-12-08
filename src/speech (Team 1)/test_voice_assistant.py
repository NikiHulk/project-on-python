import unittest
import unittest.mock
import os
import recordAndRecognizeAudio, executeCommand, commands, greet_user, create_note_interaction, delete_note_interaction #replace your_voice_assistant
import random


#Simplified Note Manager for Testing
class MockNoteManager:
    def __init__(self):
        self.notes = []

    def CreateNote(self, text):
        self.notes.append(text)

    def ReadNotes(self):
        if not self.notes:
            print("Заметок нет")
        else:
            for i, note in enumerate(self.notes):
                print(f"{i+1}. {note}")

    def DeleteNote(self, index):
        try:
            del self.notes[index - 1]
        except IndexError:
            raise IndexError("Заметки с таким номером не существует.")


class TestVoiceAssistant(unittest.TestCase):

    @unittest.mock.patch('your_voice_assistant.recordAndRecognizeAudio', return_value='здравствуйте') #replace your_voice_assistant
    def test_greeting(self, mock_recordAndRecognizeAudio):
        #Test Greeting Function
        with unittest.mock.patch('your_voice_assistant.pyttsx3.init') as mock_init:
            greet_user()
            self.assertTrue(mock_init.called)


    @unittest.mock.patch('your_voice_assistant.recordAndRecognizeAudio', side_effect=['какая погода сегодня', 'до свидания']) #replace your_voice_assistant
    @unittest.mock.patch('your_voice_assistant.CheckWeather.checkWeatherNow')
    @unittest.mock.patch('your_voice_assistant.Farewell.Farewell.farewellAndQuit')
    def test_command_execution(self, mock_farewell, mock_checkWeather, mock_recordAndRecognizeAudio):
        #Test command execution
        with unittest.mock.patch('builtins.print') as mock_print:
            executeCommand('какая погода сегодня')
            self.assertTrue(mock_checkWeather.called)

            executeCommand('до свидания')
            self.assertTrue(mock_farewell.called)


    @unittest.mock.patch('your_voice_assistant.recordAndRecognizeAudio', return_value='создать заметку') #replace your_voice_assistant
    @unittest.mock.patch('builtins.input', return_value='Тестовая заметка')
    @unittest.mock.patch('your_voice_assistant.NoteManagerClass.NotesManager', return_value=MockNoteManager()) #replace your_voice_assistant
    def test_create_note(self, mock_note_manager, mock_input, mock_recordAndRecognizeAudio):
      #Test create note functionality

        create_note_interaction()

        self.assertEqual(len(mock_note_manager().notes), 1)
        self.assertEqual(mock_note_manager().notes[0], "Тестовая заметка")


    @unittest.mock.patch('your_voice_assistant.recordAndRecognizeAudio', return_value='удалить заметку') #replace your_voice_assistant
    @unittest.mock.patch('builtins.input', side_effect=['1','0'])
    @unittest.mock.patch('your_voice_assistant.NoteManagerClass.NotesManager', return_value=MockNoteManager()) #replace your_voice_assistant
    def test_delete_note(self, mock_note_manager, mock_input, mock_recordAndRecognizeAudio):
      #Test delete note functionality
      mock_note_manager().CreateNote("Заметка для удаления")
      delete_note_interaction()
      self.assertEqual(len(mock_note_manager().notes), 0)



    @unittest.mock.patch('your_voice_assistant.recordAndRecognizeAudio', return_value='кинь монету') #replace your_voice_assistant
    @unittest.mock.patch('your_voice_assistant.TossCoin.TossCoin.tossCoin') as mock_toss_coin
    def test_toss_coin(self, mock_toss_coin, mock_recordAndRecognizeAudio):
        # Test toss coin functionality
        executeCommand('кинь монету')
        self.assertTrue(mock_toss_coin.called)


    @unittest.mock.patch('your_voice_assistant.recordAndRecognizeAudio', return_value='Неизвестная команда') #replace your_voice_assistant
    def test_unknown_command(self, mock_recordAndRecognizeAudio):
        # Test handling of unknown commands
        with unittest.mock.patch('builtins.print') as mock_print:
            executeCommand('Неизвестная команда')
            mock_print.assert_called_once_with("Неизвестная команда.")

# TODO -> докрутить тесты до конца В каком классе написания
# if __name__ == '__main__':
#     unittest.main()