from tkinter import *
from tkinter import PhotoImage


root = Tk()
root.overrideredirect(1)

root.title("Lab Extract Maker")
root.geometry("480x320")



######  function codes

def closewindow():
    root.quit()

###### top frame

topframe = Frame(root, height=60, bg="white", borderwidth=5, relief=SUNKEN)
topframe.pack_propagate(0)
topframe.pack(side=TOP, fill="x")

label_title = Label(topframe, text="Syringe Pump Extract Maker", fg="green", bg="white", font="Helvetica 20 bold")
label_title.pack(side=BOTTOM)

button_exit = Button(topframe, width=3, text="X",command=closewindow)
button_exit.pack(side=BOTTOM, anchor="se")

###### leftside frame

leftframe = Frame(root, bg="royal blue",borderwidth=4, relief=SUNKEN)
#leftframe.pack_propagate(0)
leftframe.pack(side=LEFT, fill="y")

img=PhotoImage(file="homemadan.png")
btn1 = Button(leftframe, image=img,text="HOME")
btn1.pack(padx=6, pady=10, side=TOP)

img1=PhotoImage(file="startmadan.png")
btn2 = Button(leftframe, text="START",image=img1)
btn2.pack(padx=6, side=TOP)

img2=PhotoImage(file="stopmadan.png")
btn3 = Button(leftframe, text="STOP",image=img2)
btn3.pack(padx=6, pady=10, side=TOP)

##### middle frame

middleframe = Frame(root, bg="khaki2", borderwidth=4, relief=SUNKEN)
middleframe.pack_propagate(0)
middleframe.pack(side=LEFT, fill="both")

# volume control

label_1 = Label(middleframe, bg="khaki2", text="Volume Control", fg="black", font="Helvetica 12 bold")
label_1.grid(row=0, column=0, padx=10, pady=15, columnspan=3)

buttton_dec = Button(middleframe,bg="dim gray" ,text="-", padx=10, font="Helvetica 8 bold")
buttton_dec.grid(row=1, column=0)

label_vol = Label(middleframe, bg="khaki2", text="1.5", font="Helvetica 8 bold", padx=5)
label_vol.grid(row=1, column=1)

buttton_inc = Button(middleframe, bg="dim gray",text="+", padx=10, font="Helvetica 8 bold")
buttton_inc.grid(row=1, column=2)

button_setvol = Button(middleframe,bg="light grey", text="Set Total Volume", font="Helvetica 7", padx=6, pady=5)
button_setvol.grid(row=2, column=0, pady=10)

button_defaultvol = Button(middleframe,bg="light grey", text="Reset to Default", font="Helvetica 7", padx=6, pady=5)
button_defaultvol.grid(row=2, column=2, pady=10)

# cycle control


label_2 = Label(middleframe, bg="khaki2", text="Cycles Control", fg="black", font="Helvetica 12 bold")
label_2.grid(row=3, column=0, padx=10, pady=15, columnspan=3)

buttton_dec1 = Button(middleframe,bg="dim gray", text="-", padx=10, font="Helvetica 8 bold")
buttton_dec1.grid(row=4, column=0)

label_vol1 = Label(middleframe, bg="khaki2", text="1.5", font="Helvetica 8 bold", padx=5)
label_vol1.grid(row=4, column=1)

buttton_inc1 = Button(middleframe,bg="dim gray", text="+", padx=10, font="Helvetica 8 bold")
buttton_inc1.grid(row=4, column=2)

button_setcycle = Button(middleframe,bg="light grey", text="Set Cycles Number", font="Helvetica 7", padx=6, pady=5)
button_setcycle.grid(row=5, column=0, pady=10)

button_defaultcycle = Button(middleframe,bg="light grey", text="Reset to Default", font="Helvetica 7", padx=6, pady=5)
button_defaultcycle.grid(row=5, column=2, pady=10)

##### right frame

rbg="wheat2"
rightframe = Frame(root, bg=rbg, borderwidth=4, relief=SUNKEN)
rightframe.pack(side=LEFT, fill="both")

# current cycle count label
lbl1 = Label(rightframe,bg=rbg ,text="Current Cycle", fg="black", font="Helvetica 9 bold")
lbl1.grid(row=0, column=0, pady=(30, 0), columnspan=2)

label_cyclecount = Label(rightframe,bg=rbg , fg="black", font="Helvetica 9 bold", text="0")
label_cyclecount.grid(row=1, column=0, pady=(5, 0), columnspan=2)

lbl2 = Label(rightframe, bg=rbg ,text="Time Elapsed", fg="red", font="Helvetica 7 bold")
lbl2.grid(row=2, column=0, pady=(25, 0))

lbl3 = Label(rightframe,bg=rbg , text="Time Remaining", fg="green", font="Helvetica 7 bold")
lbl3.grid(row=2, column=1, pady=(25, 0))

label_timeel = Label(rightframe,bg=rbg , text="00:00:00", fg="red", font="Helvetica 7 bold")
label_timeel.grid(row=3, column=0, pady=(5, 0), padx=5)

label_timerem = Label(rightframe,bg=rbg , text="00:00:00", fg="green", font="Helvetica 7 bold")
label_timerem.grid(row=3, column=1, pady=(5, 0), padx=5)


# message box

mbox=Message(rightframe,bg="ghost white",text="this is a sample message displayed on the screen",font="Helvetica 7")
mbox.grid(row=4,column=0,pady=15)

# scrollbar






root.mainloop()
