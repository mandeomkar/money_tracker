import pandas as pd
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog , QPushButton, QGridLayout, QLabel, QTableWidget, QTableWidgetItem, QMessageBox

class ShowExpenseWindow(QDialog):
    def __init__(self,details):
            super().__init__()
            
            self.details=details
            self.names=list(details['exp_name'].values())
            self.types=list(details['exp_type'].values())
            self.amounts=list(details['exp_amount'].values())
            self.dates=list(details['exp_date'].values())
            row_wise_data = list(zip(self.names, self.types, self.amounts, self.dates))
            self.setWindowTitle("Show Records history")
            title_label= QLabel("expense Records")
            back_button = QPushButton("Back")
            summary_button = QPushButton("Summary")
            back_button.clicked.connect(self.go_back)
            summary_button.clicked.connect(self.view_summary)
            self.records_table = QTableWidget()
            self.records_table.setColumnCount(4)
            for row,data in enumerate(row_wise_data):
                self.records_table.insertRow(row)
                for col,item in  enumerate(data):
                     self.records_table.setItem(row, col, QTableWidgetItem(str(item)))
            columns_header = ('Name', 'Type','Amount', 'Date')
            self.records_table.setHorizontalHeaderLabels(columns_header)
            self.records_table.verticalHeader().setVisible(False)
            layout = QGridLayout()
            layout.addWidget(title_label,0,0,1,0, alignment=Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(self.records_table,1,0,1,0)
            layout.addWidget(back_button,2,1)
            layout.addWidget(summary_button,2,0)
            self.setLayout(layout)

    def go_back(self):
        self.close()
    
    def view_summary(self):
    # Create a DataFrame from the details
        df = pd.DataFrame(self.details)
        
        # Group by 'Type' and sum the 'Amount'
        summary = df.groupby('exp_type')['exp_amount'].sum().reset_index().to_dict()
        print(summary)
        
        # Print the summary in a formatted way
        print("Summary of Expenses Type-wise:")
        for index, row in summary.iterrows():
            print(f"Your expense on {row['exp_type']} is {row['exp_amount']}.")
        # Find the maximum of the summed expenses
        max_expense = summary['exp_amount'].max()
        
        # Find the type associated with the maximum summed expense
        max_type = summary[summary['exp_amount'] == max_expense]['exp_type'].values[0]
        
        # Print the maximum summed expense
        print(f"Your maximum expense is on {max_type} i.e. {max_expense}.")

        
    
# class SummaryButton(QDialog):
#      def __init__(self):
#            super().__init__()