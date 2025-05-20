list_method = []
for method in dir(list):
    if method.startswith("__"):
        continue
    list_method.append(method)
     
set_method = []
for method in dir(list):
    if method.startswith("__"):
        continue
    set_method.append(method)

str_method = []
for method in dir(list):
    if method.startswith("__"):
        continue
    str_method.append(method)

tuple_method = []
for method in dir(list):
    if method.startswith("__"):
        continue
    tuple_method.append(method)

dict_method = []
for method in dir(dict):
    if method.startswith("__"):
        continue
    dict_method.append(method)

basliklar = ["list methods", "set methods", "string methods", "tuple methods", "dict methods"]
classes = [list_method, set_method, str_method, tuple_method, dict_method] 

max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)

with open("Methods.txt","w") as f:
    for baslik in basliklar:
        print(baslik,end="")
        print(" " *(30 - len(baslik)),end="")
        f.write(baslik)
        f.write(" " *(30 - len(baslik)),end="")

    for i in range(max_len):
        print()
        f.write("\n")
    for class_ in classes:
        if i >= len(class_):
            print("-------",end="")
            print(" " *23,end="")
            f.write("-------")
            f.write(" " *23)
        else: 
            print(class_[i],end="")
            print(" " * (30 - len(class_[i])),end="")
            f.write(class_[i])
            f.write(" " * (30 - len(class_[i])))





