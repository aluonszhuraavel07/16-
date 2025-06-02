import tkinter as tk
from PIL import Image, ImageTk

def move_image():
    canvas.move(car_id, 5, 0)
    canvas.after(50, move_image)

root = tk.Tk()
root.title("Анімація машини")
root.geometry("800x300")

canvas = tk.Canvas(root, width=800, height=300, bg="white")
canvas.pack()

car_img = Image.open("car.png").resize((100, 60))
car_photo = ImageTk.PhotoImage(car_img)

car_id = canvas.create_image(0, 120, anchor=tk.NW, image=car_photo)

move_image()

root.mainloop()