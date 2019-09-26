from matplotlib import pyplot as plt
from math import sin, cos, radians

angle1=int(input("첫번째 각도를 입력하세요: "))
angle2=int(input("두번째 각도를 입력하세요: "))

x=[]
y_sin=[]
y_cos=[]

for angleList in range(angle1, angle2): # 정의역
    x.append(radians(angleList))

for domain in x: # 치역
    y_cos.append(cos(domain)*1000)
    y_sin.append(sin(domain)*1000)

plt.plot(x,y_cos)
plt.plot(x,y_sin)
plt.show()