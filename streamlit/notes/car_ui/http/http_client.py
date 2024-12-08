import asyncio
import os
import httpx


# HttpClient 클래스는 비동기 및 동기 HTTP 요청 기능을 통합한 클래스
class HttpClient:
    djangoHttpxInstance = httpx.AsyncClient( # 비동기 HTTP 클라이언트 인스턴트
        base_url=os.getenv("DJANGO_URL"),
    )

    @classmethod
    async def post(cls, endpoint: str, data: dict):  # 비동기 POST 요청 메서드
        try:
            response = await cls.djangoHttpxInstance.post(endpoint, json=data)
            # 이 부분에서 비동기 POST 요청을 보내는 것임.
            # 요청 URL: base_url + endpoint =  'https://example.com/cars/add'대충 이런식

            if response.status_code == 200: # 상태 코드 확인. 200 OK이면 True를 반환
                return True
            else:
                print(f"Failed to send to Django: {response.status_code}")
                return False # 200이 아닌 경우는 실패 메시지를 출력하고 False를 반환

        except httpx.RequestError as exc: # httpx.RequestError 예외가 발생하면,
            print(f"An error occurred while sending to Django: {str(exc)}")
            return False # 에러 메시지를 출력하고 False를 반환

    @classmethod
    def post_sync(cls, endpoint: str, data: dict):  # 동기 POST 요청 메서드
        """동기적으로 post 요청을 처리할 수 있도록 래핑"""
        # 무슨말이냐? 동기 요청을 비동기 요청으로 실행하기 위해 **asyncio.run()**을 사용한다는 뜻
        return asyncio.run(cls.post(endpoint, data))
        # 동기 메서드를 호출할 때는 await를 사용할 필요가 없음

    @classmethod
    async def get(cls, endpoint: str):
        """비동기 GET 요청 처리"""
        try:
            response = await cls.djangoHttpxInstance.get(endpoint)

            if response.status_code == 200: # 200 OK이면 JSON 데이터를 반환
                return response.json()  # 또는 필요한 다른 데이터 처리
            else:
                print(f"Failed to fetch data from Django: {response.status_code}")
                return None # 200이 아닌 경우는 None을 반환

        except httpx.RequestError as exc:
            print(f"An error occurred while sending GET request: {str(exc)}")
            return None

    @classmethod
    def get_sync(cls, endpoint: str):
        """동기적으로 GET 요청을 처리하는 래핑 메서드"""
        return asyncio.run(cls.get(endpoint))

# 코드 내에서 동기(Sync) 요청과 비동기(Async) 요청을 둘 다 지원해야 하는 이유는
# 프로그램의 실행 환경과 요구사항이 서로 다르기 때문

# + 쌤이 말씀하시길... 코드들이 GET 요청만 받아서 동기 POST 코드 삭제해도 문제없이 돌아간다고 하심.