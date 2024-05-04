
try:
    with open("my_file.txt", 'w') as file:
        file.write("sleepy head \n")
        file.write("C'mon wake up!!\n")
        file.write("Nambasss7\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File creation completed.")


try:
    with open("my_file.txt", 'r') as file:
        print("Contents of my_file.txt:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File reading completed.")

try:
    with open("my_file.txt", 'a') as file:
        file.write(" append mode\n")
        file.write("randomm 0\n")
        file.write("come closer man\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
finally:
    print("File appending completed.")
