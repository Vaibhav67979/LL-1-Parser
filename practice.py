import prettytable
import pandas as pd
c=['$', 'a', 'c', 'd']
table = prettytable.PrettyTable(c)
index=[]
# table.add_row(["John Doe", 30])
# table.add_row(["Jane Doe", 25])

# print(table)
x={'S': {'d': "S->['Aa', 'B']", 'c': "S->['Aa', 'B']"}, 'A': {'c': "A->['c']"}, 'B': {'d': "B->['d']"}}
mydata=[]
for i,y in x.items():
    index.append(i)
    temp=[]
    for p in c:
        flag=0
        for j,l in y.items():
            if p==j:
                flag=1
                temp.append(l)
        if flag==0:
            temp.append("")
    mydata.append(temp)

df=pd.DataFrame(data=mydata,columns=c,index=index)

print(df)
        



# z=['S','A','B']
