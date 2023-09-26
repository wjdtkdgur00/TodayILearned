## 내부 클래스 (Inner Class)
내부 클래스 (Inner Class)란, **하나의 클래스 내부에 선언된 또 다른 클래스** 를 의미한다.

보통 클래스 자료형이 필요하면, 메인 클래스 외부에 선언하거나 따로 독립적인 클래스 파일을 만들어 불러와 사용하였다. 내부 클래스는 대신 클래스 내에 선언되어 사용되며, 내부에 정의된다는 점을 제외하고는 일반적인 클래스와 다르지 않다. 

우리가 어느 클래스에 변수나 상수가 필요하다면 클래스 멤버로 클래스 내에서 선언하였듯이, 선언 주체를 변수에서 클래스로 바꾼다면 그것이 내부 클래스인 것이다.
```java
class Creature{
    int life;

    // Creature의 내부 클래스 Animal 클래스 선언
    class Animal{

    }

    // Creature의 내부 클래스 Insect 선언
    class Insect{

    }

    public void method(){
        Animal animal = new Animal();
        Insect insect = new Insect();
    }
}
```

## 내부 클래스의 장점

#### 1. 클래스를 논리적으로 그룹화
클래스가 여러 클래스와 관계를 맺지 않고 하나의 클래스와만 관계를 맺는다면, 외부에 클래스를 새로 작성하는 것이 아닌 내부 클래스로 작성할 수 있다.

이 경우 내부, 외부 클래스를 함께 관리할 수 있으므로 유지보수, 코드 이해성 면에서 보다 더 편리해진다.

또한 새로운 클래스 생성이 필요없으므로 패키지를 간소화할 수 있다.

#### 2. 타이트한 캡슐화의 적용
내부 클래스의 private 제어자를 적용해줌으로써, 캡슐화를 통해 클래스를 내부로 숨길 수 있다.

즉, 캡슐화를 통해 외부 접근을 차단하면서도, 내부 클래스에서 외부 클래스의 멤버들을 제약 없이 쉽게 접근할 수 있어 구조적 프로그래밍이 가능해진다.

## 내부 클래스 종류
클래스 멤버 변수처럼, 내부 클래스도 선언 위치, static 키워드 유무 등에 따라 4가지로 내부 클래스가 구분된다.
1. **인스턴스 클래스 (instance class)** : 외부 클래스의 멤버변수 선언 위치에 선언하며, 외부 클래스의 인스턴스 멤버처럼 다뤄진다.
```java
// 인스턴스 클래스
public class InnerExam1{
    class Cal{
        int value = 0;
        public void plus(){
            value++;
        }
    }

    public static void main(String[] args){
        InnerExam1 t = new InnerExam1();
        InnerExam1.Cal cal = t.new Cal();
        cal.plus();
        System.out.println(cal.value);
    }
}
```
2. **static 클래스** : 외부 클래스의 멤버변수 선언 위치에 선언하며, 외부 클래스의 static 멤버처럼 다뤄진다. 그러나 static 이라 해서 new 생성자 초기화를 못하는 것은 아니다.
```java
//static 클래스
public class InnerExam2{
    static class Cal{
        int value = 0;
        public void plus(){
            value++;
        }
    }

    public static void main(String[] args){
        InnerExam2.Cal cal = new InnerExam2.Cal();
        cal.plus();
        System.out.println(cal.value);
    }
}
``` 
3. **지역 클래스 (local class)** : 외부 클래스의 메서드나 초기화 블럭 안에 선언하며, 선언된 메서드 블록 영역 내부에서만 사용될 수 있다.
```java
public class InnerExam3{
    public void exec(){
        class Cal{
            int value = 0;
            public void plus(){
                value++;
            }
        }
        Cal cal = new Cal();
        cal.plus();
        System.out.println(cal.value);
    }

    public static void main(String[] args){
        InnerExam3 t = new InnerExam3();
        t.exec();
    }
}
```
4. **익명 클래스 (anonymous class)** : 클래스의 선언과 객체의 생성을 동시에 하는 이름없는 클래스이다. 일회용 클래스로 자주 이용된다.

<img src ='https://blog.kakaocdn.net/dn/liMT3/btrPmFexS5V/F3aU2QtWsEFQ9cvBI8VkEK/img.png'>