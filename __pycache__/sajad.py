import os
import json
import hashlib
import secrets
import tkinter as tk
from tkinter import messagebox

# ---------- تنظیم مسیر فایل داده ----------
DATA_FILE = os.path.expanduser("~/sajjad.txt")


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


# ---------- اعتبارسنجی‌ها و هش کردن ----------
def _validate_email(email: str):
    
    assert email.count("@") == 1, "eror @"
        
            


def _validate_password(password: str):
    assert len(password)>=8 , "eror len password"
    bozorg = kochik = ph = adad = 0
    for i in password:
        if i.isdigit():
            adad +=1
        elif i.isupper():
            bozorg+=1
        elif i.islower():
            kochik += 1
        else :
            ph += 1 
    assert bozorg!= 0 and kochik != 0 and adad != 0 and ph != 0 , "ramz zaef ast"


def _hash_password(password: str, salt: str = None):
    if salt is None:
        salt = secrets.token_hex(16)
    h = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    return salt, h


# ---------- تابع ذخیره که توسط دکمهٔ پنجره صدا زده میشه ----------
def on_submit():
    email = entry_email.get().strip()
    password = entry_password.get()

    try:
        _validate_email(email)
        _validate_password(password)
    except AssertionError as e:
        messagebox.showerror("خطا در ورودی", str(e))
        return

    data = load_data()
    # تعیین id بعدی
    try:
        max_id = max(int(k) for k in data.keys()) if data else 0
    except ValueError:
        max_id = 0
    next_id = str(max_id + 1)

    salt, hashed = _hash_password(password)
    data[next_id] = {"email": email, "salt": salt, "password_hash": hashed}

    try:
        save_data(data)
    except Exception as e:
        messagebox.showerror("خطا در ذخیره", f"خطا هنگام ذخیره‌سازی: {e}")
        return

    messagebox.showinfo("موفق", f"حساب ذخیره شد (id={next_id}).")
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)


# ---------- ساخت رابط کاربری با Tkinter ----------
root = tk.Tk()
root.title("ثبت ایمیل و پسورد")

# لیبل و ورودی ایمیل
lbl_email = tk.Label(root, text="ایمیل:")
lbl_email.grid(row=0, column=0, padx=8, pady=8, sticky="e")
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=0, column=1, padx=8, pady=8)

# لیبل و ورودی پسورد (مخفی)
lbl_password = tk.Label(root, text="رمز عبور:")
lbl_password.grid(row=1, column=0, padx=8, pady=8, sticky="e")
entry_password = tk.Entry(root, width=40, show="*")
entry_password.grid(row=1, column=1, padx=8, pady=8)

# دکمه ارسال
btn_submit = tk.Button(root, text="ذخیره", command=on_submit, width=12)
btn_submit.grid(row=2, column=0, columnspan=2, pady=12)

# اندازه پنجره و شروع لوپ
root.resizable(False, False)
root.mainloop()

