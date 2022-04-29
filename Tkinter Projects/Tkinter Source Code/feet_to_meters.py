# Importing everything from tkinter
from tkinter import *
# Importing newer widgets from a submodule in tkinter
from tkinter import ttk

# Calculation for the program
def calculate (*args):
    try:
        value = float (feet.get ())
        meters.set (int (0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass
        
# Main application window creation
root = Tk ()
root.title ("Feet to Meters")

# Content frame creation
mainframe = ttk.Frame (root, padding="3 3 12 12")
mainframe.grid (column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure (0, weight=1)
root.rowconfigure (0, weight=1)

# Entry widget creation
feet = StringVar ()
feet_entry = ttk.Entry (mainframe, width=7, textvariable=feet)
feet_entry.grid (column=2, row=1, sticky=(W, E))

# Meters label creation
meters = StringVar ()
ttk.Label (mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# Calculate button creation
ttk.Button (mainframe, text="Calculate", command=calculate).grid(column=3, row=3, stick=W)

# Labels creation for application usage
ttk.Label (mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label (mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label (mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children ():
    child.grid_configure (padx=5, pady=5)
    
feet_entry.focus()
root.bind ("<Return>", calculate)

root.mainloop ()