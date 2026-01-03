class Adaptee:
    def specific_request(self):
        return "Специфичный запрос Adaptee"

class Target(ABC):
    @abstractmethod
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def request(self):
        return f"Адаптер: {self._adaptee.specific_request()}"

# Пример использования
adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())
