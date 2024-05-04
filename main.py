
with open("my_file.txt", "w") as file:
    file.write("sleepy head\n")
    file.write("C'mon wake up 34.\n")
    file.write("whoooo!\n")


with open("my_file.txt", "a") as file:
    file.write("append mode.\n")
    file.write("98765 r.\n")
    file.write("easy!\n")

with open("my_file.txt", "r") as file:
   
    contents = file.read()

    print(contents)
