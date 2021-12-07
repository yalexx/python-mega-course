# my_file = open("fruits.txt")
# content = my_file.read()
# my_file.close()

with open("fruits.txt", "a+") as my_file:
    my_file.write("\nOkra")
    my_file.seek(0)
    content = my_file.read()

print(content)
