from tkinter import *
from tkinter import ttk

# Function for finding CAPITAL letters in a string and returning the index
def capital_indexes (*args):
    x = user_input.get ()
    return_list = []
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range (0, len (x)):
        for l in range (0, len (capital_letters)):
            if x [i] == capital_letters [l]:
                return_list.append (i)

    index.set (str (return_list))

main = Tk ()
main.title ("Capital Index")

mainframe = ttk.Frame (main, padding = "3 3 12 12")
mainframe.grid (column = 0, row = 0, sticky = (N, W, E, S))
main.columnconfigure (0, weight = 1)
main.rowconfigure (0, weight = 1)

# User input
user_input = StringVar ()
user_entry = ttk.Entry (mainframe, width=7, textvariable=user_input)
user_entry.grid (column = 2, row = 1, sticky = (W, E))

index = StringVar ()
ttk.Label (mainframe, textvariable = index).grid (column = 2, row = 2, sticky = (W, E))

ttk.Button (mainframe, text = "Capital Index", command = capital_indexes).grid(column = 3, row = 3, sticky = (W))

ttk.Label (mainframe, text = "String").grid (column = 3, row = 1, sticky = W) 
ttk.Label (mainframe, text = "Result").grid (column = 1, row = 2, sticky = E)
ttk.Label (mainframe, text = "Capital Index List").grid (column = 3, row = 2, sticky = W)

for child in mainframe.winfo_children ():
    child.grid_configure (padx = 5, pady = 5)
  
user_entry.focus ()
main.bind ("<Return>", capital_indexes)

main.mainloop ()