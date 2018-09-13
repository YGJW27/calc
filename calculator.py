import types
from math import *
from tkinter import *
from tkinter.ttk import Button
import numpy as np


def calc(display):
    d=display.get()
    d=d.replace('√','sqrt')
    d=d.replace('^','**')
    d=d.replace('π','pi')
    try:
        if abs(eval(d))>10e15:
            display.set("ERROR")
        else:
            if type(eval(d))==type(1):
                display.set(eval(d))
            else:
                display.set("%.5f" %eval(d))
    except ValueError:
        display.set("Value Error")
    except SyntaxError:
        display.set("Syntax Error")
    except ZeroDivisionError:
        display.set("Zero Division Error")
    except:
        display.set("Error")

        
def clearfun(event):
    global display
    display.set('')

def enterfun(event):
    global display
    calc(display)
            
def exect_mat(a,b,d,t):
    lt=Toplevel(t)
    lt.title('计算结果')
    lt.iconbitmap('calc.ico')
    lt.geometry('350x270+580+240')
    matrix1F=Frame(lt)                         
    matrix1F.pack(side=LEFT,fill=BOTH)
    matrixmF=Frame(lt)
    matrixmF.pack(side=LEFT,expand=YES)
    matrix2F=Frame(lt)
    matrix2F.pack(side=LEFT,fill=BOTH)

    canvas1=Canvas(matrix1F,width=12,height=500)          
    canvas1.pack()
    canvas1.create_line(2,15,2,250)
    canvas1.create_line(2,15,12,15)
    canvas1.create_line(2,250,12,250)

    canvas2=Canvas(matrix2F,width=12,height=500)
    canvas2.pack()
    canvas2.create_line(10,15,10,250)
    canvas2.create_line(10,15,0,15)
    canvas2.create_line(10,250,0,250)
    
    if d.get()=='矩阵加法':
        try:
            res=eval('np.matrix(['+a.get()+'])'+'+'+'np.matrix(['+b.get()+'])')
            for i in range(0,res.shape[0]):
                lf=Frame(matrixmF)
                lf.pack(side=TOP,expand=YES,fill=BOTH)
                for j in range(0,res.shape[1]):
                        Label(lf,text=('%.3f' %res[i,j]),width=6).pack(side=LEFT,expand=YES,fill=BOTH)
        except ValueError:
            Label(matrixmF,text='Value Error',width=10).pack(expand=YES,fill=BOTH)
        except SyntaxError:
            Label(matrixmF,text='Syntax Error',width=10).pack(expand=YES,fill=BOTH)
        except:
            Label(matrixmF,text='Error',width=10).pack(expand=YES,fill=BOTH)
        
    elif d.get()=='矩阵减法':
        try:
            res=eval('np.matrix(['+a.get()+'])'+'-'+'np.matrix(['+b.get()+'])')
            for i in range(0,res.shape[0]):
                lf=Frame(matrixmF)
                lf.pack(side=TOP,expand=YES,fill=BOTH)
                for j in range(0,res.shape[1]):
                        Label(lf,text=('%.3f' %res[i,j]),width=6).pack(side=LEFT,expand=YES,fill=BOTH)  
        except ValueError:
            Label(matrixmF,text='Value Error',width=10).pack(expand=YES,fill=BOTH)
        except SyntaxError:
            Label(matrixmF,text='Syntax Error',width=10).pack(expand=YES,fill=BOTH)
        except:
            Label(matrixmF,text='Error',width=10).pack(expand=YES,fill=BOTH)
            
    elif d.get()=='矩阵乘法':
        try:
            res=eval('np.matrix(['+a.get()+'])'+'*'+'np.matrix(['+b.get()+'])')
            for i in range(0,res.shape[0]):
                lf=Frame(matrixmF)
                lf.pack(side=TOP,expand=YES,fill=BOTH)
                for j in range(0,res.shape[1]):
                        Label(lf,text=('%.3f' %res[i,j]),width=6).pack(side=LEFT,expand=YES,fill=BOTH)
        except ValueError:
            Label(matrixmF,text='Value Error',width=10).pack(expand=YES,fill=BOTH)
        except SyntaxError:
            Label(matrixmF,text='Syntax Error',width=10).pack(expand=YES,fill=BOTH)
        except:
            Label(matrixmF,text='Error',width=10).pack(expand=YES,fill=BOTH)
            
    elif d.get()=='逆矩阵':
        try:
            res=eval('np.matrix(['+a.get()+'])'+'**(-1)')
            for i in range(0,res.shape[0]):
                lf=Frame(matrixmF)
                lf.pack(side=TOP,expand=YES,fill=BOTH)
                for j in range(0,res.shape[1]):
                        Label(lf,text=('%.3f' %res[i,j]),width=6).pack(side=LEFT,expand=YES,fill=BOTH)
        except ValueError:
            Label(matrixmF,text='Value Error',width=10).pack(expand=YES,fill=BOTH)
        except SyntaxError:
            Label(matrixmF,text='Syntax Error',width=10).pack(expand=YES,fill=BOTH)
        except:
            Label(matrixmF,text='Error',width=10).pack(expand=YES,fill=BOTH)            
                
def matrixfun(root):
    t=Toplevel(root)
    t.title('矩阵计算')
    t.geometry('400x320+550+200')
    root.resizable(width=False, height=False)
    t.iconbitmap('calc.ico') 
    
    mat_a=StringVar()
    mat_b=StringVar()
    Entry(t,textvariable=mat_a).pack(fill=X,padx=10,pady=20)
    Entry(t,textvariable=mat_b).pack(fill=X,padx=10,pady=20)

    depot=StringVar()
    depot.set('矩阵加法')
    OptionMenu(t,depot,'矩阵加法','矩阵减法','矩阵乘法','逆矩阵').pack(pady=40)
    
    Button(t,text='执行',width=10,command=(lambda a=mat_a,b=mat_b,d=depot,r=t:exect_mat(a,b,d,t))).pack(pady=10)
    
    
root =Tk()
root.title('计算器')
root.geometry('250x320+300+200')
root.resizable(width=False, height=False)
root.iconbitmap('calc.ico')

display=StringVar()
entryF=Frame(root)
entryF.pack(side=TOP,fill=X)
entry=Entry(entryF,textvariable=display,relief=SUNKEN,bd=3,state='normal')
entry.pack(expand=YES,fill=BOTH)

clrF=Frame(root)
clrF.pack(side=TOP,expand=NO,fill=X)
clr=Button(clrF,text='CLR',command=(lambda w=display:w.set('')))
clr.bind_all("<Delete>",clearfun)
clr.pack(side=LEFT,expand=YES,fill=BOTH)

for charz in ("789+","456-","123*",".0=/"):
    keyF=Frame(root)
    keyF.pack(side=TOP,expand=YES,fill=BOTH)
    for char in charz:
        if char=='=':
            etr=Button(keyF,text=char,width=1,command=(lambda w=display:calc(w)))
            etr.bind_all("<Return>",enterfun)
            etr.pack(side=LEFT,expand=YES,fill=BOTH)
        else:
            Button(keyF,text=char,width=1,command=(lambda w=display,s=char:w.set(w.get()+s))).pack(side=LEFT,expand=YES,fill=BOTH)

advF1=Frame(root)
advF1.pack(side=TOP,fill=BOTH)
for char in ('sin','cos','tan','('):
    if char=='(':
        Button(advF1,text=char,width=1,command=(lambda w=display,s=char:w.set(w.get()+s))).pack(side=LEFT,expand=YES,fill=BOTH)
    else:
        Button(advF1,text=char,width=1,command=(lambda w=display,s=char:w.set(w.get()+s+'('))).pack(side=LEFT,expand=YES,fill=BOTH)

advF2=Frame(root)
advF2.pack(side=TOP,fill=BOTH)
for char in ('√','^','π',')'):
    if char=='√':
        Button(advF2,text=char,width=1,command=(lambda w=display,s=char:w.set(w.get()+s+'('))).pack(side=LEFT,expand=YES,fill=BOTH)
    else:
        Button(advF2,text=char,width=1,command=(lambda w=display,s=char:w.set(w.get()+s))).pack(side=LEFT,expand=YES,fill=BOTH)

advF3=Frame(root)
advF3.pack(side=TOP,fill=BOTH)
Button(advF3,text='Matrix',width=1,command=(lambda r=root:matrixfun(r))).pack(side=LEFT,expand=YES,fill=BOTH)


root.mainloop()