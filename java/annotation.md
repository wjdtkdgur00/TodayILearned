## 어노테이션

* 클래스나 메소드위에 붙는다. @기호로 이름이 시작합니다.

* 어노테이션을 클래스나 메타코드에 붙인 후, 클래스가 컴파일되거나 실행될 때 어노테이션의 유무나 어노테이션에 설정된 값을 통하여 클래스가 좀 더 다르게 실행될 수 있다.

* 어노테이션은 자바가 기본으로 제공해주는것도 있고, 사용자가 직접 만들 수도 있다.

    * 사용자가 직접 작성하는 어노테이션을 Custom 어노테이션이라고 한다.

* 커스텀 어노테이션을 이용하는 법.
    1. 어노테이션 정의
    
    2. 어노테이션을 클래스에서 사용한다.

    3. 어노테이션을 이용하여 실행한다.

```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface Count100{

}
```

* "hello"를 출력하는 hello()메소드를 가지는 MyHello 클래스를 작성한다.

    * hello 메소드 위에 @Count100 어노테이션을 붙힌다.

```java
public class MyHello{
    @Count100
    public void hello(){
        System.out.println("hello");
    }
}
```

* MyHello 클래스를 이용하는 MyHelloExam 클래스를 작성한다.

    * MyHello의 hello 메소드가 @Count100 어노테이션이 설정되어 있을 경우 hello() 메소드를 100번 호출하도록 한다.

```java
import java.lang.reflect.Method;

public class MyHelloExam{
    public static void main(String[] args){
        MyHello hello = new MyHello();
        
        try{
            Method method = hello.getClass().getDeclaredMethod("hello");
            if(method.isAnnotationPresent(Count100.class)){
                for(int i = 0;i<100;i++){
                    hello.hello();
                }
            }else{
                hello.hello();
            }
        }catch(Exception ex){
            ex.printStackTrace();
        }
    }
}
```