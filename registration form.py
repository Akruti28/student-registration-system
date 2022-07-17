from tkinter import *
def sh():
    print(name.get(),no.get(),rv.get(),cb1.get(),cb2.get())
    msg='Registration Successful  '+name.get()+'!!!!'
    msg=msg.center(100)
    print(msg)
    Label(a,text=msg,font=('times new roman',16)).place(x=40,y=500)
a= Tk()
a.geometry('700x600')
a.title('Employee Registration Form')
a['bg']='#A1B1C1'

Label(a,text='WELCOME!!!!!').pack()

Label(a,text='Employee Name').place(x=10,y=20)
name= Entry(a)
name.place(x=120,y=20)
Label(a,text='Employee no').place(x=20,y=50)
no= Entry(a,show='*')
no.place(x=120,y=50)

rv=StringVar()
Label(a,text='Select Gender').place(x=20,y=150)
Radiobutton(a,text='Male',value='M',variable=rv).place(x=120,y=150)
Radiobutton(a,text='Female',value='F',variable=rv).place(x=220,y=150)
Radiobutton(a,text='Other',value='O',variable=rv).place(x=320,y=150)

cb1=IntVar()
cb2=IntVar()
Label(a,text='Select Course').place(x=20,y=250)
Checkbutton(a,text='Python',onvalue=1,offvalue=0,variable=cb1).place(x=120,y=250)
Checkbutton(a,text='Javascript',onvalue=1,offvalue=0,variable=cb2).place(x=220,y=250)

Button(a, text='Submit',command=sh).place(x=400,y=400)


a.mainloop()