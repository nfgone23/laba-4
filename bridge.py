class Implementor(ABC):
    @abstractmethod
    def operation_impl(self):
        pass

class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        return "Implementor A"

class ConcreteImplementorB(Implementor):
    def operation_impl(self):
        return "Implementor B"

class Abstraction:
    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    def operation(self):
        return f"Абстракция использует {self._implementor.operation_impl()}"

# Пример использования
impl_a = ConcreteImplementorA()
abstraction = Abstraction(impl_a)
print(abstraction.operation())

impl_b = ConcreteImplementorB()
abstraction = Abstraction(impl_b)
print(abstraction.operation())
