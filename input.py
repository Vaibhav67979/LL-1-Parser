print("Enter the number of productions")
n=int(input())
dict={}

#Enter the production in the form S->aA|ε
print("Enter the Grammer")
for i in range(n):
    temp=input()
    arr=temp.split('->')
    head=arr[0].upper()
    body=arr[1].split('|')
    dict[head]=body

print(dict)