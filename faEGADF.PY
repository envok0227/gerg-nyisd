import os
def fuggveny(x, y):
    z=False
    v=False
    if(x%5==0 and x%10!=0):
        z=True
    if(y%5==0 and y%10!=0):
        v=True

    if(z==True and v==True):
        return x, y
    elif(z==True and v==False):
        return x
    elif(z==False and v==True):
        return y
os.system("cls")
egy=int(input("egy:  "))
ketto=int(input("ketto:  "))
print(fuggveny(egy, ketto))