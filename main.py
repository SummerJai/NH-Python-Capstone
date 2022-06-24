import mysql.connector
from mysql.connector import Error


def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name

        )
        print("MySQL Database Connection Successful")
    except Error as err:
        print(f"Error: {err}")

    return connection


#creating database defined function
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database Created Successfully")
    except Error as err:
        print(f"Error: {err}")

#Work horse Function to execute queries
def execute_query(connection,query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query Successful")
    except Error as err:
        print(f"Error: {err}")

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: {err}'")



Create_EmployeesTable = """
CREATE TABLE employees(
First_Name VARCHAR(10) NOT NULL,
Last_Name VARCHAR(10) NOT NULL,
Employee_Id INT (40) NOT NULL,
Gender VARCHAR (20) NOT NULL,
Birth_Date VARCHAR(20) NOT NULL,
Education VARCHAR (20) NOT NULL,
Years_Experience INT (20) NOT NULL,
Hire_Date VARCHAR (40) NOT NULL);"""

informationForEmployeesTable = """
INSERT INTO employees VALUES
("Kynetta", "Mitchell", "12345", "F", "06/01/1983", "RN", "15", "01/12/2007"),
("Daphne", "Love", "67890", "F", "07/26/1980", "CNA", "5", "06/16/2000"),
("Stephanie", "Greenwald", "555273", "F", "12/03/1975", "RN", "20", "05/2002"),
("Archie", "Robinson", "991826", "M", "08/17/1983", "MD", "4", "11/15/2018"),
("Kelly", "Runions", "134589", "F", "05/05/1979", "CNA", "15", "09/12/2007"),
("Christina", "Donaldson", "12345", "F", "06/01/1983", "NP", "1", "10/16/2021"),
("Marcus", "Wallace", "321654", "M", "03/21/1990", "RN", "7", "01/12/2015"),
("Larry", "Jones", "847216", "M", "04/01/1975", "NP", "25", "04/12/2007"),
("Shaun", "Johnson", "753691", "M", "06/19/1983", "MD", "10", "08/12/2012"),
("Brandon", "Brown", "147589", "M", "11/24/1983", "RN", "5", "12/01/2017");"""

Create_SalariesTable = """
INSERT INTO employees VALUES
First_Name  VARCHAR(50) NOT NULL,
Last_Name  VARCHAR(50) NOT NULL,
Employee_Id  INT (40) NOT NULL,
Hire_Date   VARCHAR (40) NOT NULL,
Salary VARCHAR (40) NOT NULL);"""

informationForSalariesTable = """
INSERT INTO salaries VALUES
("Kynetta", "Mitchell", 12345, "01/12/2007", "75,000"),
("Daphne", "Love", 67890, "06/16/2000", "$45,000"),
("Stephanie", "Greenwald", 555273, "05/2002", "$75,000"),
("Archie", "Robinson", 991826, "11/15/2018", "$280,000"),
("Kelly", "Runions", 134589, "09/12/2007", "$50,000"),
("Christina", "Donaldson", 12345, "10/16/2021", "$125,000"),
("Marcus", "Wallace", 321654, "01/12/2015", "$60,000"),
("Larry", "Jones", 847216, "04/12/2007", "$120,000"),
("Shaun", "Johnson", 753691, "08/12/2012", "$300,000"),
("Brandon", "Brown", 147589, "12/01/2017", "$65,000");"""

Create_DepartmentTable = """
CREATE TABLE department(
Surgery VARCHAR (50),
Burn_Unit VARCHAR (50),
Urgent_Care VARCHAR (50));"""


informationForDepartmentTable = """
INSERT INTO department VALUES
("N/A", "N/A", "Kynetta Mitchell ID = 12345"),
("N/A", "N/A", "Daphne Love ID = 67890"),
("N/A", "N/A", "Stephanie Greenwald ID = 555273"),
("N/A", "N/A", "Archie Robinson ID = 991826"),
("N/A", "Kelly Runions ID = 134589", "N/A"),
("Christina Donaldson ID = 12345", "N/A", "N/A"),
("Marcus Wallace ID = 321654", "N/A", "N/A"),
("N/A", "N/A", "Larry Jones ID = 847216"),
("N/A", "N/A", "Shaun Johnson ID = 753691"),
("N/A", "Brandon Brown ID = 147589", "N/A");"""



update = """
UPDATE salaries
SET salary = "$225,000"
WHERE First_Name = "Stephanie"; 
"""

delete_employee ="""
DELETE FROM employees
WHERE First_Name = "Brandon";
"""

#Call of functions
connection=create_server_connection("localhost", "root", "student", "hospital")
execute_query(connection, delete_employee)

