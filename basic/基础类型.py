print("hello,world")
message = "helloworld"# 字符串
print(message)
message = "zgy"
print(message)
print(message.title())
print(message.upper())
print(message)
print(message.lower())
name = message.upper() + message.lower()
print("\t"+name) #空格符

whiteStr = " 你最帅1"
print(whiteStr.rstrip()) #删除末尾空格
print(whiteStr.lstrip()) #删除首部空格
print(whiteStr.strip())  #删除首部和尾部空格
print("“Hello,?”")

print(2*2)
print(3**3)
print(0.2+0.1)

name = "zgy"
age = 14 #str将非字符串转化为字符串

print(name + str(age))

#数组
pythonArr = ['123',1,2]
print(pythonArr)
print(pythonArr[2])
pythonArr.append(222)
pythonArr.insert(0,"zgy")
print(pythonArr)
del pythonArr[0] #删除数组元素
print(pythonArr)
pythonArr.pop()
print(pythonArr)
pythonArr.pop()# 默认删除末尾元素
#pythonArr.pop(1)# 默认指定下标元素
print(pythonArr)
pythonArr.remove("123") #如果无此元素 会Crash
print(pythonArr)

pythonArr = ['123',"a","2"]
print(pythonArr.sort()) #改变自身排序 无返回值 None 永久性修改
print(pythonArr)
pythonArr = ['123',"a","2"]
print(sorted(pythonArr)) #临时排序  返回值
print(pythonArr.reverse()) #自身倒叙 无返回值 None 永久性修改
print(len(pythonArr))

for model in pythonArr:
	print(model)
print("你帅")

for x in range(1,3):
	print(x)

print(list(range(2,12,3)))

squares = [value**2 for value in range(1,11)]
print(squares)
print(squares[2:20])
copysquares = squares #公用一块内存地址
print(copysquares)
copysquares.append(2)
print(squares)
print(copysquares)

copysquares = squares[:] #重新开辟空间

copysquares.append(1111)
print(squares)
print(copysquares)

#元祖
dimensions = (100,"123")
# dimensions[0] = 1 元祖不可变 
dimensions = ("122",100) #可重新定义

a = 15

if a > 10 and a > 20 :
	print("正确")
else:
	print("错误")

a = [1,2,3]

if "3" in a :
	print("包含")
else:
	print("不包含")

if "3" in a:
	print("包含")
elif 3 in a:
	print("3包含")
else:
	print("都不包含")

#字典

pyDic = {"color":"red"}
pyDic["dic"] = 1
pyDic["color"] = 2
print(pyDic)
del pyDic["dic"]
print(pyDic)
for key,value in pyDic.items():
	print(key)

for key in pyDic.keys(): #pyDic.values()
	print(key)







