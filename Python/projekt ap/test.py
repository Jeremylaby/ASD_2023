import tkinter as tk

def create_input_fields():
    num_fields = int(num_fields_entry.get())

    # Usunięcie wcześniej utworzonych ramek
    for frame in input_frames:
        frame.destroy()

    # Usunięcie wcześniejszych zmiennych Entry
    for entry_var in entry_vars:
        entry_var.set("")

    # Tworzenie nowych ramek i pól wprowadzania danych
    for i in range(num_fields):
        frame = tk.Frame(form_frame)
        frame.pack()

        label_text = f"Pole {i + 1}"
        label = tk.Label(frame, text=label_text)
        label.pack(side="left")

        entry_var = tk.StringVar()
        entry = tk.Entry(frame, textvariable=entry_var)
        entry.pack(side="left")

        entry_vars.append(entry_var)
        input_frames.append(frame)

def save_user_info():
    user_info = [entry_var.get() for entry_var in entry_vars]

    info_label.config(text="Wprowadzone informacje:\n" + "\n".join(user_info))

root = tk.Tk()
root.title("Formularz użytkownika")

num_fields_label = tk.Label(root, text="Podaj liczbę pól:")
num_fields_label.pack()

num_fields_entry = tk.Entry(root)
num_fields_entry.pack()

create_fields_button = tk.Button(root, text="Utwórz pola", command=create_input_fields)
create_fields_button.pack()

form_frame = tk.Frame(root)
form_frame.pack()

input_frames = []
entry_vars = []

create_input_fields_button = tk.Button(form_frame, text="Zapisz informacje", command=save_user_info)
create_input_fields_button.pack()

info_label = tk.Label(root, text="", font=("Arial", 12))
info_label.pack()
string="vvsdfsf0123456789"
print(string[-10:])
root.mainloop()
