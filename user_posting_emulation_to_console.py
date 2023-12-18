from database_utils import *

new_connector = AWSDBConnector()

@run_infinitely
def run_infinite_post_data_loop():
    '''
    Utilizes a decorator to run infinitely at random intervals.
    Calls a class method to retrieve records and then prints those records to the console.
    '''
    new_connector.connect_and_get_records()
    print(new_connector.pin_result)
    print(new_connector.geo_result)
    print(new_connector.user_result)

if __name__ == "__main__":
    print('Working')  # Display "Working" to indicate the script is running
    run_infinite_post_data_loop()  # Execute the infinite loop
