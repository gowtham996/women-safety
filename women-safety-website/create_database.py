import sqlite3

# Connect to the SQLite database (create it if it doesn't exist)
conn = sqlite3.connect('women_safety.db')
cursor = conn.cursor()

# Create a Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        age INTEGER NOT NULL,
        password TEXT NOT NULL
    )
''')

# Create a Friendships table to store friend relationships
cursor.execute('''
    CREATE TABLE IF NOT EXISTS friendships (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        friend_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (friend_id) REFERENCES users(id),
        UNIQUE (user_id, friend_id)
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()
