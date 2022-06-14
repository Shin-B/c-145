from tkinter import *

root = Tk()
root.title("Button demo")
root.geometry("400x400")
label_id = Label(root)
label_name = Label(root)
label_dob = Label(root)
label_pin = Label(root)
label_Address = Label(root)
label_Atdtfv = Label(root)



def btnDemo():
    label_id['text']="ID: 1982719349"
    label_name['text']="Name: Winnie the Pooh"
    label_dob['text']="Date of birth :21 August 1921"
    label_pin['text']="Pin no. : 451478"
    label_Address['text']="Address: Disney Land, Hong kong"
    label_Atdtfv['text']="Authorisation to drive the following vehicles : Two four"

btn = Button(root, text="Show my driving license", command= btnDemo)
btn.pack()
label_id.pack()
label_id.pack()
label_name.pack()
label_dob.pack()
label_pin.pack()
label_Address.pack()
label_Atdtfv.pack()
root.mainloop()