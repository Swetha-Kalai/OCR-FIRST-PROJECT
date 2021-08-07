#CREATING ANOTHER TEXT FILE TO STORE EDITED RAW DATA
#TEMPSCHOOLADMIN CONTAINS DETAILS WITHOUT EXTRA SPACES
'''
with open("schooladmin.txt",'r')as f,open("tempschooladmin.txt",'w')as f1:
    x=f.readlines()
    l2=[]
    for k in x:
        if k== '\n'or k== ' \n':
            pass
        else:
            l2+=[k]
    f1.writelines(l2)   
print(l2)

'''
with open('tempschooladmin.txt','r')as f:
    x=f.read()
    l=x.split('APLLICATON DONE')

    print("COMPUTER SCIENCE GROUP STUDENTS ")
    for k in l:
        for j in k.split():
            if j=='COMPUTER':
                print(k)


    print("STUDENTS OF MBC COMMUNITY")
    for k in l:
        for j in k.split():
            if j=='MBC':
                print(k)

    print("STUDENTS OF BC COMMUNITY")
    for k in l:
        for j in k.split():
            if j=='BC':
                print(k)    



















