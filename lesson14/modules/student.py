from lesson14.modules.human import Human


class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"gender: {self.gender}\n age: {self.age}\n first name: {self.first_name}\n last name: {self.last_name}\n record book: {self.record_book}\n\n "
