import tkinter as tk
import math

root = tk.Tk()
root.title("Серце і Овал")

canvas = tk.Canvas(root, width=600, height=500, bg='white')
canvas.pack()

canvas.create_oval(220, 100, 350, 180, fill='gold', outline='black')

x_center = 100
y_center = 140
size = 5
points = []

for t in range(0, 360, 1):
    t_rad = math.radians(t)
    x = size * 16 * math.sin(t_rad)**3
    y = -size * (13 * math.cos(t_rad) - 5 * math.cos(2*t_rad) -
                 2 * math.cos(3*t_rad) - math.cos(4*t_rad))
    points.append((x_center + x, y_center + y))

flat_points = [coord for point in points for coord in point]
canvas.create_polygon(flat_points, fill='red', outline='black')

canvas.create_rectangle(200,200,400,400,fill="#40FF5C",outline="black")
canvas.create_rectangle(225,225,275,275,fill="white",outline="black")
canvas.create_rectangle(325,225,375,275,fill="white",outline="black")
canvas.create_rectangle(225,225,275,275,fill="white",outline="black")
canvas.create_rectangle(250,250,275,275,fill="black")
canvas.create_rectangle(325,250,350,275,fill="black")
canvas.create_rectangle(275,300,325,275,fill="#269637",outline="black")
canvas.create_rectangle(325,325,350,300,fill="#269637",outline="black")
canvas.create_rectangle(250,325,275,300,fill="#269637",outline="black")
canvas.create_rectangle(275,325,325,300,fill="black")
canvas.create_rectangle(250,325,350,350,fill="black")

root.mainloop()