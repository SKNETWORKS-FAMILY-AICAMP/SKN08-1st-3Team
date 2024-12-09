import asyncio
import streamlit as st
from cars.domain.usecase import GetCarsUseCase
from cars.infra.car_repository_impl import CarRepositoryImpl

# 이 코드는 Streamlit을 사용하여 자동차 목록을 화면에 표시하는 UI 애플리케이션임.
# GetCarsUseCase를 통해 자동차 목록 데이터를 가져오고, Streamlit UI에 테이블 형태로 출력


def showCarUi():
# 이름 그대로 show Car_ui
    car_repo = CarRepositoryImpl()
    # CarRepositoryImpl 인스턴스를 생성
    usecase = GetCarsUseCase(car_repo)

    try:
        df = usecase.execute()

        st.header("전체 데이터 예시")
        # "전체 데이터 예시" 라는 제목을 추가
        st.table(df)
        # DataFrame df를 테이블로 표시합

    except Exception as e: # try 블록에서 예외(Exception)가 발생하면 실행
        st.error(f"차량 데이터를 불러오지 못했습니다: {e}")
