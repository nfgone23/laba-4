class Handler(ABC):
    def __init__(self):
        self._next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    @abstractmethod
    def handle(self, request):
        if self._next:
            return self._next.handle(request)
        return None

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request == "A":
            return f"Handler A обработал запрос {request}"
        else:
            return super().handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request == "B":
            return f"Handler B обработал запрос {request}"
        else:
            return super().handle(request)

# Пример использования
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()
handler_a.set_next(handler_b)

print(handler_a.handle("A"))
print(handler_a.handle("B"))
print(handler_a.handle("C"))
