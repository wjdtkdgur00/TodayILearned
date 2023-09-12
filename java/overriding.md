## 오버라이딩
**오버라이딩이란 부모가 가지고 있는 메소드와 똑같은 모양의 메소드를 자식이 가지고 있는 것이다. 즉 오버라이딩이란 메소드를 재정의 하는 것이다.**

**메소드 오버라이딩**
* Car 클래스를 상속받은 Bus 클래스는 부모클래스가 가지고 있는 run() 메소드를 잘 사용한다.
```java
//run 메소드를 가지고 있는 Car 클래스
public class Car{
    public void run(){
        System.out.println("Car의 run메소드");
    }
}

//Car를 상속받는 Bus 클래스
public class Bus extends Car{

}

public class BusExam{
    public static void main(String[] args){
        Bus bus = new Bus();
        bus.run();  //Car의 run 메소드가 실행된다.
    }
}
```
* Bus 클래스에 부모가 가지고 있는 메소드와 모양이 같은 메소드를 선언한다.
```java
public class Bus extends Car{
    public void run(){
        System.out.println("Bus의 run 메소드");
    }
}

public class BusExam{
    public static void main(String[] args){
        Bus bus = new Bus();
        bus.run();  //Bus의 run 메소드가 실행된다.
    }
}
```
* BusExam을 실행하면, "