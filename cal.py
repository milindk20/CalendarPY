'''import calendar

year = int(input('Enter Year in digit: '))
month = int(input('Enter Month in digit: '))
cal=calendar.month(year,month)
print(cal,type(cal))'''


'''from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Calender")
Label(root,text=cal).pack()
root.mainloop()'''


def expand(data):
        file=open("cal.txt","a+")
        file.write(data)
        file.close()

def new(data):
        file=open("cal.txt","w")
        file.write(data)
        file.close()        
def show():
        global calen
        file=open("cal.txt","r")
        calen=file.read()
        file.close()        
        

import calendar

year = int(input('Enter Year in digit: '))
month = int(input('Enter Month in digit: '))
cal=calendar.month(year,month)
#print(cal,type(cal))
cal=cal.split()
cal
new(cal[0]+" "+cal[1]+"\n")
weekdays = cal[2:9]
s1=""
for s in weekdays:
     s1+=s +" "
expand(s1+"\n")
n=9
count=0
def printdays(n,count):
  #   try:
     #print(count)
     if count>9:
          return
     days = cal[n:n+7]
     days
     s1=""
     for s in days:
          if int(s)>9:
               s1+=s +""" """
          else:
               s1+=s +"""  """
     expand(s1+"\n")
     printdays(n+7,count+1)
  #   except:
   #       pass
printdays(n,count)


  
import tkinter as tk
import tkinter.scrolledtext as st
  
# Creating tkinter window
win = tk.Tk()
win.title("ScrolledText Widget")
  
# Title Label
'''tk.Label(win, 
         text = "ScrolledText Widget Example", 
         font = ("Times New Roman", 15), 
         background = 'green', 
         foreground = "white").grid(column = 0,
                                    row = 0)'''
  
# Creating scrolled text area
# widget with Read only by
# disabling the state
show()
#tk.Label(win, text=calen).pack()

text_area = st.ScrolledText(win,
                            width = 30, 
                            height = 8, 
                            font = ("Times New Roman",
                                    15))
  
text_area.grid(column = 0, pady = 10, padx = 10)
  
# Inserting Text which is read only
show()
text_area.insert(tk.INSERT,calen)

# Making the text read only
#text_area.configure(state ='disabled')
win.mainloop()