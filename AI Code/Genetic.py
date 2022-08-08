import random
c1=[0,1,1,0,1]
c2=[1,1,0,0,0]
c3=[0,1,0,0,0]
c4=[1,0,0,1,1]
converter=[pow(2,i) for i in range(5)]
conv=converter[::-1]
res=[]
ans1=0
ans2=0
ans3=0
ans4=0
for i in range(5):
    ans1+=c1[i]*conv[i]
    ans2+=c2[i]*conv[i]
    ans3+=c3[i]*conv[i]
    ans4+=c4[i]*conv[i]
res.append(ans1)
res.append(ans2)
res.append(ans3)
res.append(ans4)
x=0
sqrt=[]
for i in res:
    sqrt.append(i*i)
for i in sqrt:
    x+=i
prob=[]
for i in sqrt:
    prob.append(round(i/x,2))
rand=[]
for i in range(4):
    rand.append(round(random.uniform(0,1),2))
# for i in rand:
    # if(i>0.0&&i<prob[0]):
    # else if(i>prob[0]&&i<prob[0]+prob[1]):
    # else if(i>prob[0]+prob[1]&&i<prob[0]+prob[1]+prob[2]):
    # else:
print("Random Number :",rand)
print("Probability :",prob)
