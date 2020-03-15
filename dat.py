from tkinter import *
import pandas as pd
import datetime

def submit_feild():
    path='C:\\Users\\rvp39\\Desktop\\expenses.xlsx'
    #path is where your excel file is 
    df1=pd.read_excel(path)
    SeriesA=df1['Date']
    SeriesB=df1['Ammount']
    SeriesC=df1['Reason']
    A=pd.Series(entry1)
    B=pd.Series(entry2.get())
    C=pd.Series(entry3.get())
    SeriesA=SeriesA.append(A)
    SeriesB=SeriesB.append(B)
    SeriesC=SeriesC.append(C)
    df2=pd.DataFrame({"Date":SeriesA,"Ammount":SeriesB,"Reason":SeriesC})
    df2.to_excel(path,index = False)
    #entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


master=Tk()
Label(master,text="Date").grid(row=3)
Label(master,text="Ammount").grid(row=4)
Label(master,text="Reason").grid(row=5)
date=datetime.datetime.today()
entry1=date.strftime("%d/%m/%y")
Label(master,text=entry1).grid(row=3, column=2)
entry2=Entry(master)
entry3=Entry(master)
#entry1.grid(row=3,column=2)
entry2.grid(row=4,column=2)
entry3.grid(row=5,column=2)
Button(master, text="quit",command=master.quit).grid(row=6,column=2,pady=4)
Button(master, text="submit",command=submit_feild).grid(row=7,column=2,pady=4)

mainloop()