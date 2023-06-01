import first as fs 
import follow as fos
import table as tb
dict={}
print("Enter the number of productions")
n=int(input())

#Enter the production in the form S->aA|ε
print("Enter the Grammer")
for i in range(n):
    temp=input()
    arr=temp.split('->')
    head=arr[0].upper()
    body=arr[1].split('|')
    dict[head]=body


print("Grammer" +str(dict) )
# print(dict)

print("First : "+str(fs.firstSymbol(dict)))

print("Follow : "+str(fos.display(dict)))

tb.computeTabel(dict)

