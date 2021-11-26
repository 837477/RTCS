# RTCS (RealTime COVID-19 Status)

> 본 프로젝트는 세종대학교 소프트웨어공학 수업의 개인프로젝트로 진행되었습니다.
> *Version 0.0.1*

***

**Developer**: 837477 <8374770@gmail.com><br>
**License**: ![LICENSE][LICENSE] (See `LICENSE`)

<br>

<img width="1393" alt="image" src="https://user-images.githubusercontent.com/37999795/143528930-e04b5561-5826-49b9-8736-f40ff8231630.png">

<br>

## What ?
서울열린데이터광장의 국내 코로나 바이러스 데이터를 받아와, 정제하여 제공합니다.
주요 기능은 다음과 같습니다.
- 국내 코로나 확진자 현황
- 서울 코로나 확진자 현황
- 국내 백신 접종자 현황
- 특정 위치의 코로나 현황

특정 위치의 코로나 현황은 지도에서 원하는 위치를 선택하면 바로 확인할 수 있습니다.

<br>

## How to use
```
pip install -r requirements.txt

uvicorn run:app
# --reload --host 0.0.0.0 --port 80
```
<br>


<!-- Markdown link & img dfn's -->
[LICENSE]: https://img.shields.io/github/license/837477/raising_visitor_bot?style=flat-square
