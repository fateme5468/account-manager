import os
import json
import hashlib
import secrets
import tkinter as tk
from tkinter import messagebox

# -------------set data file path-------------
DATA_FILE = os.path.expanduser(r"C:\User\fatma\text.txt")


def ensure_data_file():
    folder = os.path.dirname(DATA_FILE)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)


def load_data():
    ensure_data_file()
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def save_data(d):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)


# ---------- validations and hashing-----------
def _validate_username(username: str):
    
    assert username.count("@") == 1, "username wrong"
        
            


def _validate_password(password: str):
    assert len(password)>=8 , "eror len password"
    d1={'upper' :0, 'lower' :0, 'digit' :0, 'sp' : 0}
    
    for i in password:
        if i.isupper():
            d1['upper'] +=1
        elif i.islower():
            d1['lower']+=1
        elif i.isdigit():
            d1['digit'] += 1
        else :
            d1["sp"] += 1 
    assert d1['upper']!= 0 and d1['lower']!= 0 and d1['digit']!= 0 and d1["sp"]!= 0 , "password wrong"


def _hash_password(password: str, salt: str = None):
    if salt is None:
        salt = secrets.token_hex(16)
    h = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return salt, h


# --------the save function that is called by the window button---------
def on_submit():
    username = entry_username.get().strip()
    password = entry_password.get()

    try:
        _validate_username(username)
        _validate_password(password)
    except AssertionError as e:
        messagebox.showerror("input error", str(e))
        return

    data = load_data()
    # next id
    try:
        max_id = max(int(k) for k in data.keys()) if data else 0
    except ValueError:
        max_id = 0
    next_id = str(max_id + 1)

    salt, hashed = _hash_password(password)
    data[next_id] = {"username": username, "salt": salt, "password_hash": hashed}

    try:
        save_data(data)
    except Exception as e:
        messagebox.showerror('save error', f"Error while saving: {e}")
        return

    messagebox.showinfo("successful", f"Account saved(id={next_id}).")
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)


# ---------- creating a user interface with Tkinter- ----------
root = tk.Tk()
root.title("sign up")

# username label and input field
lbl_username = tk.Label(root, text="username:")
lbl_username.grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_username = tk.Entry(root, width=40)
entry_username.grid(row=0, column=1, padx=8, pady=8)

# password label and input field
lbl_password = tk.Label(root, text="password:")
lbl_password.grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry_password = tk.Entry(root, width=40, show="*")
entry_password.grid(row=1, column=1, padx=8, pady=8)

# send button
btn_submit = tk.Button(root, text="save", command=on_submit, width=12)
btn_submit.grid(row=2, column=0, columnspan=2, pady=12)

# window size and main loop start
root.resizable(False, False)
root.mainloop()