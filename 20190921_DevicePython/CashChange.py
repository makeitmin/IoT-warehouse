inputCash=int(input("원화를 입력하세요: "))
exRate=float(input("환율을 입력하세요: "))
totalDollar=inputCash/exRate # 원화를 달러로 환전
hundred=int(totalDollar//100) # 100달러 장수
twenty=int((totalDollar%100)//20) # 20달러 장수
ten=int(((totalDollar%100)%20)//10) # 10달러 장수
one=int((((totalDollar%100)%20)%10)//1) # 1달러 장수
cent=int(((((totalDollar%100)%20)%10)%1)*100) # 몇 센트?
print("100달러:",hundred,"장, 20달러:",twenty,"장, 10달러:",ten,"장, 1달러:",one,"장, 잔돈:",cent,"센트")