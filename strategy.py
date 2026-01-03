from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class AddStrategy(Strategy):
    def execute(self, a, b):
        return a + b

class SubtractStrategy(Strategy):
    def execute(self, a, b):
        return a - b

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, a, b):
        return self._strategy.execute(a, b)

# Пример использования
context = Context(AddStrategy())
print("Сложение:", context.execute_strategy(5, 3))

context = Context(SubtractStrategy())
print("Вычитание:", context.execute_strategy(5, 3))
