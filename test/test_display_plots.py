# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 17:19:18 2022

@author: DELL
"""

## test cases

import os
import json
from src import plots
import datetime
import pandas as pd

def test_read_expense_json():
    filename = "test_user_expenses.json" 
    filepath = os.path.join("data","testdata",filename)
    try:
        if os.stat(filepath).st_size != 0:
            with open(filepath) as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")
        
        
def test_read_transaction_json():
    filename = "test_group_expenses.json" 
    filepath = os.path.join("data","testdata",filename)
    try:
        if os.stat(filepath).st_size != 0:
            with open(filepath) as expense_record:
                expense_record_data = json.load(expense_record)
            return expense_record_data

    except FileNotFoundError:
        print("---------NO RECORDS FOUND---------")
        

def test_get_amount_df():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    ret = plots.get_amount_df("4583959357", 4,test_dict,trans_dict, type="overall")
    assert type(ret) == pd.core.frame.DataFrame     
    
    
def test_individual_present_shared_present():
    #test_dict = test_read_expense_json()
    test_dict = {'5718815807': {'personal_expenses': ['21-Aug-2022 17:37,Groceries,124.93'],'group_expenses': ['26622027']}}
    #mocker.return_value =4
    ret_val = plots.check_data_present(chat_id="5718815807",expense_dict=test_dict)
    assert ret_val == 4     

def test_individual_present_shared_absent():
    test_dict = {'5718815807': {'personal_expenses': ['21-Aug-2022 17:37,Groceries,124.93']}}
    #mocker.return_value =2
    ret_val = plots.check_data_present("5718815807",test_dict)
    assert ret_val == 2    
    
def test_individual_absent_shared_present():
    test_dict = {'5718815807': {'personal_expenses': [],'group_expenses': ['26622027']}}
    ret_val = plots.check_data_present("5718815807",test_dict)
    assert ret_val == 3
    

def test_individual_absent_shared_absent():
    test_dict = {'5718815807': {'personal_expenses': [],'group_expenses': ['26622027']}}
    ret_val = plots.check_data_present("5555511111",test_dict)
    assert ret_val == 1  



    
    
   
    
def test_categorical_plot_noDataforDatesAndCat():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    start_date = datetime.datetime(2021,12,12)
    end_date = datetime.datetime(2022,1,12)
    ret_val = plots.categorical_plot("4583959357", start_date, end_date, "Food",test_dict,trans_dict)
    assert ret_val == 6 
    
def test_categorical_plot_noData():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    start_date = datetime.datetime(2021,12,12)
    end_date = datetime.datetime(2022,1,12)
    ret_val = plots.categorical_plot("5555511111", start_date, end_date, "Food",test_dict,trans_dict)
    assert ret_val == 1
    
    
def test_owe_plot_noData():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    ret_val = plots.owe("5555511111",test_dict,trans_dict)
    assert ret_val == 1    
    
    
def test_owe_plot_noSharedData():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    ret_val = plots.owe("5457678456",test_dict,trans_dict)
    assert ret_val == 2    


def test_overall_plot_noDataforDates():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    start_date = datetime.datetime(2021,12,12)
    end_date = datetime.datetime(2022,1,12)
    ret_val = plots.overall_plot("4583959357", start_date, end_date,test_dict,trans_dict)
    assert ret_val == 5 
    
    

def test_overall_plot_noData():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    start_date = datetime.datetime(2021,12,12)
    end_date = datetime.datetime(2022,1,12)
    ret_val = plots.overall_plot("5555511111", start_date, end_date,test_dict,trans_dict)
    assert ret_val == 1 
    
def test_overall_plot_DataPresent():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    start_date = datetime.datetime(2022,5,1)
    end_date = datetime.datetime(2022,10,1)
    ret_val = plots.overall_plot("4583959357", start_date, end_date,test_dict,trans_dict)
    os.remove('overall_expenses.png')
    assert ret_val == 7
 

    
def test_categorical_plot_DataPresent():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    start_date = datetime.datetime(2022,5,1)
    end_date = datetime.datetime(2022,10,1)
    ret_val = plots.categorical_plot("4583959357", start_date, end_date, "Groceries",test_dict,trans_dict)
    os.remove('categorical_expenses.png')
    assert ret_val == 7   
    


    
'''    
    
def test_owe_plot_SharedData():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    ret_val = plots.owe('4572343459',test_dict,trans_dict)
    os.remove('owe.png')
    assert ret_val == 7  


    
def check_owe_plot_SharedData():
    test_dict = test_read_expense_json()
    trans_dict = test_read_transaction_json()
    ret_val = plots.owe("4583959357",test_dict,trans_dict)
    os.remove('owe.png')
    assert ret_val == 7  
    
'''
    