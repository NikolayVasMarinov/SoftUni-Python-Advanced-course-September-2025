import json
import tkinter as tk

from canvas import app
from helpers import clean_screen
from products import render_products_screen


def register(**user):
    user["products"] = []

    with open("../db/user_credentials_db", "r+") as f:
        users = [line.strip().split(", ")[0] for line in f]
        if user["username"] in users:
            render_register_screen(error="User already exists!")
            return

        f.write(f"{user['username']}, {user['password']}\n")

    with open("../db/users", "r+") as f:
        f.write(json.dumps(user) + "\n")

    render_login_screen()

def render_register_screen(error: str = None):
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
        command=lambda: register(
            username=username.get(),
            password=password.get(),
            first_name=first_name.get(),
            last_name=last_name.get()
        )
    ).grid(row=4, column=0)

    if error:
        tk.Label(app, text=error).grid(row=5, column=0)

def login(username: str, password: str):
    with open("../db/user_credentials_db") as file:
        data = file.readlines()
        for line in data:
            name, pwd = line.strip().split(", ")

            if name == username and pwd == password:
                with open("../db/current_user.txt", "w") as f:
                    f.write(name)

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