import sqlite3
conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

'''
*******************************
part 2 - The Northwind Database
*******************************
'''

# What are the ten most expensive items (per unit price) in the database and their suppliers?
print('What are the ten most expensive items (per unit price) in the database?')

curs.execute('SELECT Id, ProductName, UnitPrice '
             'FROM Product '
             'ORDER BY UnitPrice DESC '
             'LIMIT 10;')

print('\n'.join([str(row) for row in curs]), '\n')
print('='*80)

# What is the average age of an employee at the time of their hiring?
print('What is the average age of an employee at the time of their hiring?')
curs.execute('SELECT AVG((JULIANDAY(HireDate)-JULIANDAY(Birthdate))/365.25) '
             'FROM Employee;')
print(curs.fetchall(), '\n')
print('='*80)

# How does the average age of employee at hire vary by city?
print('How does the average age of employee at hire vary by city?')
curs.execute('SELECT City, '
             'AVG((JULIANDAY(HireDate)-JULIANDAY(Birthdate))/365.25) '
             'FROM Employee '
             'GROUP BY City;')
print('\n'.join([str(row) for row in curs]), '\n')
print('='*80)

'''
***********************************
Part 3 - Sailing the Northwind Seas
***********************************
'''

# What are the ten most expensive items (per unit price) in the database and their suppliers?

print('What are the ten most expensive items (per unit price) in the '
      'database and their suppliers?')
curs.execute('SELECT Supplier.Id, CompanyName, top10.Id, ProductName, '
             'UnitPrice FROM '
             '(SELECT Id, SupplierID, ProductName, UnitPrice '
             'FROM Product '
             'ORDER BY UnitPrice DESC '
             'LIMIT 10) AS top10 '
             'JOIN Supplier ON top10.SupplierId = Supplier.Id;')
print('\n'.join([str(row) for row in curs]), '\n')
print('='*80)

# What is the largest category (by number of unique products in it)?
print('What is the largest category (by number of unique products in it)?')
curs.execute('SELECT CategoryID, CategoryName, '
             'COUNT(Product.ID) AS numProducts '
             'FROM Category LEFT OUTER JOIN Product ON '
             'Product.CategoryID = Category.Id '
             'GROUP BY CategoryID, CategoryName '
             'ORDER BY numProducts DESC '
             'LIMIT 1;')
print(curs.fetchall(), '\n')
print('='*80)


# Who's the employee with the most territories?
print('Who\'s the employee with the most territories?')
curs.execute('SELECT Employee.Id, Title, FirstName, LastName, numTerritories '
             'FROM '
             '(SELECT EmployeeID, COUNT(TerritoryID) as numTerritories '
             'FROM EmployeeTerritory '
             'GROUP BY EmployeeID '
             'ORDER BY numTerritories DESC '
             'LIMIT 1) '
             'JOIN Employee ON EmployeeID = Employee.Id;')
print(curs.fetchall(), '\n')



'''
OUTPUT:

What are the ten most expensive items (per unit price) in the database?
(38, 'Côte de Blaye', 263.5)
(29, 'Thüringer Rostbratwurst', 123.79)
(9, 'Mishi Kobe Niku', 97)
(20, "Sir Rodney's Marmalade", 81)
(18, 'Carnarvon Tigers', 62.5)
(59, 'Raclette Courdavault', 55)
(51, 'Manjimup Dried Apples', 53)
(62, 'Tarte au sucre', 49.3)
(43, 'Ipoh Coffee', 46)
(28, 'Rössle Sauerkraut', 45.6)

================================================================================
What is the average age of an employee at the time of their hiring?
[(37.28344360787892,)]

================================================================================
How does the average age of employee at hire vary by city?
('Kirkland', 28.588637919233403)
('London', 32.82819986310746)
('Redmond', 55.619438740588635)
('Seattle', 39.77275838466804)
('Tacoma', 40.48459958932238)

================================================================================
What are the ten most expensive items (per unit price) in the database and their suppliers?
(18, 'Aux joyeux ecclésiastiques', 38, 'Côte de Blaye', 263.5)
(12, 'Plutzer Lebensmittelgroßmärkte AG', 29, 'Thüringer Rostbratwurst', 123.79)
(4, 'Tokyo Traders', 9, 'Mishi Kobe Niku', 97)
(8, 'Specialty Biscuits, Ltd.', 20, "Sir Rodney's Marmalade", 81)
(7, 'Pavlova, Ltd.', 18, 'Carnarvon Tigers', 62.5)
(28, 'Gai pâturage', 59, 'Raclette Courdavault', 55)
(24, "G'day, Mate", 51, 'Manjimup Dried Apples', 53)
(29, "Forêts d'érables", 62, 'Tarte au sucre', 49.3)
(20, 'Leka Trading', 43, 'Ipoh Coffee', 46)
(12, 'Plutzer Lebensmittelgroßmärkte AG', 28, 'Rössle Sauerkraut', 45.6)

================================================================================
What is the largest category (by number of unique products in it)?
[(3, 'Confections', 13)]

================================================================================
Who's the employee with the most territories?
[(7, 'Sales Representative', 'Robert', 'King', 10)]
'''
