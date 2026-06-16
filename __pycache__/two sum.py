l1=[1,2,3,4,5,6]
target=9
l2=[[i,j] for i in range(len(l1)) for j in range(i,len(l1)) if i+j==target]
print(l2)