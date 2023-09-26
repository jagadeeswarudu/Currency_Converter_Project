from tkinter import *
import tkinter as tk
import requests
import pyttsx3
from Country_ID import ID
window=tk.Tk()
window.geometry("500x360")
window.configure(bg='#63d0d6')
window.title("Currency Converter")
window.resizable(False,False)
bg=PhotoImage(file="world.png")
ok=PhotoImage(file="R.png")
photo=PhotoImage(file='logo.png')
window.wm_iconphoto(False,photo)
label0=tk.Label(window,image=bg)
label0.place(x=-1,y=0)
reader=pyttsx3.init()
rate = reader.getProperty('rate')
reader.setProperty('rate',110)
voices = reader.getProperty('voices')
reader.setProperty('voice', voices[0].id)
def read(txt):
    reader.say(txt)
    reader.runAndWait()
def voice():
    read('Enter Amount')
    read('Enter FromCurrency')
    read('Enter ToCurrency')
def clicked():
    class Currency_convertor:
        rates = {}
        def __init__(self, url):
            data = requests.get(url).json()
            self.rates = data["rates"]
        def convert(self, from_currency, to_currency, oup_amount):
            initial_amount = oup_amount
            if from_currency != 'EUR':
                oup_amount = oup_amount / self.rates[from_currency]
            oup_amount = round(oup_amount * self.rates[to_currency], 2)
            data=str(initial_amount)+" "+str(from_currency)+" "+" = "+" "+str(oup_amount)+" "+str(to_currency)
            l5=tk.Label(window,text=data,font="Times 15 bold",bg="#63d0d6")
            l5.place(x=160,y=320)
            read(data)
    if __name__ == "__main__":
        YOUR_ACCESS_KEY = '58ef80aa4519eb57dcb7df22ceb6d3c3'
        url = str.__add__('http://data.fixer.io/api/latest?access_key=', YOUR_ACCESS_KEY)
        c = Currency_convertor(url)
        from_country = ID.id(e2.get())
        to_country = ID.id(e3.get())
        inp_amount = float(e1.get())
        c.convert(from_country,to_country, inp_amount)
l1=tk.Label(window,text=" Currency Converter ",font=("Comic Sans MS",20,"bold"),fg="blue",bg='#7ce7f7',borderwidth=1,relief="solid")
l1.place(x=105,y=30)
b2=tk.Button(window,text='  Start  ',font="Times 10 bold",fg="black",bg="#7ce7f7",command=voice)
b2.place(x=230,y=90)
l2=tk.Label(window,text=" Enter Amount Here :            ",font="Times 10 bold",bg='#7ce7f7',fg="#e85e02",borderwidth=1,relief="solid")
l2.place(x=80,y=130)
l3=tk.Label(window,text=" From Currency(Country) : ",font="Times 10 bold",bg='#7ce7f7',fg="#e85e02",borderwidth=1,relief="solid")
l3.place(x=80,y=170)
e1=tk.Entry(window,bg="#515657")
e1.place(x=290,y=130)
e2=tk.Entry(window,bg="#515657")
e2.place(x=290,y=170)
l3=tk.Label(window,text=" To Currency(Country) :      ",font="Times 10 bold",bg='#7ce7f7',fg="#e85e02",borderwidth=1,relief="solid")
l3.place(x=80,y=210)
e3=tk.Entry(window,bg="#515657")
e3.place(x=290,y=210)
b1=tk.Button(window,image=ok,bg="#7ce7f7",command=clicked)
b1.place(x=220,y=260)
window.mainloop()

