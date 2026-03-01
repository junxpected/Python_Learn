# Завдання 34 — Ієрархія власних виключень

class AppError(Exception): pass
class NetworkError(AppError): pass
class TimeoutError(NetworkError): pass
class AuthError(AppError): pass

def simulate(error_type):
    if error_type == "timeout": raise TimeoutError("Запит перевищив час очікування")
    if error_type == "auth":    raise AuthError("Невірний токен авторизації")
    if error_type == "network": raise NetworkError("З'єднання відхилено")
    return "OK"

for err in ["timeout", "auth", "network", "none"]:
    try:
        print(f"  [{err}]:", simulate(err))
    except TimeoutError as e:
        print(f"  TimeoutError: {e}")
    except NetworkError as e:
        print(f"  NetworkError: {e}")
    except AuthError as e:
        print(f"  AuthError: {e}")
