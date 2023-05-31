import first as fs
follow={}
def search(x,gra):
    temp=[]
    for i,j in gra.items():
        for k in j:
            if x in k:
                # print(k)
                # try:
                    
                    # cur=k.index(x)
                    indexes=[]
                    for u in range(len(k)):
                        if k[u]==x:
                            indexes.append(u)
                    # print(indexes)
                    for cur in indexes:
                        sub=[]
                        if (cur+1)<len(k):
                            sub.append(k[cur+1:])
                        if len(sub)==0:
                            sub.append("ε")
                        # print(sub)
                        if sub[0] in gra.keys():
                            while sub[0] in gra.keys():
                                t=sub[0]
                                sub.pop(0)
                                sub=list(fs.first[t])
                            fir=sub
                        else:
                            fir=fs.fc(i,sub)
                        # print("first"+str(fir))
                        if 'ε' in fir :
                            fir.pop(fir.index('ε'))
                            temp.extend(fir)
                            if follow[i]:
                                temp.extend(follow[i])
                            else:
                                continue
                        else:
                            temp.extend(fir)
                # except Exception:
                #     print("error processing")
                #     temp.extend(follow[i])
    return temp

def modifyfollow():
    for i in follow.keys():
        follow[i]=set(follow[i])

def display(grammar):
    count=0
    # print(fs.first)
    for i in grammar.keys():
        if(count==0):
            follow[i]=['$']
            count+=1
    
        temp=search(i,grammar)
        if(len(temp)!=0):
            follow[i]=temp
        else:
            continue
    # print(follow)
    validatefollow(grammar)
    # modifyfollow()
    return follow

def validatefollow(input):
    rem=input.keys()-follow.keys()
    if rem.__len__()==0:
        # print(first)
        modifyfollow()
    else:
        # print("In else")
        for k in rem:
            # print(input[k])
            temp=search(k,input)
            # print(temp)
            if temp.__len__()!=0:
                follow[k]=temp
            else:
                continue
        validatefollow(input)
