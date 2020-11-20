from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Using database")
#Data base

# #Creating a data base
# conn = sqlite3.connect("address_book.db")

# #Creating a cursor
# c = conn.cursor()

#create Table

# c.execute("""CREATE TABLE addresses(
#     first_name text,
#     last_name text,
#     address text,
#     city text,
#     zipcode integer
#     )""")
def update():
    global editor
    #Creating a data base
    conn = sqlite3.connect("address_book.db")

    #Creating a cursor
    c = conn.cursor()
    record_id =del_box.get()
    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        zipcode = :zipcode

        WHERE oid = :oid""",
        {
        "first" : f_name.get(),
        "last" : l_name.get(),
        "address" : addres.get(),
        "city":city.get(),
        "zipcode":zipcode.get(),

        "oid" : record_id

        })
    #commit changes
    conn.commit()

    #close connection
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    addres.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    editor.destroy()
def submit():
    #Creating a data base
    conn = sqlite3.connect("address_book.db")

    #Creating a cursor
    c = conn.cursor()

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :addres, :city, :zipcode)",
            {
                'f_name' : f_name.get(),
                'l_name' : l_name.get(),
                'addres' : addres.get(),
                'city' : city.get(),
                'zipcode' : zipcode.get(),
            })


    #commit changes
    conn.commit()

    #close connection
    conn.close()
    f_name.delete(0,END)
    l_name.delete(0,END)
    addres.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    
#delete a rec
def del_rec(value):
    #Creating a data base
    conn = sqlite3.connect("address_book.db")

    #Creating a cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid="+value)
    #commit changes
    conn.commit()
    #close connection
    conn.close()


#function for query
def query():
    #Creating a data base
    conn = sqlite3.connect("address_book.db")

    #Creating a cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records=c.fetchall()
    top = Toplevel()
    top.title("Record data")
    print(records)
    print_rec = ' '
    for record in records:
        for value in record:
            print_rec += str(value) +"\n"
        print_rec += "\n\n"
    print(print_rec)
    Label(top, text = print_rec).grid(row=0,column=0,columnspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

#edit the record
def edit():
    global editor
    editor = Tk()
    editor.title("Updating database")
    record_id =del_box.get()
    #Creating a data base
    conn = sqlite3.connect("address_book.db")

    #Creating a cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses WHERE oid ="+record_id)
    records=c.fetchall()
    
    #commit changes
    conn.commit()

    #close connection
    conn.close()
    #creating global variables for update func
    global f_name
    global l_name
    global addres
    global city
    global zipcode
    
    #creating input section
    f_name = Entry(editor, width=30)
    f_name.grid(row=0,column=1,padx=20)
    l_name = Entry(editor, width=30)
    l_name.grid(row=1,column=1,padx=20)
    addres = Entry(editor, width=30)
    addres.grid(row=2,column=1,padx=20)
    city = Entry(editor, width=30)
    city.grid(row=3,column=1,padx=20)
    zipcode = Entry(editor, width=30)
    zipcode.grid(row=4,column=1,padx=20)
    #set value
    for record in records:
        if record[-1] == int(record_id):
            f_name.insert(0,record[0])
            l_name.insert(0,record[1])
            addres.insert(0,record[2])
            city.insert(0,record[3])
            zipcode.insert(0,record[4])
    #creating label
    f_name1 = Label(editor, text="first_name")
    f_name1.grid(row=0,column=0)
    l_name1 = Label(editor, text="last_name")
    l_name1.grid(row=1,column=0)
    addres1 = Label(editor, text="address")
    addres1.grid(row=2,column=0)
    city1 = Label(editor, text="city")
    city1.grid(row=3,column=0)
    zipcode1 = Label(editor, text="zipcode")
    zipcode1.grid(row=4,column=0)
    save_button=Button(editor,text="Save",command=update)
    save_button.grid(row=5,column=0,columnspan=2,padx =10, pady=10, ipadx=112)
    editor.mainloop()


    
#creating input section
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1,padx=20)
addres = Entry(root, width=30)
addres.grid(row=2,column=1,padx=20)
city = Entry(root, width=30)
city.grid(row=3,column=1,padx=20)
zipcode = Entry(root, width=30)
zipcode.grid(row=4,column=1,padx=20)
#del id entry box
del_box = Entry(root,width=30)
del_box.grid(row=7 ,column=1,padx=10,pady=10)
#creating label
f_name1 = Label(root, text="first_name")
f_name1.grid(row=0,column=0)
l_name1 = Label(root, text="last_name")
l_name1.grid(row=1,column=0)
addres1 = Label(root, text="address")
addres1.grid(row=2,column=0)
city1 = Label(root, text="city")
city1.grid(row=3,column=0)
zipcode1 = Label(root, text="zipcode")
zipcode1.grid(row=4,column=0)
del_box1 = Label(root,text="ODI NO:")
del_box1.grid(row=7,column=0)
#adding rec
button =Button(root, text="Add record",command=submit)
button.grid(row = 5,column=0,columnspan=2,padx =10, pady=10, ipadx=100)

#query button
qry_button = Button(root,text="Get data",command =query)
qry_button.grid(row=6,column=0,columnspan=2,padx =10, pady=10, ipadx=107)


#create a del button
del_button=Button(root,text="Delete",command =lambda :del_rec(del_box.get()))
del_button.grid(row=8,column=0,columnspan=2,padx =10, pady=10, ipadx=112)

#create an update button
update_button=Button(root,text="Update",command =edit)
update_button.grid(row=10,column=0,columnspan=2,padx =10, pady=10, ipadx=112)

root.mainloop()