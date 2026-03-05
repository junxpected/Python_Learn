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

    # Використання властивостей (properties) для безпечного доступу
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