# -*-coding:utf-8-*-
# message = input("nihao")
# print(message)

uncofirmed_users = ['a','b','c']
confirmed_users = []

while uncofirmed_users:
    current_user = uncofirmed_users.pop()
    print("verifying user:" + current_user.title())
    confirmed_users.append(current_user)

print("\n已验证用户有:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
