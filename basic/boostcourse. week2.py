'''
Q1. 중간고사 기말고사 점수를 따로 받아 저장하는 클래스를 구현해보세요.
단, 생성자의 인스턴스는 private으로 선언되어야하며, 데코레이터를 이용해 데이터를 저장하고,
함수를 이용해 평균값을 출력해보세요.

- 자료형의 선언과 데코레이터를 이용해보세요.
'''
# test score, mid : 50, final : 75

class Score():
    def __init__(self, mid : int, final : int):
        self.__mid = mid
        self.__final = final

    @property
    def mid(self):
        return self.__mid
    @property
    def final(self):
        return self.__final

# 출력함수
score = Score(50, 75)
print((score.mid + score.final) / 2)

# 출력 예시
62.5






'''
📌Q2. 다양한 탈 것을 사용하는 게임을 만드는 중입니다.
빠른 구현을 위해서 이미 구현한 Car 클래스를 이용해서 Bike라는 클래스를 새로 제작하려고 합니다.
Car 클래스를 상속받아서 새로운 Bike 클래스를 아래와 같이 출력되도록 구성해보세요.

- Bike class는 size 인자를 추가로 가집니다.
'''
class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

class Bike():
    def __init__(self, fuel, wheels):
        super().__intit__(fuel, wheels)
        self.size = size


# 출력 예시
'''
>>> bike = Bike("gas", 2, "small")
>>> print(bike.fuel, bike.wheels, bike.size)
gas 2 small
'''

''' 
📌Q3. 이번 시험 결과에 대한 데이터를 학과 사무실에서 CSV파일로 전달해줬습니다.
우리는 이 파일을 이용해서 데이터 처리를 진행해야 합니다. 파일 입출력을 이용해 파일 데이터를 리스트로 만들어보세요.

- 파일 입출력에 사용하는 open 함수를 이용해 CSV 파일 내부의 데이터를 읽어보세요

 **CSV파일은 아래 첨부되어있습니다. 
'''
# 파일의 경로를 file_path 로 설정
# ex) file_path ="./data-01-test-score.csv"

def read_File(file_path):
    score_board = []
    with open(file_path) as file:
        while True:
            data = file.readline()
            csv_data = data.replace("₩n", "")

            if data:
                break
            else:
                score_board.append(csv_data.split(","))
        return score_board

read_CSV = read_file(file_path)
print(read_CSV)

'''
>>> print(read_file())
'''




sentence = "I love you"
reversed_sentence = ""
for char in sentence:
    reversed_sentence = char + reversed_sentence
print(reversed_sentence)




