l=int(input())
h=int(input())
for i in range(0,h):
    if(i==0 or i==h-1):
        print("*"*l,end='\n')
    else:
        print("*",end='')
        print("*".rjust(l-1),end='\n')