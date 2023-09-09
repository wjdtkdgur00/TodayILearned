
## Class
**객체지향 프로그래밍 언어**인java는 객체를 만들기 위하여 반드시 **클래스(Class)** 를 먼저 만들어야 한다.

클래스는 일종의 틀 같은 개념이다. 예를 들어 붕어빵이 객체라면 붕어빵 틀이 클래스인 셈이다.
```java
// 클래스 선언 방법
public class (클래스명){
    ......    
}
```

Car라는 클래스를 하나 생성해준다. 
```java
public class Car{

}
```
클래스를 만들었다고 객체가 만들어지지 않기 때문에 Car객체를 생성해준다.
```java
public class CarExam{
    public static void main(String args[]){
        Car c1 = new Car();
        Car c2 = new Car();
    }
}
```
* new 연산자는 new연산자 뒤에 나오는 생성자를 이용하여 메모리에 객체를 만들라는 명령.
* 메모리에 만들어진 객체를 인스턴스 (instance)라고도 한다.
* 이렇게 만들어진 변수가 c1, c2 이다.
* 위 코드가 실행되면 `Car`이라는 객체가 2개 만들어지고 각각의 객체를 참조하는 c1과 c2 변수가 선언된다.

## String 클래스

**문자열을 표현하는 java에서 가장 많이 사용하는 클래스**

모든 클래스들은 `new`연산자를 이용해서 클래스를 만들어야 하지만, String 클래스는 기본 타입처럼 바로 값을 넣어도 생성이 되고, 다른 클래스처럼 new 생성자를 사용하여 생성할 수도 있다.


1. new 연산자 사용 X
```java
// 예시
Stirng str1 = "hello";
String str2 = "hello";

```
* "hello" 라는 문자열이 메모리 중에 상수가 저장되는 영역에 저장된다.
* `String str2 = "hello";` 이 문장이 실행될 때 hello 라는 문자열 상수는 이미 만들어져 있으므로 str1이 참조하는 인스턴스를 str2도 참조한다.

2. new 연산자 사용 O 
```java
Stirng str3 = new String("hello");
String str4 = new String("hello");
```
* new 연산자를 이용하여 인스턴스를 만들면 인스턴스는 무조건 새롭게 만들어진다.
* `String str4 = new String("hello");` 이 문장이 실행될 때도 새롭게 만들게 되므로, str3과 str4는 서로 다른 인스턴스를 참조한다.

```java
 if(str1 == str2){  // 같은 인스턴스를 참조하므로 결과는 true 
        System.out.println("str1과 str2는 같은 레퍼런스입니다.");
    }

    if(str1 == str3){  // str1과 str3은 서로 다른 인스턴스를 참조하므로 결과는 false 
        System.out.println("str1과 str3는 같은 레퍼런스입니다.");
    }

    if(str3 == str4){  // str3과 str4는 서로 다른 인스턴스를 참조하므로 결과는 false 
        System.out.println("str3과 str4는 같은 레퍼런스입니다.");
    }
```
* 참조변수 끼리 `==` 로 비교하면 **서로 같은 것을 참조하는지** 비교한다.
* String은 불변 클래스이다. 불변이란 String이 인스턴스가 될 때 가지고 있던 값을 나중에 수정할 수 없다.
* String은 문자열과 관련된 다양한 메소드를 가지고 있다. 메소드를 호출한다 하더라도 String은 내부의 값이 변하지 않는다.
* String이 가지고 있는 메소드중 String을 반환하는 메소드는 모두 새로운 String을 생성해서 반환한다.
```java
String str5 = "hello World";
String str6 = str5.substring(3);
```
* substring은 문자열을 자른 결과를 반환하는 메소드이다. 해당 코드가 실행되어도 str5는 변하지 않는다.
* str6은 str5가 가지고 있는 문자열 중 3번째 위치부터 자른 결과 즉, **새로운 String을 참조하게 된다.**