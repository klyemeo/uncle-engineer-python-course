import math
from tkinter import  *
from tkinter import ttk,messagebox
GUI = Tk()
GUI.title('Plotty')
GUI.geometry('700x600')
#select your photo to put in '---'
bg = PhotoImage(file = r'D:\Users\ASUS TUF FX505DT\Downloads\cone-icon.png')
BG = Label(GUI, image = bg)
BG.pack()
#set your head(text)
L = Label(GUI, text = 'cone surface calculation', font = (None,20))
L.pack()
#create block(UI)
v_quantity = StringVar() 
v_quantity1 = StringVar() 
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()
E2 = ttk.Entry(GUI, textvariable=v_quantity1, font=(None,20))
E2.pack()
#function for create graph
class cone:
    def _init_(self,radius, height) -> float:
        self.radius = radius 
        self.height = height
        assert radius >= 0, "radius cannot be negative"
        assert height >= 0, "height cannot be negative"
        radius = float(E1.get())
        height = float(E2.get())
    def cone_surface_area(self):
        Area = math.pi*self.radius+math.sqrt(self.radius)**2+self.height**2
        messagebox.showinfo('พื้นที่ทั้งหมด','พื้นที่ผิวทั้งหมด {}' .format(Area))
    v_quantity.set('')
    v_quantity1.set('')
    E1.focus()
try:
    B = ttk.Button(GUI, text='calculate',command=cone.cone_surface_area)
    B.pack(ipadx=30,ipady=20,pady=20) 
except AttributeError:
        print()
GUI.mainloop()








