## 추상클래스
**추상 클래스란 구체적이지 않은 클래스를 의미한다. 독수리, 타조는 구체적인 새를 지칭하는데, 새, 포유류 같은 것은 구체적이지 않다.**

**이런 것을 구현한 클래스를 추상 클래스라고 한다.**

* 추상 클래스는 클래스 앞에 `abstract` 키워드를 이용해서 정의한다.
* 추상 클래스는 미완성의 추상 메소드를 포함할 수 있다.
    * 추상 메소드란 내용이 없는, 즉 구현이 되지 않은 메소드이다.
    * 추상 메소드는 리턴 타입 앞에 `abstract` 라는 키워드를 붙여야 한다.
* 추상 클래스는 인스턴스를 생성할 수 없다.
```java
public abstract class Bird{
    public abstract void sing();    //추상 메소드

    public void fly(){
        System.out.println("날다.");
    }
}
```
**추상 클래스를 상속받는 클래스 생성하기**
* 추상 클래스를 상속받은 클래스는 추상 클래스가 가지고 있는 추상 메소드를 반드시 구현해야 한다.
* 추상 클래스를 상속받고, 추상 클래스가 갖고 있는 추상 메소드를 구현하지 않으면 해당 클래스도 추상 클래스가 된다.
```java
public class Duck extends Bird{
    @Override
    public void sing(){ // Bird 클래스의 추상 메소드 구현
        System.out.println("띠띠리디~");
    }
}
```
**사용하기**
* Bird는 추상 클래스 이므로 객체를 생성할 수 없다.
```java
public class DuckExam{
    public static void main(String[] args){
        Duck duck = new Duck();
        duck.sing();
        duck.fly();

        //Bird b = new Bird(); 불가능
    }
}
```