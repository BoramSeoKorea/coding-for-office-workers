#구구단 만들기 by 보람

#1)The first trying
#num=input("which times table will you print out?")
#print("I will print out the times table"+num)
#if num=1
#print(num_1)
#num_1=1*1=1

#2)The second trying
#num=input("which times table will you print out?")
#print("I will print out the times table"+num)
#for num in range("1*1=1, 1*2=2, 1*3=3"):
#    print(num)

#3)With Marco
#1) 사용자로 부터 몇단을 출력할 지 받을 것
#2) 해당 단을 곱하기 1에서 곱하기 9까지 실행할 것

dan=int(input("which time table will you print out?"))
#input은 사용자가 숫자를 입력하더라도 문자로 바꿔서 데이더를 받는다.
for num in range(1, 10):
    print("{}*{}={}".format(dan, num, dan*num))
