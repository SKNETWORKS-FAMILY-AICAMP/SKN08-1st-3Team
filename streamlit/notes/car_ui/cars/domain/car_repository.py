# streamlit이란?
# Streamlit은 파이썬으로 데이터 대시보드, 웹 애플리케이션, 데이터 시각화 앱을 빠르고 쉽게 개발할 수 있도록 도와주는 오픈 소스 라이브러리입니다.
# 복잡한 웹 개발 기술(HTML, CSS, JavaScript)을 배우지 않고도 간단한 파이썬 코드만으로도 웹 애플리케이션을 제작할 수 있습니다.

from abc import ABC, abstractmethod
import pandas as pd


## CarRepository는 추상 클래스임. ABC는 Abstract Base Class의 약자고.
class CarRepository(ABC):
    @abstractmethod
    def fetchAll(self) -> pd.DataFrame:
        # -> 의미 : "모든 자동차 데이터를 DataFrame으로 반환하겠다"
        pass


# fetchAll : '모든 데이터를 가져오다' 라는 뜻, 데이터베이스(DB)나 API에서 전체 데이터를 조회해서 가져오는 메서드.