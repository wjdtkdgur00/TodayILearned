## 인터페이스
**인터페이스란 다른 클래스를 작성할 때 기본이 되는 틀을 제공하면서, 클래스 사이의 중간 매개 역할을 담당하는 일종의 추상 클래스를 의미한다.**

추상 클래스는 추상 메소드뿐만 아니라 필드, 일반 메소드도 포함할 수 있다.

그러하 인터페이스는 오로지 추상 메소드와 상수만을 포함할 수 있다.

## 인터페이스의 선언
인터페이스를 선언하는 방법은 아래와 같다.
```java
public interface interfaceName{
    public static final name = value;

    public abstract methodName(params);
    ...
}
```

클래스와 달리 인터페이스의 모든 필드는 `public static final` 이어야 하며, 모든 메소드는 `public abstract` 이어야 한다.

위 내용은 모든 인터페이스의 공통 내용 이므로 위 제어자는 생략할 수 있다. 이때 생략된 제어자는 컴파일 시 자바 컴파일러가 자동으로 추가해 준다.

## 인터페이스의 구현
인터페이스는 추상 클래스와 같이 자신이 직접 인스턴스를 생성할 수 없다.

따라서 인터페이스가 포함하고 있는 추상 메소드를 구현해 줄 클래스를 작성해야만 한다.

자바 인터페이스는 아래와 같이 구현된다.
```java
class className implements interfaceName{...}
```

모든 추상 메소드를 구현하지 않는다면, abstract 키워드를 사용하여 추상 클래스로 선언해야 한다.

## 인터페이스의 장점
1. 클래스를 이용한 다중 상속 시 발생하는 메소드 출처의 모호함과 같은 문제를 해결할 수 있다.
2. 대규모 프로젝트 개발 시 일관되고 정형화된 개발을 위한 표준화가 가능하다.
3. 클래스의 작성과 인터페이스의 구현을 동시 진행 할 수 있으므로, 개발 시간 단축에 도움이 된다.
4. 클래스 간의 관계를 인터페이스로 연결하면, 클래스마다 독립적인 프로그래밍이 가능하다.

## default 키워드, static 메소드
Java의 기존 인터페이스는 추상 메소드만을 멤버로 가질 수 있었다. 그러나 Java8 부터 default 키워드를 사용해서 interface에 메소드를 선언할 수 있게 되었다.

### default 키워드
```java
public interface Calculator{
    int add(int x, int y);
    int sub(int x, int y);

    default int mul(int x, int y){

        return x * y;
    }
}
```

위 코드와 같이 default 키워드를 사용해 선언함으로써 메소드의 구현을 작성할 수 있게 되었다. 위 코드는 세 메소드를 멤버로 같는 인터페이스 이며, `mul` 메소드가 default 키워드로 구현안 메소드이다.

```java
public class subCalculator implements Calculator{

    @Override
    public int add(int x, int y){
        return x+y;
    }

    @Override
    public int sub(int x, int y){
        return x-y;
    }
}
```

위의 인터페이스를 구현하는 클래스에서는 default 키워드로 구현하지 않은 add, sub 메소드만 구현하면 컴파일 에러가 발생하지 않는다.

물론 필요할 경우, default 키워드로 구현된 메소드도 overriding 할 수 있다.

### static 메소드
또한 Java8 부터 인터페이스에 static 메소드를 선언할 수 있게 되었다. 아래 코드의 `print` 메소드가 예시이다.
```java
public interface Calculator{
    int add(int x, int y);
    int sub(int x, int y);

    default int mul(int x, int y){
        return x*y;
    }

    static void print(int value){
        System.out.println(value);
    }
}
```

주의할점은 호출할 때 기존 클래스의 static 메소드처럼 `class이름.메소드`로 호출하는 것이 아닌 `interface이름.메소드`로 호출해야 한다는 것이다.

**정리하면, 기존 자바 인터페이스는 abstract 메소드만을 가질 수 있었지만, Java8 이후부터 abstract 뿐만 아니라 default, static 메소드를 정의할 수 있게 되었다.**