from tkinter import *# importing all functions frim the tkinter module
def hcf_and_lcm():
    label_num1.grid(row=1, column=4)
    label_num2.grid(row=2, column=4)
    num1.grid(row=1, column=5)
    num2.grid(row=2, column=5)

    find1.grid(row=4, column=4, columnspan=2)

def check1():
    hcf.delete(0, END)
    lcm.delete(0, END)

    x = num1.get()
    x = int(x)
    y = num2.get()
    y = int(y)

    # for HCF
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            h = i

    label_hcf.grid(row=6, column=4)
    hcf.grid(row=6, column=5)
    hcf.insert(INSERT, h)

    # for LCM
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):# if the remainder of greater divided by value of x and remainder of greater divided by y is eual to 0 
            l = greater
            break
        greater += 1

    label_lcm.grid(row=5, column=4)
    lcm.grid(row=5, column=5)
    lcm.insert(INSERT, l)

# Driver Code
top = Tk()
top.title("Anokhautomation-HCF&LCM CALCULATOR")
top.geometry("500x300")
# top.configure(bg="yellow")
top["background"] = "#ffffff"

# gui for HCF and LCM
label_num1 = Label(top, text="First Number", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")
label_num2 = Label(top, text="Second Number", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")

num1 = Entry(top, width=20)
num2 = Entry(top, width=20)

find1 = Button(top, text="CALCULATE LCM and HCF", command=lambda: check1(), width=22, background="#5D6D7E",
               foreground="white")

label_hcf = Label(top, text="HCF", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")
label_lcm = Label(top, text="LCM", fg="#5D6D7E", width=20, bg="white", font="Helvetica 14 bold italic")

hcf = Entry(top, width=20)
lcm = Entry(top, width=20)

hcf_and_lcm()
top.mainloop()
