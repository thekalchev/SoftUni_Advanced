# num_of_usernames = int(input())
# unique_usernames = set()
#
# for username in range(num_of_usernames):
#     current_user = input()
#     unique_usernames.add(current_user)
#
# print(*unique_usernames, sep='\n')
#

print(*{input() for _ in range(int(input()))}, sep='\n')