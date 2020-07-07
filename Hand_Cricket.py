arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
flag=0
sums=0
for i in range(0,len(arr1)):
        sums+=arr1[i]
        if(arr1[i]!=arr2[i]):
            flag+=1
if(flag==len(arr1) and sums>=21):
    print('Sudhakaran Win!')
else:
    print('Steev Win!')
