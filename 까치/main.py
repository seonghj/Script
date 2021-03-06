from tkinter import *
from tkinter import font
import urllib
import http.client
import tkinter.messagebox

class mainGUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x400")
        self.window.title("영화 정보 검색")
        self.Boxfontstyle = font.Font(self.window, size=14, weight='bold', family='Consolas')
        self.InitTopText()
        self.InitSearchBox()
        self.window.mainloop()

    def InitTopText(self):
        self.Topfontstyle = font.Font(self.window, size=22, weight='bold', family='Consolas')
        self.Toptext = Label(self.window,font = self.Topfontstyle,text="영화 정보 검색 APP")
        self.Toptext.pack()

    def InitSearchListBox(self):
        self.SearchListBox = Listbox(self.window, font=self.Boxfontstyle,activestlye='none'\
                                     )

    def InitSearchBox(self):
        self.SearchEntryBox = Entry(self.window, font=self.Boxfontstyle)
        self.SearchEntryBox.pack()
        self.SearchButton = Button(self.window,overrelief = 'solid',text = "검색",command=self.Search)
        self.SearchButton.pack()
        self.SearchTextBox = Entry(self.window, font=self.Boxfontstyle, text="")
        self.SearchTextBox.pack()

    def Search(self):
        pass


mainGUI()



