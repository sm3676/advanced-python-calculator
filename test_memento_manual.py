from app.calculator_memento import Caretaker

caretaker = Caretaker()

caretaker.save("State 1")
caretaker.save("State 2")

print("Undo:", caretaker.undo())
print("Redo:", caretaker.redo())