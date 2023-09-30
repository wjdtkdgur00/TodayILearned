# 익명클래스
* 익명 중첩 클래스는 익명 클래스라고 보통 말하며, 내부 클래스이기도 하다.
```java
// 추상 클래스 Action
public abstract class Action{
    public abstract void exec();
}

// Action을 상속받은 MyAction
public class MyAction extends Action{
    public void exec(){
        System.out.println("exec");
    }
}

// MyAction을 사용하는 ActionExam
public class ActionExam{
    public static void main(String[] args){
        Action action = new MyAction();
        action.exec();
    }
}

//MyAction을 사용하지 않고 Action을 상속받는 익명 클래스 생성
public class ActionExam{
    public static void main(String[] args){
        Action action = new Action(){
            public void exec(){
                System.out.println("exec");
            }
        };
        action.exec();
    }
}
```
* 생성자 다음 `{}` 가 나오면, 해당 생성자 이름에 해당하는 클래스를 상속받는 이름없는 객체를 만든다는 뜻이다.
* 괄호 안에는 메소드를 구현하거나 추가할 수 있다. 이렇게 생성된 이름 없는 객체를 action이라는 참조변수가 참조하게 하고, exec() 메소드를 호출한다.
* 익명 클래스를 만드는 이유는 Action을 상속받는 클래스를 만들 필요가 없을 경우이다.
* Action을 상속받는 클래스가 해당 클래스에서만 사용되고 다른 클래스에서는 사용되지 않는 경우이다.