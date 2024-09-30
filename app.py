# Exercise 1 
#
# Import sqlite3
# Import the display function from visualizer.py
# Create/Connect to the game.db database
# Get a cursor so you can write queries to the database
# Create a table called "scoreboard" with 3 columns:
# Round
# Player name
# Score
# make sure to check the table does not exist
# Run a SELECT query and show the output with the visualizer 
# to check that everything worked

import sqlite3

from visualizer import display

connection = sqlite3.connect('game.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS scoreboard(
    Round INTEGER,
    Player TEXT,
    Score INTEGER
)
''')

cursor.execute('SELECT * FROM scoreboard')
display(cursor)

# Write a INSERT query to add 4 players to the scoreboard table 
# Imagine you're playing your favorite game and all players are on Round (or level) 1
# Execute the query
# Create a SELECT query to retrieve the scoreboard table
# add a clause to show the highest score first, execute the query
# Check the output using the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
INSERT INTO scoreboard (Round, Player, Score) VALUES
(1, 'Alice', 100),
(1, 'Bob', 200),
(1, 'Charlie', 300),
(1, 'David', 400)
''')

cursor.execute('SELECT * FROM scoreboard ORDER BY Score DESC')
display(cursor)

# Exercise 2
# Write an UPDATE query to change Round to 2
# Execute the query
# Create a SELECT query to retrieve the scoreboard table showing the score from highest to lowest
# Execute the query and check the output using the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
UPDATE scoreboard
SET Round = 2
''')

cursor.execute('SELECT * FROM scoreboard ORDER BY Score DESC')
display(cursor)

# Exercise 3
# Write an UPDATE query to put a different player in the lead.
# Execute the query
# Create a SELECT query to retrieve the scoreboard table showing the score from highest to lowest
# Execute the query and check the output using the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
UPDATE scoreboard
SET Score = 500
WHERE Player = 'Charlie'
''')

cursor.execute('SELECT * FROM scoreboard ORDER BY Score DESC')
display(cursor)

# Exercise 4
# Write a DELETE query to remove one of your players from the game
# Execute the query
# Create a SELECT query to retrieve the scoreboard table showing the score from highest to lowest
# Execute the query and check the output using the display function
# Run this file in the terminal and check the output on tables.html

cursor.execute('''
DELETE FROM scoreboard
WHERE Player = 'David'
''')

cursor.execute('SELECT * FROM scoreboard ORDER BY Score DESC')
display(cursor)

# * Exercise 5 is in app_test.py *

# Exercise 6
# Commit your changes and close the connection to the database
# Run this file in the terminal
# Run app_test.py in the terminal and check the output with tables.html

connection.commit()
connection.close()
