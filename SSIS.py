from tkinter import ttk
import csv
from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Student Information System")
top.geometry("500x400")
top.config(bg ='black')
top.resizable(False, False)

def records():
    root = Tk()
    root.title("RECORDS")
    root.geometry("800x400")
    root.config(bg = 'white')
    root.resizable(False, False)

    def search():
        if s.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE ENTER THE ID NUMBER.")

        top2 = Tk()
        top2.title("Student Information System")
        top2.geometry("800x200")
        top2.config(bg='white')
        top2.resizable(False, False)

        frm1 = Frame(top2)
        frm1.pack(side=LEFT, padx=10, pady=(0, 120))

        tree = ttk.Treeview(frm1, columns=(1, 2, 3, 4), show="headings", height=13)
        tree.pack()

        tree.heading(1, text="Name", anchor=CENTER)
        tree.heading(2, text="ID Number", anchor=CENTER)
        tree.heading(3, text="Gender", anchor=CENTER)
        tree.heading(4, text="Course", anchor=CENTER)

        with open("studentlist.csv", 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if s.get() in row[1]:
                    tree.insert('', 'end', values=(row))

        top2.mainloop()

    def select():
        selected = tree.focus()
        values = tree.item(selected, 'values')
        E5.insert(0, values[0])
        ED.insert(0, values[1])
        E6.insert(0, values[2])
        E7.insert(0, values[3])

    def edit():

        if E5.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")
        elif ED.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")
        elif E6.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")
        elif E7.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")

        d1 = E5.get()
        d2 = ED.get()
        d3 = E6.get()
        d4 = E7.get()

        sel = tree.selection()
        tree.item(sel, values=(d1, d2, d3, d4))

        updatedlist = []
        with open("studentlist.csv", 'r', newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if ED.get() == row[1]:
                    row[0] = d1
                    row[2] = d3
                    row[3] = d4
                updatedlist.append(row)

        with open("studentlist.csv", "w", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerows(updatedlist)

        messagebox.showinfo("UPDATED","YEHEY! DATA UPDATED")

        E5.delete(0, END)
        ED.delete(0, END)
        E6.delete(0, END)
        E7.delete(0, END)

    def delete():

        if E5.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")
        elif ED.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")
        elif E6.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")
        elif E7.get() == '':
            return messagebox.showwarning("WARNING!", "PLEASE, PRESS 'SELECT' BUTTON.")

        x = tree.selection()
        tree.delete(x)

        updatedlist = list()
        with open("studentlist.csv", 'r', newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if ED.get() != row[1]:
                    updatedlist.append(row)

        with open("studentlist.csv", "w", newline="") as f:
            Writer = csv.writer(f)
            Writer.writerows(updatedlist)
        messagebox.showinfo("DELETED","YEHEY! DATA DELETED")

        E5.delete(0, END)
        ED.delete(0, END)
        E6.delete(0, END)
        E7.delete(0, END)

    frm = Frame(root)
    frm.pack(side=LEFT, padx=5, pady=(0,200))

    tree = ttk.Treeview(frm, columns=(1, 2, 3, 4), show = "headings", height=13)
    tree.pack()

    tree.heading(1, text ="Name", anchor=CENTER)
    tree.heading(2, text="ID Number", anchor=CENTER)
    tree.heading(3, text="Gender", anchor=CENTER)
    tree.heading(4, text="Course", anchor=CENTER)

    with open('studentlist.csv') as f:
        reader = csv.DictReader(f, delimiter=',')

        for row in reader:
            name = row['Name']
            id_number = row['ID Number']
            gender = row['Gender']
            course = row['Course']

            tree.insert('','end', values=(name, id_number, gender, course))


    S = Button(root, text="SELECT", command=select)
    S.place(x=100,y=305)
    GR = Button(root, text="UPDATE", command=edit)
    GR.place(x=183, y=305)
    D = Button(root, text="DELETE", command=delete)
    D.place(x=270, y=305)
    E = Button(root, text="SEARCH", command=search)
    E.place(x=740, y=200)

    E5 = Entry(root, bd=3, width=35)
    E5.place(x=100, y=200)
    ED = Entry(root, bd=3, width=35)
    ED.place(x=100, y=225)
    E6 = Entry(root, bd=3, width=35)
    E6.place(x=100, y=250)
    E7 = Entry(root, bd=3, width=35)
    E7.place(x=100, y=275)
    s = Entry(root, bd=3, width=35)
    s.place(x=520, y=203)

    LName = Label(root, text = "NAME:", bg="white", font=("Lucida Console", 10, "bold"))
    LName.place(x = 0, y = 200)
    LID_number = Label(root, text="ID NUMBER:", bg="white", font=("Lucida Console", 10, "bold"))
    LID_number.place(x=0, y=225)
    LGender = Label(root, text="GENDER:", bg="white", font=("Lucida Console", 10, "bold"))
    LGender.place(x=0, y=250)
    LCourse = Label(root, text="COURSE:", bg="white", font=("Lucida Console", 10, "bold"))
    LCourse.place(x=0, y=275)
    LSearch = Label(root, text = "ID Number to Find:", bg="white", font=("Lucida Console", 10, "bold"))
    LSearch.place(x =350, y = 203)

    root.mainloop()


def register():
    #headerList = ['Name', 'ID Number', 'Gender', 'Course']
    #with open('studentlist.csv', 'a') as file:
         #dw = csv.DictWriter(file, delimiter = ',', fieldnames = headerList)
         #dw.writeheader()

    if E1.get() == '':
        return messagebox.showwarning("WARNING!", "TRY AGAIN")
    elif E2.get() == '':
        return messagebox.showwarning("WARNING!", "TRY AGAIN")
    elif E3.get() == '':
        return messagebox.showwarning("WARNING!", "TRY AGAIN")
    elif E4.get() == '':
        return messagebox.showwarning("WARNING!", "TRY AGAIN")

    name = E1.get()
    id_number = E2.get()
    gender = E3.get()
    course = E4.get()

    with open('studentlist.csv', 'a', newline = '') as f:
        w = csv.writer(f,dialect='excel')
        w.writerow([
            name,
            id_number,
            gender,
            course])

    messagebox.showinfo("YEHEY!", "YOU JUST GOT REGISTERED!")

    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)

L = LabelFrame(top, text = "Registration Form", width = 500, height = 200, bg = "black", fg ="white", font=("Lucida Console", 20, "bold"))
L.place(x=0, y=0)
L0 = LabelFrame(top, text = "Student's Information", width = 500, height = 200, bg = "black", fg ="white", font=("Lucida Console", 20, "bold"))
L0.place(x=0, y=200)
L1 = Label(top, text = "NAME:", bg = "black", fg = "white", font=("Lucida Console", 11, "bold"))
L1.place(x = 70, y = 50)
L2 = Label(top, text = "ID NUMBER:", bg = "black", fg = "white", font=("Lucida Console", 11, "bold"))
L2.place(x = 70, y = 80)
L3 = Label(top, text = "GENDER:", bg = "black", fg = "white", font=("Lucida Console", 11, "bold"))
L3.place(x = 70, y = 110)
L4 = Label(top, text = "COURSE:", bg = "black", fg = "white", font=("Lucida Console", 11, "bold"))
L4.place(x = 70, y = 140)

E1 = Entry(top, bd = 3, width = 35)
E1.place(x = 180, y = 50)
E2 = Entry(top, bd = 3, width = 35)
E2.place(x = 180, y = 80)
E3 = Entry(top, bd = 3, width = 35)
E3.place(x = 180, y = 110)
E4 = Entry(top, bd = 3, width = 35)
E4.place(x = 180, y = 140)


B = Button(top, text = "REGISTER",font=("Lucida Console", 9, "bold"), command=register)
B.place(x=410, y=170)

G = PhotoImage(file="record.icon.png")
R = Frame(top, width = 120, height = 145, highlightbackground = "white", highlightthickness = 2, bg = "black")
R.place(x = 200, y = 240)
C = Button(top, image = G, borderwidth = 0, compound = CENTER, command=records, activebackground = "white", bg = "black")
C.place(x=210, y=245)

top.mainloop()