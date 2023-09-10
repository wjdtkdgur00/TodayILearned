## 메소드
**필드가 Class의 속성이라면, Class의 동작에 해당하는 것이 메소드이다.**
* 메소드는 입력값이 있고, 그 입력값을 받아서 무언가 한 다음 결과를 도출해 내는 함수와 비슷한 개념이다.
* 함수처럼 int형, void 형 등으로 나뉘어져 있고, 파라미터로 값을 받고, return 할 수 있다.
* Car 클래스에 void형 메소드를 선언해보자
```java
public class Car{
    public void myMethod(){
        System.out.println("메소드 호출 완료!");
    }
}
```
* 메소드도 인스턴스처럼 사용할 수 있다.
```java
public class CarExam{
    Car car = new Car();
    car.myMethod();
}
```
```java
//출력 결과

메소드 호출 완료!
```

## String클래스의 메소드
* 문자열의 길이 구하기
    
    * str.length()는 str이 참조하는 문자열의 길이를 구해서 int 타입으로 리턴해주는 메소드이다.
```java
System.out.println(str.length()); //str
```
* 문자열 붙히기 (concat)

    * str.concat("world") 메소드는 str이 참조하는 문자열 hello에다가 메소드의 인자로 들어온 문자열 world를 붙혀서 String 타입으로 리턴하는 메소드이다.
    * String Class는 불변 클래스로, 메소드가 수행되면 새로운 문자열을 만든다. 그러므로, 원래 클래스는 변하지 않는다.
```java
String str = new String("hello");

System.out.println(str.concat(" world!")); // 출력 결과 = hello wolrd!
System.out.println(str);    //String 클래스는 불변이므로 출력결과는 hello
```
* 문자열 자르기 (subString)

    * str.subString(1,3) 은 str이 참조하는 문자열을 인덱스 1번부터 3번까지 자른 결과이다.
    * str.substirng(2) 은 str이 참조하는 문자열을 2번 인덱스부터 마지막까지 자른 결과이다.
    * 문자열의 인덱스는 0번 부터 시작한다.
```java
System.out.println(str.substring(1,3)); //출력결과 el
System.out.println(str.substring(2));   //출력결과 llo world
```