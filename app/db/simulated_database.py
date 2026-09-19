################################################
#The simulated_database.py file provides a simple interface 
# for managing checkout transactions in a SQLite database. 
# It includes mechanisms for locking the database to prevent
# concurrent modifications, ensuring data integrity during transactions.
###############################################


import sqlite3 # sqlite3: For interacting with the SQLite database.
from pathlib import Path # Path from pathlib: To handle file paths.
from datetime import datetime # datetime: To manage date and time.

# DB_PATH is set to "checkout.db", which is the database file that will be created or accessed.
DB_PATH = Path("checkout.db")

# DatabaseLockException: A custom exception that is raised when a database operation is attempted while the database is locked.
class DatabaseLockException(Exception):
    pass


class SimulatedDatabase:

    def __init__(self):

        #Establishes a connection to the SQLite database.
        self.connection = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )
        #Initializes a locked state to track whether the database is locked.
        self.locked = False
        #Calls the  initialize method to set up the database schema if it doesn't already exist
        self.initialize()

    #Creates a table named checkout_transactions with three columns: id, status, and created_at
    def initialize(self):
        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS checkout_transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                status TEXT,
                created_at TEXT
            )
            """
        )

        self.connection.commit()

#Locking Methods:
#lock_db : Sets the 
#locked state to True.
#unlock_db: Sets the 
#locked state to False.
#is_locked: Returns the current locked state

    def lock_db(self):
        self.locked = True

    def unlock_db(self):
        self.locked = False

    def is_locked(self):

        return self.locked

    #Checkout Transaction Methods

    def checkout_transaction(self):

    # Checkout_transaction): Checks if the database is locked. If it is, raises a DatabaseLockException.
        if self.locked:
            raise DatabaseLockException(
                "Database lock detected"
            )

        cursor = self.connection.cursor()

        # If not locked, it inserts a new record into the checkout_transactions table with a status of "SUCCESS" and the current UTC timestamp.
        if not self.locked:
            cursor.execute(
                """
                INSERT INTO checkout_transactions(
                    status,
                    created_at
                )
            VALUES(
                ?,
                ?
            )
            """,
            (
                "SUCCESS",
                datetime.utcnow().isoformat()
            )
        )

        self.connection.commit()

        return True

    def count_transactions(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM checkout_transactions
            """
        )

        return cursor.fetchone()[0]

#At the end of the file, an instance of  SimulatedDatabase  is created, which initializes the database connection and schema.
db = SimulatedDatabase()