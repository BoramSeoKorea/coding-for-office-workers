#참과 거짓 boolean
#if
#Ture, False
#and, or, not

a=True
b=False
#A가 참이고, 그리고 B가 참이라면(A와 B가 둘다 참이여야 된다.)
print(a and b)
#A가 참이거나 혹은B가 참이라면(A나 B 중에 하나라도 참이면 된다.)
print(a or b)

# = & ==
a=True
print(a==True)
print(a is True)

#if
d=7
if d>10:
    print("The number is bigger than 10.")
elif d>5 and d<=10:
    print("The number is samller than 10 or same, and bigger than 5.")
else:
    print("The number is bigger than 5 or same.")
