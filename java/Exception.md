## 예외(Exception)
* 사용자의 잘못된 조작이나 개발자의 코딩 실수로 인해 발생하는 오류이다.

* 예외 처리를 통해 프로그램을 종료하지 않고 정상 실행 상태가 유지되도록 할 수 있다.

### try, catch
* 예외가 발생했을 때 `try...catch...finally` 라는 키워드로 예외를 처리할 수 있거나 메소드를 호출한 곳으로 던질 수 있다.

```java
try{
	//예외가 발생될만한 코드
}catch(FileNotFoundException e){	//FileNotFoundException이 발생했다면

}catch(IOException e){ //IOException이 발생했다면

}catch(Exception e){	//Exception이 발생했다면

}finally{	
	///어떤 예외가 발생하던 말던 무조건 실행
}
```

* try 블록에 예외가 발생할만한 코드가 쓰여진다.

* catch 블록에서 예외가 발생되었을 때 처리하는 동작을 명시한다. 

* catch 블록은 여러 개가 있을 수 있다. 처음 catch 블록에서 잡히지 않는 예외라면 다음 catch의 예외를 검사한다. 

* 이때 상속관계에 있는 예외 중 부모가 위의 catch, 자식 예외 클래스가 아래의 catch로 놓일 순 없다.

```java
try{
	//.. 중략 ..//
} catch (Exception e){
	//컴파일 오류 발생(IOException의 부모 예외 클래스인 Exception은 위의 catch 블록에 올 수 없다.)
} catch (IOException e){

}
```

* finally 블록에는 예외 발생 여부에 관계없이 공통으로 수행될 코드가 쓰여진다.

### throws

* 호출된 메소드가 호출부에 에러 처리를 전가하겠다는 뜻이다.

```java
public static void divide(int a,int b) throws ArithmeticException {
	if(b==0) throw new ArithmeticException("0으로 나눌 수는 없다니까?");
	int c=a/b;
	System.out.println(c);
}
public static void main(String[] ar){
	int a=10;
	int b=0;
		
	divide(a,b);
}
```

* divide() 메소드에서 try, catch로 예외 처리를 할 수 있지만, divide()를 호출한 곳에서 예외 발생 다음의 처리를 divide() 메소드가 정하지 않기 때문에 호출한 곳으로 예외를 던진다.

* 예외를 던지는 방법은 아래와 같다.

```java
throw [예외객체]
ex) throw new Exception("예외 발생!");
```

* 이때 예외를 throw 하였으므로 main은 그 예외를 처리하기 위해 try, catch 블록을 쓴다.

```java
try {
	divide(a,b);
}catch(ArithmeticException e) {
	e.getMessage();
	e.printStackTrace();
}
```