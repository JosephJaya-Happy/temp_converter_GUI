import tkinter as tink

Jaya = tink.Tk()
Jaya.title("temp")
Jaya.geometry('600x600')

input_var = tink.StringVar()
e1 = tink.Entry(master = Jaya, textvar=  input_var)
e1.place(x = 50, y = 100, width = 120)

output_var = tink.StringVar()
e2 = tink.Entry(Jaya, textvar = output_var)
e2.place(x = 50, y = 400, width = 120)

def convert():
    try:
        value = float(input_var.get())
        if conversion_type.get() == "c to f":
            result = value*1.8 + 32.0
        else:
            result = (value-32)/1.8
        output_var.set(str(result))

    except ValueError:
        output_var.set("no, Womp Womp")

conversion_type = tink.StringVar(value="c to f")
options = ["c to f", "f to c"]
dropdown = tink.OptionMenu(Jaya, conversion_type, *options)
dropdown.place(x = 50,y = 180)

b1 = tink.Button(Jaya, text = "convert", command = convert)
b1.place(x = 50, y = 250)

l1 = tink.Label(Jaya, text = "input")
l1.place(x = 50, y = 75)

l2 = tink.Label(Jaya, text = "output")
l2.place(x = 50, y = 425)

Jaya.mainloop()