import json
import tkinter as tk

from canvas import app
from helpers import clean_screen
from products import render_products_screen


def register(username: str, password: str, first_name: str, last_name: str):
    data = {
        "username": username,
        "password": password,
        "first name": first_name,
        "last name": last_name,
        "products": []
    }

    with open("../db/user_credentials_db", "a") as f:
        f.write(json.dumps(data) + "\n")

    render_login_screen()

def render_register_screen():
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)
    first_name = tk.Entry(app)
    first_name.grid(row=2, column=0)
    last_name = tk.Entry(app)
    last_name.grid(row=3, column=0)

    tk.Button(
        app,
        text="Register",
        bg="green",
        fg="white",
        command=lambda: register(username.get(), password.get(), first_name.get(), last_name.get())
    ).grid(row=4, column=0)

def login(username: str, password: str):
    with open("../db/user_credentials_db") as file:
        data = file.readlines()
        for line in data:
            user = json.loads(line)
            name = user.get("username")
            pwd = user.get("password")

            if name == username and pwd == password:
                render_products_screen()
                return

    render_login_screen(error="Invalid username/password")

def render_login_screen(error: str = None):
    clean_screen()
    username = tk.Entry(app)
    username.grid(row=0, column=0)
    password = tk.Entry(app)
    password.grid(row=1, column=0)

    tk.Button(
        app,
        text="Enter",
        bg="green",
        fg="black",
        command=lambda: login(username.get(), password.get())
    ).grid(row=2, column=0)

    if error:
        tk.Label(app, text=error).grid(row=3, column=0)


def render_main_enter_screen():
    tk.Button(
        app,
        text="Login",
        bg="green",
        fg="white",
        command=render_login_screen
    ).grid(row=0, column=0)

    tk.Button(
        app,
        text="Register",
        bg="yellow",
        fg="black",
        command = render_register_screen
    ).grid(row=0, column=1)