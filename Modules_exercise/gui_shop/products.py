import json
import tkinter as tk
from PIL import Image, ImageTk

from canvas import app
from helpers import clean_screen

def update_current_user(username: str, product_id):
    with open("../db/users", "r+") as f:
        users = [json.loads(line.strip()) for line in f]

        for user in users:
            if user["username"] == username:
                user["products"].append(product_id)
                break

        f.seek(0)
        f.truncate()
        for u in users:
            f.write(json.dumps(u) + "\n")

def decrease_product_count(product_id):
    with open("../db/products", "r+") as f:
        products = [json.loads(line.strip()) for line in f]

        for product in products:
            if product["id"] == product_id:
                product["count"] = str(int(product["count"]) - 1)
                break

        f.seek(0)
        f.truncate()
        for p in products:
            f.write(json.dumps(p) + "\n")

def buy_product(product_id: str):
    decrease_product_count(product_id)

    with open("../db/current_user.txt") as f:
        current_user = f.read().strip()

    update_current_user(current_user, product_id)

    render_products_screen()

def render_products_screen():
    clean_screen()

    with open("../db/products") as f:
        max_products_per_line = 3
        for i, line in enumerate(f):
            product = json.loads(line)
            product_id = product.get("id")
            product_name = product.get("name")
            product_img_path = product.get("img_path")
            product_count = int(product.get("count"))

            if product_count == 0:
                continue

            lines_per_product = len(product)

            row = i // max_products_per_line * lines_per_product
            col = i % max_products_per_line

            tk.Label(app, text=product_name).grid(row=row, column=col)

            img = Image.open(f"../db/{product_img_path}")
            img = img.resize((200, 150))
            tk_img = ImageTk.PhotoImage(img)

            label = tk.Label(app, image=tk_img) #type: ignore
            label.image = tk_img
            label.grid(row=row + 1, column=col)

            tk.Label(app, text=product_count).grid(row=row + 2, column=col)

            tk.Button(
                app,
                text=f"Buy {product_id}",
                command=lambda p_id=product_id: buy_product(p_id)
            ).grid(row=row + 3, column=col)