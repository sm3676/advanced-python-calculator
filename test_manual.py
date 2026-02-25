from app.operations import OperationFactory
from app.calculation import Calculation

operation = OperationFactory.create("add")
calc = Calculation(10, 5, operation)

print(calc.perform())