from Classes import Dog
def greet_user():
    print("hello")

greet_user()

def greet_user(username):
    print("hello" + username)

greet_user(username="zgy")
# greet_user() 方法定义覆盖上述同名方法

def greet_user(username,age=10):
    print("hello" + username,"age=" + str(age))

greet_user(username="zgy")

def getFormattedNAME(name):
    return  name

print(getFormattedNAME("zgy"))

def make_pizza(*toppings):#*toppings 一个空元祖
    print(toppings)

make_pizza((1,2,3))
make_pizza("2")

def build_profile(**userinfo):
    profile={}
    for key,value in userinfo.items():
        profile[key] = value

    return  profile

print(build_profile(abc=1,cd="22"))