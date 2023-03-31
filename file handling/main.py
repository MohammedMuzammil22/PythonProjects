# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

# with open("my_file.txt",mode="a") as file:
#     file.write("\nsorry bhai")   

# # with open("muzammil.txt",mode="w") as file:
# #     file.write("\nsorry bhai")   

# with open("muzammi.txt",mode="w") as file:
#     file.write("\nhi muzammil")

# with open("hs.txt",mode="r") as h:
#     hs = int(h.read())
#     print(type(hs))

# ****** absolute path ******
with open("/Users/ACER/Desktop/my_file.txt", mode="r") as file:
    content = file.read()
    print(content)

# ****** relative path ******
with open("../../../my_file.txt", mode="r") as file:
    content = file.read()
    print(content)