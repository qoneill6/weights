#gym math
import streamlit as st
m= [45,25,10,5,2.5]
b = [90,50,20,10,5]
def find_m (insert,weight,c):
    round2(insert)
    if insert==0 or weight ==[]:
        return c  
    elif insert >= weight [0]:
         c.append(weight[0])
         return find_m((insert-(weight[0])),weight,c)
    else:
        return find_m(insert,weight[1:],c)
            
        
def run (insert,weight,c):
    if insert==0 or weight==[]:
        return  c   
    elif insert >= weight [0]:
        c.append(weight[0]/2)
        return run((insert-(weight[0])),weight,c)
    else:
        return run(insert,weight[1:],c)
def find_b(insert,weight,c):
    round5(insert)
    if insert > 45:
        insert = insert - 45
        return run(insert,weight,c)
    else:
        return "lighter then barbell "

def round5(n):
    n=round(n)
    if n%5 ==0:
        return n
    else:
        return round5(n+1)
def round2(n):
    n= (round(n)-.5)
    if n%2.5 ==0:
        return n
    else:
        return round2( n + .5) 


def calc(insert,x):
    if  x==b :
        return find_b (insert,b,[])
    elif  x==m :
        return find_m (insert,m,[])
    elif x==m or x==b :
        return "Please selcted a weigth set "


#findinding out what weights are changing


n=[]
o=[]
def changeb(old,new):
    if old==new : hold = "1"
    if old>new: hold = "2"
    if new>old: hold = "3"
    if old>new and (old or new )%5 !=0: hold="4"
    if new>old and (old or new )%5 !=0: hold="5"
    match hold :
        case "1":  #same
            return f"The same weight{calc(new,b)}" 
        case "2":#old>new
            return f"Take off {old-new}lb from the bar should now look like {calc(new,b)}"    
        case "3":# new>old
            return f"Add {new-old}lb to the bar should now look like {calc(new,b)}"
        case "4":#old>new and (old or new )% !=0
            old=round5(old)
            new= round5(new)
            return f"Take off {old-new}lb from the bar should now look like {calc(new,b)}(rounded up)"   
        case"5":# new>old and (old or new )%5 !=0
            old=round5(old)
            new= round5(new)
            return f"Add {new-old}lb to the bar should now look like {calc(new,b)} (rounded up)"
def changem(old,new):
    if old==new : hold = "1"
    if old>new: hold = "2"
    if new>old: hold = "3"
    if old>new and (old or new )%2.5 !=0: hold="4"
    if new>old and (old or new )%2.5 !=0: hold="5"
    match hold :
        case "1":  #same
            return f"The same weight{calc(new,m)}" 
        case "2":#old>new
            return f"Take off {old-new}lb from the machine should now look like {calc(new,m)}"    
        case "3":# new>old
            return f"Add {new-old}lb to the machine should now look like {calc(new,m)}"
        case "4":#old>new and (old or new )% !=0: 
            old =round2(old)
            new = round2(new)
        
            return f"Take off {old-new}lb from the machine should now look like {calc(new,m)}(rounded up)"   
        case"5": #new>old and (old or new )%5 !=0
            old = round2(old)
            new = round2(new)
            
            return f"Add {new-old}lb to the machine should now look like {calc(new,m)}(rounded up)"
def p():
    c=[]
    ma=int(input("what is you max:"))
    count = int(input("how many sets :") )
    def pwork(count):
        if count == 0:
            return c
        elif count > 8:
            return "do less sets and more weight:"
        else:
            h= int(input("what percetage:"))
            h=(h/100)*ma
            c.append(h)
            return pwork(count-1)
    re=pwork(count)
    return re

def changes(x):
    g=p()
    if x==b:
        print (f"Start by putting {calc(g[0],b)} on the bar")
        for i in range(1,len(g)):
            print (changeb(g[i-1],g[i]))
    else : #x==m
        print (f"Start by putting {calc(g[0],m)} on the machine")
        for i in range(1,len(g)):
            print (changem(g[i-1],g[i]))

# this is where i am starting to write interface 




    
        
            




        
        
        
        

    



   
        

        
