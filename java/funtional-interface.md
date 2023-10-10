## 함수형 인터페이스

* 1개의 추상 메소드를 갖는 인터페이스이다. 여러 개의 디폴트 메소드가 있어도 추상 메서드가 오직 하나면 함수형 인터페이스 이다.

* 자바의 람다 표현식은 함수형 인터페이스로만 사용 가능합니다.

* `@FuntionalInterface` 어노테이션을 사용한다. 이 어노테이션은 해당 인터페이스가 함수형 인터페이스 조건에 맞는지 검사해준다.

    * `@FuntionalInterface` 어노테이션이 없어도 함수형 인터페이스로 동작하고 사용할 수 있지만, 인터페이스 검증과 유지보수를 위해 붙여주는게 좋다.

## 인터페이스 구현

* 두 매개변수의 합을 반환하는 구현 클래스를 만들기 위하여 제네릭 함수형 인터페이스를 생성한다.

```java
public interface MyFunctionInterface<T, R>{
    public R sum(T x, T y);
}
```

* 인터페이스에 작성된 sum() 메소드를 Override 한다.

```java
// 함수형 인터페이스 구현
public class FuntionalInterfaceClass implements MyFunctionInterface<Integer, Integer>{
    @Override
    public Integer sum(Integer x, Integer y){
        return x+y;
    }
}

public class Main{
    public static void main(String[] args){
        FunctionalInterfaceClass obj = new FunctionalInterfaceClass();
        System.out.println(obj.sum(10,20));
    }
}
```

## 람다식을 이용한 인터페이스의 구현

* 클래스로 구현하는 방법의 단점은 함수형 인터페이스가 제네릭인 경우 타입 개수만큼 클래스를 생성해야 한다는 점이다.

```java
public class IntegerClass
        implements MyFunctionInterface<Integer, Integer> {
  @Override
  public Boolean sum(Integer x, Integer y) {
    return x + y;
  }
}

public class DoubleClass
        implements MyFunctionInterface<Double, Double> {
  @Override
  public Double sum(Double x, Double y) {
    return x + y;
  }
}

public class StringClass
        implements MyFunctionInterface<String, String> {
  @Override
  public String sum(String x, String y) {
    return x + y;
  }
}
```

* 람다식을 사용하면 클래스 없이 함수형 인터페이스를 구현할 수 있다.

```java
public interface MyFunctionInterface<T> {
  public void myMethod();
}

public class Main {
  public static void main(String args[]) {
    MyFunctionInterface<Integer> myFunctionInterface = () -> {
      System.out.println("실행");
    };
  }
}
```


|함수형 인터페이스|Descripter|Method|
|------|-----|------|
|Predicate|T -> boolean|boolean test(T t)|
|Consumer|T -> void|void accept(T t)|
|Supplier|() -> T|T get()|
|Function<T, R>|T -> R|R apply(T t)|
|Comparator|(T, T) -> int|int compare(T o1, T o2)|
|Runnable|() -> void|void run()|
|Callable|() -> T|V call()|

### Predicate

```java
@FunctionalInterface
public interface Predicate<T>{
    boolean test(T, t);
}
```

* Predicate는 인자 하나를 받아서 boolean 타입을 리턴한다.

* 람다식으로는 `T -> boolean`로 표현한다.

### Consumer

```java
@FunctionalInterface
public interface Consumer<T>{
    void accept(T t);
}
```

* Consumer는 인자 하나를 받고 아무것도 리턴하지 않는다.

* 람다식으로는 `T -> void` 로 표현한다.

* Consumer(소비자) 라는 이름에 맞게 인자를 받아서 소비만 하고 끝낸다.

### Supplier

```java
@FunctionalInterface
public interface Supplier<T>{
    T get();
}
```

* Supplier는 아무런 인자를 받지 않고 T 타입의 객체를 리턴한다.

* 람다식으로는 `() -> T`로 표현한다.

### Function

```java
@FunctionalInterface
public interface Function<T, R>{
    R apply(T t);
}
```

* Function은 T 타입 인자를 받아서 R 타입을 리턴한다.

* 람다식으로는 `T -> R`로 표현한다.

* 수학식의 함수처럼 특정 값을 받아서 다른 값으로 반환해준다.

### Comparator

```java
@FunctionalInterface
public interface Comparator<T>{
    int compare(T o1, T o2)
}
```

* Comparator은 T타입 인자 두개를 받아서 int 타입을 리턴한다.

* 람다식으로는 `(T, T) -> int`로 표현한다.

### Runnable

```java
@FunctionalInterface
public interface Runnable{
    public abstract void run();
}
```

* Runnable은 아무런 객체를 받지 않고 리턴도 하지 않는다.

* 람다식으로는 `() -> void`로 표현한다.

* Runnable이라는 이름처럼 실행만 할 수 있다.

### Callable

```java
@FunctionalInterface
public interface Callable<V>{
    V call() throws Exception;
}
```

* Callable은 아무런 인자를 받지 않고 T 타입 객체를 리턴한다.

* 람다식으로는 `() -> T`로 표현한다.

* Runnable 처럼 '호출 가능한' 이라는 뜻이다.