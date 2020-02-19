import time
import csv

f=open("text1.csv","r")
array = [row for row in csv.reader(f, delimiter=';')]
array = [list(map(int, x)) for x in array]
leng=len(array)
table = [2,3,4,5]
turn=[]
couter=0
sat=[]
pep=[]

def clean():
    i=0
    while len(turn)!=i:
        if(turn[i]==0):
            turn.remove(turn[i])
            i=i-1
        i=i+1
    return turn
def add_person(a):
    time.sleep(2)
    res=turn.append(array[a][0])
    print('В очередь добавилось '+str(array[a][0])+' человек(а)')
    return res
def to_table():
    for i in range(len(turn)-couter):
        for j in range(len(table)):
            if(turn[i]==table[j] and turn[i]!=0):
                time.sleep(1)
                sat.append(table[j])
                pep.append(turn[i])
                print(str(turn[i])+' сел(и) за столик номер '+str(table[j]))
                table[j]=0
                turn[i]=0
                i-1            
    for i in range(len(turn)-couter):
        for j in range(len(table)):            
            if (turn[i]<=table[j] and turn[i]!=0):
                time.sleep(1)
                sat.append(table[j])
                pep.append(turn[i])
                print(str(turn[i])+' сел(и) за столик номер '+str(table[j]))
                table[j]=0
                turn[i]=0
                i-1
    return turn, table
def replace_table(s,many_people,a):
    #time.sleep(s)
    table[many_people-2]=many_people
    print(str(a)+' человек(а) ушло из-за столика '+str(many_people))
    return table
    
   
for i in range(7):
    turn.append(array[i][0])
print("Изначальная очередь: "+str(turn).replace('[','').replace(']',''))
to_table()

for i in range (7,leng):
    if(couter<3):
        couter=couter+1
    #time.sleep(1)
    add_person(i-6)
    replace_table(array[i-6][1],sat[i-6],pep[i-6])
    clean()
    print('Очередь: '+str(turn).replace('[','').replace(']','').replace('0, ','')) 
    print('Свободные столики на '+str(table).replace('[','').replace(']','')) 
    to_table()
print()
turn.remove(turn[0])
turn.sort(reverse=True)
couter = 0
for i in range(len(turn)):
    to_table()
    replace_table(array[i][1],sat[i],pep[i])
    print('Очередь: '+str(turn).replace('[','').replace(']','').replace('0, ','')) 
    print('Свободные столики на '+str(table).replace('[','').replace(']','')) 
    couter=couter+1
couter=0
to_table()
print()
for i in range(len(sat)-5,len(sat)-1):
    if(table[i-len(sat)+5]==0 or table[i-len(sat)+4]==0):
        replace_table(array[i][1],sat[i+1],pep[i+1])
print('Свободные столики на '+str(table).replace('[','').replace(']','')) 

clean()
f.close