# def gather_credits(*args):
#     credits_needed = args[0]
#     credits_obtained = 0
#     courses_taken = []
#     for course, credits in args[1:]:
#         if credits_obtained < credits_needed:
#             if course not in courses_taken:
#                 courses_taken.append(course)
#                 credits_obtained += credits
#     if credits_obtained >= credits_needed:
#         return (f'Enrollment finished! Maximum credits: {credits_obtained}.\n'
#                 f'Courses: {", ".join(sorted(courses_taken))}')
#     if credits_needed > credits_obtained:
#         return (f'You need to enroll in more courses! '
#                 f'You have to gather {credits_needed - credits_obtained} credits more.')
#
#
# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
#
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
#
# print(gather_credits(
#     60,
#     ("Basics", 27),
#     ("Fundamentals", 27),
#     ("Advanced", 30),
#     ("Web", 30)
# ))

def gather_credits(number_of_credits_needed, *course_info):
    current_credits = 0
    courses_enrolled = {}

    for course_name, credits in course_info:
        if current_credits < number_of_credits_needed:
            if course_name in courses_enrolled:
                continue
            courses_enrolled[course_name] = credits
            current_credits += credits
        else:
            break

    if current_credits >= number_of_credits_needed:
        return (f'Enrollment finished! Maximum credits: {current_credits}.\n'
                f'Courses: {", ".join(sorted(courses_enrolled))}')
    return (f'You need to enroll in more courses! '
            f'You have to gather {number_of_credits_needed - current_credits} credits more.')

print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))