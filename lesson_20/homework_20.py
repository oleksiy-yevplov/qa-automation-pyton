
import random
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.orm import declarative_base, relationship, Session

DB_URL = "sqlite:///students_sqlalchemy.db"
Base = declarative_base()


class Enrollment(Base):
    __tablename__ = "enrollments"
    student_id = Column(Integer, ForeignKey("students.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    courses = relationship("Course", secondary="enrollments", back_populates="students")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)

    students = relationship("Student", secondary="enrollments", back_populates="courses")


engine = create_engine(DB_URL, echo=False)
Base.metadata.create_all(engine)


def seed():
    with Session(engine) as s:
        if s.scalar(select(Course.id).limit(1)) is not None:
            return

        courses = [Course(title=t) for t in ["Math", "Physics", "Databases", "Python", "DevOps"]]
        s.add_all(courses)
        s.flush()

        for i in range(1, 21):
            st = Student(name=f"Student {i}", email=f"student{i}@mail.com")
            st.courses.extend(random.sample(courses, k=random.randint(1, 3)))
            s.add(st)

        s.commit()


def add_student_to_course(name: str, email: str, course_title: str):
    with Session(engine) as s:
        course = s.scalar(select(Course).where(Course.title == course_title))
        if not course:
            print("No such course:", course_title)
            return

        st = Student(name=name, email=email)
        st.courses.append(course)
        s.add(st)
        s.commit()
        print("Added:", st.id, st.name, "->", course.title)


def students_in_course(course_title: str):
    with Session(engine) as s:
        course = s.scalar(select(Course).where(Course.title == course_title))
        if not course:
            return []
        return [(st.id, st.name, st.email) for st in course.students]


def courses_of_student(email: str):
    with Session(engine) as s:
        st = s.scalar(select(Student).where(Student.email == email))
        if not st:
            return []
        return [(c.id, c.title) for c in st.courses]


def update_student_email(student_id: int, new_email: str):
    with Session(engine) as s:
        st = s.get(Student, student_id)
        if not st:
            print("No such student:", student_id)
            return
        st.email = new_email
        s.commit()
        print("Updated student email:", student_id, "->", new_email)

def test_student_exists(student_id: int):
    with Session(engine) as s:
        st = s.get(Student, student_id)
        assert st is not None, f"Student {student_id} does not exist"


def test_student_email(student_id: int, email: str ):
    with Session(engine) as s:
        st = s.get(Student, student_id)
        assert st, f"No such student: {student_id}"
        assert st.email == email, f"Student {student_id} does not match email {email}"



def update_course_title(old_title: str, new_title: str):
    with Session(engine) as s:
        c = s.scalar(select(Course).where(Course.title == old_title))
        if not c:
            print("No such course:", old_title)
            return
        c.title = new_title
        s.commit()
        print("Updated course title:", old_title, "->", new_title)


def delete_student(student_id: int):
    with Session(engine) as s:
        st = s.get(Student, student_id)
        if not st:
            print("No such student:", student_id)
            return
        s.delete(st)
        s.commit()
        print("Deleted student:", student_id)


if __name__ == "__main__":
    random.seed(42)
    seed()

    add_student_to_course("New Student", "new@student.com", "Databases")

    print("\nStudents in Databases:")
    for row in students_in_course("Databases"):
        print(row)

    print("\nCourses of new@student.com:")
    print(courses_of_student("new@student.com"))

    with Session(engine) as s:
        new_id = s.scalar(select(Student.id).where(Student.email == "new@student.com"))

    update_student_email(new_id, "new2@student.com")
    update_course_title("Python", "Advanced Python")
    delete_student(new_id)
