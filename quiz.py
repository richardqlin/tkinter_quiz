from tkinter import *

root =Tk()

import time


frame1=Frame(root)
frame1.grid(row=0,column=0)

Score = IntVar()        


frame3=Frame(root)
frame3.grid(row=7, column=0)


class Quiz:

    def __init__(self, question, values ,answer,index):
        self.frame=Frame(root)
        self.question = Label(self.frame,text=question)
        self.answer = answer
        self.tracker = StringVar()
        self.options = values
        self.answer_index = index

    def show_question(self):
        self.frame.grid(row=2,column=0)
        self.question.grid(row=2,column=0)
        i=0
        self.tracker.set(0)
        for j in self.options:
            Radiobutton(self.frame,text =j,variable =self.tracker,value=j).grid(row=i+3,column=0)
            i+=1
    def hide_question(self):
        self.frame.grid_forget()
      
        self.question.grid_forget()
        i=0
        for j in self.options:
            Radiobutton(self.frame,text =j,variable =self.tracker,value=j).grid_forget()
            i+=1
    def changecolor(self):
        i=0
  
        for j in self.options:
            Radiobutton(self.frame,text =j,fg='red',variable =self.tracker,value=j).grid(row=i+3,column=0)
            #print(j)
            i+=1
    def correct(self):
        print( self.options)
        self.options[self.answer_index]
        Radiobutton(self.frame,fg='green',text=self.options[self.answer_index]).grid(row=self.answer_index+3,column=0)

lst1=['3','2','4','10']
quiz1 = Quiz('what is 1+1?',lst1,'2',1)


lst2=['Sacremento','Washangton DC','Settle','Houston','New York']
quiz2 = Quiz('what is the capital in USA?',lst2,'Washangton DC',1)

lst3=['Jupiter','Saturn','Earth','Mars']
quiz3 = Quiz('What is the largest planet in the solor system?',lst3,'Jupiter',0)

lst4=['China','India','USA','Japan']
quiz4 = Quiz('Which country has the most population in the world?',lst4,'China',0)


lst= [quiz1,quiz2,quiz3,quiz4]

ind=score=0

flag =0
def submit():
    global ind,score, flag
    ans=lst[ind-1]
    ans.changecolor()
    ans.correct()
   
    if ans.answer==ans.tracker.get() and flag==0:
        score += 1
        flag=1 
    
    Score.set(score)

def next():
    global ind,i,flag
    try:
        lst[ind].show_question()
        flag=0
        button= Button(frame3,text='Submit',command=submit)
        button.grid(row=7,column=0)
        
        ind +=1
        if ind==len(lst)-1:
            ind =len(lst)-1
        lst[ind].hide_question()
    except:
        print('index out of range')

 
b1=Button(frame3,text='Next', command=next)
b1.grid(row=7,column=1)
button= Button(frame3,text='Submit',command=submit)
button.grid(row=7,column=0)
label0=Label(frame1, text="Score: ")
label0.grid(row=0,column=0)


label1=Label(frame1, text="Score",textvariable=Score)
label1.grid(row=0,column=1)




