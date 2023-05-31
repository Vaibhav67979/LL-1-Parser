from first import first as fs
from follow import follow as fos

import pandas as pd

mydata={}
terminals=['$']
def computeData(dict):
    for i,j in dict.items():
        for k in j:
            for l in k:
                if l in "abcdefghijklmnopqrstuvwxyz1234567890id()+-*/=/{/}":
                    terminals.append(l)

def computeTabel(dict):
    computeData(dict)
    for i,j in dict.items():
        s1=fs[i]
        s2=fos[i]
        temp={}
        for k in s1:
            if k!="ε":
                temp[k]=f"{i}->{j}"
            else:
                for l in s2:
                    temp[l]=f"{i}->ε"
        mydata[i]=temp
    formatTable()

def formatTable():
    index=[]
    dfdata=[]
    for i,y in mydata.items():
        index.append(i)
        temp=[]
        for p in terminals:
            flag=0
            for j,l in y.items():
                if p==j:
                    flag=1
                    temp.append(l)
            if flag==0:
                temp.append("")
        dfdata.append(temp)
    df=pd.DataFrame(data=dfdata,columns=terminals,index=index)
    print(df)


                    


            
        
    

            




