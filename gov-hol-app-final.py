import requests
import json
from datetime import datetime
import argparse 

# Converts the input date into a python datetime object
# def search_england_and_wales_public_holidays(from_input_date_as_string, england_holiday_json):
#     # Define format for the input date
#     gov_holiday_date_date_format = '%Y-%m-%d'

#     for event in england_holiday_json['event']:
#         current_event_date_string = event['date']

#         current_event_date = datetime.strptime(current_event_date_string, gov_holiday_date_date_format)
#         input_date = datetime.strptime(from_input_date_as_string, gov_holiday_date_date_format)
#         if input_date < current_event_date:
#             print(event['title']+ ' : ' + event['date'])



# Parse Argument via the Command Line Interface (CLI), the command line language is called BASH 
parser = argparse.ArgumentParser()

# Defining the arguments to parse i.e. what we must write in terminal to execute our code
parser.add_argument("--from_date", '-f', help='from date', type= str, required = True)

# Passes Arguments into parser
args = parser.parse_args()

# This gets the from date from the parsed argument, this is getting the information from what we write in terminal 
from_input_date_as_string = args.from_date


# Loading the Data 
# Create a request object for the Gov API 
gov_holiday_data_response_object = requests.get('https://www.gov.uk/bank-holidays.json')
# Create JSON object 
gov_holiday_data_json = gov_holiday_data_response_object.json()
# Create JSON object of only Engaland and Wales 
england_holiday_json = gov_holiday_data_json["england-and-wales"]

# date_in_question = datetime.strptime(from_input_date_as_string, gov_holiday_date_date_format)
#print(json.dumps(gov_holiday_data_json, indent=2))

# def date_converter(date_in_question):
#     # "" date in question must be in format YYYY-MM-DD ""
#     # "" This function will convert the date into a datetime object"""
#     date_formatted = datetime.strptime(date_in_question, gov_holiday_date_date_format)
#     return(date_formatted)

#date_converter('2020-05-28')

# Gives all the public holidays past a certain date 
# Maybe we should but in a range here, start date and then an end date 

def search_england_and_wales_public_holidays(from_input_date_as_string, england_holiday_json):
    # Define format for the input date
    gov_holiday_date_date_format = '%Y-%m-%d'

    for event in england_holiday_json["event"]:
        current_event_date_string = event['date']

        current_event_date = datetime.strptime(current_event_date_string, gov_holiday_date_date_format)
        input_date = datetime.strptime(from_input_date_as_string, gov_holiday_date_date_format)
        if input_date < current_event_date:
            print(event['title']+ ' : ' + event['date'])

            
# Example 
search_england_and_wales_public_holidays(from_input_date_as_string, england_holiday_json)



# To run off BASH 
# python3 gov-hol-app-final.py