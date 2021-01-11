import tkinter as tk
from tkinter import ttk
from view.tkinter.distribution_tk import DistributionApp
from view.tkinter.staff_units_tk import StaffUnitsApp
from view.tkinter.division_tk import DivisionApp


root = tk.Tk()
root.title("Tab Widget")
root.geometry("800x670+351+174")
tabControl = ttk.Notebook(root)

tab1 = DistributionApp()
tab2 = DivisionApp()
tab3 = StaffUnitsApp()

tabControl.add(tab1, text='Distribution')
tabControl.add(tab2, text='Division')
tabControl.add(tab3, text='Staff unit')
tabControl.pack(expand=1, fill="both")


root.mainloop()