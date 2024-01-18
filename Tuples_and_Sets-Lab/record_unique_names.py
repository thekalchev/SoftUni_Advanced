# n = int(input())
# unique_students = []
# for student in range(n):
#     current_student = input()
#     if current_student not in unique_students:
#         unique_students.append(current_student)
#         print(current_student)

n = int(input())
unique_students = set()
for _ in range(n):
    current_student = input()
    unique_students.add(current_student)
for student in unique_students:
    print(student, end='\n')
