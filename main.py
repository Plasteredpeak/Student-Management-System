from tkinter import *
import tkinter.messagebox
import os.path

def lab_e():
    lab = labm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[6] = lab + "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    labw.destroy()

def cal_e():
    cal = calm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[5] = cal + "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    calw.destroy()

def Ap_e():
    ap = Apm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[0] = ap + "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    Ap.destroy()

def isl_e():
    isl = islm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[3] = isl + "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    islw.destroy()

def eng_e():
    eng = engm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[2] = eng + "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    engw.destroy()

def ict_e():
    ict = ictm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[1] = ict+ "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    ict_w.destroy()

def pp_e():
    ppit = ppm.get()
    Sf = open(reg+"m.txt", "r").readlines()
    Sf[4] = ppit + "\n"
    w = open(reg+"m.txt", "w")
    w.writelines(Sf)
    w.close()
    ppitw.destroy()

def lab_ew():
    global labw
    labw = Toplevel(Tw)
    labw.configure(bg="black")
    labw.geometry("200x150")
    labw.resizable(0, 0)
    global labm
    labm = StringVar()
    labw.title("change")
    Label(labw, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(labw, textvariable=labm, width=25)
    e.grid(row=2, pady=10)
    b = Button(labw, text="OK", bg="white", fg="black", width=10, height=1, command=lab_e).grid(row=3, pady=5)
    labw.mainloop()

def cal_ew():
    global calw
    calw = Toplevel(Tw)
    calw.configure(bg="black")
    calw.geometry("200x150")
    calw.resizable(0, 0)
    global calm
    calm = StringVar()
    calw.title("change")
    Label(calw, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(calw, textvariable=calm, width=25)
    e.grid(row=2, pady=10)
    b = Button(calw, text="OK", bg="white", fg="black", width=10, height=1, command=cal_e).grid(row=3, pady=5)
    calw.mainloop()

def ppit_ew():
    global ppitw
    ppitw = Toplevel(Tw)
    ppitw.configure(bg="black")
    ppitw.geometry("200x150")
    ppitw.resizable(0, 0)
    global ppm
    ppm = StringVar()
    ppitw.title("change")
    Label(ppitw, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(ppitw, textvariable=ppm, width=25)
    e.grid(row=2, pady=10)
    b = Button(ppitw, text="OK", bg="white", fg="black", width=10, height=1, command=pp_e).grid(row=3, pady=5)
    ppitw.mainloop()

def isl_ew():
    global islw
    islw = Toplevel(Tw)
    islw.configure(bg="black")
    islw.geometry("200x150")
    islw.resizable(0, 0)
    global islm
    islm = StringVar()
    islw.title("change")
    Label(islw, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(islw, textvariable=islm, width=25)
    e.grid(row=2, pady=10)
    b = Button(islw, text="OK", bg="white", fg="black", width=10, height=1, command=isl_e).grid(row=3, pady=5)
    islw.mainloop()

def eng_ew():
    global engw
    engw = Toplevel(Tw)
    engw.configure(bg="black")
    engw.geometry("200x150")
    engw.resizable(0, 0)
    global engm
    engm = StringVar()
    engw.title("change")
    Label(engw, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(engw, textvariable=engm, width=25)
    e.grid(row=2, pady=10)
    b = Button(engw, text="OK", bg="white", fg="black", width=10, height=1, command=eng_e).grid(row=3, pady=5)
    engw.mainloop()

def ict_ew():
    global ict_w
    ict_w = Toplevel(Tw)
    ict_w.configure(bg="black")
    ict_w.geometry("200x150")
    ict_w.resizable(0, 0)
    global ictm
    ictm = StringVar()
    ict_w.title("change")
    Label(ict_w, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(ict_w, textvariable=ictm, width=25)
    e.grid(row=2, pady=10)
    b = Button(ict_w, text="OK", bg="white", fg="black", width=10, height=1, command=ict_e).grid(row=3, pady=5)
    ict_w.mainloop()

def AP_ew():
    global Ap
    Ap = Toplevel(Tw)
    Ap.configure(bg="black")
    Ap.geometry("200x150")
    Ap.resizable(0, 0)
    global Apm
    Apm = StringVar()
    Ap.title("change")
    Label(Ap, text="Enter new Marks:", bg="black", fg="white", font="calibri 14 bold").grid(row=1, pady=10, padx=30)
    e = Entry(Ap, textvariable=Apm, width=25)
    e.grid(row=2, pady=10)
    b = Button(Ap, text="OK", bg="white", fg="black", width=10, height=1, command=Ap_e).grid(row=3, pady=5)
    Ap.mainloop()
def EditTd():
    Td = nT_d.get()
    Sf=open("teacher info.txt","r").readlines()
    Sf[4]=Td + "\n"
    w=open("teacher info.txt","w")
    w.writelines(Sf)
    w.close()
    T_esw.destroy()
def EditTf():
    Tfield = nT_field.get()
    Sf=open("teacher info.txt","r").readlines()
    Sf[5]=Tfield + "\n"
    w=open("teacher info.txt","w")
    w.writelines(Sf)
    w.close()
    T_efw.destroy()
def EditTemail():
    Temail = nT_email.get()
    Sf=open("teacher info txt","r").readlines()
    Sf[2]=Temail + "\n"
    w=open("teacher info.txt","w")
    w.writelines(Sf)
    w.close()
    T_eenw.destroy()
def EditTCn():
    STno = nT_Cn.get()
    Sf=open("teacher info.txt","r").readlines()
    Sf[1]=STno + "\n"
    w=open("teacher info.txt","w")
    w.writelines(Sf)
    w.close()
    T_eCnw.destroy()
def EditTn():
    Tname = nT_name.get()
    Sf=open("teacher info.txt","r").readlines()
    Sf[0]=Tname + "\n"
    w=open("teacher info.txt","w")
    w.writelines(Sf)
    w.close()
    T_enw.destroy()

def EditTd_w():
    global T_esw
    T_esw=Toplevel(Aw)
    T_esw.configure(bg="black")
    T_esw.geometry("230x150")
    T_esw.resizable(0,0)
    global nT_d
    nT_d = StringVar()
    T_esw.title("Change department")
    Label(T_esw,text="Enter new department:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(T_esw,textvariable=nT_d,width=25)
    e.grid(row=2,pady=10)
    b=Button(T_esw,text="OK",bg="white",fg="black",width=10,height=1,command=EditTd).grid(row=3,pady=5)
def EditTf_w():
    global T_efw
    T_efw=Toplevel(Aw)
    T_efw.configure(bg="black")
    T_efw.geometry("230x150")
    T_efw.resizable(0,0)
    global nT_field
    nT_field = StringVar()
    T_efw.title("change teacher field")
    Label(T_efw,text="Enter new field:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(T_efw,textvariable=nT_field,width=25)
    e.grid(row=2,pady=10)
    b=Button(T_efw,text="OK",bg="white",fg="black",width=10,height=1,command=EditTf).grid(row=3,pady=5)
def EditTemail_w():
    global T_eenw
    T_eenw=Toplevel(Aw)
    T_eenw.configure(bg="black")
    T_eenw.geometry("200x150")
    T_eenw.resizable(0,0)
    global nT_email
    nT_email = StringVar()
    T_eenw.title("Change E-mail")
    Label(T_eenw,text="Enter new E-mail:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(T_eenw,textvariable=nT_email,width=25)
    e.grid(row=2,pady=10)
    b=Button(T_eenw,text="OK",bg="white",fg="black",width=10,height=1,command=EditTemail).grid(row=3,pady=5)
def EditTCn_w():
    global T_eCnw
    T_eCnw=Toplevel(Aw)
    T_eCnw.configure(bg="black")
    T_eCnw.geometry("200x150")
    T_eCnw.resizable(0,0)
    global nT_Cn
    nT_Cn = StringVar()
    T_eCnw.title("change Contact No:")
    Label(T_eCnw,text="Enter Contact No:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(T_eCnw,textvariable=nT_Cn,width=25)
    e.grid(row=2,pady=10)
    b=Button(T_eCnw,text="OK",bg="white",fg="black",width=10,height=1,command=EditTCn).grid(row=3,pady=5)



def EditTn_w():
    global T_enw
    T_enw=Toplevel(Aw)
    T_enw.configure(bg="black")
    T_enw.geometry("200x150")
    T_enw.resizable(0,0)
    global nT_name
    nT_name = StringVar()
    T_enw.title("change Teacher name")
    Label(T_enw,text="Enter new Name:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(T_enw,textvariable=nT_name,width=25)
    e.grid(row=2,pady=10)
    b=Button(T_enw,text="OK",bg="white",fg="black",width=10,height=1,command=EditTn).grid(row=3,pady=5)
    T_enw.mainloop()
def Te_w():
    if os.path.exists("teacher info.txt"):
        Tvw = Toplevel(Aw)
        Tvw.geometry("550x600")
        Tvw.configure(bg="#002b2b")
        Tvw.resizable(0, 0)
        Tvw.title("VIEW INFO")

        Sf = open("teacher info.txt", "r").readlines()
        T_name = Sf[0]
        Tf = open("teacher login info.txt", "r").read()
        Tf = Tf.split()
        U_name = Tf[0]
        P = Tf[1]
        TC_no = Sf[1]
        T_email = Sf[2]
        T_field = Sf[3]
        T_dep = Sf[4]
        Label(Tvw, text="Teacher details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                           padx=10, pady=5)
        Label(Tvw, text="Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                      sticky="e")
        Label(Tvw, text="\n"+T_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
        b1 = Button(Tvw, text="Edit", bg="white", fg="black", width=10, height=1,command=EditTn_w).grid(row=2, column=2,
                                                                                                         padx=10, pady=5)
        Label(Tvw, text="User Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                           sticky="e")
        Label(Tvw, text="\n"+U_name, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)
        Label(Tvw, text="Password:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                         pady=5, sticky="e")
        Label(Tvw, text="\n"+P, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
        Label(Tvw, text="Contact no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                            pady=5, sticky="e")
        Label(Tvw, text="\n"+TC_no, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
        b2 = Button(Tvw, text="Edit", bg="white", fg="black", width=10, height=1,command=EditTCn_w ).grid(row=5, column=2,
                                                                                         padx=10, pady=5)
        Label(Tvw, text="Email:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                       sticky="e")
        Label(Tvw, text="\n"+T_email, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
        b3 = Button(Tvw, text="Edit", bg="white", fg="black", width=10, height=1, command=EditTemail_w).grid(row=6, column=2,
                                                                                         padx=10, pady=5)
        Label(Tvw, text="Field:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                       sticky="e")
        Label(Tvw, text="\n"+T_field, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
        b4 = Button(Tvw, text="Edit", bg="white", fg="black", width=10, height=1,command=EditTf_w ).grid(row=7, column=2,
                                                                                         padx=10, pady=5)
        Label(Tvw, text="Department:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30,
                                                                                            pady=5,
                                                                                            sticky="e")
        Label(Tvw, text="\n"+T_dep, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)
        b5 = Button(Tvw, text="Edit", bg="white", fg="black", width=10, height=1,command=EditTd_w ).grid(row=8, column=2,
                                                                                         padx=10, pady=5)


        Button(Tvw, text="Cancel", width=10, height=2, bg="#480607", fg="White", command=Tvw.destroy).grid(row=10,
                                                                                                            column=1,
                                                                                                            pady=10, padx=0)

        Tvw.mainloop()
    else:
        tkinter.messagebox.showerror("Not found","Info doesn't exist\n Try Adding")
def T_f():
    a=tkinter.messagebox.askquestion("Confirmartion","DO you want to fire Teacher")
    if a == "yes":
        os.remove("teacher info.txt")
def T_vr():
    Tvw = Toplevel(Aw)
    Tvw.geometry("550x600")
    Tvw.configure(bg="#002b2b")
    Tvw.resizable(0, 0)
    Tvw.title("VIEW INFO")

    Sf = open("teacher info.txt", "r").readlines()
    T_name = Sf[0]
    Tf = open("teacher login info.txt", "r").read()
    Tf = Tf.split()
    U_name = Tf[0]
    P = Tf[1]
    TC_no = Sf[1]
    T_email = Sf[2]
    T_field = Sf[3]
    T_dep = Sf[4]
    Label(Tvw, text="Teacher details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                       padx=10, pady=5)
    Label(Tvw, text="Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                  sticky="e")
    Label(Tvw, text="\n"+T_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
    Label(Tvw, text="User Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                    sticky="e")
    Label(Tvw, text="\n"+U_name, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)
    Label(Tvw, text="Password:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                           pady=5, sticky="e")
    Label(Tvw, text="\n"+P, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
    Label(Tvw, text="Contact no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                        pady=5, sticky="e")
    Label(Tvw, text="\n"+TC_no, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
    Label(Tvw, text="Email:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                   sticky="e")
    Label(Tvw, text="\n"+T_email, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
    Label(Tvw, text="Field:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                   sticky="e")
    Label(Tvw, text="\n"+T_field, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
    Label(Tvw, text="Department:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                      sticky="e")
    Label(Tvw, text="\n"+T_dep, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)

    Button(Tvw, text="Go back", width=10, height=2, bg="#480607", fg="White", command=Tvw.destroy).grid(row=10,
                                                                                                        column=2,
                                                                                                        pady=10, padx=0)
    Button(Tvw, text="Fire", width=10, height=2, bg="#480607", fg="White", command=T_f).grid(row=10,
                                                                                                           column=0,
                                                                                                           pady=10,
                                                                                                           padx=30,
                                                                                                           sticky="w")

    Tvw.mainloop()
def T_clear():
    te1.delete(0, END)
    te4.delete(0, END)
    te5.delete(0, END)
    te6.delete(0, END)
    te7.delete(0, END)
def Save_Tr():
    name = T_name.get()
    c_no = TC_no.get()
    email = T_email.get()
    field = T_field.get()
    subject = T_subject.get()
    Sf = open("teacher info.txt", "w")
    Sf.write(str(name) + "\n")
    Sf.write(str(c_no) + "\n")
    Sf.write(str(email) + "\n")
    Sf.write(str(field) + "\n")
    Sf.write(str(subject) + "\n")
    Sf.close()
    Trw.destroy()

def T_r():
    if os.path.exists("teacher info.txt"):
        tkinter.messagebox.showerror("Already exists","Try viewing or Editing")
    else:

        global Trw
        global T_name
        global U_name
        global P
        global TC_no
        global T_email
        global T_field
        global T_subject
        global te1
        global te4
        global te5
        global te6
        global te7
        Trw = Toplevel(Aw)
        Trw.geometry("530x500")
        Trw.configure(bg="#0e4d92")
        Trw.resizable(0, 0)
        T_name = StringVar()
        Tf=open("teacher login info.txt","r").read()
        Tf=Tf.split()
        U_name=Tf[0]
        P=Tf[1]
        TC_no=StringVar()
        T_email=StringVar()
        T_field=StringVar()
        T_subject=StringVar()
        Label(Trw, text="Teacher details:", bg="#0e4d92", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                           padx=10, pady=10)
        Label(Trw, text="Name:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=2, column=0, padx=30, pady=10,
                                                                                      sticky="e")
        e1 = Entry(Trw, textvariable=T_name,width=30)
        e1.grid(row=2, column=1, padx=0, pady=10)
        Label(Trw, text="User name:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=3, column=0, padx=30, pady=10,
                                                                                        sticky="e")
        Label(Trw, text=U_name, bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=3, column=1, padx=10, pady=10)
        Label(Trw, text="Password:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=4, column=0, padx=30,
                                                                                               pady=10, sticky="e")
        Label(Trw, text=P, bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=4, column=1, padx=10, pady=10)
        Label(Trw, text="Contact no:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=5, column=0, padx=30,
                                                                                            pady=10, sticky="e")
        e4 = Entry(Trw, textvariable=TC_no,width=30)
        e4.grid(row=5, column=1, padx=10, pady=10)
        Label(Trw, text="Email:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=6, column=0, padx=30, pady=10,
                                                                                       sticky="e")
        e5 = Entry(Trw, textvariable=T_email,width=30)
        e5.grid(row=6, column=1, padx=10, pady=10)
        Label(Trw, text="Field:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=7, column=0, padx=30, pady=10,
                                                                                       sticky="e")
        e6 = Entry(Trw, textvariable=T_field,width=30)
        e6.grid(row=7, column=1, padx=10, pady=10)
        Label(Trw, text="Department:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=8, column=0, padx=30, pady=10,
                                                                                          sticky="e")
        e7 = Entry(Trw, textvariable=T_subject,width=30)
        e7.grid(row=8, column=1, padx=10, pady=10)
        Button(Trw, text="Clear All", width=15, height=2, bg="white", fg="black", padx=20, command=T_clear).grid(row=9,
                                                                                                                 column=0,
                                                                                                                 pady=10,
                                                                                                                 padx=0,
                                                                                                                 sticky="e")
        sb=Button(Trw, text="Save", width=15, height=2, bg="white", fg="black", font="none 9 bold", padx=20,command=Save_Tr).grid(row=9,
                                                                                                               pady=10,
                                                                                                               padx=20,
                                                                                                               column=1,
                                                                                                               sticky="e")
        Button(Trw, text="Go back", width=10, height=2, bg="brown", fg="White", command=Trw.destroy).grid(row=10, column=2,
                                                                                                          pady=10, padx=0)

        Trw.mainloop()
def std_v_marks():
    if os.path.exists(reg+"m.txt"):
        Sew = Toplevel(w)
        Sew.geometry("650x640")
        Sew.configure(bg="#002b2b")
        Sew.resizable(0, 0)
        Sew.title("VIEW Marks")

        Sf = open(reg + "m.txt", "r").readlines()
        Ap = Sf[0]
        ICT = Sf[1]
        Eng = Sf[2]
        Isl = Sf[3]
        ppit = Sf[4]
        calculas = Sf[5]
        ict_lab = Sf[6]
        Label(Sew, text="Student marks details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1,
                                                                                                                 columnspan=3,
                                                                                                                 padx=150,
                                                                                                                 pady=10)
        Label(Sew, text="Apllied Physics:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30,
                                                                                                 pady=5,
                                                                                                 sticky="e")
        Label(Sew, text="\n"+Ap, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
        Label(Sew, text="ICT:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                     sticky="e")
        Label(Sew, text="\n"+ICT, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)

        Label(Sew, text="English:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                         pady=5, sticky="e")
        Label(Sew, text="\n"+Eng, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
        Label(Sew, text="Islamic studies:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                                 pady=5, sticky="e")
        Label(Sew, text="\n"+Isl, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
        Label(Sew, text="PPIT:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                      sticky="e")
        Label(Sew, text="\n"+ppit, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
        Label(Sew, text="Calculas:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                          sticky="e")
        Label(Sew, text="\n"+calculas, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
        Label(Sew, text="ICT Lab:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                         sticky="e")
        Label(Sew, text="\n"+ict_lab, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)

        Button(Sew, text="Exit", width=10, height=2, bg="#480607", fg="White", command=Sew.destroy).grid(row=10,
                                                                                                           columnspan=3,
                                                                                                           pady=10, padx=0)
        Sew.mainloop()
    else:
        tkinter.messagebox.showerror("Not found","Marks not Uploaded Yet")

def Std_e_marks():
    global Tem
    global reg
    reg = reg_no.get().upper()
    if reg_check(reg) is True:
        if os.path.exists(reg+".txt"):
            if os.path.exists(reg + "m.txt"):


                Sem_w.destroy()
                Sew = Toplevel(Tw)
                Sew.geometry("650x640")
                Sew.configure(bg="#002b2b")
                Sew.resizable(0, 0)
                Sew.title("VIEW Marks")

                Sf = open(reg + "m.txt", "r").readlines()
                Ap = Sf[0]
                ICT = Sf[1]
                Eng= Sf[2]
                Isl = Sf[3]
                ppit = Sf[4]
                calculas = Sf[5]
                ict_lab= Sf[6]
                Label(Sew, text="Student marks details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1,
                                                                                                                   columnspan=3,
                                                                                                                   padx=150,
                                                                                                                   pady=10)
                Label(Sew, text="Apllied Physics:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                              sticky="e")
                Label(Sew, text="\n"+Ap, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
                b1 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=AP_ew).grid(row=2, column=2,
                                                                                                                 padx=10, pady=5)
                Label(Sew, text="ICT:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                                sticky="e")
                Label(Sew, text="\n"+ICT, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)
                b = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=ict_ew).grid(row=3, column=2,
                                                                                                  padx=10, pady=5)

                Label(Sew, text="English:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                                       pady=5, sticky="e")
                Label(Sew, text="\n"+Eng, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
                b2 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=eng_ew).grid(row=4, column=2, padx=10, pady=5)
                Label(Sew, text="Islamic studies:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                                    pady=5, sticky="e")
                Label(Sew, text="\n"+Isl, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
                b3 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=isl_ew).grid(row=5, column=2, padx=10, pady=5)
                Label(Sew, text="PPIT:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                               sticky="e")
                Label(Sew, text="\n"+ppit, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
                b4 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=ppit_ew).grid(row=6, column=2, padx=10, pady=5)
                Label(Sew, text="Calculas:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                               sticky="e")
                Label(Sew, text="\n"+calculas, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
                b5 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=cal_ew).grid(row=7, column=2, padx=10, pady=5)
                Label(Sew, text="ICT Lab:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                                  sticky="e")
                Label(Sew, text="\n"+ict_lab, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)
                b6 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=lab_ew).grid(row=8, column=2, padx=10, pady=5)

                Button(Sew, text="Cancel", width=10, height=2, bg="#480607", fg="White", command=Sew.destroy).grid(row=10,
                                                                                                                   columnspan=3,
                                                                                                                   pady=10, padx=0)
                Sew.mainloop()
            else:
                Sf = open(reg + "m.txt", "w")
                Sf.write("0" + "\n")
                Sf.write("0" + "\n")
                Sf.write("0" + "\n")
                Sf.write("0" + "\n")
                Sf.write("0" + "\n")
                Sf.write("0" + "\n")
                Sf.write("0" + "\n")
                Sf.close()


                Sem_w.destroy()
                Sew = Toplevel(Tw)
                Sew.geometry("610x500")
                Sew.configure(bg="#002b2b")
                Sew.resizable(0, 0)
                Sew.title("VIEW Marks")

                Sf = open(reg + "m.txt", "r").readlines()
                Ap = Sf[0]
                ICT = Sf[1]
                Eng = Sf[2]
                Isl = Sf[3]
                ppit = Sf[4]
                calculas = Sf[5]
                ict_lab = Sf[6]
                Label(Sew, text="Student marks details:", bg="#002b2b", fg="white",
                      font=("TimesNewRoman 20 bold")).grid(row=1,
                                                           columnspan=3,
                                                           padx=150,
                                                           pady=10)
                Label(Sew, text="Apllied Physics:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2,
                                                                                                         column=0,
                                                                                                         padx=30,
                                                                                                         pady=5,
                                                                                                         sticky="e")
                Label(Sew, text=Ap, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30,
                                                                                         pady=5)
                b1 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1, command=AP_ew).grid(row=2, column=2,
                                                                                                 padx=10, pady=5)
                Label(Sew, text="ICT:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30,
                                                                                             pady=5,
                                                                                             sticky="e")
                Label(Sew, text=ICT, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0,
                                                                                           pady=5)
                b = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=ict_ew ).grid(row=3, column=2,
                                                                                                padx=10, pady=5)

                Label(Sew, text="English:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0,
                                                                                                 padx=30,
                                                                                                 pady=5, sticky="e")
                Label(Sew, text=Eng, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0,
                                                                                          pady=5)
                b2 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=eng_ew ).grid(row=4, column=2,
                                                                                                 padx=10, pady=5)
                Label(Sew, text="Islamic studies:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5,
                                                                                                         column=0,
                                                                                                         padx=30,
                                                                                                         pady=5,
                                                                                                         sticky="e")
                Label(Sew, text=Isl, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0,
                                                                                          pady=5)
                b3 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=isl_ew ).grid(row=5, column=2,
                                                                                                 padx=10, pady=5)
                Label(Sew, text="PPIT:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30,
                                                                                              pady=5,
                                                                                              sticky="e")
                Label(Sew, text=ppit, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0,
                                                                                            pady=5)
                b4 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=ppit_ew).grid(row=6, column=2, padx=10,
                                                                                               pady=5)
                Label(Sew, text="Calculas:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0,
                                                                                                  padx=30, pady=5,
                                                                                                  sticky="e")
                Label(Sew, text=calculas, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0,
                                                                                               pady=5)
                b5 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=cal_ew ).grid(row=7, column=2,
                                                                                                 padx=10, pady=5)
                Label(Sew, text="ICT Lab:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0,
                                                                                                 padx=30, pady=5,
                                                                                                 sticky="e")
                Label(Sew, text=ict_lab, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0,
                                                                                              pady=5)
                b6 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=lab_ew ).grid(row=8, column=2,
                                                                                                 padx=10, pady=5)

                Button(Sew, text="Cancel", width=10, height=2, bg="#480607", fg="White", command=Sew.destroy).grid(
                    row=10,
                    columnspan=3,
                    pady=10, padx=0)
                Sew.mainloop()

        else:
            tkinter.messagebox.showerror("No Info", "Student doesn't exist! Try Adding")
    else:
        tkinter.messagebox.showerror("Error", "invalid registeration no format!")
def delS_r():
    a=tkinter.messagebox.askquestion("confirmation","Delete student record?")
    if a=="yes":
        os.remove(reg+".txt")
        A_Svw.destroy()
    else:
        tkinter.messagebox.showinfo("delete record"," cancelled!")

def SV_login():
    global Svlw
    global reg_no
    Svlw = Toplevel(Aw)
    Svlw.title("Student")
    Svlw.configure(bg="white")
    Svlw.geometry("300x200")
    Svlw.resizable(0, 0)
    reg_no=StringVar()
    l = Label(Svlw, text="Enter Registration NO:            ", bg="white",
              font="Arial 14 bold", padx=10, pady=10).grid(row=1)
    format = Label(Svlw, text="Format:\"AA00-BBB-000\"""", bg="white", fg="grey", font="none 12 italic").grid(
        row=2, padx=10, pady=5)
    e_u = Entry(Svlw,textvariable=reg_no, width=20, bg="light blue",)
    e_u.grid(row=3, padx=20, pady=5)
    b=Button(Svlw,text="Enter",bg="black",fg="white",width=10,height=2,command=SV_w).grid(row=4,pady=5)
    q = Button(Svlw, text="exit", bg="brown", fg="white", width=5, height=1, command=Svlw.destroy).grid(row=5,
                                                                                                      pady=5,
                                                                                                      sticky=E)

    Svlw.mainloop()
def EditSs():
    Ss = nS_s.get()
    Sf=open(reg+".txt","r").readlines()
    Sf[6]=Ss + "\n"
    w=open(reg+".txt","w")
    w.writelines(Sf)
    w.close()
    S_esw.destroy()
def EditSf():
    Sfield = nS_field.get()
    Sf=open(reg+".txt","r").readlines()
    Sf[5]=Sfield + "\n"
    w=open(reg+".txt","w")
    w.writelines(Sf)
    w.close()
    S_efw.destroy()
def EditSemail():
    Semail = nS_email.get()
    Sf=open(reg+".txt","r").readlines()
    Sf[4]=Semail + "\n"
    w=open(reg+".txt","w")
    w.writelines(Sf)
    w.close()
    S_eenw.destroy()
def EditSCn():
    SCno = nS_Cn.get()
    Sf=open(reg+".txt","r").readlines()
    Sf[3]=SCno + "\n"
    w=open(reg+".txt","w")
    w.writelines(Sf)
    w.close()
    S_eCnw.destroy()
def EditSn():
    Sname = nS_name.get()
    Sf=open(reg+".txt","r").readlines()
    Sf[0]=Sname + "\n"
    w=open(reg+".txt","w")
    w.writelines(Sf)
    w.close()
    S_enw.destroy()
def EditSfn():
    Sfname = nfS_name.get()
    Sf=open(reg+".txt","r").readlines()
    Sf[2]=Sfname + "\n"
    w=open(reg+".txt","w")
    w.writelines(Sf)
    w.close()
    S_efnw.destroy()
def EditSs_w():
    global S_esw
    S_esw=Toplevel(Sew)
    S_esw.configure(bg="black")
    S_esw.geometry("200x150")
    S_esw.resizable(0,0)
    global nS_s
    nS_s = StringVar()
    S_esw.title("Change semester")
    Label(S_esw,text="Enter new semester:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(S_esw,textvariable=nS_s,width=25)
    e.grid(row=2,pady=10)
    b=Button(S_esw,text="OK",bg="white",fg="black",width=10,height=1,command=EditSs).grid(row=3,pady=5)
def EditSf_w():
    global S_efw
    S_efw=Toplevel(Aw)
    S_efw.configure(bg="black")
    S_efw.geometry("230x150")
    S_efw.resizable(0,0)
    global nS_field
    nS_field = StringVar()
    S_efw.title("change student field")
    Label(S_efw,text="Enter new field:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(S_efw,textvariable=nS_field,width=25)
    e.grid(row=2,pady=10)
    b=Button(S_efw,text="OK",bg="white",fg="black",width=10,height=1,command=EditSf).grid(row=3,pady=5)
def EditSemail_w():
    global S_eenw
    S_eenw=Toplevel(Sew)
    S_eenw.configure(bg="black")
    S_eenw.geometry("200x150")
    S_eenw.resizable(0,0)
    global nS_email
    nS_email = StringVar()
    S_eenw.title("Change E-mail")
    Label(S_eenw,text="Enter new E-mail:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(S_eenw,textvariable=nS_email,width=25)
    e.grid(row=2,pady=10)
    b=Button(S_eenw,text="OK",bg="white",fg="black",width=10,height=1,command=EditSemail).grid(row=3,pady=5)
def EditSCn_w():
    global S_eCnw
    S_eCnw=Toplevel(Sew)
    S_eCnw.configure(bg="black")
    S_eCnw.geometry("200x150")
    S_eCnw.resizable(0,0)
    global nS_Cn
    nS_Cn = StringVar()
    S_eCnw.title("change Contact No:")
    Label(S_eCnw,text="Enter Contact No:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(S_eCnw,textvariable=nS_Cn,width=25)
    e.grid(row=2,pady=10)
    b=Button(S_eCnw,text="OK",bg="white",fg="black",width=10,height=1,command=EditSCn).grid(row=3,pady=5)
def EditSfn_w():
    global S_efnw
    S_efnw=Toplevel(Sew)
    S_efnw.configure(bg="black")
    S_efnw.geometry("250x150")
    S_efnw.resizable(0,0)
    global nfS_name
    nfS_name = StringVar()
    S_efnw.title("change father name")
    Label(S_efnw,text="Enter new father Name:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(S_efnw,textvariable=nfS_name,width=25)
    e.grid(row=2,pady=10)
    b=Button(S_efnw,text="OK",bg="white",fg="black",width=10,height=1,command=EditSfn).grid(row=3,pady=5)


def EditSn_w():
    global S_enw
    S_enw=Toplevel(Sew)
    S_enw.configure(bg="black")
    S_enw.geometry("200x150")
    S_enw.resizable(0,0)
    global nS_name
    nS_name = StringVar()
    S_enw.title("change student name")
    Label(S_enw,text="Enter new Name:",bg="black",fg="white",font="calibri 14 bold").grid(row=1,pady=10,padx=30)
    e=Entry(S_enw,textvariable=nS_name,width=25)
    e.grid(row=2,pady=10)
    b=Button(S_enw,text="OK",bg="white",fg="black",width=10,height=1,command=EditSn).grid(row=3,pady=5)
    S_enw.mainloop()

def Sem_login():
    global Sem_w
    global reg_no
    Sem_w = Toplevel(Tw)
    Sem_w.title("Edit")
    Sem_w.configure(bg="white")
    Sem_w.geometry("300x200")
    Sem_w.resizable(0, 0)
    reg_no = StringVar()
    l = Label(Sem_w, text="Enter Registration NO:            ", bg="white",
              font="Arial 14 bold", padx=10, pady=10).grid(row=1)
    format = Label(Sem_w, text="Format:\"AA00-BBB-000\"""", bg="white", fg="grey", font="none 12 italic").grid(
        row=2, padx=10, pady=5)
    e_u = Entry(Sem_w, textvariable=reg_no, width=20, bg="light blue", )
    e_u.grid(row=3, padx=20, pady=5)
    b = Button(Sem_w, text="Enter", bg="black", fg="white", width=10, height=2, command=Std_e_marks).grid(row=4, pady=5)
    q = Button(Sem_w, text="exit", bg="brown", fg="white", width=5, height=1, command=Sem_w.destroy).grid(row=5,
                                                                                                      pady=5,
                                                                                                      sticky=E)
def Se_login():
    global Sw
    global reg_no
    Sw = Toplevel(Aw)
    Sw.title("Edit")
    Sw.configure(bg="white")
    Sw.geometry("300x200")
    Sw.resizable(0, 0)
    reg_no = StringVar()
    l = Label(Sw, text="Enter Registration NO:            ", bg="white",
              font="Arial 14 bold", padx=10, pady=10).grid(row=1)
    format = Label(Sw, text="Format:\"AA00-BBB-000\"""", bg="white", fg="grey", font="none 12 italic").grid(
        row=2, padx=10, pady=5)
    e_u = Entry(Sw, textvariable=reg_no, width=20, bg="light blue", )
    e_u.grid(row=3, padx=20, pady=5)
    b = Button(Sw, text="Enter", bg="black", fg="white", width=10, height=2, command=Std_e).grid(row=4, pady=5)
    q = Button(Sw, text="exit", bg="brown", fg="white", width=5, height=1, command=Sw.destroy).grid(row=5,
                                                                                                      pady=5,
                                                                                                      sticky=E)

    Sw.mainloop()
def Std_e():
    global Sew
    global reg
    reg = reg_no.get().upper()
    if reg_check(reg) is True:
        if os.path.exists(reg+".txt"):

            Sw.destroy()
            Sew = Toplevel(Aw)
            Sew.geometry("650x640")
            Sew.configure(bg="#002b2b")
            Sew.resizable(0, 0)
            Sew.title("VIEW INFO")

            Sf = open(reg + ".txt", "r").readlines()
            S_name = Sf[0]
            R_no = Sf[1]
            Sf_name = Sf[2]
            SC_no = Sf[3]
            S_email = Sf[4]
            S_field = Sf[5].upper()
            S_semester = Sf[6]
            Label(Sew, text="Student details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1,
                                                                                                               columnspan=3,
                                                                                                               padx=190,
                                                                                                               pady=10)
            Label(Sew, text="Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                          sticky="e")
            Label(Sew, text="\n"+S_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
            b1 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=EditSn_w).grid(row=2, column=2,
                                                                                                             padx=10, pady=5)
            Label(Sew, text="Reg no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                            sticky="e")
            Label(Sew, text="\n"+R_no, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)

            Label(Sew, text="Father's Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                                   pady=5, sticky="e")
            Label(Sew, text="\n"+Sf_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
            b2 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=EditSfn_w).grid(row=4, column=2, padx=10, pady=5)
            Label(Sew, text="Contact no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                                pady=5, sticky="e")
            Label(Sew, text="\n"+SC_no, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
            b3 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=EditSCn_w).grid(row=5, column=2, padx=10, pady=5)
            Label(Sew, text="Email:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(Sew, text="\n"+S_email, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
            b4 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=EditSemail_w).grid(row=6, column=2, padx=10, pady=5)
            Label(Sew, text="Field:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(Sew, text="\n"+S_field, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
            b5 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=EditSf_w).grid(row=7, column=2, padx=10, pady=5)
            Label(Sew, text="Semester:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                              sticky="e")
            Label(Sew, text="\n"+S_semester, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)
            b6 = Button(Sew, text="Edit", bg="white", fg="black", width=10, height=1,command=EditSs_w).grid(row=8, column=2, padx=10, pady=5)

            Button(Sew, text="Cancel", width=10, height=2, bg="#480607", fg="White", command=Sew.destroy).grid(row=10,
                                                                                                               columnspan=3,
                                                                                                               pady=10, padx=0)
            Sew.mainloop()

        else:
            tkinter.messagebox.showerror("No Info", "Student doesn't exist! Try Adding")
    else:
        tkinter.messagebox.showerror("Error", "invalid registeration no format!")
def reg_check(r):
    if len(r) == 12:
        if r.count("-") == 2:
            a = list(r)
            if a[4] == "-" and a[8] == "-":
                if a[0].isalpha() is True and a[1].isalpha() is True and a[5].isalpha() is True and a[
                    6].isalpha() is True and a[7].isalpha() is True:
                    if a[2].isdigit() is True and a[3].isdigit() is True and a[9].isdigit() is True and a[
                        10].isdigit() is True and a[11].isdigit() is True:
                        return True


def SV_w():
    global A_Svw
    global reg
    reg = reg_no.get().upper()
    if reg_check(reg) is True:
        if os.path.exists(reg+".txt"):
            Svlw.destroy()
            A_Svw = Toplevel(Aw)
            A_Svw.geometry("570x640")
            A_Svw.configure(bg="#002b2b")
            A_Svw.resizable(0, 0)
            A_Svw.title("VIEW INFO")

            Sf = open(reg + ".txt", "r").readlines()
            S_name = Sf[0]
            R_no = Sf[1]
            Sf_name = Sf[2]
            SC_no = Sf[3]
            S_email = Sf[4]
            S_field = Sf[5].upper()
            S_semester = Sf[6]
            Label(A_Svw, text="Student details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                               padx=10, pady=5)
            Label(A_Svw, text="Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                          sticky="e")
            Label(A_Svw, text="\n"+S_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
            Label(A_Svw, text="Reg no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                            sticky="e")
            Label(A_Svw, text="\n"+R_no, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)
            Label(A_Svw, text="Father's Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                                   pady=5, sticky="e")
            Label(A_Svw, text="\n"+Sf_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
            Label(A_Svw, text="Contact no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                                pady=5, sticky="e")
            Label(A_Svw, text="\n"+SC_no, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
            Label(A_Svw, text="Email:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(A_Svw, text="\n"+S_email, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
            Label(A_Svw, text="Field:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(A_Svw, text="\n"+S_field, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
            Label(A_Svw, text="Semester:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                              sticky="e")
            Label(A_Svw, text="\n"+S_semester, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)

            Button(A_Svw, text="Go back", width=10, height=2, bg="#480607", fg="White", command=A_Svw.destroy).grid(row=10, column=2,
                                                                                                              pady=10, padx=0)
            Button(A_Svw, text="Delete", width=10, height=2, bg="#480607", fg="White", command=delS_r).grid(row=10,
                                                                                                                column=0,
                                                                                                                pady=10,
                                                                                                                padx=0)

            A_Svw.mainloop()
        else:
            tkinter.messagebox.showerror("No Info", "Student doesn't exist! Try Adding")
    else:
        tkinter.messagebox.showerror("Error", "invalid registeration no format!")

def TSV_w():
    global T_Svw
    global reg
    reg = reg_no.get().upper()
    if reg_check(reg) is True:
        if os.path.exists(reg+".txt"):
            T_Slw.destroy()
            T_Svw = Toplevel(Tw)
            T_Svw.geometry("570x640")
            T_Svw.configure(bg="#002b2b")
            T_Svw.resizable(0, 0)
            T_Svw.title("VIEW INFO")

            Sf = open(reg + ".txt", "r").readlines()
            S_name = Sf[0]
            R_no = Sf[1]
            Sf_name = Sf[2]
            SC_no = Sf[3]
            S_email = Sf[4]
            S_field = Sf[5].upper()
            S_semester = Sf[6]
            Label(T_Svw, text="Student details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                               padx=10, pady=5)
            Label(T_Svw, text="Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                          sticky="e")
            Label(T_Svw, text="\n"+S_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
            Label(T_Svw, text="Reg no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                            sticky="e")
            Label(T_Svw, text="\n"+R_no, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)
            Label(T_Svw, text="Father's Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                                   pady=5, sticky="e")
            Label(T_Svw, text="\n"+Sf_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
            Label(T_Svw, text="Contact no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                                pady=5, sticky="e")
            Label(T_Svw, text="\n"+SC_no, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
            Label(T_Svw, text="Email:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(T_Svw, text="\n"+S_email, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
            Label(T_Svw, text="Field:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(T_Svw, text="\n"+S_field, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
            Label(T_Svw, text="Semester:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                              sticky="e")
            Label(T_Svw, text="\n"+S_semester, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)

            Button(T_Svw, text="Go back", width=10, height=2, bg="#480607", fg="White", command=T_Svw.destroy).grid(row=10, column=2,
                                                                                                              pady=10, padx=0)


            T_Svw.mainloop()
        else:
            tkinter.messagebox.showerror("No Info", "Student doesn't exist! Try Adding")
    else:
        tkinter.messagebox.showerror("Error", "invalid registeration no format!")

def ST_login():
    global T_Slw
    global reg_no
    T_Slw = Toplevel(w)
    T_Slw.title("Student")
    T_Slw.configure(bg="white")
    T_Slw.geometry("300x200")
    T_Slw.resizable(0, 0)
    reg_no=StringVar()
    l = Label(T_Slw, text="Enter Registration NO:            ", bg="white",
              font="Arial 14 bold", padx=10, pady=10).grid(row=1)
    format = Label(T_Slw, text="Format:\"AA00-BBB-000\"""", bg="white", fg="grey", font="none 12 italic").grid(
        row=2, padx=10, pady=5)
    e_u = Entry(T_Slw,textvariable=reg_no, width=20, bg="light blue",)
    e_u.grid(row=3, padx=20, pady=5)
    b=Button(T_Slw,text="Enter",bg="black",fg="white",width=10,height=2,command=TSV_w).grid(row=4,pady=5)
    q = Button(T_Slw, text="exit", bg="brown", fg="white", width=5, height=1, command=T_Slw.destroy).grid(row=5,
                                                                                                      pady=5,
                                                                                                      sticky=E)

    T_Slw.mainloop()
def Std_view():
    global reg
    global Svw
    reg = reg_no.get().upper()
    if reg_check(reg) is True:
        if os.path.exists(reg+".txt"):
            Slw.destroy()
            Svw = Tk()
            Svw.geometry("570x640")
            Svw.configure(bg="#002b2b")
            Svw.resizable(0, 0)
            Svw.title("VIEW INFO")

            Sf = open(reg + ".txt", "r").readlines()
            S_name = Sf[0]
            R_no = Sf[1]
            Sf_name = Sf[2]
            SC_no = Sf[3]
            S_email = Sf[4]
            S_field = Sf[5].upper()
            S_semester = Sf[6]
            Label(Svw, text="Student details:", bg="#002b2b", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                               padx=10, pady=5)
            Label(Svw, text="Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=2, column=0, padx=30, pady=5,
                                                                                          sticky="e")
            Label(Svw, text=("\n"+S_name), bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=2, column=1, padx=30, pady=5)
            Label(Svw, text="Reg no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=3, column=0, padx=30, pady=5,
                                                                                            sticky="e")
            Label(Svw, text="\n"+R_no, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=3, column=1, padx=0, pady=5)
            Label(Svw, text="Father's Name:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=4, column=0, padx=30,
                                                                                                   pady=5, sticky="e")
            Label(Svw, text="\n"+Sf_name, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=4, column=1, padx=0, pady=5)
            Label(Svw, text="Contact no:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=5, column=0, padx=30,
                                                                                                pady=5, sticky="e")
            Label(Svw, text="\n"+SC_no, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=5, column=1, padx=0, pady=5)
            Label(Svw, text="Email:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=6, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(Svw, text="\n"+S_email, bg="#002b2b", fg="white", font="Arial 12 bold ").grid(row=6, column=1, padx=0, pady=5)
            Label(Svw, text="Field:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=7, column=0, padx=30, pady=5,
                                                                                           sticky="e")
            Label(Svw, text="\n"+S_field, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=7, column=1, padx=0, pady=5)
            Label(Svw, text="Semester:", bg="#002b2b", fg="white", font=("calibri 14 ")).grid(row=8, column=0, padx=30, pady=5,
                                                                                              sticky="e")
            Label(Svw, text="\n"+S_semester, bg="#002b2b", fg="white", font="Arial 12 bold").grid(row=8, column=1, padx=0, pady=5)

            Button(Svw, text="Go back", width=10, height=2, bg="#480607", fg="White", command=Svw.destroy).grid(row=10, column=2,
                                                                                                              pady=10, padx=0)
            Button(Svw, text="View Marks", width=10, height=2, bg="#480607", fg="White", command=std_v_marks).grid(row=10,
                                                                                                                column=0,
                                                                                                                pady=10,
                                                                                                                padx=30,sticky="w")

            Svw.mainloop()
        else:
            tkinter.messagebox.showerror("No Info", "Student doesn't exist!")
    else:
        tkinter.messagebox.showerror("Error", "invalid registeration no format!")


def saveS_r():
    reg = R_no.get().upper()
    if reg_check(reg) is True:
        if os.path.exists(reg+".txt"):
            tkinter.messagebox.showerror("Error", "Info Already exists! try editing")

        else:
            name = S_name.get()
            fname = Sf_name.get()
            c_no = SC_no.get()
            email = S_email.get()
            field = S_field.get()
            semester = S_semester.get()
            Sf = open(reg + ".txt", "w")
            Sf.write(str(name) + "\n")
            Sf.write(str(reg) + "\n")
            Sf.write(str(fname) + "\n")
            Sf.write(str(c_no) + "\n")
            Sf.write(str(email) + "\n")
            Sf.write(str(field) + "\n")
            Sf.write(str(semester) + "\n")
            Sf.close()
            S_clear()
            Srw.destroy()
    else:
        tkinter.messagebox.showerror("Error", "invalid registeration no. format!")
        e2.delete(0, END)



def S_clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)

def Std_r():

    global Srw
    global S_name
    global R_no
    global Sf_name
    global SC_no
    global S_email
    global S_field
    global S_semester
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global e7
    Srw = Toplevel(Aw)
    Srw.geometry("550x500")
    Srw.configure(bg="#0e4d92")
    Srw.resizable(0, 0)
    S_name = StringVar()
    R_no=StringVar()
    Sf_name=StringVar()
    SC_no=StringVar()
    S_email=StringVar()
    S_field=StringVar()
    S_semester=StringVar()
    Label(Srw, text="Student details:", bg="#0e4d92", fg="white", font=("TimesNewRoman 20 bold")).grid(row=1, column=0,
                                                                                                       padx=10, pady=10)
    Label(Srw, text="Name:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=2, column=0, padx=30, pady=10,
                                                                                  sticky="e")
    e1 = Entry(Srw, textvariable=S_name,width=30)
    e1.grid(row=2, column=1, padx=0, pady=10)
    Label(Srw, text="Reg no:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=3, column=0, padx=30, pady=10,
                                                                                    sticky="e")
    e2 = Entry(Srw, textvariable=R_no,width=30)
    e2.grid(row=3, column=1, padx=10, pady=10)
    Label(Srw, text="Father's Name:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=4, column=0, padx=30,
                                                                                           pady=10, sticky="e")
    e3 = Entry(Srw, textvariable=Sf_name,width=30)
    e3.grid(row=4, column=1, padx=10, pady=10)
    Label(Srw, text="Contact no:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=5, column=0, padx=30,
                                                                                        pady=10, sticky="e")
    e4 = Entry(Srw, textvariable=SC_no,width=30)
    e4.grid(row=5, column=1, padx=10, pady=10)
    Label(Srw, text="Email:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=6, column=0, padx=30, pady=10,
                                                                                   sticky="e")
    e5 = Entry(Srw, textvariable=S_email,width=30)
    e5.grid(row=6, column=1, padx=10, pady=10)
    Label(Srw, text="Field:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=7, column=0, padx=30, pady=10,
                                                                                   sticky="e")
    e6 = Entry(Srw, textvariable=S_field,width=30)
    e6.grid(row=7, column=1, padx=10, pady=10)
    Label(Srw, text="Semester:", bg="#0e4d92", fg="white", font=("calibri 12 ")).grid(row=8, column=0, padx=30, pady=10,
                                                                                      sticky="e")
    e7 = Entry(Srw, textvariable=S_semester,width=30)
    e7.grid(row=8, column=1, padx=10, pady=10)
    Button(Srw, text="Clear All", width=15, height=2, bg="white", fg="black", padx=20, command=S_clear).grid(row=9,
                                                                                                             column=0,
                                                                                                             pady=10,
                                                                                                             padx=0,
                                                                                                             sticky="e")
    sb=Button(Srw, text="Save", width=15, height=2, bg="white", fg="black", font="none 9 bold", padx=20,command=saveS_r).grid(row=9,
                                                                                                           pady=10,
                                                                                                           padx=20,
                                                                                                           column=1,
                                                                                                           sticky="e")
    Button(Srw, text="Go back", width=10, height=2, bg="brown", fg="White", command=Srw.destroy).grid(row=10, column=2,
                                                                                                      pady=10, padx=0)

    Srw.mainloop()

def T_resign():
    a = tkinter.messagebox.askyesno("Confirmation!", "Are you sure you want to Resign!!")
    if a is True:
        Tf = open("teacher login info.txt", "w")
        Tf.close()
        Tw.destroy()

def A_resign():
    a = tkinter.messagebox.askyesno("Confirmation!", "Are you sure you want to Resign!!")
    if a is True:
        Af=open("admin login info.txt","w")
        Af.close()
        Aw.destroy()

def Admin():
    global Aw
    verify=[Au_verify.get(),Ap_verify.get()]
    Af=open("admin login info.txt", "r")
    r = Af.read()
    c=r.split()
    if len(r)>1:
        if c[0]==verify[0]:
            if c[1]==verify[1]:
                Alw.destroy()
                Aw=Toplevel(w)
                Aw.geometry("700x500")
                Aw.resizable(0, 0)
                Aw.configure(bg="#F5F5DC")
                Label(Aw, text="Welcome to Admin portal", font="algerian 30", bg="#F5F5DC", fg="BROWN").grid(row=1, pady=20,
                                                                                                             padx=80,
                                                                                                             columnspan=2)
                Button(Aw, text="View Student Record", width=20, height=2, bg="black", fg="white",
                       font=("Arial 12 bold"),command=SV_login).grid(row=2, columnspan=2, pady=10)
                Button(Aw, text="Add Student record", width=20, height=2, bg="black", fg="white",command=Std_r,
                       font=("Arial 12 bold")).grid(row=3, column=0, pady=10, )
                Button(Aw, text="Edit Student record", width=20, height=2, bg="black", fg="white",
                       font=("Arial 12 bold"),command=Se_login).grid(row=3, column=1, pady=10)
                Button(Aw, text="View Teacher Record", width=20, height=2, bg="black", fg="white",
                       font=("Arial 12 bold"), command=T_vr).grid(row=4, columnspan=2, pady=10)
                Button(Aw, text="Add Teacher record", width=20, height=2, bg="black", fg="white", command=T_r,
                       font=("Arial 12 bold")).grid(row=5, column=0, pady=10, )
                Button(Aw, text="Edit Teacher record", width=20, height=2, bg="black", fg="white",
                       font=("Arial 12 bold"),command=Te_w).grid(row=5, column=1, pady=10)

                Button(Aw, text="Resign", width=15, height=2, bg="brown", fg="white", font=("Arial 12 bold"),command=A_resign).grid(row=6,
                                                                                                                   column=0,
                                                                                                                   pady=30)
                Button(Aw, text="Logout", width=15, height=2, bg="brown", fg="white", font=("Arial 12 bold"),command=Aw.destroy).grid(row=6,
                                                                                                                   column=1,
                                                                                                                   pady=50)

                Aw.mainloop()
            else:
                Label(Alw,text="inncorrect password!!!!",bg="white",fg="red",pady=5).grid(row=5)
                Ap_e.delete(0, END)
        else:
            Label(Alw, text="inncorrect username!!!!", bg="white", fg="red", pady=5).grid(row=5)
            Au_e.delete(0, END)
            Ap_e.delete(0, END)
    else:
        tkinter.messagebox.showerror("Error", "Not registered!")
        Au_e.delete(0, END)
        Ap_e.delete(0, END)

def Teacher():
    global Tw
    verify = [Tu_verify.get(), Tp_verify.get()]
    Tf = open("teacher login info.txt", "r")
    r = Tf.read()
    c = r.split()
    if len(r)>1:
        if c[0] == verify[0]:
            if c[1] == verify[1]:
                Tlw.destroy()
                Tw = Toplevel(w)
                Tw.title("Teacher")
                Tw.geometry("500x400")
                Tw.configure(bg="#F5F5DC")
                Tw.resizable(0, 0)
                Label(Tw, text="Welcome to \nTeacher portal", font="algerian 30", bg="#F5F5DC", fg="BROWN").grid(row=1,
                                                                                                                 pady=20,
                                                                                                                 padx=70)
                Button(Tw, text="View Student Record", width=20, height=2, bg="black", fg="white",
                       font=("Arial 12 bold"),command=ST_login).grid(row=2, pady=10)
                Button(Tw, text="Edit marks", width=20, height=2, bg="black", fg="white", font=("Arial 12 bold"),command=Sem_login).grid(
                    row=3, pady=10)
                Button(Tw, text="Resign", width=15, height=2, bg="brown", fg="white", font=("Arial 12 bold"),command=T_resign).grid(row=4,
                                                                                                                   pady=50,
                                                                                                                   padx=20,
                                                                                                                   sticky=W)
                Button(Tw, text="Logout", width=15, height=2, bg="brown", fg="white", font=("Arial 12 bold"),
                       command=Tw.destroy).grid(row=4, pady=50, padx=0, sticky=E)

                Tw.mainloop()
            else:
                Label(Tlw, text="inncorrect password!!!!", bg="white", fg="red", pady=5).grid(row=5)
                Tp_e.delete(0, END)
        else:
            Label(Tlw, text="inncorrect username!!!!", bg="white", fg="red", pady=5).grid(row=5)
            Tu_e.delete(0, END)
            Tp_e.delete(0, END)
    else:
        tkinter.messagebox.showerror("Error", "Not registered!")
        Tu_e.delete(0, END)
        Tp_e.delete(0, END)

def reg_admin():
    Alogin_info=[A_Uname.get()," ",A_p.get()]
    Af = open("admin login info.txt", "w")
    for i in range(3):
        Af.write(Alogin_info[i])
    Af.close()

    A_u_e.delete(0, END)
    A_p_e.delete(0, END)

    tkinter.messagebox.showinfo("Success", "Registered Sucessfully")
    Arw.destroy()


def reg_teacher():
    Tlogin_info = [T_Uname.get(), " ", T_p.get()]
    Tf = open("teacher login info.txt", "w")
    for i in range(3):
        Tf.write(Tlogin_info[i])
    Tf.close()
    T_u_e.delete(0, END)
    T_p_e.delete(0, END)

    tkinter.messagebox.showinfo("Success","Registered Sucessfully")
    Trw.destroy()



def A_reg():
    Af = open("admin login info.txt", "r")
    e=Af.read()
    if len(e)>1:
        tkinter.messagebox.showerror("Error69","Already registered please login")
        Alw.destroy()
    else:

        global Arw
        Arw = Toplevel(w)
        Arw.title("Register")
        Arw.configure(bg="white")
        Arw.geometry("300x200")
        Arw.resizable(0, 0)
        global A_Uname
        global A_p
        global A_u_e
        global A_p_e
        A_Uname = StringVar()
        A_p = StringVar()
        u = Label(Arw, text="UserName*:", font="bold", bg="white", fg="black", ).grid(row=2, pady=10)
        A_u_e = Entry(Arw, textvariable=A_Uname, bg="lightgrey")
        A_u_e.grid(row=3)
        p = Label(Arw, text="Password*:", font="bold", bg="white", fg="black", ).grid(row=4, pady=10)
        A_p_e = Entry(Arw, textvariable=A_p, bg="lightgrey")
        A_p_e.grid(row=5)
        b_R = Button(Arw, text="Register", bg="black", fg="white", width=10, height=2, command=reg_admin).grid(row=6,
                                                                                                               pady=10,
                                                                                                               padx=100)
        Arw.mainloop()


def T_reg():
    Tf = open("teacher login info.txt", "r")
    e = Tf.read()
    if len(e) > 1:
        tkinter.messagebox.showinfo("Error69", "Already registered please login")
        Tlw.destroy()
    else:
        global Trw
        global T_Uname
        global T_p
        global T_u_e
        global T_p_e
        Trw = Toplevel(w)
        Trw.title("Register")
        Trw.configure(bg="white")
        Trw.geometry("300x200")
        Trw.resizable(0, 0)
        T_Uname = StringVar()
        T_p = StringVar()
        u = Label(Trw, text="UserName*:", font="bold", bg="white", fg="black", ).grid(row=2, pady=10)
        T_u_e = Entry(Trw, textvariable=T_Uname, bg="lightgrey")
        T_u_e.grid(row=3)
        p = Label(Trw, text="Password*:", font="bold", bg="white", fg="black", ).grid(row=4, pady=10)
        T_p_e = Entry(Trw, textvariable=T_p, bg="lightgrey")
        T_p_e.grid(row=5)
        b_R = Button(Trw, text="Register", bg="black", fg="white", width=10, height=2, command=reg_teacher).grid(row=6,
                                                                                                                 pady=10,
                                                                                                                 padx=100)
        Trw.mainloop()


def A_login():
    global Alw
    global Au_verify
    global Ap_verify
    global Au_e
    global Ap_e
    Alw = Toplevel(w)
    Alw.title("Admin login")
    Alw.configure(bg="white")
    Alw.geometry("330x300")
    Alw.resizable(0, 0)
    Au_verify=StringVar()
    Ap_verify=StringVar()
    l = Label(Alw, text="login to access Admin controls:", bg="white",
              font="Arial 14 bold", padx=10, pady=10).grid(row=1, sticky=W)
    u = Label(Alw, text="UserName:", bg="white", fg="black", ).grid(row=2, sticky=W, padx=20, pady=10)
    Au_e = Entry(Alw,textvariable=Au_verify)
    Au_e.grid(row=2, padx=100)
    p = Label(Alw, text="Password:", bg="white", fg="black", ).grid(row=3, sticky=W, padx=20, pady=10)
    Ap_e = Entry(Alw,textvariable=Ap_verify,show="*")
    Ap_e.grid(row=3, padx=100)
    b_L = Button(Alw, text="login", bg="black", fg="white", width=10, height=2,command=Admin).grid(row=4)
    Label(Alw,bg="white",pady=5).grid(row=5)
    b_R = Button(Alw, text="Register", bg="black", fg="white", width=10, height=2, command=A_reg).grid(row=7, pady=5)
    q = Button(Alw, text="exit", bg="brown", fg="white", width=5, height=1, command=Alw.destroy).grid(row=8, padx=0,
                                                                                                      pady=5,
                                                                                                      sticky=E)
    Alw.mainloop()


def T_login():
    global Tlw
    global Tu_verify
    global Tp_verify
    global Tu_e
    global Tp_e
    Tlw = Toplevel(w)
    Tlw.title("Teacher login")
    Tlw.configure(bg="white")
    Tlw.geometry("330x300")
    Tlw.resizable(0, 0)
    Tu_verify = StringVar()
    Tp_verify = StringVar()
    l = Label(Tlw, text="login to access Teacher controls:", bg="white",
              font="Arial 14 bold", padx=4, pady=10).grid(row=1, sticky=W)
    u = Label(Tlw, text="UserName:", bg="white", fg="black", ).grid(row=2, sticky=W, padx=20, pady=10)
    Tu_e = Entry(Tlw,textvariable=Tu_verify)
    Tu_e.grid(row=2, padx=100)
    p = Label(Tlw, text="Password:", bg="white", fg="black", ).grid(row=3, sticky=W, padx=20, pady=10)
    Tp_e = Entry(Tlw,textvariable=Tp_verify,show="*")
    Tp_e.grid(row=3, padx=100)
    b_L = Button(Tlw, text="login", bg="black", fg="white", width=10, height=2,command=Teacher).grid(row=4)
    Label(Tlw, bg="white").grid(row=5, pady=5)
    b_R = Button(Tlw, text="Register", bg="black", fg="white", width=10, height=2, command=T_reg).grid(row=6, pady=5)
    q = Button(Tlw, text="exit", bg="brown", fg="white", width=5, height=1, command=Tlw.destroy).grid(row=7, padx=0,
                                                                                                      pady=5,
                                                                                                      sticky=E)
    Tlw.mainloop()


def S_login():
    global Slw
    global reg_no
    Slw = Toplevel(w)
    Slw.title("Student")
    Slw.configure(bg="white")
    Slw.geometry("300x200")
    Slw.resizable(0, 0)
    reg_no=StringVar()
    l = Label(Slw, text="Enter Registration No:            ", bg="white",
              font="Arial 14 bold", padx=10, pady=10).grid(row=1)
    format = Label(Slw, text="Format:\"AA00-BBB-000\"""", bg="white", fg="grey", font="none 12 italic").grid(
        row=2, padx=10, pady=5)
    e_u = Entry(Slw,textvariable=reg_no, width=20, bg="light blue",)
    e_u.grid(row=3, padx=20, pady=5)
    b=Button(Slw,text="Enter",bg="black",fg="white",width=10,height=2,command=Std_view).grid(row=4,pady=5)
    q = Button(Slw, text="exit", bg="brown", fg="white", width=5, height=1, command=Slw.destroy).grid(row=5,
                                                                                                      pady=5,
                                                                                                      sticky=E)

    Slw.mainloop()


def main_w():
    global w
    w = Tk()
    w.title("STUDENT MANAGEMNET SYSTEM")
    w.configure(bg="#002b2b")
    w.resizable(0, 0)
    l = Label(w, text="Welcome to\n\"Student Managment System\"\nchoose which profile you want to access:",
              bg="#002b2b", fg="white", font="algerian 20 bold", padx=20, pady=30).grid(row=1)
    b_a = Button(text="ADMIN", bg="#000000", fg="white",font=("none 12 bold") ,width=10, height=2, command=A_login).grid(row=2, pady=15)
    b_t = Button(text="TEACHER", bg="#000000", fg="white",font=("none 12 bold") , width=10, height=2, command=T_login).grid(row=4, pady=15)
    b_s = Button(text="STUDENT", bg="#000000", fg="white",font=("none 12 bold") , width=10, height=2, command=S_login).grid(row=6, pady=15)
    q = Button(w, text="quit", bg="#480607", fg="white",font=("none 12 bold") , width=5, height=1, command=w.destroy).grid(row=8, padx=10, pady=15,
                                                                                                sticky=E)

    w.mainloop()

main_w()
