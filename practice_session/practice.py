# Practice Session
# Exercise 1
# Import sqlite3
# Import display from visualizer.py
# Connect to the simplefolks database and get a cursor
# Create a SELECT * query for the pets table
# Pass the output to display, run this file in the terminal, and check your results

import sqlite3

from visualizer import display

connection = sqlite3.connect('simplefolks.sqlite')
cursor = connection.cursor()

cursor.execute('SELECT * FROM pets')
display(cursor)

# Exercise 2
# In the pets table, it shows Sherry has 3 dogs. Update one of the dog's names to "Gizmo"
# Create an update query to make the change
# Execute the query
# Create a SELECT all query to retrieve the table 
# Execute the query and pass results to the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
UPDATE pets
SET name = 'Gizmo'
WHERE owner_name = 'Sherry' AND type = 'dog' AND name = 'Essy'
''')

cursor.execute('SELECT * FROM pets')
display(cursor)

# Exercise 3
# There is an error in the table. Michael's pet Xerses is not a horse, but a mouse. Update the record.
# Create an update query to make the change
# Execute the query
# Create a SELECT all query to retrieve the table 
# Execute the query and pass results to the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
UPDATE pets
SET type = 'mouse'
WHERE owner_name = 'Michael' AND name = 'Xerses'
''')

cursor.execute('SELECT * FROM pets')
display(cursor)

# Exercise 4
# Sadly, Carolina moved out of the neighborhood. Remove her from the table.
# Create a query to make the change
# Execute the query
# Create a SELECT all query to retrieve the table 
# Execute the query and pass results to the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
DELETE FROM pets
WHERE owner_name = 'Carolina'
''')

cursor.execute('SELECT * FROM pets')
display(cursor)

# Exercise 5 This election is awful, there are no good politicians running. Delete all the politicians from the
# politicians table Create a query to make the change Execute the query Create a SELECT all query to retrieve the
# table Execute the query and pass results to the display function Run this file in the terminal and check the output
# on tables.html

cursor.execute('''
DELETE FROM politicians
''')

cursor.execute('SELECT * FROM politicians')
display(cursor)

# Exercise 6
# Check to make certain all of your queries worked
# Add a method to save your changes to the tables
# Add a method to close the connection to the database

connection.commit()
connection.close()
