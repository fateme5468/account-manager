import tkinter as tk
def data(year , month , day : int) :
    assert 1 <= month <=12 and 1<= day <= 31 , "wrong format"
    if month == 10 and day > 10 or month > 10 :
        return year + 622

    return year + 621

def calc() :
    try :
        year = int(year_entry.get())
        mounth= int(month_entry.get())
        day = int(day_entry.get())
        result = data(year , mounth , day)
        lbl_result.config(text=f'Result:{result}')
    except Exception as e :
        lbl_result.config(text= f'Error : {e}')
root = tk.Tk()
root.geometry("300x200")
root.title('Date change')
tk.Label(root, text="year: ",bg='light green').pack()
year_entry = tk.Entry(root)
year_entry.pack()

tk.Label(root, text='month: ',bg='light green').pack()
month_entry = tk.Entry(root)
month_entry.pack()

tk.Label(root, text="day: ",bg='light green').pack()
day_entry = tk.Entry(root)
day_entry.pack()

tk.Button(root, text='convert',
command=calc,bg='green').pack(pady=10)
lbl_result = tk.Label(root, text="")
lbl_result.pack()

root.mainloop()
