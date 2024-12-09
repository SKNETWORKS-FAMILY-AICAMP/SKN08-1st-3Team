import httpx
import pandas as pd
from cars.domain.car_repository import CarRepository
from httpx import AsyncClient, RequestError

from dotenv import load_dotenv
import os

load_dotenv()
# .env 파일에 저장된 환경 변수를 로드(load)하는 함수

base_url = os.getenv("DJANGO_URL")
# settings.py에서 DJANGO_URL이라는 이름의 환경 변수를 가져옵니다.
print(f"DJANGO_URL: {base_url}")


class CarRepositoryImpl(CarRepository):
# CarRepositoryImpl는 CarRepository의 구현체
    __http_client = httpx.Client(
        base_url=os.getenv("DJANGO_URL"), timeout=25.0
    )
    # httpx.Client(): HTTP 요청을 보내는 클라이언트로, requests와 유사한 라이브러리
    # base_url: 모든 API 요청의 기본 URL로, 환경 변수 DJANGO_URL에서 가져옴
    # timeout=25.0: 요청이 25초 이내에 응답하지 않으면 실패로 처리

    def fetchAll(self) -> pd.DataFrame:
        try:
            endpoint = "/car/request-car-list"
            response = self.__http_client.get(endpoint)
            # 실제로 호출되는 URL: base_url + endpoint = 예를들어 'https://example.com/car/request-car-list'
            # self.__http_client.get() : GET 요청을 보내서 자동차 데이터를 가져옴. 응답객체 response를 반환

            if response.status_code == 200:
                #HTTP 상태 코드를 확인해서, 200이면 정상 응답이므로 데이터를 반환합니다. 200이 아닌 경우는 Exception으로 넘어감
                return pd.DataFrame(response.json())
                # 정상이면 API의 JSON 응답을 Python 딕셔너리로 변환함

            else: # 200이 아닌 경우
                raise Exception(f"Failed to fetch car data: {response.status_code}")
            # 예를 들어, 서버가 500 (Internal Server Error) 또는 404 (Not Found)를 반환하면,
            # "Failed to fetch car data: 500" 또는 **"Failed to fetch car data: 404"**를 출력

        except RequestError as exc: # RequestError 예외: 네트워크 오류(서버 연결 불가, 시간 초과 등)가 발생했을 때 발생
            raise Exception(f"HTTP request failed: {str(exc)}")
            # 위와 같은 에러메세지 출력