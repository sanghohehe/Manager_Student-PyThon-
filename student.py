from person import Person
from course import Course

class Student(Person):
    def __init__(self, id, name, age, major):
        super().__init__(id, name, age)
        self.major = major
        self.courses = []  # list[Course]

    def add_course(self, course):
        self.courses.append(course)

    def calculate_gpa(self):
        if not self.courses:
            return 0.0
        total_score = sum(c.score * c.credit for c in self.courses)
        total_credit = sum(c.credit for c in self.courses)
        return round(total_score / total_credit, 2) if total_credit > 0 else 0.0

    def __str__(self):
        return f"SV: {self.name} ({self.id}), Ngành: {self.major}, GPA: {self.calculate_gpa()}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "courses": [c.to_dict() for c in self.courses]
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["id"], data["name"], data["age"], data["major"])
        student.courses = [Course.from_dict(c) for c in data.get("courses", [])]
        return student
