## Byte 단위 입출력
Byte 단위 입출력 클래스는 이름이 `InputStream`이나 `OutputStream`으로 끝난다.

* 파일로 부터 1byte씩 읽어들여 파일 1byte씩 저장하는 프로그램

    * 파일로 부터 읽어오는 객체 - FileInputStream

    * 파일에 쓸 수 있게 해주는 객체 - FileOutputStream

* read() 메소드

    * byte를 리턴한다면 끝을 나타내는 값을 표현할 수 없다. 그러므로 byte가 아닌 int를 리턴한다.

    * 음수의 경우 맨 좌측 비트는 1이다. 읽어들일 것이 있다면 항상 양수를 리턴하는 것이다.

* FileInputStream과 FileOutputStream을 이용하여 1바이트씩 읽어들여 1바이트씩 저장한다.

    * read() 메소드가 리턴하는 타입은 정수이다. 정수 4바이트중 마지막 바이트에 읽어들인 1바이트를 저장한다.

    * read() 메소드는 더 이상 읽어들일 것이 없을 때 -1을 리턴한다.

```java
    public class ByteIOExam1 {
        public static void main(String[] args){     
            FileInputStream fis = null; 
            FileOutputStream fos = null;        
            try {
                fis = new FileInputStream("src/javaIO/exam/ByteExam1.java");
                fos = new FileOutputStream("byte.txt");

                int readData = -1; 
                while((readData = fis.read())!= -1){
                    fos.write(readData);
                }           
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }finally{
                try {
                    fos.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
                try {
                    fis.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        }
    }
```

### 심화

* 파일로 부터 512byte씩 읽어들여 파일에 512byte씩 저장하는 프로그램을 작성한다.

    * `byte[] buffer = new byte[512];`
    * 512byte만큼 읽어들이기 위해 byte 배열을 사용한다.

```java
    public class ByteIOExam1 {
        public static void main(String[] args){     
            //메소드가 시작된 시간을 구하기 위함
            long startTime = System.currentTimeMillis();        
            FileInputStream fis = null; 
            FileOutputStream fos = null;        
            try {
                fis = new FileInputStream("src/javaIO/exam/ByteExam1.java");
                fos = new FileOutputStream("byte.txt");

                int readCount = -1; 
                byte[] buffer = new byte[512];
                while((readCount = fis.read(buffer))!= -1){
                    fos.write(buffer,0,readCount);
                }
            } catch (Exception e) {
                // TODO Auto-generated catch block
                e.printStackTrace();
            }finally{
                try {
                    fos.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
                try {
                    fis.close();
                } catch (IOException e) {
                    // TODO Auto-generated catch block
                    e.printStackTrace();
                }
            }
        //메소드가 끝났을때 시간을 구하기 위함. 
        long endTime = System.currentTimeMillis();
        //메소드를 수행하는데 걸린 시간을 구할 수 있음. 
        System.out.println(endTime-startTime); 
        }
    }
```