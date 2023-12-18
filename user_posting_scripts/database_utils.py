import datetime
import json
import os
import random
import requests
import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import text
from time import sleep

# Load environment variables for database credentials
load_dotenv()

# Seed for reproducible 'random' results
random.seed(100)

class AWSDBConnector:
    '''
    This class contains methods for establishing a connection to a database 
    using SQLAlchemy and acquiring records from the connected database
    '''
    def __init__(self):
        # Database credentials from environment variables
        self.HOST = os.getenv('RDSHOST')
        self.USER = os.getenv('RDSUSER')
        self.PASSWORD = os.getenv('RDSPASSWORD')
        self.DATABASE = os.getenv('RDSDATABASE')
        self.PORT = os.getenv('RDSPORT')
        # Results placeholders for database queries
        self.pin_result = {}
        self.geo_result = {}
        self.user_result = {}
    
    def create_db_connector(self):
        '''Generate connection engine using SQLAlchemy create_engine() method'''
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:"
            f"{self.PORT}/{self.DATABASE}?charset=utf8mb4"
        )
        return engine
    
    def get_record_from_table(self, table: str, connection, row_number: int):
        '''Execute a query to obtain a row record from a specified table'''
        query_string = text(f"SELECT * FROM {table} LIMIT {row_number}, 1")
        selected_row = connection.execute(query_string)
        for row in selected_row:
            result = dict(row._mapping)
        return result
    
    def connect_and_get_records(self):
        '''Retrieve a random row from three different tables in the database'''
        random_row = random.randint(0, 11000)
        engine = self.create_db_connector()
        with engine.connect() as connection:
            self.pin_result = self.get_record_from_table("pinterest_data", connection, random_row)
            self.geo_result = self.get_record_from_table("geolocation_data", connection, random_row)
            self.user_result = self.get_record_from_table("user_data", connection, random_row)


def post_record_to_API(method: str, invoke_url: str, record_dict: dict, *args):
    '''
    Prepare and send data payload to an API (Kafka batch API or Kinesis stream API)

    Parameters
    ----------
        method: str
            'POST' for Kafka batch API, 'PUT' for Kinesis stream API
        invoke_url: str
            API's invoke URL
        record_dict: dict
            Database record
        *args:
            For Kinesis stream API: stream name string
    '''
    # Convert datetime values in record_dict to string format
    for key, value in record_dict.items():
        if type(value) == datetime.datetime:
            record_dict[key] = value.strftime("%Y-%m-%d %H:%M:%S")

    if len(args) == 1:
        # Prepare payload for Kinesis stream API
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({
            "StreamName": args[0],
            "Data": record_dict,
            "PartitionKey": args[0][23:]    
        })
    elif len(args) == 0:
        # Prepare payload for Kafka batch API
        headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}
        payload = json.dumps({
            "records": [
                {
                    "value": record_dict
                }
            ]     
        })

    # Send request to API
    response = requests.request(method, invoke_url, headers=headers, data=payload)
    print(response.status_code)


def run_infinitely(func):
    '''Decorator to run a function infinitely at random intervals between 0 and 2 seconds'''
    def inner():
        while True:
            sleep(random.randrange(0, 2))  # Pause for a random length of time between 0 and 2 seconds
            func()  # Execute the function
    return inner
