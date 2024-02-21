def age_assignment(*names, **age_data):
    info = ''
    for k, v in sorted(age_data.items()):
        for name in names:
            if k == name[0]:
                info += f'{name} is {v} years old.\n'
    return info


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
