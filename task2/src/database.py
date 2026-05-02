import sqlite3

def connection():
    conn = sqlite3.connect("./journal.db") 
    return conn
    
def index():
    with connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """ 
            CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    major TEXT
            );
        """
        )
        cur.execute(
            """ 
            CREATE TABLE IF NOT EXISTS courses (
                    course_id INTEGER PRIMARY KEY,
                    course_name TEXT,
                    instructor TEXT
            );
        """
        )
        cur.execute(
            """ 
            CREATE TABLE IF NOT EXISTS student_coursers (
                    student_id INTEGER,
                    course_id INTEGER,
                    PRIMARY KEY (student_id, course_id)
                    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
                    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
            );
        """
        )
        conn.commit()

def fill():
    with connection() as conn:
        cur = conn.cursor()
        cur.executemany(
            """INSERT INTO students (name, age, major) VALUES (?, ?, ?)""",
            [("Alice", 20, "IT"), ("Bob", 21, "Design"), ("Tom", 18, "Economics")],
        )
        cur.executemany(
            """INSERT INTO courses (course_name, instructor) VALUES (?, ?)""",
            [("Programming", "LP"), ("Design", "BM"), ("3D Modeling", "AR")],
        )
        conn.commit()

index()
fill()

