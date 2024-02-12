import sqlite3 as sql
from tkinter import *
import tkinter.messagebox as tkmb
import tkinter.ttk as ttk

ise = 0

conn = sql.connect("mydb.db")
cur = conn.cursor()

def callback(event):
    selected_indices = Lb1.curselection()
    print(selected_indices)



def add_page():
    global first_name, last_name,phone_number,email,addpage
    addpage = Toplevel()
    addpage.geometry("500x500")
    addpage.resizable(False,False)
    Label(addpage,text="Add a new Content",font=("Arial",22)).pack()
    Label(addpage,text="First Name",font=("Arial",15)).place(x=20,y=60)
    first_name = Entry(addpage,width=20,font=("Arial",10))
    first_name.place(x=150,y=70)

    Label(addpage,text="Last Name",font=("Arial",15)).place(x=20,y=120)
    last_name = Entry(addpage,width=20,font=("Arial",10))
    last_name.place(x=150,y=120)

    Label(addpage,text="Phone Number",font=("Arial",15)).place(x=20,y=180)
    phone_number = Entry(addpage,width=20,font=("Arial",10))
    phone_number.place(x=200,y=182)
    
    Label(addpage,text="Email Address",font=("Arial",15)).place(x=20,y=240)
    email = Entry(addpage,width=20,font=("Arial",10))
    email.place(x=200,y=250)

    send = ttk.Button(addpage,text="Add",command=add)
    send.place(x=200,y=300)


def add():
    global first_name, last_name,phone_number,email,Lb1,addpage,cur,conn
    l = [first_name.get(),last_name.get(),phone_number.get(),email.get(),Lb1.index(END)]
    # Lb1.insert(END,f"{first_name.get()}   {last_name.get()}    {phone_number.get()}    {email.get()}")
    sql_cmd = """INSERT 
                    INTO phones(firstname,lastname,phone,email,Field) VALUES (?,?,?,?,?)"""
    cur.execute(sql_cmd,l)
    conn.commit()
    collectdata()
    addpage.destroy()



def collectdata():
    global Lb1
    print("hi")

    sql_cmd = """SELECT * FROM phones"""
    res = cur.execute(sql_cmd)
    conn.commit() 
    Lb1.delete(0,END)
    data = res.fetchall()       
    for person in data:
        print(person)
        id = str(person[0]).center(5)
        name = str(person[1]).center(20)
        last_name = str(person[2]).center(20)
        phone = str(person[3]).center(20)
        email = str(person[4]).center(30)
        Lb1.insert(person[5],f"{id}{name}{last_name}{phone}{email}")




    
def edit_page():
    global first_name, last_name,phone_number,email,edite_page,Lb1,index
    index = Lb1.curselection()
    print(index)
    l = [index[0]]
    sql_cmd2 = """SELECT * FROM phones WHERE Field = ?"""
    res2 = cur.execute(sql_cmd2,l)
    res4 = res2.fetchall()
    edite_page = Toplevel()
    edite_page.geometry("500x500")
    edite_page.resizable(False,False)
    Label(edite_page,text="Edit a Content",font=("Arial",22)).pack()
    Label(edite_page,text="First Name",font=("Arial",15)).place(x=20,y=60)
    first_name = Entry(edite_page,width=20,font=("Arial",10))
    first_name.place(x=150,y=70)
    print(res4)
    first_name.insert(0,res4[0][1])

    Label(edite_page,text="Last Name",font=("Arial",15)).place(x=20,y=120)
    last_name = Entry(edite_page,width=20,font=("Arial",10))
    last_name.place(x=150,y=120)
    last_name.insert(0,res4[0][2])

    Label(edite_page,text="Phone Number",font=("Arial",15)).place(x=20,y=180)
    phone_number = Entry(edite_page,width=20,font=("Arial",10))
    phone_number.place(x=200,y=182)
    phone_number.insert(0,res4[0][3])
    
    Label(edite_page,text="Email Address",font=("Arial",15)).place(x=20,y=240)
    email = Entry(edite_page,width=20,font=("Arial",10))
    email.place(x=200,y=250)
    email.insert(0,res4[0][4])

    send = ttk.Button(edite_page,text="Edit",command=edit)
    send.place(x=200,y=300)


def edit():
    global first_name, last_name,phone_number,email,edite_page,Lb1,ise,index
    ise = 1
    delete()
    add()
    collectdata()
    edite_page.destroy()


def delete():
    global Lb1,ise,index
    if (not ise):
        sql_cmd2 = """SELECT * FROM phones"""
        res2 = cur.execute(sql_cmd2)
        index = Lb1.curselection()
        res4 = res2.fetchall()
        for person1 in res4:
            
            id = str(person1[0]).center(5)
            name = str(person1[1]).center(20)
            last_name = str(person1[2]).center(20)
            phone = str(person1[3]).center(20)
            email = str(person1[4]).center(30)
            id2 = Lb1.get(0, "end").index(f"{id}{name}{last_name}{phone}{email}") 
            l2 = [id2,id]
            sql_cmd3 = """ UPDATE phones SET Field = ? WHERE id = ? """
            cur.execute(sql_cmd3,l2)
            print(index)
        index = index[0] 
        l = [index]
        sql_cmd = """DELETE FROM phones WHERE Field=?"""
        cur.execute(sql_cmd,l)


        res3 = res2.fetchall()
        for person in res3:
            
            id = str(person[0]).center(5)
            name = str(person[1]).center(20)
            last_name = str(person[2]).center(20)
            phone = str(person[3]).center(20)
            email = str(person[4]).center(30)
            id2 = Lb1.get(0, "end").index(f"{id}{name}{last_name}{phone}{email}") 
            l2 = [id2,id]
            sql_cmd3 = """ UPDATE phones SET Field = ? WHERE id = ? """
            cur.execute(sql_cmd3,l2)

        conn.commit()
        collectdata()
    else:
        sql_cmd2 = """SELECT * FROM phones"""
        res2 = cur.execute(sql_cmd2)
        res4 = res2.fetchall()
        for person1 in res4:
            
            id = str(person1[0]).center(5)
            name = str(person1[1]).center(20)
            last_name = str(person1[2]).center(20)
            phone = str(person1[3]).center(20)
            email = str(person1[4]).center(30)
            id2 = Lb1.get(0, "end").index(f"{id}{name}{last_name}{phone}{email}") 
            l2 = [id2,id]
            sql_cmd3 = """ UPDATE phones SET Field = ? WHERE id = ? """
            cur.execute(sql_cmd3,l2)
            print(index)
        index = index[0] 
        l = [index]
        sql_cmd = """DELETE FROM phones WHERE Field=?"""
        cur.execute(sql_cmd,l)


    res3 = res2.fetchall()
    for person in res3:
        
        id = str(person[0]).center(5)
        name = str(person[1]).center(20)
        last_name = str(person[2]).center(20)
        phone = str(person[3]).center(20)
        email = str(person[4]).center(30)
        id2 = Lb1.get(0, "end").index(f"{id}{name}{last_name}{phone}{email}") 
        l2 = [id2,id]
        sql_cmd3 = """ UPDATE phones SET Field = ? WHERE id = ? """
        cur.execute(sql_cmd3,l2)
        collectdata()

    conn.commit()

def search():
    global Lb1,searchbox,root
    search_page = Toplevel(root)
    entery = searchbox.get()
    print(entery)
    l = [f"%{entery}%",f"%{entery}%",f"%{entery}%",f"%{entery}%"]
    sql_cmd = """SELECT * FROM phones WHERE firstname LIKE ? OR lastname LIKE ? OR phone LIKE ? OR email LIKE ?"""
    res = cur.execute(sql_cmd,l)
    conn.commit() 
    res = res.fetchall()
    print(res)
    search_page.geometry("1000x1000")
    search_page.title("Modern Phones Number UI using tkinter")
    search_page.resizable(False,False)
    # searchbox = Entry(editpage,width=50,font=("Arial",20))
    # searchbox.pack()

    en = ttk.Label(search_page,text="").pack(pady=10)
    addc = ttk.Button(search_page,text="Add Contact",command=add_page).place(x=170,y=45)
    deletc = ttk.Button(search_page,text="Delete Contact",command=delete).place(x=370,y=45)
    editc = ttk.Button(search_page,text="Edit Contact",command=edit_page).place(x=570,y=45)
    # searchc = ttk.Button(editpage,text="Search Contact",command=search).place(x=770,y=45)



    Lb1 = Listbox(search_page,width=70,font=("Arial",20))
    for person in res:
        id = str(person[0]).center(5)
        name = str(person[1]).center(20)
        last_name = str(person[2]).center(20)
        phone = str(person[3]).center(20)
        email = str(person[4]).center(30)
        Lb1.insert(END,f"{id}{name}{last_name}{phone}{email}")


    Lb1.pack()
    collectdata()


#Strat GUI with the Tkinter


root = Tk()
root.geometry("1000x1000")
root.title("Modern Phones Number UI using tkinter")
root.resizable(False,False)


searchbox = Entry(root,width=50,font=("Arial",20))
searchbox.pack()

en = ttk.Label(root,text="").pack(pady=10)
addc = ttk.Button(root,text="Add Contact",command=add_page).place(x=170,y=45)
deletc = ttk.Button(root,text="Delete Contact",command=delete).place(x=370,y=45)
editc = ttk.Button(root,text="Edit Contact",command=edit_page).place(x=570,y=45)
searchc = ttk.Button(root,text="Search Contact",command=search).place(x=770,y=45)



Lb1 = Listbox(root,width=70,font=("Arial",20))



Lb1.pack()


Lb1.bind('<<ListboxSelect>>', callback)

collectdata()

root.mainloop()