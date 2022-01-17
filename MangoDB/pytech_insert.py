from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.vy4xh.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

ralph = {
    "student_id": "1007",
    "first_name": "ralph",
    "last_name": "McRalph",
    "enrollments": [
        {
            "term": "Winter Semester",
            "gpa": "3.2",
            "start_date": "November 27, 2021",
            "end_date": "March 21, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security (2223-1)",
                    "instructor": "Luke Donoho",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR350",
                    "description": "Web, Commerce & Application Se (2223-1)",
                    "instructor": "Professor Karla Carter",
                    "grade": "A+"
                }
            ]
        }
    ]

}


balph = {
    "student_id": "1008",
    "first_name": "balph",
    "last_name": "McBalph",
    "enrollments": [
        {
            "term": "Winter Semester",
            "gpa": "3.2",
            "start_date": "November 27, 2021",
            "end_date": "March 21, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security (2223-1)",
                    "instructor": "Luke Donoho",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR350",
                    "description": "Web, Commerce & Application Se (2223-1)",
                    "instructor": "Professor Karla Carter",
                    "grade": "A+"
                }
            ]
        }
    ]

}


salph = {
    "student_id": "1009",
    "first_name": "salph",
    "last_name": "McSalph",
    "enrollments": [
        {
            "term": "Winter Semester",
            "gpa": "3.2",
            "start_date": "November 27, 2021",
            "end_date": "March 21, 2022",
            "courses": [
                {
                    "course_id": "CYBR410",
                    "description": "Data/Database Security (2223-1)",
                    "instructor": "Luke Donoho",
                    "grade": "A"
                },
                {
                    "course_id": "CYBR350",
                    "description": "Web, Commerce & Application Se (2223-1)",
                    "instructor": "Professor Karla Carter",
                    "grade": "A+"
                }
            ]
        }
    ]

}

students = db.students

print("\n  -- INSERT STATEMENTS --")
ralph_student_id = students.insert_one(ralph).inserted_id
print("  Inserted student record Ralph McRalph into the students collection with document_id " + str(ralph_student_id))

balph_student_id = students.insert_one(balph).inserted_id
print("  Inserted student record Balph McBalph into the students collection with document_id " + str(balph_student_id))

salph_student_id = students.insert_one(salph).inserted_id
print("  Inserted student record Salph McSalph into the students collection with document_id " + str(salph_student_id))

input("\n\n  End of program, press any key to exit... ")