import mysql.connector
from mysql.connector import Error

SQL_FILE = "alx_book_store.sql"

def create_database():
    try:
        # Connect to MySQL server (update credentials)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="A!ch#m!$7007!@#$.."
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
        print(f"Error creating database: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def run_sql_file():
	try:
		connection = mysql.connector.connect(
			host = "localhost",
			user="root",
			password="A!ch#m!$7007!@#$..",
			database="alx_book_store"
			)

		if connection.is_connected():
			cursor = connection.cursor()

			# Read SQL file
			with open(SQL_FILE, "r") as file:
				sql_commands = file.read()

			# Execute multiple commands
			for command in sql_commands.split(";"):
				cmd = command.strip()
				if cmd:
					cursor.execute(cmd)

			connection.commit()
			print(f"SQL file '{SQL_FILE}' executed successfully!")

	except FileNotFoundError:
		print(f"Error: SQL file '{SQL_FILE}' not found.")
	except Error as e:
		print(f"Error executing SQL file: {e}")
	finally:
		if 'connection' in locals() and connection.is_connected():
			cursor.close()
			connection.close()

if __name__ == "__main__":
    create_database()
    run_sql_file()