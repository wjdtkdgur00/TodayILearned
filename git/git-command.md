## git 기본 명령어

* `git init` : 깃 저장소 생성

* `git add .` : 저장소에 수정된 점(업데이트 된 점)을 추가한다. `.` 을 붙히면 변경된 모든 사항을 추가하고 파일 이름을 입력해서 그 파일의 변경사항만 추가할 수 있다.

* `git status` : 저장소의 현재 상태를 알 수 있다. 파일 추가, 삭제, 내용 변경 등이 있다.

* `git remote -v` : 내 로컬 저장소와 연결된 원격 저장소(깃허브 레포지토리 주소)를 확인한다.

* `git remote add origin [깃허브의 레포지토리 주소]` : 내 로컬 저장소와 원격 저장소를 연결한다.

* `git push origin [원격 저장소의 브랜치명]` : 원격 저장소의 브랜치로 변경 사항을 업로드 한다.

* `git clone [레포지토리 주소]` : 원격 저장소의 내용을 로컬 저장소로 복제 및 다운로드 한다.

* `git pull` : 원격 저장소의 변경 내용을 현재 디렉토리로 가져온다.

* `git commit -m "commitMessage"` : 로컬 저장소의 변경내용을 원격 저장소로 커밋한다.

## Branch 관련

* `git branch [브랜치명]` : 브랜치를 생성한다.

* `git checkout [브랜치명]` : 해당 브랜치로 이동한다.

* `git branch -b [브랜치명]` : 브랜치를 생성하면서 동시에 해당 브랜치로 이동한다.

* `git branch` : 브랜치가 무엇이있는지, 지금 어디에 위치하는지 확인한다.

* `git branch -d [브랜치명]` : 해당 브랜치를 삭제한다.

## Config 관련

* `git config` : 전체 config 리스트를 확인한다.

* ```git config --global user.name "username" / git config --global user.email "useremail"``` : git config를 설정한다.

* `git config --unset` : git config를 삭제한다.

* `git config --unset --global` : 삭제되지 않을 경우, global 옵션을 주어 삭제한다.