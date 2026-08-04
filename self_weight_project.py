#gym math
import streamlit as st

m= [45,25,10,5,2.5]
b = [90,50,20,10,5]

st.title("Weight clalculator")
st.header( "Please selcect you means of lifing and what you want calculated ")


def find_m (insert,weight,c):
    insert = round2(insert)
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
    insert=round5(insert)
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
    n= (round(n))
    if n%2.5 ==0:
        return n
    else:
        return round2( n + 1) 


def calc(insert,x):
    if  x==b :
        return f"You should have {find_b (insert,b,[])} on the bar "
    elif  x==m :
        return f" you should have {find_m (insert,m,[])} on the machine"



#findinding out what weights are changing

n=[]
o=[]
def changeb(old,new):
    if old==new : hold = "1"
    if old>new: hold = "2"
    if new>old: hold = "3"
    if old>new and (old% 5 !=0 or new%5 !=0): hold="4"
    if new>old and (old% 5 !=0 or new%5 !=0): hold="5"
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
            return f"Take off {old-new}lb from the bar should now look like {calc(new,b)}(rounded)"   
        case"5":# new>old and (old or new )%5 !=0
            old=round5(old)
            new= round5(new)
            return f"Add {new-old}lb to the bar should now look like {calc(new,b)} (rounded)"
def changem(old,new):
    if old==new : hold = "1"
    if old>new: hold = "2"
    if new>old: hold = "3"
    if old>new and (old% 2.5 !=0 or new%2.5 !=0): hold="4"
    if new>old and (old% 2.5 !=0 or new%2.5 !=0): hold="5"
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
        
            return f"Take off {old-new}lb from the machine should now look like {calc(new,m)}(rounded)"   
        case"5": #new>old and (old or new )%5 !=0
            old = round2(old)
            new = round2(new)
            
            return f"Add {new-old}lb to the machine should now look like {calc(new,m)}(rounded)"
def change1(x):
    if x==b :
        return changeb(old,new)
    else :
        return changem(old,new)
def changes(x):
    g=st.session_state.sets
    if not g:
        return
    if x==b:
        st.write(f"Start by putting {calc(g[0],b)} on the bar")
        for i in range(1,len(g)):
            st.write (changeb(g[i-1],g[i]))
    else : #x==m
        st.write(f"Start by putting {calc(g[0],m)} on the machine")
        for i in range(1,len(g)):
            st.write(changem(g[i-1],g[i]))


choice=st.radio("Equipment:",["Barbell","Machine"])
weight= b if choice=="Barbell" else m

pick= st.radio("Pick a option:" ,["Find one weight","Percent calculations","Find change in weight"])
if pick == "Find one weight":
    display=1
elif pick == "Percent calculations":
    display= 2
else : display = 3        

if display ==1 :
    hold =st.number_input("What weight",min_value=0, step= 5 )
    if st.button ("Find"):
        st.write (calc(hold,weight))


elif display == 2 :
    if "sets" not in st.session_state:
        st.session_state.sets =[]
    ma= st.number_input("What is you max?:",min_value=0, step=5)
    count = st.number_input("How many sets? :",min_value=0 , max_value=6, step=1)
    percentges=[]
    
    for i in range(count):
        pct= st.number_input(f"Percent of Set {i+1} : ", min_value=0,max_value=100)
        percentges.append(pct)
        st.session_state.sets=[p/100*ma for p in percentges]   
                
    if st.button("Show my weights"):
        changes(weight)
    
if display == 3 :
    old = st.number_input("What is currently on the bar :", min_value=0,step=5)
    new = st.number_input("what weight do you want on the bar :", min_value=0,step=5)
    if st.button("Show change"):
        st.write(change1(weight))

if st.button("Reset"):
    for i in ["hold","sets","ma","count","old","new"]:
        st.session_state.pop(i,None)
    st.rerun()
    
    
   
  
