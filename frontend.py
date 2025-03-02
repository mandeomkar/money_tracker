from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMainWindow,QLabel,QWidget,QGridLayout,QPushButton,QMessageBox,\
      QDialog, QLineEdit, QComboBox, QCalendarWidget
from expense_class import ExpenseDetails
from show_record import ShowExpenseWindow
from expense_class import ShowingDetails
class MainWindow(QMainWindow): #inheritance Qmain is parent and main is child
    def __init__(self):  
        super().__init__()
        self.setStyleSheet("background-color: brown;")
        self.setWindowTitle("Finance management App") 
        title_label =QLabel("This is my UI window")
        show_expense_window_button = QPushButton("Show Expense records")
        show_expense_window_button.setStyleSheet("QPushButton { border: 1px solid black; }")
        show_expense_window_button.clicked.connect(self.show_expense_window)
        log_expense_window_button = QPushButton("log New Expense")
        log_expense_window_button.setStyleSheet("QPushButton { border: 1px solid black; }")
        log_expense_window_button.clicked.connect(self.log_expense_window)
        exit_button = QPushButton("  Exit  ")
        exit_button.setStyleSheet("QPushButton { border: 1px solid black; }")
        exit_button.clicked.connect(self.close_window)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QGridLayout()
        layout.addWidget(title_label,0,0,1,0, alignment=Qt.AlignmentFlag.AlignCenter) #rowspan,coloumnspan
        layout.addWidget(show_expense_window_button,1,0)
        layout.addWidget(log_expense_window_button,1,1)
        layout.addWidget(exit_button,2,0,1,0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.centralWidget.setLayout(layout)

    def log_expense_window(self):
        log_expense_window= LogExpenseWindow()
        log_expense_window.exec()

    def show_expense_window(self):
        showing_details=ShowingDetails()
        
        details=showing_details.show_expense()[0]
        show_record_window = ShowExpenseWindow(details)
        show_record_window.exec()

    def close_window(self):
        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Close Window?")
        confirmation_widget.setText("Are you sure you want to exit the App?")
        confirmation_widget.setIcon(QMessageBox.Icon.Question)
        confirmation_widget.setStandardButtons(QMessageBox.StandardButton.Yes |
                                               QMessageBox.StandardButton.No)
        confirm= confirmation_widget.exec()
        if confirm == QMessageBox.StandardButton.Yes:
            self.close()
        else:
            confirmation_widget.close()

class LogExpenseWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.pop_up_of_nonumeric= False
        self.setWindowTitle("Log Records")
        expense_label = QLabel("Log New Expense")
        name_label = QLabel("Name")
        type_label =QLabel("Type")
        amount_label =QLabel("Amount")
        date_label =QLabel("Select date")
        self.name_input =QLineEdit()
        self.name_input.setToolTip("Give name of expense, Eg:crocin")
        self.type_input = QComboBox()
        expense_type_list = [
            'Education','Travel','Groceries','Rent','Utilities','Investments','Medical','Pharmaceutical','Maintanance',
            'Taxes','Loan EMIs','Hygiene','Entertainment','Food','Vacation (holiday)','Fashion','Shopping','Self care','Misclenious'
        ]
        self.amount_input = QLineEdit()
        self.amount_input.setToolTip("Give amount only in numeric value Eg: 5452.65")
        self.type_input.addItems(expense_type_list)
        self.calendar= QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.setMaximumDate(QDate.currentDate())
        log_expense_button = QPushButton("Record Expenses")
        log_expense_button.clicked.connect(self.log_expense)
        layout = QGridLayout()
        layout.addWidget(expense_label,0,0,1,0, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(name_label,1,0)
        layout.addWidget(self.name_input,1,1)
        layout.addWidget(type_label,2,0)
        layout.addWidget(self.type_input,2,1)
        layout.addWidget(amount_label,3,0)
        layout.addWidget(self.amount_input,3,1)
        layout.addWidget(date_label,4,0,1,0,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.calendar,5,0,1,0, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(log_expense_button,6,0,1,0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)

    def log_expense(self):
        name =self.name_input.displayText()
        amount= self.amount_input.displayText()
        
        try:
            amount= float(amount)
        
        except ValueError:
            self.amount_input.clear()
            amount = 0.0
            if len(name) != 0:
                self.pop_up_of_nonumeric=True
                Warning_Widget = QMessageBox()
                Warning_Widget.setStyleSheet("background-color: red;")
                Warning_Widget.setWindowTitle("Unacceptable Input")
                Warning_Widget.setText("Please check amount may not be numeric.")
                Warning_Widget.setIcon(QMessageBox.Icon.Warning)
                Warning_Widget.setStandardButtons(QMessageBox.StandardButton.Ok)
                confirm =Warning_Widget.exec()
                if confirm == QMessageBox.StandardButton.Ok:
                    Warning_Widget.close()
            # if len(name.strip()) == 0:
            #     self.pop_up_of_nonumeric = False
       
        type_exp = self.type_input.currentText()
        date = self.calendar.selectedDate().toString()
        if (len(name.strip())!=0 and amount>0 ) :
                expense_details= ExpenseDetails(
                name=name,
                type_exp= type_exp,
                amount=amount,
                date=date
                )
                expense_details.log_expense()
                del expense_details
                confirmation_widget = QMessageBox()
                confirmation_widget.setWindowTitle("Sucess!")
                confirmation_widget.setText("Expense logged succesfully\n"
                                            "Do you want to log a new record")
                confirmation_widget.setIcon(QMessageBox.Icon.Question)
                confirmation_widget.setStandardButtons(QMessageBox.StandardButton.Yes |
                                               QMessageBox.StandardButton.No)
                confirm= confirmation_widget.exec()
                if confirm == QMessageBox.StandardButton.Yes:
                    self.amount_input.clear()
                    self.name_input.clear()
                    confirmation_widget.close()
                else:
                    confirmation_widget.close()
                    self.close()

        else:
            if not self.pop_up_of_nonumeric :
                Warning_Widget = QMessageBox()
                Warning_Widget.setStyleSheet("background-color: light blue;")
                Warning_Widget.setWindowTitle("Donkey")
                Warning_Widget.setText("Please check input some of the fields maybe empty.")
                Warning_Widget.setIcon(QMessageBox.Icon.Warning)
                Warning_Widget.exec()

