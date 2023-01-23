import tkinter as tk

def on_button_click():
    global count
    count += 1
    label.config(text=f"Tombol ditekan {count} kali!")

root = tk.Tk()
root.title("Jumlah Tekan")

count = 0
label = tk.Label(root, text="Selamat datang di program GUI sederhana")
label.pack()

button = tk.Button(root, text="Tekan Sini", command=on_button_click)
button.pack()

root.mainloop()