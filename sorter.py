import os,shutil

os.mkdir('All')
files=os.listdir()
stroka = ''
for i in files:
    print(i)
    stroka += i

first_symbol=[]
allset=set()
for i in files:
    allset.add(i[:i.find('(')].rstrip())
    print(len(allset))


    if i[0].upper() not in first_symbol:
            first_symbol.append(i[0].upper())

for i in first_symbol:
    os.mkdir(os.getcwd()+'/All/'+i)

for i in files:
    for j in first_symbol:
        if i[0].upper()==j and i!='All':
            shutil.move(os.getcwd()+'/'+i,os.getcwd()+'/All/'+j+'/'+i)


