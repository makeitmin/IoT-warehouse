x=int(input("정수 x를 입력하시오"))
y=int(input("정수 y를 입력하시오"))
sum=0
for num in range(min(x,y),max(x,y)+1):
    sum+=num
print(min(x,y),"부터",max(x,y),"까지의 총 합은",sum)
multi=1
for num in range(min(x,y),max(x,y)+1):
    multi*=num
print(min(x,y),"부터",max(x,y),"까지의 총 곱은",multi)