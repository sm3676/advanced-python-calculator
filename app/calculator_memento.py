# app/calculator_memento.py

class CalculatorMemento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._history = []
        self._redo_stack = []

    def save(self, state):
        self._history.append(CalculatorMemento(state))
        self._redo_stack.clear()

    def undo(self):
        if not self._history:
            return None

        memento = self._history.pop()
        self._redo_stack.append(memento)
        return memento.get_state()

    def redo(self):
        if not self._redo_stack:
            return None

        memento = self._redo_stack.pop()
        self._history.append(memento)
        return memento.get_state()