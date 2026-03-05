from abc import ABC, abstractmethod
from enum import Enum

# --- ДОКУМЕНТАЦІЯ ТА КОМЕНТУВАННЯ ---
class FileStatus(Enum):
    """Перелік можливих станів файлу."""
    NEW = "New"
    MODIFIED = "Modified"
    DONE = "Done"

# --- АБСТРАКЦІЯ ТА ІНТЕРФЕЙСИ ---
class IAsset(ABC):
    """
    Абстрактний базовий клас (Інтерфейс).
    Визначає контракт для всіх медіа-активів у системі.
    """
    @abstractmethod
    def get_info(self) -> str:
        """Повертає рядок з інформацією про актив."""
        pass

# --- СТВОРЕННЯ ОСНОВНИХ КЛАСІВ ТА ІНКАПСУЛЯЦІЯ ---
class BaseAsset(IAsset):
    """
    Базовий клас для файлів. Реалізує базову логіку та інкапсулює дані.
    """
    def __init__(self, name: str, size_kb: int):
        # Інкапсуляція: атрибути приховані (private)
        self.__name = name
        self.__size_kb = size_kb
        self.__status = FileStatus.NEW

    # Використання властивостей для безпечного доступу
    @property
    def name(self) -> str:
        """Гетер для отримання імені файлу."""
        return self.__name

    @property
    def status(self) -> FileStatus:
        """Гетер для статусу файлу."""
        return self.__status

    @status.setter
    def status(self, new_status: FileStatus):
        """Сетер для статусу з перевіркою типу."""
        if not isinstance(new_status, FileStatus):
            raise ValueError("Неприпустимий статус файлу")
        self.__status = new_status

    def get_info(self) -> str:
        """Реалізація абстрактного методу."""
        return f"File: {self.__name} | Size: {self.__size_kb}KB | Status: {self.__status.value}"

# --- НАСЛІДУВАННЯ ---
class VideoAsset(BaseAsset):
    """
    Спеціалізований клас для відеофайлів. Успадковує BaseAsset.
    """
    def __init__(self, name: str, size_kb: int, duration_sec: int):
        super().__init__(name, size_kb) # Виклик конструктора базового класу
        self.duration_sec = duration_sec # Унікальний атрибут

    # Поліморфізм: перевизначення методу базового класу
    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info} | Duration: {self.duration_sec}s"

class CodeAsset(BaseAsset):
    """
    Спеціалізований клас для файлів з кодом.
    """
    def __init__(self, name: str, size_kb: int, language: str):
        super().__init__(name, size_kb)
        self.language = language

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info} | Lang: {self.language}"

    class ProjectManager:
        """
        Клас-сценарій для демонстрації поліморфізму.
        Працює з будь-якими об'єктами, що реалізують інтерфейс IAsset.
        """

        def __init__(self):
            self.__assets = []

        def add_asset(self, asset: IAsset):
            """Додає актив до проєкту. Очікує інтерфейс IAsset."""
            if not isinstance(asset, IAsset):
                raise TypeError("Об'єкт має реалізовувати інтерфейс IAsset")
            self.__assets.append(asset)

        def print_project_report(self) -> str:
            """
            Сценарій використання поліморфізму:
            цикл проходить по всіх об'єктах і викликає get_info().
            Програмі не потрібно знати, чи це VideoAsset, чи CodeAsset.
            """
            report_lines = ["--- Звіт по проєкту ---"]
            for asset in self.__assets:
                # Ось тут працює поліморфізм:
                report_lines.append(asset.get_info())

            return "\n".join(report_lines)

    #  Приклад сценарію
    if __name__ == "__main__":
        manager = ProjectManager()

        # Додаємо об'єкти різних класів
        manager.add_asset(BaseAsset("notes.txt", 15))
        manager.add_asset(VideoAsset("interview.mp4", 1024000, 3600))
        manager.add_asset(CodeAsset("StatusEvaluator.cs", 45, "C#"))

        # Виконуємо поліморфний виклик
        print(manager.print_project_report())