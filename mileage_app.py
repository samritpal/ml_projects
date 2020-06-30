import tkinter as tk
import pickle

with open('mileage.pkl', 'rb') as fp:
    model = pickle.load(fp)
    fp.close()


root=tk.Tk()
h=tk.DoubleVar()
w=tk.DoubleVar()
d=tk.DoubleVar()
m=tk.DoubleVar()
def predict():
    price=model.predict([[h.get(),w.get(),d.get()]])[0]
    m.set(price)
def clear():
    h.set('')
    w.set('')
    d.set('')
    m.set('')

f1=tk.Frame(root)
label1=tk.Label(f1,text='Horsepower',fg='white',bg='black').pack(side=tk.LEFT)
e1=tk.Entry(f1,textvariable=h,bg='#eeeeee', fg='#333333').pack()
f1.pack(fill=tk.BOTH,padx=20)
f2=tk.Frame(root)
label2=tk.Label(f2,text='weight',fg='white',bg='black').pack(side=tk.LEFT)
e2=tk.Entry(f2,textvariable=w,bg='#eeeeee', fg='#333333').pack()
f2.pack(fill=tk.BOTH,padx=20)
f3=tk.Frame(root)
label3=tk.Label(f3,text='Displacement',fg='white',bg='black').pack(side=tk.LEFT)
e3=tk.Entry(f3,textvariable=d,bg='#eeeeee', fg='#333333').pack()
f3.pack(fill=tk.BOTH,padx=20)
f4=tk.Frame(root)
label4=tk.Label(f4,text='Milage',fg='white',bg='black').pack(side=tk.LEFT)
e4=tk.Entry(f4,textvariable=m,bg='#eeeeee', fg='#333333').pack()
f4.pack(fill=tk.BOTH,padx=20)
pb=tk.Button(root,text='Predict',fg='white',bg='black',command=predict).pack(fill=tk.X)

eb=tk.Button(root,text='Exit',fg="black",bg='red',command=root.quit).pack(fill=tk.X)
cb=tk.Button(root,text='clear',fg='black',bg='cyan',command=clear).pack(fill=tk.X)
root.title('Mileage Calculator')
root.mainloop()
