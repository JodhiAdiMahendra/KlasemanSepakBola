import tkinter as tk
from tkinter import messagebox

class Klub:
    def __init__(self, nama, kota):
        self.nama = nama
        self.kota = kota
        self.main = 0
        self.menang = 0
        self.seri = 0
        self.kalah = 0
        self.goal_menang = 0
        self.goal_kalah = 0
        self.point = 0

def input_data_klub():
    nama = entry_nama_klub.get()
    kota = entry_kota_klub.get()
    return Klub(nama, kota)

def input_data_pertandingan():
    klub1 = entry_klub1.get()
    klub2 = entry_klub2.get()

    if klub1 not in klubs or klub2 not in klubs:
        messagebox.showerror("Error", "Klub tidak ditemukan.")
        return None

    score1 = int(entry_score1.get())
    score2 = int(entry_score2.get())
    return klub1, klub2, score1, score2

def update_klasemen(klub1, klub2, score1, score2):
    klubs[klub1].main += 1
    klubs[klub2].main += 1

    if score1 > score2:
        klubs[klub1].menang += 1
        klubs[klub1].point += 3
    elif score1 < score2:
        klubs[klub2].menang += 1
        klubs[klub2].point += 3
    else:
        klubs[klub1].seri += 1
        klubs[klub2].seri += 1
        klubs[klub1].point += 1
        klubs[klub2].point += 1

    klubs[klub1].goal_menang += score1
    klubs[klub2].goal_menang += score2
    klubs[klub1].goal_kalah += score2
    klubs[klub2].goal_kalah += score1

def view_klasemen():
    text_klasemen.delete("1.0", tk.END)
    text_klasemen.insert(tk.END, "{:<4} {:<15} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<5}\n".format("No", "Klub", "Ma", "Me", "S", "K", "GM", "GK", "Point"))
    for i, klub in enumerate(sorted(klubs.values(), key=lambda x: (x.point, x.goal_menang - x.goal_kalah), reverse=True), start=1):
        text_klasemen.insert(tk.END, "{:<4} {:<15} {:<4} {:<4} {:<4} {:<4} {:<4} {:<4} {:<5}\n".format(
            i, klub.nama, klub.main, klub.menang, klub.seri, klub.kalah, klub.goal_menang, klub.goal_kalah, klub.point))

def menu_input_data_klub():
    klub = input_data_klub()
    if klub.nama not in klubs:
        klubs[klub.nama] = klub
        messagebox.showinfo("Info", "Data Klub berhasil disimpan.")
    else:
        messagebox.showerror("Error", "Klub sudah ada.")

def menu_input_skor_pertandingan():
    mode = input_mode.get()
    if mode == "A":
        pertandingan = input_data_pertandingan()
        if pertandingan:
            pertandingans.append(pertandingan)
            update_klasemen(*pertandingan)
            messagebox.showinfo("Info", "Data Pertandingan berhasil disimpan.")
    elif mode == "B":
        while True:
            pertandingan = input_data_pertandingan()
            if pertandingan:
                pertandingans.append(pertandingan)
                messagebox.showinfo("Info", "Data Pertandingan berhasil disimpan.")
            else:
                break
        view_klasemen()

def menu_view_klasemen():
    view_klasemen()

# Membuat objek Tkinter
app = tk.Tk()
app.title("Aplikasi Klasemen Sepak Bola")

# Membuat variabel global
klubs = {}
pertandingans = []

# Membuat widget dan menempatkannya di dalam grid
label_nama_klub = tk.Label(app, text="Nama Klub:")
label_nama_klub.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_nama_klub = tk.Entry(app)
entry_nama_klub.grid(row=0, column=1, padx=10, pady=5, sticky="w")

label_kota_klub = tk.Label(app, text="Kota Klub:")
label_kota_klub.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_kota_klub = tk.Entry(app)
entry_kota_klub.grid(row=1, column=1, padx=10, pady=5, sticky="w")

button_save_klub = tk.Button(app, text="Save", command=menu_input_data_klub)
button_save_klub.grid(row=2, column=0, columnspan=2, pady=10)

label_klub1 = tk.Label(app, text="Klub 1:")
label_klub1.grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_klub1 = tk.Entry(app)
entry_klub1.grid(row=3, column=1, padx=10, pady=5, sticky="w")

label_klub2 = tk.Label(app, text="Klub 2:")
label_klub2.grid(row=4, column=0, padx=10, pady=5, sticky="e")

entry_klub2 = tk.Entry(app)
entry_klub2.grid(row=4, column=1, padx=10, pady=5, sticky="w")

label_score1 = tk.Label(app, text="Score 1:")
label_score1.grid(row=5, column=0, padx=10, pady=5, sticky="e")

entry_score1 = tk.Entry(app)
entry_score1.grid(row=5, column=1, padx=10, pady=5, sticky="w")

label_score2 = tk.Label(app, text="Score 2:")
label_score2.grid(row=6, column=0, padx=10, pady=5, sticky="e")

entry_score2 = tk.Entry(app)
entry_score2.grid(row=6, column=1, padx=10, pady=5, sticky="w")

label_mode = tk.Label(app, text="Mode Input (A/B):")
label_mode.grid(row=7, column=0, padx=10, pady=5, sticky="e")

input_mode = tk.StringVar(value="A")
entry_mode = tk.Entry(app, textvariable=input_mode)
entry_mode.grid(row=7, column=1, padx=10, pady=5, sticky="w")

button_save_pertandingan = tk.Button(app, text="Save", command=menu_input_skor_pertandingan)
button_save_pertandingan.grid(row=9, column=0, columnspan=2, pady=5)

button_view_klasemen = tk.Button(app, text="View Klasemen", command=menu_view_klasemen)
button_view_klasemen.grid(row=10, column=0, columnspan=2, pady=10)

text_klasemen = tk.Text(app, height=15, width=70)
text_klasemen.grid(row=11, column=0, columnspan=2, pady=10)

# Menjalankan main loop
app.mainloop()
