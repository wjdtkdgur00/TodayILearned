# 쓰레드 (thread)

**동시에 여러 작업을 수행할 수 있게하는것**

* 동시에 여러가지 작업을 수행할 수 있다.

* 자바 프로그램은 JVM에 위해 실행된다. 이 JVM도 프로그램 중 하나다.

* 하나의 프로세스 안에도 여러개의 흐름이 동작할 수 있는데, 이것을 Thread라고 한다.

## 쓰레드 만들기 (extend Thread)

**자바에서 Thread를 만드는 법은 크게 Thread 클래스를 상속받는 방법과 Runnable 인터페이스를 구현하는 방법이 있다.**

* Thread를 상속 받아서 쓰레드를 생성하는 방법

    * java.lang.Thread 클래스를 상속받는다. 그리고 Thread 클래스의 run() 메소드를 오버라이딩한다.

    * 10번 반복하며 str을 찍는다.

```java
    public class MyThread1 extends Thread {
        String str;
        public MyThread1(String str){
            this.str = str;
        }

        public void run(){
            for(int i = 0; i < 10; i ++){
                System.out.print(str);
                try {
                    //컴퓨터가 너무 빠르기 때문에 수행결과를 잘 확인 할 수 없어서 Thread.sleep() 메서드를 이용해서 조금씩 
                    //쉬었다가 출력할 수 있게한다. 
                    Thread.sleep((int)(Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } 
        } 
    }
```

* MyThread1 을 사용하는 클래스

    * Thread를 상속 받았기 때문에 MyThread1은 Thread이다.

    * Thread 클래스가 가지고 있는 start() 메소드를 호출한다.

```java
    public class ThreadExam1 {
        public static void main(String[] args) {
            // MyThread인스턴스를 2개 만듭니다. 
            MyThread1 t1 = new MyThread1("*");
            MyThread1 t2 = new MyThread1("-");

            t1.start();
            t2.start();
            System.out.print("!!!!!");  
        }   
    }

```

## 쓰레드 만들기 (implements Runnable)

* Runnable 인터페이스를 구현해서 쓰레드 만들기

    * Runnable 인터페이스가 가지고 있는 run() 메소드를 구현한다.

```java
    public class MyThread2 implements Runnable {
        String str;
        public MyThread2(String str){
            this.str = str;
        }

        public void run(){
            for(int i = 0; i < 10; i ++){
                System.out.print(str);
                try {
                    Thread.sleep((int)(Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } 
        } 
    }
```

* Runnable 인터페이스를 구현한 MyThread2 사용하기

    * MyThread2는 Thread를 상속받지 않았으므로 Thread가 아니다.

    * Thread를 생성하고, 해당 생성자에게 MyThread2를 넣어서 Thread를 생성한다.

    * Thread 클래스가 가진 start() 메소드를 호출한다.

```java
    public class ThreadExam2 {  
        public static void main(String[] args) {
            MyThread2 r1 = new MyThread2("*");
            MyThread2 r2 = new MyThread2("-");

            Thread t1 = new Thread(r1);
            Thread t2 = new Thread(r2);

            t1.start();
            t2.start();
            System.out.print("!!!!!");  
        }   
    }
```

## 쓰레드와 공유객체

**하나의 객체를 여러개의 Thread가 사용한다는 것을 의미한다.**

ex) MusicBox라는 클래스가 있는데, 해당 클래스는 3개의 메소드를 가지고 있다. 각 메소드는 1초 이하의 시간동안 10번 반복하며 어떤 음악을 출력한다. 이러한 MusicBox를 사용하는 MusicPlayer를 3명 정도 만든다.

MusicPlayer 3명은 하나의 MusicBox를 사용한다.

* 공유객체 MusicBox

```java
    public class MusicBox { 
        //신나는 음악!!! 이란 메시지가 1초이하로 쉬면서 10번 반복출력
        public void playMusicA(){
            for(int i = 0; i < 10; i ++){
                System.out.println("신나는 음악!!!");
                try {
                    Thread.sleep((int)(Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } // for        
        } //playMusicA

        //슬픈 음악!!!이란 메시지가 1초이하로 쉬면서 10번 반복출력
        public void playMusicB(){
            for(int i = 0; i < 10; i ++){
                System.out.println("슬픈 음악!!!");
                try {
                    Thread.sleep((int)(Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } // for        
        } //playMusicB
        //카페 음악!!! 이란 메시지가 1초이하로 쉬면서 10번 반복출력
        public void playMusicC(){
            for(int i = 0; i < 10; i ++){
                System.out.println("카페 음악!!!");
                try {
                    Thread.sleep((int)(Math.random() * 1000));
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } // for        
        } //playMusicC  
    }
```

* MusicBox를 가지는 Thread객체 MusicPlayer

```java
   public class MusicPlayer extends Thread{
        int type;
        MusicBox musicBox;  
        // 생성자로 부터 musicBox와 정수를 하나 받아들여서 필드를 초기화
        public MusicPlayer(int type, MusicBox musicBox){
            this.type = type;
            this.musicBox = musicBox;
        }       
        // type이 무엇이냐에 따라서 musicBox가 가지고 있는 메소드가 다르게 호출
        public void run(){
            switch(type){
                case 1 : musicBox.playMusicA(); break;
                case 2 : musicBox.playMusicB(); break;
                case 3 : musicBox.playMusicC(); break;
            }
        }       
    }
~~~  
```

* MusicBox와 MusicPlayer를 이용하는 MusicBoxExam1 클래스
```java
    public class MusicBoxExam1 {

        public static void main(String[] args) {
            // MusicBox 인스턴스
            MusicBox box = new MusicBox();

            MusicPlayer kim = new MusicPlayer(1, box);
            MusicPlayer lee = new MusicPlayer(2, box);
            MusicPlayer kang = new MusicPlayer(3, box);

            // MusicPlayer쓰레드를 실행합니다. 
            kim.start();
            lee.start();
            kang.start();           
        }   
    }

```