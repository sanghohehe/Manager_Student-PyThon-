from student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def update_student(self, student_id, **kwargs):
        student = self.find_student_by_id(student_id)
        if student:
            for key, value in kwargs.items():
                if hasattr(student, key):
                    setattr(student, key, value)
            return True
        return False

    def remove_student(self, student_id):
        self.students = [s for s in self.students if s.id != student_id]

    def find_student_by_id(self, student_id):
        return next((s for s in self.students if s.id == student_id), None)

    def get_all_students(self):
        return self.students
