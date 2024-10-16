import pandas as pd

class LoggingTable:
    def __init__(self, table):
        self.table_placeholder = table
        self.table_rows = pd.DataFrame(columns=["Detection"])
        
    def get_table(self):
        return self.table_placeholder.table(self.table_rows)
        
    def add_rows(self, to_add_rows=[]):
        new_rows = pd.DataFrame(to_add_rows, columns=["Detection"])
        
        self.table_rows = pd.concat([self.table_rows, new_rows], ignore_index=True).tail(10)
        
        return self.table_placeholder.table(self.table_rows)