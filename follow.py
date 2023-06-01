import first as fs
follow={}
def search(x,gra):
    temp=[]
    flagtocheck=0
    for i,j in gra.items():
        for k in j:
            if x in k:
                flagtocheck=1
                indexes=[]
                for u in range(len(k)):
                    if k[u]==x:
                        indexes.append(u)
                for cur in indexes:
                    sub=[]
                    if (cur+1)<len(k):
                        sub.append(k[cur+1:])
                    if len(sub)==0:
                        sub.append("ε")
                    if sub[0] in gra.keys():
                        while sub[0] in gra.keys():
                            t=sub[0]
                            sub.pop(0)
                            sub=list(fs.first[t])
                        fir=sub
                    else:
                        fir=fs.fc(i,sub)
                    if 'ε' in fir :
                        fir.pop(fir.index('ε'))
                        temp.extend(fir)
                        try:
                            temp.extend(follow[i])
                        except Exception:
                            continue
                    else:
                        temp.extend(fir)
    if flagtocheck==0 and x not in follow.keys():
        # print("None"+str(x))
        return ["ε"]
    return temp

def modifyfollow():
    for i in follow.keys():
        follow[i]=set(follow[i])

def display(grammar):
    count=0
    for i in grammar.keys():
        if(count==0):
            follow[i]=['$']
            count+=1
    
        temp=search(i,grammar)
        if(len(temp)!=0):
            follow[i]=temp
        else:
            continue
    validatefollow(grammar)
    return follow

def validatefollow(input):
    rem=input.keys()-follow.keys()
    if rem.__len__()==0:
        modifyfollow()
    else:
        for k in rem:
            temp=search(k,input)
            if temp.__len__()!=0:
                follow[k]=temp
            else:
                continue
        validatefollow(input)
