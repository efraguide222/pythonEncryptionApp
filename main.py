# Modul Base64
import base64

# Modul Hashlib
import hashlib

# Ui python
from tkinter import *

# Alert
from tkinter import messagebox

# Import the cryptography library
from cryptography.fernet import Fernet

screen = Tk()
# Merubah icons program dengan logo 2D
screen.iconbitmap("./img/2d.ico")

# Ukuran aplikasi
screen.geometry("500x500")

# Title aplikasi paling atas
screen.title("Program Dekripsi dan Enkripsi Sederhana")

# warna background aplikasi
screen.configure(bg="#87CEFA")

# Nonaktifkan pembesaran ui program
screen.resizable(width=False, height=False)


#   FUNGSI ENKRIPSI MULAI


def encrypt():
    bahanKey = code.get()
    keyMd5 = hashlib.md5(bytes(bahanKey, "utf-8"))
    key = base64.b64encode(bytes(keyMd5.hexdigest(), "utf-8"))

    f = Fernet(key)
    screen1 = Toplevel(screen)
    screen1.title("Data di Enkripsi")
    screen1.geometry("400x250")
    screen1.configure(bg="#000000")

    message = text1.get(1.0, END)
    encode_message = message.encode("ascii")
    encrypt = f.encrypt(encode_message)

    Label(screen1, text="Kode telah tersandi", font="impack 10 bold").place(x=5, y=6)
    text2 = Text(screen1, font="30", bd=4, wrap=WORD)
    text2.place(x=2, y=30, width=390, height=180)
    text2.insert(END, encrypt)


# FUNGSI ENKRIPSI SELESAI


# FUNGSI DEKRIPSI MULAI


def decrypt():
    message = text1.get(1.0, END)
    encode_message = message.encode("ascii")
    try:
        bahanKey = code.get()
        keyMd5 = hashlib.md5(bytes(bahanKey, "utf-8"))
        key = base64.b64encode(bytes(keyMd5.hexdigest(), "utf-8"))

        f = Fernet(key)
        decode_script = f.decrypt(encode_message)
        decrypt = decode_script.decode("ascii")
        screen2 = Toplevel(screen)
        screen2.title("Data telah di dekripsi")
        screen2.geometry("400x250")
        screen2.configure(bg="#2E8B57")

        Label(screen2, text="Kode telah tersandi", font="impack 10 bold").place(
            x=5, y=6
        )
        text2 = Text(screen2, font="30", bd=4, wrap=WORD)
        text2.place(x=2, y=30, width=390, height=180)
        text2.insert(END, decrypt)

    except:
        messagebox.showerror("Error", "Kode root yang anda masukkan salah")


# FUNGSI DEKRIPSI SELESAI


# FUNGSI RESET TOMBOL MULAI
def reset():
    text1.delete(1.0, END)


# FUNGSI RESET TOMBOL SELESAI

# Text
text1 = Text(screen, font="20")
text1.place(x=5, y=45, width=490, height=160)

# Label
Label(screen, text="Silahkan masukkan sandi", font="impack 13 bold").place(x=144, y=290)

# Entry
code = StringVar()
Entry(textvariable=code, bd=4, font="20", show="*").place(x=129, y=220)

# Label
Label(
    screen,
    text="Masukkan text untuk mengenkripsi dan mendekripsi",
    font="impack 14 bold",
    bg="aliceblue",
).place(x=5, y=6)

# Text
text1 = Text(screen, font="20")
text1.place(x=5, y=45, width=490, height=160)


# setting tombol
Button(
    screen,
    text="Encrypt",
    font="arial 15 bold",
    bg="#FFD700",
    fg="white",
    width="10",
    command=encrypt,
).place(x=70, y=370)
Button(
    screen,
    text="Decrypt",
    font="arial 15 bold",
    bg="#228B22",
    fg="white",
    width="10",
    command=decrypt,
).place(x=298, y=370)
Button(
    screen,
    text="Reset",
    font="arial 15 bold",
    bg="#DC143C",
    fg="white",
    width="10",
    command=reset,
).place(x=185, y=450)
mainloop()
