import cx_Oracle

# Establish a connection to the database
dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
conn = cx_Oracle.connect(user='yourusername', password='yourpassword', dsn=dsn_tns)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Function to add a new student to the database
def add_student(id, name, email):
    cursor.execute("INSERT INTO students (id, name, email) VALUES (:id, :name, :email)", {'id': id, 'name': name, 'email': email})
    conn.commit()
    print("Student added successfully")

# Function to view a specific student's details
def view_student(id):
    cursor.execute("SELECT * FROM students WHERE id = :id", {'id': id})
    result = cursor.fetchone()
    if result:
        print(result)
    else:
        print("Student not found")

# Function to view all students' details
def view_all_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for student in result:
        print(student)

# Function to update a student's details
def update_student(id, name, email):
    cursor.execute("UPDATE students SET name = :name, email = :email WHERE id = :id", {'name': name, 'email': email, 'id': id})
    conn.commit()
    print(cursor.rowcount, "record(s) updated")

# Function to delete a student from the database
def remove_student(id):
    cursor.execute("DELETE FROM students WHERE id = :id", {'id': id})
    conn.commit()
    print(cursor.rowcount, "record(s) deleted")

# Test the functions
add_student(1, "John Doe", "john.doe@example.com")
add_student(2, "Jane Smith", "jane.smith@example.com")
view_all_students()
view_student(1)
update_student(1, "John Doe Jr.", "john.doe.jr@example.com")
remove_student(2)

# Close the database connection
conn.close()