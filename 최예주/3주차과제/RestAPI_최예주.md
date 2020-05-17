## Rest API

### 1. RestAPI 정의 

**HTTP 통신에서 어떤 자원에 대한 CRUD요청을 Resource와 Method로 표현하여 특정한 형태로 전달하는 방식.**

즉, 어떤 자원에 대해 CRUD(Create, Read, Update, Delete) 연산을 수행하기 위해 URI(Resource)로 요청을 보내는 것으로, Get, Post 등의 방식(Method)을 사용하여 요청을 보내며, 요청을 위한 자원은 특정한 형태(Representation of Resource)으로 표현된다. 

- - -

### 2. Rest API의 구성요소 

 **-Resource**
 
 서버는 Unique한 ID를 가지는 Resource를 가지고 있으며, 클라이언트는 이러한 Resource에 요청을 보낸다.  이러한 Resource는 URI에 해당한다.
 
 **-Method**
 
 서버에 요청을 보내기 위한 방식으로 GET, POST, PUT, DELETE가 있다. CRUD 연산 중에서 처리를 위한 연산에 맞는 Method를 사용하여 서버에 요청을 보내야 한다.

**-Representation of Resource**

클라이언트와 서버가 데이터를 주고받는 형태로 json, xml, text, rss 등이 있습다. 최근에는 Key, Value를 활용하는 json을 주로 사용한다. 

- - -
 
 ### 3. Rest API의 조건 

**1) Uniforim interface(일관된 인터페이스)**

Resource(URI)에 대한 요청을 통일되고, 한정적으로 수행하는 아키텍처 스타일을 의미한다.

이것은 요청을 하는 Client가 플랫폼(Android, Ios, Jsp 등) 에 무관하며, 특정 언어나 기술에 종속받지 않는 특징을 의미한다. 이러한 특징 덕분에 Rest API는 HTTP를 사용하는 모든 플랫폼에서 요청가능하며, Loosely Coupling(느슨한 결함) 형태를 갖게 되었다. 

**2) Stateless(무상태성)**

서버는 각각의 요청을 별개의 것으로 인식하고 처리해야하며, 이전 요청이 다음 요청에 연관되어서는 안된다.  그래서 Rest API는 세션정보나 쿠키정보를 활용하여 작업을 위한 상태정보를 저장 및 관리하지 않는다. 

**3) Cacheable(캐시 가능)**

Rest API는 결국 HTTP라는 기존의 웹표준을 그대로 사용하기 때문에, 웹의 기존 인프라를 그대로 활용할 수 있다.  그러므로 Rest API에서도 캐싱 기능을 적용할 수 있는데,  HTTP 프로토콜 표준에서 사용하는 Last-Modified Tag 또는 E-Tag를 이용하여 캐싱을 구현할 수 있고, 이것은 대량의 요청을 효율적으로 처리할 수 있게 도와준다. 

**4) Client-Server Architecture (서버-클라이언트 구조)**

 Rest API에서 자원을 가지고 있는 쪽이 서버, 자원을 요청하는 쪽이 클라이언트에 해당한다.  서버는 API를 제공하며, 클라이언트는 사용자 인증, Context(세션, 로그인 정보) 등을 직접 관리하는 등 역할을 확실히 구분시킴으로써 서로 간의 의존성을 줄입니다.

**5) Self-Descriptiveness(자체 표현)**

REST API 메시지만 보고도 이를 쉽게 이해 할 수 있는 자체 표현 구조로 되어 있다. 

**6) Layered System(계층 구조)**

Rest API의 서버는 다중 계층으로 구성될 수 있으며 보안, 로드 밸런싱, 암호화 등을 위한 계층을 추가하여 구조를 변경할 수 있다. 또한 Proxy, Gateway와 같은 네트워크 기반의 중간매체를 사용할 수 있게 해준다. 하지만 클라이언트는 서버와 직접 통신하는지, 중간 서버와 통신하는지 알 수 없다. 


- - -

### 4.Rest API 디자인 가이드


REST API 설계 시 가장 중요한 항목은 다음의 2가지로 요약할 수 있습니다.

첫 번째, URI는 정보의 자원을 표현해야 한다.

두 번째, 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.

- - -

### 5.Rest API 장점

**1. 언어와 플랫폼에 독립적이다.**

**2. SOAP(다른 통신방식)보다 개발이 쉽고 단순하다.**

**3. REST가 지원하는 프레임워크나 언어등 도구들이 없어도 구현이 가능하다.**

**4. 기존 웹 인프라를 사용가능하다. HTTP를 그대로 사용하기 때문에 그런 것이다.**

- - -

### 6.Rest API 단점 

**1.HTTP 프로토콜만 사용이 가능하다.**

**2.p2p 통신 모델을 가정했기 때문에 둘 이상을 대상으로 하는 분산환경엔 유용하지 않다.**

**3.보안, 정책등에 대한 표준이 없기 때문에 관리가 어렵고 이러한 부분까지 고려해서 구현 할 경우 설계나 구현에서 좀 더 어려움을 갖는다.**


