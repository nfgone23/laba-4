class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        return "Вызов RealSubject"

class Proxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        return f"Прокси: {self._real_subject.request()}"

# Пример использования
proxy = Proxy()
print(proxy.request())
