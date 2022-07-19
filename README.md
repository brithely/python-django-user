# python-django-user
### 작업 환경
- Python 3.9.4 
- Django 3.2.14
- DRF 3.13.1
- sqlite3

### 실행 방법
        export DJANGO_SECRET_KEY='django-insecure-v&rj1swl^h()onx!ag5^o=y^*410gyca(y=e@ap6r^irysc&gh'
        export DB_HOST='postgres'
        export DB_PASSWORD='test1234'
        export DB_USER='postgres'
        export DB_DATABASE='test_db'
        export DB_PORT='5432'
        docker-compose up
        # 디비 초기화 후 재시작
        docker-compose down
        docker-compose up --build --force-recreate

### ERD 다이어그램


### API Endpoint
- 핸드폰 번호 인증 발송
> POST /api/phone-numbers/generate-code
- 핸드폰 번호 인증 완료
> POST /api/phone-numbers/verify
- 사용자 회원 가입
> POST /api/users/signup
- 사용자 로그인
> POST /api/users/signin
- 내 정보 보기
> POST /api/users/me
- 비밀번호 초기화
> POST /api/users/password/reset

### 사용자 흐름
1. /api/phone-numbers/generate-code 로 핸드폰 인증 코드 발송
2. /api/phone-numbers/verify 로 핸드폰 코드 인증 완료 후 response로 받은 key 사용
3. /api/users/signup 에 key를 포함하여 회원 가입



### API Docs
http://localhost:8000/docs

