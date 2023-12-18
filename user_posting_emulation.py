import random
from time import sleep
import sqlalchemy
from sqlalchemy import text

class AWSDBConnector:
    def __init__(self):
        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306

    def create_db_connector(self):
        engine = sqlalchemy.create_engine(
            f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

new_connector = AWSDBConnector()

def fetch_data_and_print():
    while True:
        sleep(random.randrange(0, 2))
        random_row = random.randint(0, 11000)
        engine = new_connector.create_db_connector()

        with engine.connect() as connection:
            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {random_row}, 1")
            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {random_row}, 1")
            user_string = text(f"SELECT * FROM user_data LIMIT {random_row}, 1")

            # Fetch the latest row for each table
            pin_selected_row = connection.execute(pin_string).fetchone()
            geo_selected_row = connection.execute(geo_string).fetchone()
            user_selected_row = connection.execute(user_string).fetchone()

            # Convert the fetched rows into dictionaries
            pin_result = dict(pin_selected_row._mapping)
            geo_result = dict(geo_selected_row._mapping)
            user_result = dict(user_selected_row._mapping)

            print("pin_result:", pin_result)
            print("geo_result:", geo_result)
            print("user_result:", user_result)

if __name__ == "__main__":
    fetch_data_and_print()
    print('Working')
