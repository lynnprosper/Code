def save_data():
    fileD = open("deliveries.txt", "a")
    fileD.write("Depot:\n")
    fileD.write("%s\n" % depot.get())
    fileD.write("Desciption:\n")
    fileD.write("%s\n" % description.get())
    fileD.write("Address:\n")
    fileD.write("%s\n" % address.get("1.0", END))
    depot.delete(0, END)
    description.delete(0, END)
    address.delete("1.0", END)

def read_depots(file):
    depots=[]
    depots_f = open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots

from tkinter import *

app = Tk()
app.title('Head-Ex Deliveries')
Label(app, text = "Depot:").pack()
depot = StringVar()
depot.set(None)
option = read_depots("depots.txt")
OptionMenu(app, depot, *option).pack()
#depot = Entry(app)
#depot.pack()
Label(app, text = "Description:").pack()
description = Entry(app)
description.pack()
Label(app, text = "Address:").pack()
address = Text(app)
address.pack()
Button(app, text = "Save", command = save_data).pack()
app.mainloop()
