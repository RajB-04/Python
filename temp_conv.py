from tkinter import *

window = Tk()
window.title('Celcius to Fahrenheit')
window.minsize(width=300, height=100)
window.config(padx=10, pady=20)

def calculate():
    temp = float(input.get())
    f_temp = (temp * (9/5)) + 32
    output['text'] = f"{f_temp:.2f}" 

label_1 = Label(text='Enter temp in celcius', font=("Arial"))
label_1.grid(column=2, row=0, pady=5)

temp = Label(text='Temperature', font=(12))
temp.grid(column=1, row=2)
input = Entry(text="Enter here", width=10)
input.grid(column=2, row=2, pady=5)
celcius = Label(text="Celcius")
celcius.grid(column=3, row=2, pady=5)

button = Button(text='Calculate', command=calculate, width=8, bg='green', font='italic')
button.grid(column=2, row=4, pady=10)

label_2 = Label(text="is equal to", font=(12))
label_2.grid(column=1, row=6, pady=5)
output = Label(text="0")
output.grid(column=2, row=6, pady=5)
fahrenheit = Label(text="Fahrenheit")
fahrenheit.grid(column=3, row=6, pady=5)





window.mainloop()