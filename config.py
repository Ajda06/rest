#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     30.04.2025
# Copyright:   (c) User 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------


import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="restaurant_db"
    )