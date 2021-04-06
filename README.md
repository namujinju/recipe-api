# 아파트 현관 출입 시스템의 보고서 API

아파트 현관의 출입 기록을 바탕으로 관리비를 계산해 조회하는 API입니다.


## Endpoint
- /api/: api-root
- /api/admin: 관리자용 관리비 조회
- /api/v1/public: 세대별 관리비 조회
- /api/door-use-log: 출입 기록 조회

## 사용 방법
- /api/admin: 관리자용 계정으로 로그인 후 각 세대 별 관리비 조회.
- /api/v1/public: 일반 세대 계정으로 로그인 후 그 세대에 해당하는 링크 클릭 후 `Extra Actions`로 관리비 조회
- /api/door-use-log: 관리자 계정으로 로그인 후 조회

## 테스트 계정
- 관리자   
email: `admin@gmail.com`
password: `password123`

- 일반 세대
email: `user1@gmail.com`
password: `password7121`
