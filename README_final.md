# MEOVA
🎬 SSAFY 11기 관통 프로젝트 - 영화 추천 사이트

[추가: 시연 영상 넣고 싶음...]

## 📑 목차
- 프로젝트 배경
- 팀 구성 및 역할
- 프로젝트 일정
- 프로젝트 기획서
- 프로젝트 수행 절차 및 방법
- 프로젝트 수행 결과
- AI적용시 사용 내역 (기능, 코드, 프롬프트)
- 소감

## 1. 프로젝트 배경
### 기획 배경
- 가족/친구/연인 등과 함께 영화를 볼 때 ‘영화 뭐 보지?’ 고민하는 경험이 다수 있었다. 그러나 정보 과부하 시대에서 그때그때 적합한 추천 영화를 고르기도 쉽지 않은 일이다. 가족 영화라고 추천을 받아도 장면 중 노골적이거나 잔인한 장면 등이 있어 불편했던 경험이 있다.

⇒ 필요한 때에 빠르게, 간단하게 ‘함께’ 보기에 적합한 영화를 찾을 방법 없을까?

⇒ 메인 화면에 검색창을 두고 태그를 통해 검색한다면 어떨까? 검색 시간을 줄이고 접근성을 높일 수 있지 않을까?
### 개요
![logo.gif](README/logo_2.gif)
<aside>
    💡 MEOVA?

    “영화 뭐 봐?”에서 착안한 이름 MEOVA(머바)
    발음하기 쉬운 귀여운 어감과 MOVIE와 비슷한 스펠링으로 이용자에게 친숙한 이미지를 선사함
</aside>

- 기존 영화 플랫폼의 경우 메인 화면에 최신/인기/유저 기반 추천 영화들이 나열되어서 현재 이용자의 상황에 적합한 영화를 간단하게 찾기에는 어려움이 있었음
- 머바는 메인 화면에 직관적으로 검색창을 띄우고, 유저가 원하는 태그를 선택해 그에 기반해 영화 정보를 필터링하고 제공
- 영화 태그에 대한 간략한 코멘트를 구현해 이용자 경험 향상을 위한 서비스 제공
- AI 기술을 활용해 매일 웹사이트만의 독창적인 추천 영화 3개 제공
- 최신 영화, 인기 영화 정보 및 각종 영화의 상세 정보 및 감독/출연 배우 상세 정보 제공

<aside>
    🎬 목적

    최소 시간 최소 비용으로 관람할 영화를 손쉽게 추천받을 수 있는, 검색 기능에 중점을 둔 웹사이트
</aside>

[추가: 웹 사이트 메인 img]

## 2. 팀 구성 및 역할
### 팀명: 바조
- 김예운 (팀장)
    - 백엔드 / 프론트엔드
    - 영화 및 리뷰 기능 중심
- 윤채영
    - 백엔드 / 프론트엔드
    - 로그인 서버, 영화 및 리뷰 기능 중심

## 3. 프로젝트 일정
### Gantt Chart
![gantt-chart](README/gantt-chart.png)

- 5/5-5/10 프로젝트 구상 및 기획
- 5/13-5/16 프로젝트 모델 및 DB 설계, API 요청
- 5/16-5/22 프로젝트 백엔드 기능 구현 및 수정
- 5/18-5/23 프로젝트 프론트 구현 및 수정

## 4. 프로젝트 기획서

### 화면 및 기능 설계
💻 화면 설계 
- [figma](https://www.figma.com/proto/A5Q4TMCcsThwYGinL1q1aA/MOVIE?page-id=0%3A1&node-id=1-233&viewport=1091%2C-34%2C0.09&t=xA1Tlm1Y1lJSASJD-1&scaling=min-zoom&starting-point-node-id=1%3A233&show-proto-sidebar=1)

[추가: 화면 정의 이미지를 더 넣는 게 좋을지? 아니면 완성된 웹사이트에 집중하는 게 좋을지?]
<aside>
    ⚙ 기능 설계

    - 영화 추천
    - 영화 상세 정보 조회
    - 평점 및 리뷰 공유
    - 커뮤니티 기능
    - 태그 검색 기능
    - 태그 코멘트
    - 관람 기록 캘린더
    - 유저 추천 영화 리스트
    - 다크 모드
</aside>
<aside>

### Architecture 설계
![architecture](README/Untitled%209.png)
### ERD
![erd](README/Untitled%2010.png)
### 명세서
- 기능 명세서
  ![function](README/Untitled%2011.png)
  ![function2](README/Untitled%2012.png)
- API 명세서
  ![api](README/Untitled%2013.png)
### Sequence Diagram
- USER Sequence Diagram
  ![sequence1](README/Untitled%2014.png)
- MOVIE Sequence Diagram
  ![sequence2](README/Untitled%2015.png)

# 4. 프로젝트 수행 절차 및 방법
### 일정 계획 및 공유
- 월간 일정
![planner2](README/planner2.png)
- 주간 일정
![planner1](README/planner1.png)
- 일일 일정
![planner3](README/planner3.png)
### github 협업
![git1](README/git1.png)
![git2](README/git2.png)