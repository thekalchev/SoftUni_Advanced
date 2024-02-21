set1 = set(int(x) for x in input().split())
set2 = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command

    if command == "Add First":
        [set1.add(int(el)) for el in data]
    elif command == "Add Second":
        [set2.add(int(el)) for el in data]
    elif command == "Remove First":
        [set1.discard(int(el)) for el in data]
    elif command == "Remove Second":
        [set2.discard(int(el)) for el in data]
    elif command == "Check Subset":
        print(set1.issubset(set2) or set2.issubset(set1))

print(*sorted(set1), sep=", ")
print(*sorted(set2), sep=", ")