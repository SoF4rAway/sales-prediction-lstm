import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()

# Connect to PostgreSQL database
def connect():
    try:
        # Connect to an existing database
        connection = psycopg2.connect(user=os.getenv("db_user"),
                                    password=os.getenv("db_password"),
                                    host=os.getenv("db_host"),
                                    port=os.getenv("db_port"),
                                    database=os.getenv("db_name"))

        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    return cursor

