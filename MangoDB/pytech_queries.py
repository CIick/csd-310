from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
students = db.students

student_list = students.find({})


print("\n  ----------------------------------------------------------------------------------------------------\n")
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --\n")
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
balph = students.find_one({"student_id": "1008"})
print("\n  ----------------------------------------------------------------------------------------------------\n")
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --\n")
print("  Student ID: " + balph["student_id"] + "\n  First Name: " + balph["first_name"] + "\n  Last Name: " + balph["last_name"] + "\n")
print("\n  ----------------------------------------------------------------------------------------------------\n")
input("\n\n  End of program, press any key to continue...")