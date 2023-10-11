## Optional Class

* Optional<T>는 null이 올 수 있는 값을 감싸는 Wrapper 클래스로, 참조하더라도 NPE(NullPointerException)가 발생하지 않도록 도와준다.

```java
public final class Optional<T>{

    //Null이 아닐 경우 -> value; Null일 경우 -> no value is present
    private final T value;

    ...
}
```

## Optinal 활용하기

## Optional 생성하기

#### Optional.empty() - 값이 Null일 때

* Optional은 Wrapper 클래스로 값이 없을 수도 있다. 이때는 Optional.empty()로 생성할 수 있다.

```java
Optional<String> optional = Optional.empty();

System.out.println(optional);   // Optional.empty
System.out.println(optional.isPresent());   // false
```

* Optional 클래스는 내부에서 static 변수로 empty 객체를 미리 생성하여 가지고 있다. 그러므로 빈 객체를 여러 번 생성해줘야 하는 경우에도 1개의 empty 객체를 공유함으로써 메모리를 절약하고 있다.

```java
public final class Optional<T> {
    private static final Optional<?> EMPTY = new Optional<>();
    private final T value;

    private Optional(){
        this.value = null;
    }

    ...
}
```

#### Optional.of() - 값이 Null이 아닐 때

* 어떤 데이터가 절대 Null이 아니라면 Optional.of()로 생성할 수 있다. 이때 Optional.of()로 Null 저장하려 한다면 NPE가 발생한다.

```java
// Optional의 value는 절대 null이 아니다.
Optional<String> optional = Optional.of("Myname");
```

#### Optional.ofNullable() - 값이 Null일수도, 아닐수도 있을 때

* 어떤 데이터가 Null이 올 수도 있고 아닐 수도 있을 경우에는 Optional.ofNullable로 생성할 수 있다.

    * 그 후에 orElse 또는 orElseGet 메소드를 이용해서 값이 없는 경우라도 안전하게 값을 가져올 수 있다.

```java
Optional<String> optional = Optional.ofNullable(getName());
String name = optional.orElse("NOVALUE!")   // 값이 없다면 "NOVALUE"를 리턴
```