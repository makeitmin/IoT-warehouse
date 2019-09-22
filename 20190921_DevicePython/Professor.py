score=int(input("파이썬 점수를 입력하세요: "))
gpa=""
if score>=90:
    gpa='A'
elif score>=80:
    gpa='B'
elif score>=70:
    gpa='C'
elif score>=60:
    gpa='D'
else:
    gpa='F'
print("파이썬  학점은",gpa,"학점입니다.")