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

def buy_product(product_id: str, count: int):
    if count == 0:
        render_products_screen(error="Out of stock")
        return

    else:
        decrease_product_count(product_id)

        with open("../db/current_user.txt") as f:
            current_user = f.read().strip()

        update_current_user(current_user, product_id)

    render_products_screen()

def render_products_screen(error: str = None):
    clean_screen()

    with open("../db/products") as f:
        for i, line in enumerate(f):
            product = json.loads(line)
            product_id = product.get("id")
            product_name = product.get("name")
            product_img_path = product.get("img_path")
            product_count = product.get("count")

            tk.Label(app, text=product_name).grid(row=0, column=i)

            img = Image.open(f"../db/{product_img_path}")
            img = img.resize((200, 150))
            tk_img = ImageTk.PhotoImage(img)

            label = tk.Label(app, image=tk_img) #type: ignore
            label.image = tk_img
            label.grid(row=1, column=i)

            tk.Label(app, text=product_count).grid(row=2, column=i)

            tk.Button(
                app,
                text=f"Buy {product_id}",
                command=lambda c=int(product_count), p_id=product_id: buy_product(p_id, c)
            ).grid(row=3, column=i)

        if error:
            tk.Label(app, text=error).grid(row=4, column=0)