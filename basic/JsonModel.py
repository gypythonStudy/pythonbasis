import  json

numbers = [1,2,3]

filename = "number.json"

with open(filename,"w") as f_obj:
    json.dump(numbers,f_obj)
with open(filename,"r") as f_obj:
    number = json.load(f_obj)
print(number)