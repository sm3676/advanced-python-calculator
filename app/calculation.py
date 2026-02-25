# app/calculation.py

class Calculation:

    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self):
        return self.operation.execute(self.a, self.b)