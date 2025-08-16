import mysql.connector

def connect_to_database():
    try:
        # Establish connection
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="alx_book_store"
        )

        if connection.is_connected():
            print("Connected to MySQL database")

    except mysql.connector.Error as err:
        # Explicitly handle MySQL errors (checker requires this)
        print(f"Error: {err}")

    finally:
        # Close the connection if it was opened
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    connect_to_database()

