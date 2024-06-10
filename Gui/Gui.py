import base64
import ctypes
import tkinter as tk
from io import BytesIO
from PIL import ImageTk, Image
from Excel.ProcessExcel import ProcessExcel
from Gui.pic2str import apple

class Gui:

    def __init__(self,inputfile):
        self.inputfile = inputfile

    def open_gui(self):

        global label_status

        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

        window = tk.Tk()
        window.configure(background='#00AAE4')
        window.title("Apple")

        window.columnconfigure(0, weight=1, minsize=75)
        window.rowconfigure(0, weight=1, minsize=50)
        window.columnconfigure(1, weight=1, minsize=75)
        window.rowconfigure(1, weight=1, minsize=50)
        window.columnconfigure(2, weight=1, minsize=75)
        window.rowconfigure(2, weight=1, minsize=50)

        w = 350
        h = 400
        x = 900
        y = 0

        window.geometry('%dx%d+%d+%d' % (w, h, x, y))

        frame_image = tk.Frame(
            master=window,
            relief=tk.RAISED,
            background='#00AAE4',
        )

        byte_data = base64.b64decode(apple)
        image_data = BytesIO(byte_data)
        image = Image.open(image_data)
        resize_image = image.resize((120, 100))
        img = ImageTk.PhotoImage(resize_image)
        label2 = tk.Label(master=frame_image, image=img)
        label2.pack()

        frame_button = tk.Frame(
            master=window,
            relief=tk.RAISED,
            background='#00AAE4',
        )

        button = tk.Button(
            master=frame_button,
            width=15,
            height=2,
            text="PlaceOrder",
            command=self.read_excel
        )
        button.pack()

        frame_status = tk.Frame(
            master=window,
            relief=tk.RAISED,
            background='#00AAE4',
        )

        label_status = tk.Label(master=frame_status, text="", fg="white", bg="#00AAE4", font=('Arial', 13))
        label_status.pack()

        frame_image.grid(row=0, column=0)
        frame_button.grid(row=1, column=1, pady=50)
        frame_status.grid(row=2, column=1, pady=50)

        window.mainloop()

    def read_excel(self):

        excel = ProcessExcel(self.inputfile,label_status=label_status)
        excel.process_excel()

