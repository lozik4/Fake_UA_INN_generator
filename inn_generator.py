import random
from datetime import datetime, date


class InnGenerator:

    def __init__(self, birthdate=None, gender=None):
        if gender not in (0, 1, None):
            raise ValueError("Value mast be 0 - Female, or 1 - Male")
        if not birthdate:
            birthdate = '21-06-1990'
        if not gender:
            gender = random.randint(0, 1)
        self.birthdate = datetime.strptime(birthdate, '%d-%m-%Y').date()
        self.gender = gender

    def __gender(self) -> int:
        if self.gender == 0:
            return random.choice([0, 2, 4, 6, 8])
        return random.choice([1, 3, 5, 7, 9])

    @staticmethod
    def __people_number() -> int:
        return random.randint(100, 999)

    def __day_count(self) -> int:
        __START_INN_COUNT = date(1899, 12, 31)
        return (self.birthdate - __START_INN_COUNT).days

    @staticmethod
    def __check_sum_calculate(val: str) -> int:
        check_sum = int(val[0]) * (-1) + \
                    int(val[1]) * 5 + \
                    int(val[2]) * 7 + \
                    int(val[3]) * 9 + \
                    int(val[4]) * 4 + \
                    int(val[5]) * 6 + \
                    int(val[6]) * 10 + \
                    int(val[7]) * 5 + \
                    int(val[8]) * 7

        return (check_sum % 11) % 10

    def generate_inn(self) -> int:
        people_num = self.__people_number()
        gender = self.__gender()
        day_count = self.__day_count()

        inn = f"{day_count}{people_num}{gender}"
        check_sum = self.__check_sum_calculate(inn)

        return int(f"{inn}{check_sum}")


if __name__ == '__main__':
    print(InnGenerator('08-11-2000', 0).generate_inn())
