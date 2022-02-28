# RTCS - RealTime COVID-19 Status
<br><br>

<div align=center>
    <strong># FastAPI</strong> &nbsp;
    <strong># MongoDB</strong> &nbsp;
    <br><br><br>
    <p><img width="1393" alt="image" src="https://user-images.githubusercontent.com/37999795/143528930-e04b5561-5826-49b9-8736-f40ff8231630.png"></p>
</div>
<br>

## What is this?
> 본 프로젝트는 "소프트웨어공학" 수업의 개인 과제로 진행된 토이 프로젝트입니다.

서울열린데이터광장의 데이터 기반으로 실시간 코로나 바이러스 현황을 제공합니다.<br>

#### 주요 기능
- 국내 코로나 확진자 현황
- 서울 코로나 확진자 현황
- 국내 백신 접종자 현황
- 특정 위치의 코로나 현황

특정 위치의 코로나 현황은 지도에서 원하는 위치를 선택하면 바로 확인할 수 있습니다.

<br>

## Dependency
```shell
python 3.8.X
MongoDB 5.X
```
<br>

## How to use
```shell
# Environments
export MONGODB_URI="<MongoDB Host>"
export MONGODB_NAME="<MongoDB Name>"
export API_SECRET_KEY="<JWT_SECRET_KEY>"
export KAKAO_MAP_API_KEY="<KAKAO Developer API Key>"
```
```shell
# Run
pip install -r requirements.txt
uvicorn app:app --reload --host=0.0.0.0 --port=80
```
<br>

## About Me
🙋🏻‍♂️ Name: 837477

📧 E-mail: 8374770@gmail.com

🐱 Github: https://github.com/837477

<br>

## Contributing
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
