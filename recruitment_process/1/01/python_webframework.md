## Python의 대표 웹 프레임워크 3가지 및 특성

Python은 다양한 웹 프레임워크를 제공하여 

개발자가 효율적으로 웹 애플리케이션을 구축할 수 있도록 돕는다. 

다음은 그 중 가장 대표적인 3가지 프레임워크와 그 특성이다.

------

### 1. Django (장고)

* 풀스택(Full-stack) 프레임워크: 웹 개발에 필요한 모든 기능을 내장하고 있어, 별도의 라이브러리 추가 없이 데이터베이스 ORM, 관리자 페이지, 인증 시스템 등 다양한 기능을 제공합.
* "배터리 포함(Batteries-included)" 철학: 많은 기능이 기본으로 제공되어 개발 시간을 단축.
* MTV (Model-Template-View) 패턴: MVC(Model-View-Controller) 패턴의 변형으로, 데이터 모델, 템플릿(UI), 뷰(로직)가 명확하게 분리.
* 보안: XSS, CSRF, SQL Injection 등 일반적인 웹 취약점에 대한 강력한 보안 기능을 내장.
* 확장성: 대규모 프로젝트 및 복잡한 웹 애플리케이션 개발에 적합합니다. 인스타그램, 핀터레스트, 워싱턴 포스트 등이 Django로 구축.


### 2. Flask (플라스크)

* 마이크로(Micro) 프레임워크: 핵심 기능만 제공하며, 필요한 라이브러리나 기능을 직접 선택하여 추가할 수 있는 유연성.
* 경량성 및 높은 자유도: 가볍고 배우기 쉬워 소규모 프로젝트나 API 서버 개발에 적합.
* Werkzeug (WSGI 유틸리티) 및 Jinja2 (템플릿 엔진) 기반: 이 두 가지 핵심 라이브러리를 기반으로 작동.
* "Opinionated" 하지 않음: 특정 개발 방식이나 구조를 강요하지 않아 개발자가 원하는 대로 설계.
* 확장성: 다양한 확장(Extension)을 통해 기능을 추가할 수 있지만, Django처럼 모든 것이 내장되어 있지는 않음.

### 3. FastAPI (패스트API)

* 모던하고 고성능: 최신 Python 3.6+ 기능을 활용하며, 비동기(Asynchronous) 처리를 기본으로 지원하여 매우 높은 성능.
* 자동 문서화 (Swagger UI, ReDoc): OpenAPI(구 Swagger) 표준을 기반으로 API 문서를 자동으로 생성해주어 개발 및 협업 효율성.
* 데이터 유효성 검사 및 직렬화: Pydantic 라이브러리를 통해 데이터 모델 정의, 유효성 검사, 직렬화를 쉽게 처리.
* 타입 힌트(Type Hints) 활용: Python의 타입 힌트를 적극적으로 사용하여 코드의 가독성과 유지보수성을 높이고, IDE의 자동 완성 기능을 강화.
* API 개발에 최적화: 주로 RESTful API 서버 구축에 사용되며, 빠른 개발 속도와 뛰어난 성능이 필요한 프로젝트에 적합.
