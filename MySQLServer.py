#!/usr/bin/env python3
"""
A simple Python script to create the database 'alx_book_store' in MySQL.
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='jetbeam'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"mysql.connector.Error: {e}")

    finally:
        # Closing your database
        if connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: confirmation message
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
