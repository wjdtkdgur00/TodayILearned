## 변수의 scope와 static
**프로그램 상에서 사용되는 변수들은 사용 가능한 범위를 가지는데, 그 범위를 변수의 스코프라고 한다.**

변수가 선언되 블록어 그 변수의 사용범위이다.
```java
public class ValableScopeExam{
    int globalScope=10;

    public void scopeTest(int value){
        int localscope=10;
        System.out.println(globalScope);
        System.out.println(localScope);
        System.out.println(value);
    }
}
```
* 클래스의 속성으로 선언된 변수 globalScope 의 사용 범위는 **클래스 전체**이다.
* 매개변수로 선언된 int value는 블럭 바깥에 존재하기는 하지만, 메서드 선언부에 존재하므로 사용범위는 해당 메소드 블록내이다.
* 메서드 블럭내에서 선언된 localScope 변수의 사용범위는 메소드 블럭내이다.

### main 메소드
* 같은 클래스 안에 있는데 globalScope를 메인에서 사용할 수 없다.
* main은 static 메서드이기 때문에 static한 메서드에서는 static하지 않은 필드를 사용할 수 없다.
```java
public class VariableScopeExam{
    int globalScope=10;

    public void scopeTest(int value){
        int localScope=20;
        System.out.println(globalScope);
        System.out.println(localScope);
        System.out.println(value);
    }
    public static void main(String[] args){
        System.out.println(globalScope);    //오류
        System.out.println(localScope); //오류
        System.out.println(value);  //오류
    }
}
```
### static
* 같은 클래스 내에 있음에도 해당 변수들을 사용할 수 없다.
* main 메소드는 static 이라는 키워드로 메소드가 정의되어 있다. 이러한 메서드를 static 한 메소드 라고 한다.
* static한 필드나, static한 메소드는 Class가 인스턴스화 되지 않아도 사용할 수 있다.
```java
public class VariableScopeExam{
    int globalScope=10;
    static int staticVal=7;

    public void scopeTest(int value){
        int localScope=20;
    }

    public static void main(String[] args){
        System.out.println(staticVal);  //사용가능
    }
}
```
**static한 변수는 공유된다.**


* static하게 선언된 변수는 값을 저장할 수 있는 공간이 하나만 생성된다. 그러므로, 인스턴스가 여러개 생성되어도 static한 변수는 하나이다.
```java
    ValableScopeExam v1 = new ValableScopeExam();
    ValableScopeExam v2 = new ValableScopeExam();
    v1.golbalScope = 20;
    v2.golbalScope = 30; 

    System.out.println(v1.golbalScope);  //20 이 출력된다. 
    System.out.println(v2.golbalScope);  //30이 출력된다. 

    v1.staticVal = 10;
    v2.staticVal = 20; 

    System.out.println(v1.statVal);  //20 이 출력된다. 
    System.out.println(v2.statVal);  //20 이 출력된다. 
```
