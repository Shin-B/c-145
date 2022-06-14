from tkinter import *

root=Tk()

root.geometry("1920x1080")

root.title("FIBONACCI")

root.configure(bg="lightblue")

label_series = Label(root, text="Fibonacci series: ")
label_flower = Label(root)
label_spiral = Label(root)

def Fibonacci():
    num=200
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter<= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1 
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    label_flower['text'] = "flower if fully bloomed"
    label_spiral["text"] = "Spirals in right direction are " + str(first_no) + " and spirals in the left direction are " + str(second_no) + "\n. Total spiral are " + str(sum)

btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()

