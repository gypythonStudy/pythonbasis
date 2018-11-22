with open('python.text') as gy_object:
    contents = gy_object.read()
    print(contents)

with open('python.text') as gy_object:
    for line in gy_object:
        print(line.rstrip())

with open('python.text','w') as gy_object: #覆盖原有内容
    gy_object.write("i love zhu\n")
    gy_object.write("i love zhu\n")

with open('python.text','a') as gy_object:
    gy_object.write("hao")

try:
    print(5/0)
except ZeroDivisionError:
    print("can't zero")

try:
    with open("12.text") as gy_obj:
        con = gy_obj.readlines()
except FileNotFoundError:
    # print("notexits")
    pass