import unittest
from models import FileStatus, BaseAsset, VideoAsset, CodeAsset


class TestAssetClasses(unittest.TestCase):
    """Клас для unit-тестування моделей."""

    def test_encapsulation_and_status_update(self):
        """Тестування інкапсуляції та зміни статусу."""
        asset = BaseAsset("document.txt", 150)

        # Перевіряємо початковий стан
        self.assertEqual(asset.status, FileStatus.NEW)

        # Змінюємо стан через сетер
        asset.status = FileStatus.DONE
        self.assertEqual(asset.status, FileStatus.DONE)

        # Перевірка, що прямий доступ до приватної змінної викличе помилку
        with self.assertRaises(AttributeError):
            print(asset.__size_kb)

    def test_inheritance_and_polymorphism(self):
        """Тестування спеціалізованих класів (VideoAsset)."""
        video = VideoAsset("render_v1.mp4", 500000, 120)

        # Перевіряємо, чи правильно формується рядок
        info = video.get_info()
        self.assertIn("render_v1.mp4", info)
        self.assertIn("Duration: 120s", info)


if __name__ == '__main__':
    unittest.main()