n=int(input())
temp=n
rev=0
while(n!=0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("the number is penimdrome number")
    print(dig)
    print(rev)
    print(n)
else:
    print("not a penimdrome number")
#done