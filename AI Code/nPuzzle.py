X=[[6,1,10,2],[7,11,4,14],[5,10000,9,15],[8,12,13,3]]
#X=[[7,1,2],[5,10000,4],[8,3,6]]
#X=[[13,10,11,6],[5,7,4,8],[1,12,14,9],[3,15,2,10000]]
Array=[]
def inversion_count(X):
    for rows in X:
        for cols in rows:
            Array.append(cols)
    #print(Array)
    dim=0
    for i in Array:
        dim=dim+1
    inv=0
    for i in range(dim):
        cnt=0
        for j in range(i+1,dim):
            if(Array[i]>Array[j]):
                if(Array[i]==10000):continue
                cnt=cnt+1
        #print(cnt)
        inv=inv+cnt
    blank=0
    for rows in X:
        for cols in rows:
            if(cols==10000):
                blank=len(X)-X.index(rows)
                
    return dim,inv,blank
dim,inv,blank=inversion_count(X)
print("Dimension :",dim)
print("Inversion Count :",inv)
print("Blank tiles position from bottom :",blank)
def is_Even(value):
    if(value%2==0):return True
    else: return False
    

def solvability(dim,inv,blank):
    solve=False
    if(is_Even(dim)==False and is_Even(inv)==True):solve=True
    elif(is_Even(dim)==True and is_Even(blank)==False and is_Even(inv)==True):solve=True
    elif(is_Even(dim)==True and is_Even(blank)==True and is_Even(inv)==False):solve=True
    return solve
    
solve=solvability(dim,inv,blank)
if(solve==True):print("Puzzle is solvable")
else:print("Puzzle is not solvable")

