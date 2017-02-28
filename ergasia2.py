#O KODIKAS GRAFTIKE SE PYTHON 3.6
import string
PARENTHESI=input('DOSE TIN AKOLOUTHIASOU: ')
TABLE=[]
TABLE=list(PARENTHESI)
count=-1
for i in TABLE:
    count=count+1
z=0
for i in range(len(TABLE)):
    if not(TABLE[0]=='(' and TABLE[count]==")"):
        z=1
        break
    if TABLE[i]=="(" and z>=0:
        z=z+1
    elif TABLE[i]==")" and z>=0:
        z=z-1
    elif (TABLE[i]=="(" or TABLE[i]==")") and z<0:
        z=1
        break
if z==0:
    print("TRUE")
else:
    print('FALSE')
    
