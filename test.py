#trying round clock
import tkinter as tk

def create_circle(x, y, r, canvas, outline_color="black", fill_color="white"):  
    canvas.create_oval(x - r, y - r, x + r, y + r, outline=outline_color, fill=fill_color, width=2)
    canvas.create_text(x, y, text="Hello", font=("Arial", 14), fill="white")  # Add text inside the circle

root = tk.Tk()
root.geometry("300x300")

# Create a Canvas to draw shapes
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a circle at (150, 150) with radius 50, filled with blue
create_circle(150, 150, 50, canvas, outline_color="black", fill_color="blue")

root.mainloop()
