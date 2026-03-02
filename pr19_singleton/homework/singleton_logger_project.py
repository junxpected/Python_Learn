from datetime import datetime
from pathlib import Path
import threading


class AppLogger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, log_path: str = "app.log"):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance.log_path = Path(log_path)
                    cls._instance.log_path.touch(exist_ok=True)
        return cls._instance

    def info(self, message: str) -> None:
        line = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] INFO: {message}\n"
        with self._lock:
            with self.log_path.open("a", encoding="utf-8") as f:
                f.write(line)


def service_auth():
    logger = AppLogger()
    logger.info("Auth service: user signed in")


def service_orders():
    logger = AppLogger()
    logger.info("Orders service: order #1024 created")


def service_notifications():
    logger = AppLogger()
    logger.info("Notifications service: email sent")


if __name__ == "__main__":
    logger_a = AppLogger("app.log")
    logger_b = AppLogger("other_name_ignored.log")

    print("Один екземпляр логера:", logger_a is logger_b)
    print("Файл логу:", logger_a.log_path)

    threads = [
        threading.Thread(target=service_auth),
        threading.Thread(target=service_orders),
        threading.Thread(target=service_notifications),
    ]

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Події записано у спільний лог.")
