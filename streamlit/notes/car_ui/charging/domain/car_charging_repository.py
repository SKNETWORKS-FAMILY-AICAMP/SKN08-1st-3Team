from abc import ABC, abstractmethod
import pandas as pd

# 이 도메인은 '충전'을 뜻함. 코드는 cars와 동일

class CarChargingRepository(ABC):
    @abstractmethod
    def fetchAll(self) -> pd.DataFrame:
        pass
