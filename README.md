# 역파카 기기 API & 리버스 프록시 서버

채널톡 HACKY-TALKY 챌린저스 2기 해커톤 11조

## Background

> 역파카 프로젝트 전반에 대한 내용은 [Notion](https://www.notion.so/jseoplim/cf74e6ce58e64bb6b494b815fb0c35b4?pvs=4)을 참고

### Contents

#### 📌 불법 주정차 위험 영역을 지도 위에 표시하기

- 사용자가 입력한 특정 위치 주변의 CCTV/신고 위치를 마커로 지도 위에 표시하기
- 사용자 위치는 현재 위치 혹은 검색한 주소로 입력

#### 📢 불법 주정차 위험 영역에 진입 시 알리기

- 사용자 주변 10m 이내에 CCTV/신고 위치가 없던 상태에서 10m 이내에 CCTV/신고위치가 존재하는 위치로 이동하면 알리기

### Infra Architecture

![image](https://github.com/HACKY-TALKY-2-2/team19-proxy/assets/86508420/5b4ac497-bbf1-4ea6-b8ed-f4ae00a7e6e3)

### Database Schema

<img src="https://github.com/HACKY-TALKY-2-2/team19-proxy/assets/86508420/9d3a452e-4a24-415f-be17-ffbee74422ac.png" width="60%">

## Features

> 자세한 API Endpoint는 [Notion](https://abaft-red-b93.notion.site/b94dcd77078944c9be84cb7d7f727a28?v=f8fbd9835a1a4cc4a558f10898c1c58f&pvs=4)을 참고

* 기기에 대한 API 요청을 처리하여 응답
* CCTV, 신고 위치 API를 제공하는 다른 포트의 API 서버에 대한 리버스 프록시 기능 제공

## Technology Stack

* 언어: Python
* 웹 프레임워크: FastAPI 
* DBMS: MySQL 8.0

## See More

* [역파카 API 서버](https://github.com/HACKY-TALKY-2-2/team19-api)
* [역파카 앱](https://github.com/HACKY-TALKY-2-2/team19-app)
