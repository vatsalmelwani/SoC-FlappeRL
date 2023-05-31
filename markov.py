import numpy as np

T=int(input("Enter the final time in seconds: "))
n=int(input("Enter the dimension: "))
M=np.zeros((n,n))
for i in range(0,n):
    for j in range(0,n):
        print("Enter the probabilty of transition from S",i+1," to S",j+1," : ")
        M[i][j]=float(input())
x=int(input("Enter the intial state: "))
a=np.zeros((1,n))
a[0][x-1]=1
for i in range(0,T):
    a=np.matmul(a,M)
print("The final probabilities of reaching states at time ",T," are:")
for i in range (n):
    print("    S",i+1,": ",a[0][i])