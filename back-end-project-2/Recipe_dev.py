import json
import mysql.connector
# pip install mysql-connector
def Loginuser(username, password):
    if username == 'peter' and password == 'honey':
        return True
    else:
        return False
