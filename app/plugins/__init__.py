import importlib
import calculator
class Plugin:
    def execute(self, a, b):
        raise NotImplementedError("Subclasses must implement execute()")

class AdditionPlugin(Plugin):
    def execute(self, a, b):
        return a + b

class SubtractionPlugin(Plugin):
    def execute(self, a, b):
        return a - b

class MultiplicationPlugin(Plugin):
    def execute(self, a, b):
        return a * b

class DivisionPlugin(Plugin):
    def execute(self, a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero")

# Load plugins dynamically
plugins = {
    'add': AdditionPlugin(),
    'sub': SubtractionPlugin(),
    'mul': MultiplicationPlugin(),
    'div': DivisionPlugin()
}