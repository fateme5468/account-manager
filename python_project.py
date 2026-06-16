import tkinter as tk
import  v
f2=open(r'C:\Users\NORI\Desktop\save.taxt','a')
lines=f2.readlines()
f2.close

if len(lines)==0:
    varible_id=1
else:
    last_line=lines[-1]
    last_id=last_line.split(':')[0]
    varible_id=int(last_id.strip())
flag=True ; id=varible_id
while flag:
    v.validation(id,input('username:',input('password:')))
    retry=input('no/yes:').lower()
    if retry=='no':
        flag=False
    id+=1
def vali():
    entry_s=tk.Entry(width=30)
    entry_p=tk.Entry(width=30)

    tk.Label.config(text="Enter your username:")
    tk.Label.config(text="Enter your password:")

window=tk.Tk()
window.title('sign up')
window.geometry(300*500)
window.button(text='sign in')
command=vali,fg='red'
window.mainloop()

v.validation(id,'entry_s:','entry_p:z')
