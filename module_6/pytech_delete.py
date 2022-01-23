from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

test_delete = {
    "student_id": "1010",
    "first_name": "Test",
    "last_name": "Delete"
}

test_doc_id = students.insert_one(test_delete).inserted_id
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(test_doc_id))

student_test_delete = students.find_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_test_delete["student_id"] + "\n  First Name: " + student_test_delete["first_name"] + "\n  Last Name: " + student_test_delete["last_name"] + "\n")

new_student_list = students.find({})

print("\n  -- DISPLAYING FULL STUDENTS DOCUMENTS FROM find() QUERY (WITH 1010 STUDENT)--")

for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

deleted_student_test_doc = students.delete_one({"student_id": "1010"})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY (DELETED 1010 STUDENT)--")

new_student_list_without_1010 = students.find({})

for doc in new_student_list_without_1010:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")


input("\n\n  End of program, press any key to continue...")