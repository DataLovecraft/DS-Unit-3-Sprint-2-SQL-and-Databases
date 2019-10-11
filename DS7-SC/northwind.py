import sqlite3

'''
part 2 - The Northwind Database
'''

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

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
Part 3 - Sailing the Northwind Seas
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
