from first import fc
from follow import follow as fos

import pandas as pd

mydata={}
terminals=['$']
def computeTerminals(dict):
    for i,j in dict.items():
        for k in j:
            for l in k:
                if l in "abcdefghijklmnopqrstuvwxyz1234567890id()+-*/=/{/}" and l not in terminals:
                    terminals.append(l)

def computeTabel(dict):
    computeTerminals(dict)
    for i,j in dict.items():
        temp={}
        for k in j:
            fstemp=[]
            fstemp.append(k)
            s1=fc(i,fstemp)
            s2=fos[i]
            # print("first"+str(s1))
            # for "ε" in s1:
            if "ε" not in s1:
                for l in s1:
                    temp[l]=f"{i}->{k}"
            else:
                for l in s2:
                    temp[l]=f"{i}->ε"
        mydata[i]=temp
    print(mydata)
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


                    


            
        
    

            




