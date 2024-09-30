# Exercise 5
# Import sqlite3
# Import the display function from visualizer.py
# Create/Connect to the game.db database
# Create a SELECT query to retrieve the scoreboard table showing the score from highest to lowest
# Execute the query and check the output using the display function
# Don't forget to run this file in the terminal

import sqlite3

from visualizer import display

connection = sqlite3.connect('game.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM scoreboard ORDER BY Score DESC')
display(cursor)
