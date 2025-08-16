import mysql.connector

def create_database():
    try:
        # First connect to MySQL server (without specifying a database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        cursor = connection.cursor()

        # Create the database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database alx_book_store is ready.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_database()

