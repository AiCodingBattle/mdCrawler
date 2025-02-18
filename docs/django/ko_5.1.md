Django
The web framework for perfectionists with deadlines.
테마 토글 (현재 테마:자동)
테마 토글 (현재 테마: 밝음)
테마 토글 (현재 테마: 어두움)
Toggle Light / Dark / Auto color theme
Menu
  * Overview
  * Download
  * Documentation
  * News
  * Community
  * Code
  * Issues
  * About
  * ♥ Donate
  * 테마 토글 (현재 테마:자동)
테마 토글 (현재 테마: 밝음)
테마 토글 (현재 테마: 어두움)
Toggle Light / Dark / Auto color theme


# 문서
Search: 검색
  * Getting Help


  * el
  * en
  * es
  * fr
  * id
  * it
  * ja
  * pl
  * pt-br
  * zh-hans
  * 언어: **ko**


  * 1.11
  * 2.0
  * 2.1
  * 3.0
  * 3.1
  * 3.2
  * 4.0
  * 4.1
  * 4.2
  * 5.0
  * dev
  * 문서 버전: **5.1**


  * 

# Django 문서¶
장고에 대해 알아야 할 모든 것
## 첫걸음¶
Django 또는 프로그래밍이 처음이신가요? 이곳에서 시작하세요!
  * **바닥부터 시작하기:** 개요 | 설치
  * **튜토리얼:** Part 1: 요청과 응답 | Part 2: 모델과 관리자 사이트 | Part 3: 뷰와 템플릿 | Part 4: 폼과 제네릭 뷰 | Part 5: 테스팅 | Part 6: 정적 파일 | Part 7: 관리자 사이트 커스터마이징 | Part 8: 서드 파티 패키지 추가하기
  * **Advanced Tutorials:** How to write reusable apps | Writing your first contribution to Django


## 도움말¶
문제가 있나요? 도와드리고 싶어요!
  * FAQ를 참고하세요 – 흔한 질문에 대한 답변을 얻을 수 있습니다.
  * 특정 정보를 찾으시나요? 색인, 모듈 목록 또는 상세한 목차 를 이용하세요.
  * 해결법을 못 찾으셨나요? 자주 묻는 질문: 도움을 받는법 에서 도움을 받는 방법과 커뮤니티에 질문하는 법을 확인하세요.
  * ticket tracker 를 통해 장고로 버그를 레포트 하세요


## 이 문서의 구조¶
Django는 문서가 아주 많습니다. 높은 수준에서의 개요를 알면 원하는 정보를 어떤 문서에서 찾을지 알 수 있습니다.
  * 자습서는 웹 애플리케이션을 만드는 모든 과정을 자세히 설명합니다. Django 또는 웹 애플리케이션 개발이 처음이라면 여기에서 시작하세요. 또한 “첫걸음” 도 살펴보세요.
  * 주제 안내 주요 주제와 개념을 높은 수준에서 논의하고 유용한 배경 지식과 설명을 제공합니다.
  * 레퍼런스 가이드 API와 Django의 여러 기능들에 대한 기술적 레퍼런스를 담고 있습니다. 이 가이드는 독자가 기본적인 주요 개념에 대해 이해하고 있다고 가정하고, 어떻게 동작하고 사용하는지 설명합니다.
  * How-to 가이드는 레시피입니다. 주요 문제와 사용 사례들의 해결 방법들을 단계별로 안내해 줍니다. 여기서는 Django가 어떻가 동작하는지 알고 있다고 가정하고 튜토리얼보다 심화된 내용을 다룹니다.


## 모델 계층¶
Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적 계층(모델)을 제공합니다. 아래에서 자세히 알아보세요.
  * **모델:** 모델 소개 | 필드 타입 | 인덱스 | 메타 옵션 | 모델 클래스
  * **쿼리셋:** 쿼리 실행하기 | 쿼리셋 메소드 레퍼런스 | 룩업 표현식
  * **모델 인스턴스:** 인스턴스 메소드 | 관련 객체에 접근하기
  * **마이그레이션:** 마이그레이션 소개 | 연산자 레퍼런스 | 스키마에디터 | 마이그레션 작성하기
  * **심화:** 매니저 | Raw SQL | 트랜잭션 | 집계 | 검색 | 맞춤 필드 | 다중 데이터베이스 | 맞춤 룩업 | 쿼리 표현식 | 조건식 | 데이터베이스 함수
  * **그 외:** 지원되는 데이터베이스 | 레거시 데이터베이스 | 초기 데이터 제공 | 데이터베이스 접근 최적화 | PostgreSQL만의 기능


## 뷰 계층¶
Django는 사용자의 요청을 처리하고 결과를 반환하기 위한 로직을 캡슐화한 “뷰”의 개념을 갖고 있습니다. 뷰에 대하여 알아야할 모든 것을 아래 링크에서 찾아보세요.
  * **기본 사항:** URL 구성 View 함수 | Shortcuts 패키지 | 데코레이터 | 비동기 지원
  * **레퍼런스** 내장된 뷰 | Request/response 객체 | TemplateResponse 객체
  * **파일 업로드** 개요 | File 객체 | 스토리지 API | 파일 다루기 | 커스텀 스토리지
  * **클래스 기반 뷰:** 개요 | 내장된 디스플레이 뷰 | 내장된 편집 뷰 | 믹스인 사용하기 | API 레퍼런스 | 납작한 인덱스
  * **심화:** CSV 생성 | PDF 생성
  * **미들웨어:** 개요 | 내장된 미들웨어 클래스


## 템플릿 계층¶
템플릿 계층은 사용자에게 표시할 정보를 표현하기 위해 디자이너에게 친숙한 문법을 제공합니다. 디자이너들이 이 문법을 사용하는 방법과 프로그래머들이 확장하기 위한 방법을 알아보세요.
  * **기초:** 개요
  * **디자이너:** 언어 개요 | 빌트인 태그와 필터 | 휴머나이제이션
  * **프로그래머:** 템플릿 API | 커스텀 태그와 필터 | 커스텀 템플릿 백엔드


## 폼¶
Django는 쉽게 폼을 만들고 폼 데이터를 다루기 위한 풍부한 프레임워크를 제공합니다.
  * **기초:** 개요 | 폼 API | 내장된 필드 | 내장된 위젯
  * **고급:** 모델을 위한 폼 | 미디어 통합 | 폼셋 | 맞춤 유효성 검증


## 개발 프로세스¶
여러 구성 요소들과 Django 애플리케이션의 개발과 테스트를 도와줄 다양한 도구들을 알아보세요.
  * **설정:** 개요 | 전체 설정 목록
  * **애플리케이션.** 개요
  * **예외:** 개요
  * **django-admin과 manage.py:** 개요 | 맞춤 명령 추가하기
  * **테스팅:** 소개 | 테스트를 작성하고 실행하기 | 내장된 테스팅 도구 | 심화 주제
  * **배포:** Django 배포 개요 | WSGI 서버 | ASGI 서버 | 이메일로 에러 코드 추적하기 | 배포 전 체크리스트


## 관리자¶
Django의 가장 인기 있는 기능 중 하나인 자동적 관리 인터페이스를 이해하기 위한 모든 것들을 찾아보세요:
  * Admin 사이트
  * Admin 액션
  * Admin 문서 생성기


## 보안¶
보안은 웹 애플리케이션 개발에서 가장 중요한 주제이며 Django는 여러 보호 도구와 메커니즘을 제공합니다.
  * 보안 개요
  * Django에서 알려진 보안 문제
  * 클릭재킹 방어
  * 사이트 간 요청 위조
  * 암호화 서명
  * 보안 미들웨어


## 국제화와 지역화¶
Django는 강력한 국제화와 지역화 프레임워크를 제공하여, 여러 언어와 세계 여러 지역을 위한 어플리케이션 개발을 지원합니다:
  * 개요 | 국제화 | 지역화 | 지역화 된 웹 UI 형식과 폼 입력
  * 표준 시간대


## 성능과 최적화¶
코드를 더욱 빠르고 더 적은 시스템 자원을 사용하여 효율적으로 실행 할 수 있는 다양한 기법과 도구들이 있습니다.
  * 성능과 최적화 개요


## 지리 프레임워크¶
GeoDjango는 세계적 수준의 지리 웹 프레임워크가 되려고 합니다. 가능한 GIS 웹 애플리케이션을 쉽게 만들고, 공간 데이터의 성능을 충분히 활용하는 것이 목표입니다.
## 일반적인 웹 애플리케이션 도구¶
Django는 웹 애플리케이션들의 개발에 보편적으로 필요한 여러가지 기능들을 제공합니다.
  * **인증:** 개요 | 인증 시스템 사용하기 | 비밀번호 관리 | 맞춤 인증 | API 참조
  * 캐싱
  * 로깅
  * 이메일 보내기
  * 신디케이션 피드 (RSS/Atom)
  * 페이지네이션
  * 메세지 프레임워크
  * 직렬화
  * 세션
  * 사이트맵
  * 정적 파일 관리
  * 데이터 유효성 검증


## 다른 핵심 기능들¶
Django 프레임워크의 다른 핵심 기능들에 대해 좀 더 배우기:
  * 조건부 콘텐츠 처리
  * 콘텐츠 타입과 제네릭 릴레이션
  * 플랫페이지
  * 리다이렉션
  * 시그널
  * 시스템 점검 프레임워크
  * sites 프레임워크
  * Django의 유니코드


## Django 오픈 소스 프로젝트¶
Django의 개발과정을 알아보고 어떻게 기여할 수 있는지 알아보세요.
  * **Community:** Contributing to Django | The release process | Team organization | The Django source code repository | Security policies | Mailing lists and Forum
  * **디자인 철학:** 개요
  * **문서:** 이 문서에 대하여
  * **써드파티 분포:** 개요
  * **Django의 장기 계획:** API 안정성 | 릴리스 노트와 업그레이드 지침 | 디프리케이션 타임라인


Django 문서
시작하기 
Back to Top
# 추가 정보
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * AQHJ donated to the Django Software Foundation to support Django development. Donate today! 


## Browse
  * 이전: Django 문서
  * 다음: 시작하기
  * 목차
  * 전체 색인
  * Python 모듈 목록


## 현재 위치:
  * Django 5.1 문서
    * Django 문서


## 도움말
FAQ
    공통적인 질문에 대한 답을 FAQ에서 찾아보세요.
색인, 모듈 색인, or 목차
    Handy when looking for specific information.
Django Discord Server
    Join the Django Discord Community.
Official Django Forum
    Join the community on the Django Forum.
Ticket tracker
    Report bugs with Django or Django documentation in our ticket tracker.
## 다운로드:
오프라인(Django 5.1): HTML | PDF | ePub Read the Docs 제공. 
# Django Links
## Learn More
  * About Django
  * Getting Started with Django
  * Team Organization
  * Django Software Foundation
  * Code of Conduct
  * Diversity Statement


## Get Involved
  * Join a Group
  * Contribute to Django
  * Submit a Bug
  * Report a Security Issue
  * Individual membership


## Get Help
  * Getting Help FAQ
  * Django Discord
  * Official Django Forum


## Follow Us
  * GitHub
  * Twitter
  * Fediverse (Mastodon)
  * News RSS


## Support Us
  * Sponsor Django
  * Corporate membership
  * Official merchandise store
  * Benevity Workplace Giving Program


Django
  * Hosting by In-kind donors
  * Design by Threespot & andrevv


© 2005-2025  Django Software Foundation and individual contributors. Django is a registered trademark of the Django Software Foundation. 
