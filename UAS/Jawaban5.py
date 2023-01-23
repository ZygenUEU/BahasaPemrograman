import tkinter as tk
from tkinter import messagebox

import mysql.connector


def on_save_button_click():
    # ambil data dari form
    name = name_entry.get()
    age = age_entry.get()

    # sisipkan data ke tabel
    insert_data = "INSERT INTO karyawan (nama, umur) VALUES (%s, %s)"
    cursor.execute(insert_data, (name, age))
    cnx.commit()

    # tampilkan pesan berhasil
    messagebox.showinfo("Info", "Data berhasil disimpan!")

    # kosongkan form
    name_entry.delete(0, 'end')
    age_entry.delete(0, 'end')


def on_view_button_click():
    # hapus data dari listbox
    listbox.delete(0, 'end')

    # ambil data dari tabel
    select_data = "SELECT * FROM karyawan"
    cursor.execute(select_data)

    # tampilkan data ke listbox
    for row in cursor:
        listbox.insert('end', row)

# konfigurasi koneksi ke database
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'uasbp',
    'raise_on_warnings': True
}

# membuat koneksi ke database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# membuat form aplikasi
root = tk.Tk()
root.title("Menyimpan data")
root.geometry("700x350")

# membuat label dan entry untuk nama
name_label = tk.Label(root, text="Nama:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# membuat label dan entry untuk usia
age_label = tk.Label(root, text="Usia:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# membuat tombol simpan
save_button = tk.Button(root, text="Simpan", command=on_save_button_click)
save_button.grid(row=2, column=0)

# membuat tombol tampilkan
view_button = tk.Button(root, text="Tampilkan", command=on_view_button_click)
view_button.grid(row=2, column=1)

# membuat listbox untuk menampilkan data
listbox = tk.Listbox(root, width=100)
listbox.grid(row=3, column=0, columnspan=100)
root.mainloop()
