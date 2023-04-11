import os

import pandas as pd
import json

'''
@Author : Dashree Anil
Description:This function returns the json object(dictionary object) with key value pair of test data stored 
            in the controller file
@Param1: Test Case ID
@Return : json object(dictionary object) with key value pair of test data stored 
            in the controller file
'''
def get_test_data_from_controller(test_case_id):
    df = pd.read_excel("../TestData/CONTROLLER.xlsx")
    mask = df['TEST_CASE_ID'] == test_case_id
    df_new = df[mask]
    str_converted_data = df_new["TEST_DATA"].item()
    json_data = json.loads(str_converted_data)
    return json_data


value = get_test_data_from_controller("TC_W2A_001")
print(value)
print(type(value))


'''
@Author : Dashree Anil
Description:This function returns the dictionary with key value pair of queries stored 
            in the text file
@Param1: text file path
@Return : A Dictionary containing all quires present in the text file
'''
def read_text_file(text_file_path):
    text_file_dictionary = {}
    try:
        with open(text_file_path) as f:
            for line in f:
                (key, val) = line.split(":")
                text_file_dictionary[key] = val
        print("Retrival of data from text file was successful")
    except:
        print("Retrival of data from text file failed")



