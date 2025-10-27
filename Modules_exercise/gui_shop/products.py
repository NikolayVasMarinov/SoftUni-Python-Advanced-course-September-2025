import json
import tkinter as tk
from PIL import Image, ImageTk

from canvas import app
from helpers import clean_screen


def render_products_screen():
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

            label = tk.Label(app, image=tk_img)
            label.img = tk_img
            label.grid(row=1, column=i)

            tk.Label(app, text=product_count).grid(row=2, column=i)

            tk.Button(
                app,
                text=f"Buy {product_id}"
            ).grid(row=3, column=i)
