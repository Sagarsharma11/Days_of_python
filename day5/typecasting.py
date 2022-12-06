#explicit typecasting
a='1'
b='2'
print(a+b)
a = int(a)
b = int(b)
print(a)
print(type(b))
b = str(b)
print(type(b))
b = float(b)
print(type(b))
print(b)

#implicit typecasting
x=1.1
y=10
print(x+y)
x='a'
y='bc'
print(x+y)

