class Course:
    def __init__(self, course_id, name, credit, score=0):
        self.course_id = course_id
        self.name = name
        self.credit = credit
        self.score = score

    def __str__(self):
        return f"{self.course_id} - {self.name} ({self.credit} tín chỉ) | Điểm: {self.score}"

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "name": self.name,
            "credit": self.credit,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["course_id"], data["name"], data["credit"], data["score"])
