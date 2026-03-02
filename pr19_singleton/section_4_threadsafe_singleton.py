# Розділ 4 — Потокобезпечний Singleton

import threading


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance


def create_instance(index, storage):
    obj = ThreadSafeSingleton()
    storage[index] = id(obj)


if __name__ == "__main__":
    ids = [None] * 10
    threads = []

    for i in range(10):
        t = threading.Thread(target=create_instance, args=(i, ids))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("ID екземплярів з різних потоків:", ids)
    print("Унікальні ID:", set(ids))
    print("Один екземпляр:", len(set(ids)) == 1)
