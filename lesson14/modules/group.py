from lesson14.modules.error_exception import Students10Error


class Group:
    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: str):
        try:
            if len(self.group) >= 10:
                raise Students10Error("A group cannot contain more than 10 students")
            else:
                self.group.add(student)
        except Students10Error as e:
            print(e)

    def delete_student(self, last_name: str):
        self.group.discard(self.find_student(last_name))

    def find_student(self, last_name: str) -> str|None:
        result = None
        for student in self.group:
            if last_name == student.last_name:
                result = student
        return result

    def __str__(self) -> str:
        all_students = ''
        for student in self.group:
            all_students += f"{student}"
        return f'----Number:{self.number}----\n {all_students} '
