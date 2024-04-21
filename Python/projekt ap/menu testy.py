import tkinter as tk
from PIL import Image, ImageTk
curent_scale=1
def switch_image():
    global current_image_index,curent_scale
    curent_scale/=1.5
    current_image_index = (current_image_index + 1) % len(images)
    canvas.itemconfig(image_item, image=images[current_image_index].subsample(curent_scale))

root = tk.Tk()
root.title("Przełączanie obrazów")

# Wczytaj tło jako obraz
background_image = Image.open("gym.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Wczytaj obrazy PNG
image_paths = ["frame3.png", "frame.png"]
images = [ImageTk.PhotoImage(Image.open(path)) for path in image_paths]
current_image_index = 0

# Utwórz Canvas do wyświetlania obrazów
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Wyświetl tło
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Wyświetl początkowy obraz PNG
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=images[current_image_index])

# Utwórz przycisk do przełączania obrazów
switch_button = tk.Button(root, text="Przełącz obraz", command=switch_image)
switch_button.pack()

root.mainloop()