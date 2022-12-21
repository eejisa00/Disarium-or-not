def is_disarium(inp):

    l=len(inp)
    sum=0
    po=1
    for i in inp:
        m=int(i)**po
        po=po+1
        #print(m)
        sum=sum+m
    A=sum
    #print(A)
    #print(inp)
    if(A==int(inp)):
        print("True")
    else:
        print("False")

inp=input()
is_disarium(inp)
