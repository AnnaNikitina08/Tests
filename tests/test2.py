import unittest
from api_yandex import create_folder
from api_yandex import get_metatype_folder
from api_yandex import get_token_ya

TOKEN = get_token_ya()

class TestApiYa(unittest.TestCase):
    def test_create_folder(self):
        result = create_folder(TOKEN, "photo")
        self.assertTrue(result == 201, f'Ошибка создания папки: {result}')

    def test_type_folder(self):
        result = get_metatype_folder(TOKEN, "photo")
        self.assertTrue(result == "dir", f'Папка не появилась на диске')