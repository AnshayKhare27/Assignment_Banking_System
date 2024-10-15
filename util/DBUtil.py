import pyodbc

class DBUtil:
    
    @staticmethod
    def getDBConn():
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'Server=MSI\SQLEXPRESS;'
                                  'Database=BankingSystem;'
                                  'Trusted_Connection=yes;')
            return conn

        except:
            print("Connection failed")