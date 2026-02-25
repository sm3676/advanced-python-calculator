from app.history import HistoryManager

history = HistoryManager()

history.add_record(2, 3, "add", 5)
history.save()

print(history.get_history())