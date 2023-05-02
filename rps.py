from tkinter import *
from tkinter import messagebox

import sys
import os
r=Tk()


def home_page():
    r.title('game options')
    r.geometry('1920x1080')
    r['bg']='pink'
    #'D:/Surabhi/rps-bg2.png'
    
    '''img = PhotoImage(file = 'D:/Surabhi/help-icon2.png')
    label = Label(r,image=img)
    label.grid(columnspan=5,rowspan=5)'''

    l1=Label(text='ROCK PAPER SCISSORS' +'  \U0001F311 '+' \U0001F4C3 '+' \u2702  ',background='#CC99FF',font='arial',fg='black',anchor=CENTER,bd=5,height=3,width=126,relief=GROOVE)
    l1.grid(columnspan=4,row=0,padx=15,pady=15)
    l2=Label(text='Choose game mode',background='#99CCFF',font='arial',fg='black',anchor=CENTER,bd=5,height=3,width=120,relief=GROOVE)
    l2.grid(columnspan=4,row=1,padx=15,pady=15)
    b1=Button(text='single player game  '+'\U0001F464',background='#89CFF0',font='arial',fg='black',anchor=CENTER,bd=5,height=3,width=30,relief=GROOVE,command=lambda:single())
    b1.grid(column=3,row=2,padx=15,pady=15)
    b2=Button(text='two player game  '+'\U0001F465 ',background='#89CFF0',font='arial',fg='black',anchor=CENTER,bd=5,height=3,width=30,relief=GROOVE,command=lambda:double())
    b2.grid(column=1,row=2,pady=15,padx=15)

    
import random
sc=0

def single():

    sc=0
    root=Tk()
    root.geometry('1920x1080')
    root.title("Rock Paper Scissors")
    root.configure(bg="#89CFF0")
 
    computer_value=["Rock","Paper","Scissor"]
 
    def reset_game():
       b1["state"] = "active"
       b2["state"] = "active"
       b3["state"] = "active"
       l1.config(text = "Player              ")
       l3.config(text = "Computer")
       l4.config(text = "")
 
    def end():
       global sc
       root2=Tk()
       root2.geometry='300x300'
       root2.configure(bg='#CCCCFF')
       root2.title("Your wins:")
       l3 = Label(root2, text ='Your score is  '+str(sc) +'!', font = 50, fg="#5B2C6F",bg='#CCCCFF' ,height=10, width=30)
       l3.pack()
       
       #messagebox.showinfo(sc)
 
    def button_disable():
       b1["state"] = "disable"
       b2["state"] = "disable"
       b3["state"] = "disable"
 
# If player selected rock
    def isrock():
       global sc
       c_v = random.choice(computer_value)
       if c_v == "Rock":    
           match_result = "Match Draw"
       elif c_v=="Scissor":
           match_result = "Player Win"
           sc=sc+1 
       else:
           match_result = "Computer Wins"
                     
       l4.config(text = match_result)
       l1.config(text = "Rock            ")
       l3.config(text = c_v)
       button_disable()
# If player selected paper
    def ispaper():
       global sc
       
       c_v = random.choice(computer_value)
       if c_v == "Paper":
           match_result = "Match Draw"
       elif c_v=="Scissor":
           match_result = "Computer Wins"
       else:
           match_result = "Player Win"
           sc=sc+1
                    
       l4.config(text = match_result)
       l1.config(text = "Paper           ")
       l3.config(text = c_v)
       button_disable()
# If player selected scissor
    def isscissor():
       global sc
       c_v = random.choice(computer_value)
       if c_v == "Rock":
           match_result = "Computer Wins"
       elif c_v == "Scissor":
           match_result = "Match Draw"
       else:
           match_result = "Player Win"
           sc=sc+1
       
       l4.config(text = match_result)
       l1.config(text = "Scissor         ")
       l3.config(text = c_v)
       button_disable()
    Label(root,text = "Rock Paper Scissor",font = "normal 20 bold",fg = "#8E44AD").pack(pady = 20)
    frame = Frame(root)
    frame.pack()
    l1 = Label(frame,
              text = "Player              ",
              font = 10)
    l2 = Label(frame,
              text = "VS             ",
              font = "normal 10 bold")
    l3 = Label(frame, text = "Computer", font = 10)
    l1.pack(side = LEFT)
    l2.pack(side = LEFT)
    l3.pack()
    l4 = Label(root,
              text = "",
              font = "normal 20 bold",
              bg = "white",
              width = 15 ,
              borderwidth = 2,
              relief = "solid")
    l4.pack(pady = 20)
    frame1 = Frame(root)
    frame1.pack()
    b1 = Button(frame1, text = "Rock",
               font = 10, width = 7,
               command = isrock)
    b2 = Button(frame1, text = "Paper ",
               font = 10, width = 7,
               command = ispaper)
    b3 = Button(frame1, text = "Scissor",
               font = 10, width = 7,
               command = isscissor)
 
    b1.pack(side = LEFT, padx = 10)
    b2.pack(side = LEFT,padx = 10)
    b3.pack(padx = 10)
    Button(root, text = "play again",
          font = 10, fg = "#8E44AD",
          bg = "black", command = reset_game).pack(pady = 20)
    Button(root, text = "End",
          font = 10, fg = "#8E44AD",
          bg = "black", command = lambda:end()).pack(pady = 20)
    
 
    #root.mainloop()




def double():



    a=Tk()

    global gg
    gg=-1

    def two_user():
        a.title('game')
        a.geometry('1920x1080')
        a['bg']='#CCCCFF'
        l1=Label(a,text="R O C K   P A P E R   S C I S S O R S !" +'  \U0001F311 '+' \U0001F4C3 '+' \u2702  ',background='#990033',font='impact',fg='black',anchor=CENTER,bd=5,height=3,width=100,relief=GROOVE)
        l1.grid(columnspan=5,row=0,padx=5,pady=5)

        global eg
        lg=Label(a,text='Enter how many games you want to play   ' + '  \u2794',background='#CC99FF',font='calibri',fg='black',anchor=CENTER,bd=5,height=2,width=40,relief=GROOVE)    
        lg.grid(column=2,row=1,padx=5,pady=5)
        eg=Entry(a,text='num of games',textvariable='gg',background='#CC99FF',font='calibre',bd=5,width=25,relief=GROOVE,fg='blue')
        eg.grid(column=3,row=1,padx=5,pady=5)
    
        global e1
        global e2
        l2=Label(a,text='Enter player 1 name '+'  \u2794',background='#0099CC',fg='black',font='calibre',anchor=CENTER,bd=5,height=2,width=25,relief=GROOVE)    #name1
        l2.grid(column=0,row=2,padx=5,pady=5)
        e1=Entry(a,text='Enter name1',background='#99CCFF',font='calibre',textvariable='n1',bd=5,width=15,relief=GROOVE,fg='blue')
        e1.grid(column=1,row=2,padx=8,pady=8)

        l3=Label(a,text='Enter player 2 name '+'  \u2794',background='#0099CC',font='calibre',fg='black',anchor=CENTER,bd=5,height=2,width=25,relief=GROOVE)    #name2
        l3.grid(column=3,row=2,padx=5,pady=5)
        e2=Entry(a,text='Enter name2',background='#99CCFF',font='calibre',textvariable='n2',bd=5,width=15,relief=GROOVE,fg='blue')
        e2.grid(column=4,row=2,padx=5,pady=5)

        global l5
        global l7
        global l9
        n1=e1.get()
        n2=e2.get()
        l4=Label(a,text=n1+' score '+' \u2794',background='#FF7C80',fg='black',font='calibre',anchor=CENTER,bd=5,height=2,width=25,relief=GROOVE)    #score1
        l4.grid(column=0,row=4,padx=5,pady=5)
        l5=Label(a,text='0',background='#FFCCCC',fg='blue',font='calibre',anchor=CENTER,bd=5,height=2,width=15,relief=GROOVE)     
        l5.grid(column=1,row=4,padx=5,pady=5)

        l6=Label(a,text=n2+' score '+' \u2794',background='#FF7C80',fg='black',font='calibre',anchor=CENTER,bd=5,height=2,width=25,relief=GROOVE)    #score1
        l6.grid(column=3,row=4,padx=5,pady=5)
        l7=Label(a,text='0',background='#FFCCCC',fg='blue',font='calibre',anchor=CENTER,bd=5,height=2,width=15,relief=GROOVE)     
        l7.grid(column=4,row=4,padx=5,pady=5)

        l8=Label(a,text='GAMES LEFT '+' \u2794',background='#CC9900',font='calibre',fg='black',anchor=CENTER,bd=5,height=2,width=35,relief=GROOVE)     #games left
        l8.grid(column=2,row=5,padx=5,pady=5)
        l9=Label(a,text='',background='#CC9900',fg='blue',font='calibre',anchor=CENTER,bd=5,height=2,width=26,relief=GROOVE)     #l9 to be config
        l9.grid(column=3,row=5,padx=5,pady=5)

        '''photo = PhotoImage(file = "D:/Surabhi/help-icon2.png")
        bh=Button(a,image=photo,bd=5,relief='raised',command=lambda:help())    #help 
        bh.image=photo
        bh.grid(column=4,row=0)''' 
        
        bh=Button(a,text='help ?',background='#89CFF0',bd=5,relief='raised',fg='black',font='lucida',height=3,width=5,command=lambda:help())    #help 
        bh.grid(column=4,row=0,padx=5,pady=5)


        l10=Label(a,text="LET'S START!",background='#993366',font='impact',fg='black',anchor=CENTER,bd=5,height=2,width=40,relief=GROOVE)     
        l10.grid(columnspan=5,row=6,padx=5,pady=5) 

        b1=Button(a,text='  rock  ',background='#996633',font='lucida',fg='black',command=lambda:f1('rock'),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b1.grid(column=1,row=7,padx=5,pady=5)

        b2=Button(a,text='  rock  ',background='#996633',font='lucida',fg='black',command=lambda:func('rock'),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b2.grid(column=3,row=7,padx=5,pady=5)

        b3=Button(a,text=' paper  ',background='#996633',font='lucida',fg='black',command=lambda:f1('paper'),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b3.grid(column=1,row=8,padx=5,pady=5)

        b4=Button(a,text=' paper  ',background='#996633',font='lucida',fg='black',command=lambda:func('paper'),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b4.grid(column=3,row=8,padx=5,pady=5)

        b5=Button(a,text='scissors',background='#996633',font='lucida',fg='black',command=lambda:f1('scissors'),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b5.grid(column=1,row=9,padx=5,pady=5)

        b6=Button(a,text='scissors',background='#996633',font='lucida',fg='black',command=lambda:func('scissors'),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b6.grid(column=3,row=9,padx=5,pady=5)

        b7=Button(a,text='restart game',background='#006600',font='calibre',fg='white',command=lambda:restart_program(),height=2,width=15,activebackground='green',bd=5,relief='raised')    
        b7.grid(columnspan=5,row=10,padx=5,pady=5)



    
    def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)    

    def f1(x):
        global u1
        u1=x
        


    def help():
        messagebox.showinfo('help box','\nClick on rock or paper or scissors button to choose your option.\n \n rock wins over scissors. scissors wins over paper and paper wins over rock.\n\n   (SCISSORS > PAPER)\n   (PAPER > ROCK) \n   (ROCK > SCISSORS)\n ')

    global call_num
    call_num=0
    global p1
    global p2
    p1=0
    p2=0

    def func(y):
        n1=e1.get().upper()
        n2=e2.get().upper()
        global call_num
        if call_num==0:
            global gg
            gg=int(eg.get())
            gg=gg+1

        call_num=1
        global u1
        global u2
        u2=y
        global p1
        global p2


        if gg!=1:    
            gg=gg-1
            n=gg-1
            l9.config(text=n)
            if u1=='scissors':
                if u2=='paper':
                    p1=1+p1
                    l5.config(text=p1)
                    l7.config(text=p2)          

                elif u2=='rock':
                    p2=1+p2
                    l5.config(text=p1)
                    l7.config(text=p2)          

                elif u2==u1:
                    l5.config(text=p1)
                    l7.config(text=p2)          

                else:
                    print('invalid')    
        

            elif u1=='paper':
                if u2=='paper':
                    l5.config(text=p1)
                    l7.config(text=p2)          

                elif u2=='rock':
                    p1=p1+1
                    l5.config(text=p1)
                    l7.config(text=p2)          

                elif u2=='scissors':
                    p2=p2+1
                    l5.config(text=p1)
                    l7.config(text=p2)          
                    
                else:
                    print('invalid')              
                

            elif u1=='rock':
                if u2=='rock':
                    l5.config(text=p1)
                    l7.config(text=p2)          

                elif u2=='scissors':
                    p1=p1+1
                    l5.config(text=p1)
                    l7.config(text=p2)          
        
                elif u2=='paper':
                    p2=p2+1
                    l5.config(text=p1)
                    l7.config(text=p2)                
    
                else:
                    print('invalid')
            if gg==1:
                if p1>p2:
                    s=n1+' WINS THE GAME '+'\U0001F3C6 '
                elif p1<p2:
                    s=n2+' WINS THE GAME '+'\U0001F3C6 '
                else:
                    s="GAME IS A TIE "+'\U0001F91D '        
                messagebox.showinfo('result',s)  
    
        
            else:
                print('invalid')


 
        


    two_user()
    a.mainloop()





   

home_page()
r.mainloop()
