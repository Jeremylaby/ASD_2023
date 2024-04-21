import tkinter as tk
from tkinter import ttk

from PIL import Image,ImageTk
# Funkcja do wyświetlania informacji na płótnie
def display_info():
    # Wyczyść płótno, jeśli jest już coś na nim
    canvas.delete("all")
    
    # Wyświetl tekst na płótnie
    text = "To jest przykładowy tekst."
    canvas.create_text(1000, 1000, text=text, font=("Arial", 12), fill="blue")

# Inicjalizacja okna głównego
root = tk.Tk()
root.title("Wyświetlanie informacji na płótnie")
root.geometry("750x500")
root.maxsize(750,500)
root.minsize(750,500)

background_image = Image.open("gym.jpg")
background_image = background_image.resize((750, 500), Image.ADAPTIVE)
# Konwertuj obraz na format, który tkinter może wykorzystać
background_photo = ImageTk.PhotoImage(background_image)

# Utwórz etykietę z obrazem jako tłem
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)
background_label.pack()
root.configure(borderwidth=5, relief="ridge")  # Ustawienie obramowania z szerokością 5 pikseli i efektem "ridge"
root.configure(bg="lightblue")
frame_bg=Image.open("frame3.png")
frame_bg=frame_bg.resize((193,156),Image.ADAPTIVE)
frame_bgg=ImageTk.PhotoImage(frame_bg)
menu_frame=tk.Canvas(background_label,width=193,height=156)
menu_frame.place(relx=0.5,rely=0.2,anchor="center")




root.mainloop()