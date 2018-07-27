
with open('MYPAGE') as file:
    content1 = file.read()

with open('MYPAGE') as file:
    content2 = file.readlines()
print(content1)
print(content2)
