# SKN08-1st-3Team

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,70:003300,100:00FF00&height=240&text=SKN01-4th-1Team&animation=&fontColor=00FF00&fontSize=90" width="1000" />
  
  <img width="1000" alt="image" src="https://github.com/Jh-jaehyuk/Jh-jaehyuk.github.io/assets/126551524/7ea63fc3-95f0-44d5-a0f0-cf431cae34f1"> 
  
  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN01-4th-1Team&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
</div>



# 0. Introduction Team (팀 소개)
### ✅ 팀명 : NC🐘(Nose Childs)
<table align=center>
  <tbody>
    <tr>
      <td align=center><b>양의정</b></td>
      <td align=center><b>유제나</b></td>
      <td align=center><b>박예닮</b></td>
      <td align=center><b>정현서</b></td>
    </tr>
    <tr>
      <td align="center">
        <div>
          <img src="https://avatars.githubusercontent.com/u/100367503?v=4"width="200px; alt="양의정"/>
        </div>
      </td>
      <td align="center">
        <div>
          <img src="https://avatars.githubusercontent.com/u/167101468?v=4"width="200px;" alt="유제나"/>
        </div>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/188152811?v=4"width="200px;" alt="박예닮"/>
      </td>
      <td align="center">
        <img src="https://avatars.githubusercontent.com/u/122842851?v=4"width="200px;" alt="정현서"/>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/UiJungYang"><div align=center>@UiJungYang</div></a></td>
      <td><a href="https://github.com/denalog"><div align=center>@denalog</div></a></td>
      <td><a href="https://github.com/pyd525"><div align=center>@pyd525</div></a></td>
      <td><a href="https://github.com/jungs0914"><div align=center>@jungs0914</div></a></td>
    </tr>
  </tbody>
</table>
  
  
  
# 1. Introduction Project (프로젝트 개요)

### ✅프로젝트 명
전기차 정보조회 포털

### ✅프로젝트 소개
전국 자동차 등록 현황 및 기업 FAQ 조회 웹앱

이 프로젝트는 다양한 자동차 관련 웹사이트에서 차량 등록 현황 및 정보를 크롤링하여 데이터를 수집하고, 
이를 기반으로 데이터를 시각화 및 분석하며, 웹앱 사용자에게 직관적인 UI로 제공하는 시스템입니다. 
특히, Streamlit 기반의 대화형 웹 애플리케이션을 통해 사용자가 데이터를 간편하게 탐색할 수 있도록 설계되었습니다.

### ✅프로젝트 필요성(배경) 
1. **데이터 관리 및 효율화**: 차량 관련 정보를 체계적으로 수집하고, 잘못된 데이터를 쉽게 수정할 수 있어 데이터 관리의 정확성과 효율성을 높입니다.  
2. **분석 및 의사결정 지원**: 지역별 차량 등록 정보와 기업별 충전 요금 데이터를 시각화 및 분석하여 정책 수립, 시장 전략, 인프라 개선 등에 필요한 유용한 통찰을 제공합니다.  
3. **전기차 보급 및 충전 인프라 최적화**: 전기차 등록 현황과 충전 요금 데이터를 통해 지역별 전기차 보급 현황과 충전소 배치의 효율성을 확인하고 개선할 수 있습니다.  
4. **사용자 친화적인 정보 제공**: Streamlit UI를 통해 데이터를 직관적이고 간단하게 시각화하여, 비전문가도 쉽게 정보를 이해하고 활용할 수 있도록 지원합니다.
   
## 비동기 통신 방식의 Deep Learning Local Server
### Syncronous Communication
- 동기(Syncronous)란 동시에 일어난다는 뜻입니다. 즉, Request와 Response가 동시에 일어나는 통신 방식입니다.
- 노드 A와 노드 B 사이의 작업 처리 단위를 동시에 맞춥니다.
- 요청한 결과가 그 자리에서 동시에 주어집니다.
### Asyncronous Communication
- 비동기(Asyncronous)란 동시에 일어나지 않는다는 뜻입니다. 즉, Request와 Response가 동시에 일어나지 않는 통신 방식입니다.
- 노드 사이의 작업 처리 단위를 동시에 맞추지 않겠다는 것으로, 요청한 결과가 그 자리에서 주어지지 않습니다.
### 각 통신 방식의 장단점
- 동기 통신의 경우 설계가 간단하며, 직관적이지만 그 작업이 끝날 때까지 아무런 작업도 할 수 없다는 단점이 있습니다.
- 비동기 통신의 경우 동기 통신보다 비교적 복잡한 구현이 필요하지만, 작업이 끝날 때 까지 기다리지 않아도 되기 때문에 그 동안 다른 작업을 수행할 수 있으므로 효율적인 자원의 사용이 가능합니다.


### ✅프로젝트 목표
1. **데이터 수집 및 관리 자동화**: 차량 정보를 효율적으로 크롤링하고 잘못된 데이터를 자동으로 수정할 수 있는 시스템 구축.  
2. **정보 시각화 및 분석 제공**: 지역별 차량 등록 현황 및 기업별 충전 요금을 시각화하여 사용자에게 유용한 데이터를 제공.  
3. **사용자 친화적 인터페이스 개발**: Streamlit 기반 UI를 통해 데이터를 쉽게 조회하고 이해할 수 있는 환경 제공.  
4. **전기차 인프라 최적화 지원**: 데이터 분석을 통해 전기차 보급 및 충전 인프라 관련 정책 수립과 개선에 기여.  



# 2. Tech Stack (기술 스택)

>### <span style="color:cyan"> Co-Work Tool </span>
<table>
  <tr>
    <td>Communication & Messenger</td>
    <td><img src="https://img.shields.io/badge/Discord-5865F2?style=flat&logo=Discord&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/Notion-000000?style=flat&logo=Notion&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/Slack-4A154B?style=flat&logo=Slack&logoColor=white"/></td>
  </tr>
  <tr>
    <td>Development & Merge</td>
    <td><img src="https://img.shields.io/badge/Git-F05032?style=flat&logo=Git&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=GitHub&logoColor=white"/></td>
    
</table>

>### <span style="color:cyan"> Frontend </span>
<table>
  </tr>
  <tr>
    <td>Markup & Style & JS</td>
    <td><img src="https://img.shields.io/badge/HTML-E34F26?style=flat&logo=html5&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/css-1572B6?style=flat&logo=css3&logoColor=white"/></td>
</table>

>### <span style="color:cyan"> Backend </span>
<table>
  <tr>
    <td>BE IDE & Language</td>
    <td><img src="https://img.shields.io/badge/pycharm-%23000000?style=flat&logo=pycharm&logoColor=white"/></td>
    <td><img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white"/></td>
  </tr>  
  <tr>
    <td>RDBMS</td>
    <td><img src="https://img.shields.io/badge/mysql-4479A1?style=flat&logo=mysql&logoColor=white"/></td>
    <td></td>
  </tr>
  
</table>
<br><br><br>



# 3. 시스템 구성도
![image](https://github.com/user-attachments/assets/9788694e-e1c0-47a4-81d8-bdbfacb7e267)

<br><br><br>



## 애자일 보드를 사용하는 이유
```c
애자일 보드는 마치 네비게이션과 같습니다. 전체 개발 과정을 한눈에 파악하고,
각 팀원이 맡은 역할을 명확히 구분하고 이해할 수 있도록 돕습니다. 

덕분에 사소한 막힘과 실시간 소통이 어려운 상황에도 빠르게 각자 할일을 조정하며 효율적으로 목표를 달성할 수 있습니다😊.
```
# 4. 애자일 보드
![image](https://github.com/user-attachments/assets/e426e258-d47e-49cb-8ad8-9e61db17803c)
![image](https://github.com/user-attachments/assets/13b87327-f1d3-4184-b742-d229ed28ecce)


# 5. 비용 최적화를 위한 Deep Learning Local Server 구성 + 보안 설정을 위한 TLS / SSL 소켓 구성
### 5-1 Socket Server (FastAPI) 구성 및 구동 방법


### 5-2 Socket Client (ai-client) 구성 및 구동 방법




# 6. Result (수행 결과)

### ✅ PostMan 결과
![image](https://github.com/user-attachments/assets/66107076-2e88-4354-bd3a-d184c9ffa312)
![image](https://github.com/user-attachments/assets/2c373fae-ef69-4731-b7bb-f8cabc370438)
![image](https://github.com/user-attachments/assets/0201f50d-1a61-4f27-a365-4b3a71dd4748)
![image](https://github.com/user-attachments/assets/392a1097-8016-4cd9-8177-214cb843dec9)

### ✅ SQL 동작 확인: MySQL 데이터베이스에서 데이터를 정확히 삽입하고 가져오는 기능이 정상적으로 작동함을 확인했습니다.
![image](https://github.com/user-attachments/assets/8ce37889-8a67-4ae5-8585-c2210fd84f2c)
![image](https://github.com/user-attachments/assets/4ad7156f-38e1-495d-bcfc-4982eb2a528a)
![image](https://github.com/user-attachments/assets/600e565e-d874-4764-9197-cf38bdc2bcc3)
![image](https://github.com/user-attachments/assets/d7c9c2a9-9cdf-4305-aee7-e91bbf184157)


### ✅ 데이터 크롤링 성공: 주요 자동차 등록 정보를 제공하는 웹사이트로부터 데이터를 성공적으로 크롤링하여 MySQL 데이터베이스에 저장하였습니다.
![image](https://github.com/user-attachments/assets/8aecd593-11ed-4325-ac2b-282e0f1cc977)
![image](https://github.com/user-attachments/assets/5b63c972-38ac-4c28-9e61-ff486701bf9d)
![image](https://github.com/user-attachments/assets/761dbbee-f4c5-4a28-a90a-4f59b31d1132)

<br><br><br>

  
# 7. 한 줄 회고
🤓<b>양의정</b>  
_👏크롤링을 통해 데이터를 수집하고 데이터베이스에 저장한 정보를 한눈에 볼 수 있는 사이트를 만들었습니다. 이 프로젝트를 통해 개발이 이런 것이구나를 느낄 수 있는 기회였습니다.👏_

👨‍💻<b>유제나</b>  
_😍데이터를 크롤링하고 MySQL 데이터베이스에 연동하며 데이터 수집부터 저장, 처리, Streamlit을 활용한 시각화까지 전 과정을 직접 다뤄볼 수 있어 유익한 경험이었습니다. 이 과정을 통해 데이터 활용의 흐름을 이해할 수 있었습니다.😍_

😺<b>정현서</b>  
_첫 팀프로젝트라 여러 어려움이 있었지만, 그래도 무사히 마칠 수 있어 다행이라고 생각합니다. 팀원들 모두 고생하셨습니다.😊_

🪐<b>박예닮</b>  
_해보고 느낀건 아직은 많이 미숙한거같습니다 열심히해야될거같습니다 미안합니다 사랑합니다 감사합니다._

