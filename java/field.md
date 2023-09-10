## filed
**자바에서 클래스가 가지고 있는 속성을 field 라는 용어로 사용한다.**

* 이름과 번호를 필드로 가지고 있는 Car 클래스를 선언한다.
```java
public class Car{
    String name;
    int number;
}
```
* Car 클래스를 인스턴스화 한다.
```java
public class CarExam{
    Car c1 = new Car();
    Car c2 = new Car();

    //c1.name 은 c1이 참조하는 객체의 name을 의미한다.

    c1.name = "경찰차"; // c1이 참조하는 객체의 name을 "경찰차"로 설정한다.
    c1.number = 1234; // c1이 참조하는 객체의 number를 1234로 설정한다.

    c2.name = "구급차"; //c2가 가리키는 객체의 name을 구급차로 설정
    c2.number = 5678;   //c2가 가리키는 객체의 number를 5678로 설정

    System.out.println(c1.name);
    System.out.println(c1.number); //출력

    String name = c2.name;  //c2가 ㅊ참조하는 객체의 name을 String 타입 변수 namee도 참조하게 한다.
}
```