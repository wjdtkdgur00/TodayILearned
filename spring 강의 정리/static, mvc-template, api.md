## 정적 컨텐츠 (static content)
정적 컨텐츠란 static 폴더에 내장된 파일을 그대로 화면에 보여주는 방법이다.

스프링 부트에서는 static 문서를 기본적으로 제공한다.

프로젝트 문서 구조에 static 이라는 폴더가 있다.

static 폴더에 `hello-static.html` 문서를 만들어보자.
```html
<!DOCTYPE>
<html>
<head>
    <title>static content</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
</head>
<body>
this is static content!!!!
</body>
</html>
```

만든 후 서버를 열고 `localhost:8080/hello-static.html` 로 접속하면 내가 만든 `hello-static.html` 문서의 내용이 그대로 화면에 나온다.

<img src ='https://velog.velcdn.com/images/kansun12/post/1a573fdc-3ab7-475a-827a-e80a323835fc/image.png'>

## MVC와 템플릿 엔진
MVC란 Model, View, Controller의 약자로, 모델, 컨트롤러, 뷰를 나누어 웹을 구성하겠다는 것이다.

아래는 예시로 구현한 컨트롤러와 모델이다.
```java
    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam( "name") String name, Model model){
        model.addAttribute("name",name);
        return "hello-template";
    }
```
`return hello-template` 이 정상적으로 작동하도록 `hello-template.html` 을 만든다.
```html
<html xmlns:th="http://www.thymeleaf.org">
<body>
<p th:text="'hello '+ ${name}">hello! empty</p>
</body>
</html>
```

요청 보낼때의 name 값이 필요하므로 브라우저의 url 뒤에 `?name=kse` 이라고 데이터를 넣어준다.

<img src='https://velog.velcdn.com/images/kansun12/post/7c0f63e2-bb5e-46e0-afba-705a1c206cb7/image.png'>

이 처럼 작성한 파일을 그대로 화면에 띄우는 정적 컨텐츠 와는 달리, MVC와 template 엔진을 이용하면 사용자가 입력한 데이터에 맞추어 화면을 구성할 수 있다.

## API

### ResponseBody
```java
    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name){
        return "hello " +name;
    }
```

이 코드는 앞서 쓴 코드와 달리 `@ResponseBody` 어노테이션이 추가되었다.

**이것은 http 통신 시 body 부분에 내가 설정한 데이터를 넣겠다는 의미로 사용한다. 즉, 내가 name에 kim이라고 넣으면 hello kim 이 클라이언트에 응답으로 전달되는 것이다.**
<img src='https://velog.velcdn.com/images/kansun12/post/b0baf536-d60d-45d2-bce0-915e202b4352/image.png'>

파라미터를 출력하는 방식은 mvc와 같지만 페이지 소스코드에는 html 코드 없이 데이터만 있다는 점이 다르다. 

### 데이터 형식으로 보내기
컨트롤러에 데이터 JSON을 보내는 컨트롤 코드를 짠다.
```java
    @GetMapping("hello-api")
    @ResponseBody
    public Hello helloApi(@RequestParam("name") String name){
        Hello hello=new Hello();
        hello.setName(name);
        return hello;
    }
    static class Hello{
        private String name;

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
```
그 후 서버를 열어보면 아래 사진처럼 데이터가 JSON형식으로 뜨게 된다.

<img src ='https://velog.velcdn.com/images/kansun12/post/e0fadd89-4fab-4683-a081-3a7663ca35e1/image.png'>

### ResponseBody의 동작원리
<img src ='https://velog.velcdn.com/images/kansun12/post/35a8b4fc-7b93-47d1-8d7e-874aa48ddaa5/image.png'>

이 어노테이션을 사용하면 HTTP의 바디에 문자 데이터를 직접 반환하게 된다.

이전에는 `viewResolver`가 자동으로 작동해서 보여줬지만 이 api에서는 `HttpMessageConverter`가 동작하면서 안에 있는 `JsonConverter` (객체 처리), `StringConverter` (기본 문자처리) 같은 컨버터가 작업해주는 것이다.

이 외에도 byte 처리 같은 것들이 HttpMessageConvert에 등록되어 있다.

