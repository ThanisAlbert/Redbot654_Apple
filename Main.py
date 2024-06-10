import os
import tkinter
from tkinter import messagebox
from Gui.Gui import Gui

class Main:

    def __init__(self,input_file):
        self.input_file = input_file

    def open_gui(self):
        gui = Gui(self.input_file)
        gui.open_gui()

input_file = "CTO_Order_loading_BOT_Template.xlsm"
main = Main(input_file)
try:
    os.remove("Log.log")
except:
    pass
main.open_gui()

