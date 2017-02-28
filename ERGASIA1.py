#O KODIKAS GRAFTIKE SE PYTHON 3.6
import string
print('kalosorises dose tin protasi sou kai meta patise to enter')
protasi=input('DOSE TIN PROTASI SOU: ')
TABLE=[]
TABLE=list(protasi)
j=0
z=0
c=0
for i in TABLE:
    j=j+1
    z=z+1
j=j-1
while (j>-1):
    if (TABLE[j]=="!"):
        c=c+1
    else:
        break
        
    j=j-1
z=z-1
e=0
while(z>e):
    if TABLE[e]=="!":
        TABLE.remove("!")
        z=z-1
        e=e-1
    e=e+1
c=c-1
for i in range(c):
    TABLE.append('!')

teL_protasi="".join(TABLE)
print (teL_protasi)

