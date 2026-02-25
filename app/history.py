import pandas as pd
import os


class HistoryManager:

    def __init__(self, filename="history.csv"):
        self.filename = filename

        if os.path.exists(self.filename):
            self.history_df = pd.read_csv(self.filename)
        else:
            self.history_df = pd.DataFrame(
                columns=["a", "b", "operation", "result"]
            )

    def add_record(self, a, b, operation, result):
        new_row = {
            "a": a,
            "b": b,
            "operation": operation,
            "result": result,
        }

        self.history_df = pd.concat(
            [self.history_df, pd.DataFrame([new_row])],
            ignore_index=True,
        )

    def save(self):
        self.history_df.to_csv(self.filename, index=False)

    def clear(self):
        self.history_df = self.history_df.iloc[0:0]
        self.save()

    def get_history(self):
        return self.history_df