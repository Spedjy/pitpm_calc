from tkinter import *
def m():
    try: 
        l1["text"]=float(e1.get())-float(e2.get())
    except:
        l1["text"]="Введите числа"
def p():
    try:
        l1["text"]=float(e1.get())+float(e2.get())
    except:
        l1["text"]="Введите числа"
def y():
    try:
        l1["text"]=float(e1.get())*float(e2.get())
    except:
        l1["text"]="Введите числа"
def d():
    try:   
        l1["text"]=float(e1.get())/float(e2.get())
    except:
        l1["text"]="Введите числа или замените второе число"
root=Tk()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2-200
h = h//2-200
root.geometry(f'200x173+{w}+{h}')
e1=Entry(root, text="Введите число 1",bg="#DDA0DD",border="3")
e2=Entry(root, text="Введите число 2",bg="#DDA0DD",border="3")
e1.pack(fill=X)
e2.pack(fill=X)
bm=Button(root,text="-",bg="#FFC0CB",command=m, border="5")
bm.pack(fill=X)
bp=Button(root,text="+",bg="#FFB6C1",command=p, border="5")
bp.pack(fill=X)
by=Button(root,text="*",bg="#FF69B4",command=y, border="5")
by.pack(fill=X)
bd=Button(root,text="/",bg="#FF1493",command=d, border="5")
bd.pack(fill=X)
l1=Label(root,text="")
l1.pack()
root.mainloop()