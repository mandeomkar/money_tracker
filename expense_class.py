import pandas as pd
import os.path
class ExpenseDetails :
    def __init__(self,name, type_exp,amount,date):
        
        self.file_name='expense_records.csv'
        self.exp_name =name
        self.exp_type =type_exp
        self.exp_amount =amount  
        self.exp_date =date
        self.exp_details={
            'exp_name': [],
            'exp_type': [],
            'exp_amount': [],
            'exp_date': []
        }

    def log_expense(self):
        self.exp_details['exp_amount'].append(self.exp_amount)
        self.exp_details['exp_type'].append(self.exp_type)
        self.exp_details['exp_date'].append(self.exp_date)
        self.exp_details['exp_name'].append(self.exp_name) 
        self.df = pd.DataFrame(self.exp_details)
        if os.path.exists(self.file_name):
            file_exists=True
        else:
            with(open(self.file_name, 'w') as file):  
                file.write(','.join(list(self.exp_details.keys())) +'\n')
                file_exists=True
        self.df.to_csv(self.file_name, index=False, mode='a' , header=not file_exists)
    
class ShowingDetails:
    def __init__(self):
        self.file_name='expense_records.csv'
    def show_expense(self):
        
        details = pd.read_csv(self.file_name).to_dict()
        
        return [details]