from tkinter import *
from tkinter import ttk
import webbrowser
import pyautogui as pg
GUI = Tk()
GUI.title('program for calendar')
GUI.geometry('500x300')
def calendar():
    pg.click(1808,1053)
def Google():
    webbrowser.open('https://www.google.com')
def vscode():
    pg.click(453,1055)
B1 = Button(GUI, text = 'calendar1',command =  calendar)
B1.pack()
B2 = Button(GUI,text = 'calendar2',command =  calendar)
B2.pack()
B3 = Button(GUI,text = 'Google Chrome', command = Google)
B3.pack()
B4 = Button(GUI,text = 'Open vscode', command = vscode)
B4.pack()



GUI.mainloop

