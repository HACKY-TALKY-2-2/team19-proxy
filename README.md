# 역파카 - 강남구 주차 플랫폼

프록시 서버 리포지토리

<aside>
💡 핵심 기능: 불법 주차 신고 피하기!
- CCTV 위치 표시, 지점별 신고 개수 표시 → 자주 신고 당하는(하는) 곳을 강조
- 현재 위치 신고 위험 지역일 경우 사용자에게 알림으로 알려줌

## 계기

- 강남구청 민원 분석 (역삼역)
![image](https://github.com/HACKY-TALKY-2-2/team19-api/assets/78073229/e83c9f97-101c-45ff-a9d6-2e19caab231c)
- 안전교통이 매우 큰 비중을 차지하고 있음.
- 강남구는 특히 주차 문제로 인해 여러 문제를 안고 있고, 그 중 하나가 불법 주차 문제임. ([link](https://mobile.newsis.com/view.html?ar_id=NISX20230518_0002307371#_PA))
- 이러한 과정에 발생하는 비의도적으로 불법 주차 신고를 당하는 등의 문제를 해결하고, 불법 주차 장소에 대한 정보를 알리기 위해 고안된 어플

## 기능
> 배포된 [Swagger](http://parking-api.jseoplim.com/docs)에서 확인 가능

### 사용자 기기 등록

### 주소 입력받아 위치 좌표 반환

### 주소 키워드 입력받아 연관된 주소 목록 반환

### 네 위치 좌표 사각형 내부에 있는 CCTV/신고위치 목록 반환

### 기기의 현재 위치 좌표 업데이트

### 기기의 CCTV/신고위치 근처 진입 여부 판단

## 기능 api
[notion](https://www.notion.so/README-69584b85cb5b41c4b0a3ef5aa3af0e93?pvs=4#e96e404ccfd0443f8d5884da1efc85e3)

## 인프라 구조
Client <-> Nginx(HTTP:80) <-> FastAPI Server(:8000) <-> Express Server(:8080)

Client 뒷 단은 모두 한 Amazon EC2 서버 내에 존재

## 기술 스택
* 언어: Python
* 웹 프레임워크: FastAPI
* DBMS: MySQL 8.0
