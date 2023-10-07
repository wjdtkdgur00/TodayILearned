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

## 쓰레드와 상태제어

**쓰레드가 3개가 있다면 JVM은 시간을 잘게 쪼갠 후에 3개의 쓰레드를 돌아가며 실행한다. 이것이 매우 빠르게 일어나면서 쓰레드가 모두 동작하는것 처럼 보이는 것이다.**

* 쓰레드는 실행가능상태인 Runnable과 실행상태인 Running 상태로 나뉜다.

* 실행되는 쓰레드 안에서 Thread.sleep() 이나 Object가 가지고 있는 wait() 메소드가 호출이 되면 쓰레드는 블록상태가 된다.

* Thread.sleep()은 특정 시간이 지나면 자신 스스로 블록상태에서 빠져나와 Runnable이나 Running 상태가 된다.

* Object가 가지고 있는 wait() 메소드는 다른 쓰레드가 notify()나 notifyAll() 메소드를 호출하지 전까지는 블록상태에서 해제되지 않는다.

    * notify() 메소드는 임의로 잠들어있던 쓰레드를 하나 깨운다.

    * notifyAll() 메소드는 호출로 잠들어 있던 쓰레드를 모두 깨운다.

* wait() 메소드는 호출이 되면 모니터링 락을 놓게된다. 그래서 대기중이던 다른 메소드가 실행된다.

* 쓰레드의 run 메소드가 종료되면, 쓰레드는 종료된다. 즉 Dead 상태가 된다.

* 쓰레드의 yeild 메소드가 호출되면 해당 쓰레드는 다른 쓰레드에게 자원을 양보하게 된다.

* 쓰레드가 가지고 있는 join 메소드를 호출하면 해당 쓰레드가 종료될 때까지 대기하게 된다.

## 쓰레드와 상태제어(join)

**join() 메소드는 쓰레드가 멈출때까지 기다리게 한다.**

* 0.5초씩 쉬면서 숫자를 출력하는 MyThread5를 작성한다.

```java
    public class MyThread5 extends Thread{
        public void run(){
            for(int i = 0; i < 5; i++){
                System.out.println("MyThread5 : "+ i);
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } // run
    }
```

* 해당 쓰레드를 실행하고, 해당 쓰레드가 종료될때까지 기다린 후, 내용을 출력하는 JoinExam 클래스

```java
    public class JoinExam { 
        public static void main(String[] args) {
            MyThread5 thread = new MyThread5();
            // Thread 시작 
            thread.start(); 
            System.out.println("Thread가 종료될때까지 기다립니다.");
            try {
                // 해당 쓰레드가 멈출때까지 멈춤
                thread.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Thread가 종료되었습니다."); 
        }   
    }
```

* 실행 결과
```
        Thread가 종료될때까지 기다립니다.
        MyThread5 : 0
        MyThread5 : 1
        MyThread5 : 2
        MyThread5 : 3
        MyThread5 : 4
        Thread가 종료되었습니다.
```

## 쓰레드와 상태제어(wait, notify)

**wait와 notify는 동기화된 블럭안에서 사용해야 한다. wait를 만나게 되면 해당 쓰레드는 해당 객체의 모니터링 락에 대한 권한을 놓고 대기한다.**

* Thread를 상속받는 ThreadB를 작성한다.

```java
    public class ThreadB extends Thread{
       // 해당 쓰레드가 실행되면 자기 자신의 모니터링 락을 획득
       // 5번 반복하면서 0.5초씩 쉬면서 total에 값을 누적
       // 그후에 notify()메소드를 호출하여 wait하고 있는 쓰레드를 깨움 
        int total;
        @Override
        public void run(){
            synchronized(this){
                for(int i=0; i<5 ; i++){
                    System.out.println(i + "를 더합니다.");
                    total += i;
                    try {
                        Thread.sleep(500);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                notify();
            }
        }
    }
```

* ThreadB를 이용하여 wait하는 클래스를 작성한다.

```java
    public class ThreadA {
        public static void main(String[] args){
            // 앞에서 만든 쓰레드 B를 만든 후 start 
            // 해당 쓰레드가 실행되면, 해당 쓰레드는 run메소드 안에서 자신의 모니터링 락을 획득
            ThreadB b = new ThreadB();
            b.start();

            // b에 대하여 동기화 블럭을 설정
            // 만약 main쓰레드가 아래의 블록을 위의 Thread보다 먼저 실행되었다면 wait를 하게 되면서 모니터링 락을 놓고 대기       
            synchronized(b){
                try{
                    // b.wait()메소드를 호출.
                    // 메인쓰레드는 정지
                    // ThreadB가 5번 값을 더한 후 notify를 호출하게 되면 wait에서 깨어남
                    System.out.println("b가 완료될때까지 기다립니다.");
                    b.wait();
                }catch(InterruptedException e){
                    e.printStackTrace();
                }

                //깨어난 후 결과를 출력
                System.out.println("Total is: " + b.total);
            }
        }
    }
```

* 실행결과

```
        b가 완료될때까지 기다립니다.
        0를 더합니다.
        1를 더합니다.
        2를 더합니다.
        3를 더합니다.
        4를 더합니다.
        Total is: 10
```

## 데몬 쓰레드

**보통 리눅스와 유닉스계열의 운영체제에서 백그라운드로 동작하는 프로그램을 말한다.**

* 데몬쓰레드를 만들 때에는 쓰레드에 데몬 설정을 하면 된다.

    * 이런 쓰레드는 자바프로그램을 만들 때 백그라운드에서 특별한 작업을 처리하게 하는 용도로 만든다.

* 데몬쓰레드는 일반 쓰레드(main 등)가 모두 종료되면 강제적으로 종료되는 특징을 가지고 있다.

```java
    public class DaemonThread implements Runnable {

        // 무한루프안에서 0.5초씩 쉬면서 데몬쓰레드가 실행중입니다를 출력하도록 run()메소드를 작성
        @Override
        public void run() {
            while (true) {
                System.out.println("데몬 쓰레드가 실행중입니다.");

                try {
                    Thread.sleep(500);

                } catch (InterruptedException e) {
                    e.printStackTrace();
                    break; //Exception발생시 while 문 빠찌도록 
                }
            }
        }

        public static void main(String[] args) {
            // Runnable을 구현하는 DaemonThread를 실행하기 위하여 Thread 생성
            Thread th = new Thread(new DaemonThread());
            // 데몬쓰레드로 설정
            th.setDaemon(true);
            // 쓰레드를 실행
            th.start();

            // 메인 쓰레드가 1초뒤에 종료되도록 설정. 
            // 데몬쓰레드는 다른 쓰레드가 모두 종료되면 자동종료.
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }   
            System.out.println("메인 쓰레드가 종료됩니다. ");    
        }   
    }
```