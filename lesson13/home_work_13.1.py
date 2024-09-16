class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"gender: {self.gender}\n age: {self.age}\n first name: {self.first_name}\n last name: {self.last_name}\n record book: {self.record_book}\n\n "


class Group:

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name: str):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name: str):
        result = None
        for student in self.group:
            if last_name == student.last_name:
                result = student
        return result

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += f"{student}"
        return f'----Number:{self.number}----\n {all_students} '


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!