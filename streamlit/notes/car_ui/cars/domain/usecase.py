import pandas as pd
from cars.domain.car_repository import CarRepository
# 같은 domain 하위 폴더인 car_repository를 받아옴.


# entity의 car.py 같은 느낌.
class GetCarsUseCase:
    def __init__(self, carRepository: CarRepository):
        self.carRepository = carRepository
        # 여기서는 CarRepository를 carRepository에 입력하고 쓸 생각인가봄

    def execute(self) -> pd.DataFrame:
        return self.carRepository.fetchAll()
    # CarRepository 가서 fetchAll()을 실행하고 와. 그리고 결과는 DataFrame으로 반환할거야! 라는 뜻.

# usecase.py의 코드는 '의존성 주입(Dependency Injection)'의 한 예임
# GetCarsUseCase 클래스가 CarRepository에 의존한다는 것을 나타냄

# execute() 메서드가 호출되면-> CarRepository의 fetchAll() 메서드를 호출되고, 자동차 데이터(pandas DataFrame)를 반환하게 되는 것임.