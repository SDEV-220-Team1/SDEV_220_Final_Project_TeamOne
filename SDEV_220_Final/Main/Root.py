import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a SQLite database and table to store user information
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

def create_user():
    new_username = entry_new_username.get()
    new_password = entry_new_password.get()

    # Check if the username already exists
    cursor.execute('SELECT * FROM users WHERE username=?', (new_username,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
    else:
        # Insert the new user into the database
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (new_username, new_password))
        conn.commit()
        messagebox.showinfo("Success", "User created successfully!")

def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password match a user in the database
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    matched_user = cursor.fetchone()

    if matched_user:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Create the main window
root = tk.Tk()
root.title("Login System")

# Create and place widgets for creating a new user
label_new_username = tk.Label(root, text="New Username:")
label_new_username.pack(pady=10)
entry_new_username = tk.Entry(root)
entry_new_username.pack(pady=10)

label_new_password = tk.Label(root, text="New Password:")
label_new_password.pack(pady=10)
entry_new_password = tk.Entry(root, show="*")
entry_new_password.pack(pady=10)

button_create_user = tk.Button(root, text="Create User", command=create_user)
button_create_user.pack(pady=10)

# Create and place widgets for logging in
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=10)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=10)

button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()

# Close the database connection when the program exits
conn.close()