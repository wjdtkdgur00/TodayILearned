```python
def add(n,m):
    print(int(n)+int(m))

def sub(n,m):
    print(int(n)-int(m))

def mul(n,m):
    print(int(n)*int(m))

def div(n,m):
    print(int(n)/int(m))

def square(n,m):
    print(int(n)**int(m))

n=input("n의 값을 입력하세요 : ")
c=input("부호를 입력하세요 (제곱을 선택할 시 n^m 입니다!): ")
m=input("m의 값을 입력하세요 : ")

if c=='+':
    add(n,m)
elif c=='-':
    sub(n,m)
elif c=='x':
    mul(n,m)
elif c=='/':
    div(n,m)
elif c=='^':
    square(n,m)
else:
    print("안할거면 가셈ㅡㅡ")
```
