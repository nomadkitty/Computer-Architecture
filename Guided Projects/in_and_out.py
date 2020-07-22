# try:
#     file = open("print8.ls8", "r")
#     lines = file.read()
#     # print(lines)
#     raise Exception("hi")
# except Exception:
#     print(file.closed)
import sys

if len(sys.argv) < 2:
    print("Please pass in a second filename: py -3 in_and_out.py second_filename.py")
    sys.exit()

file_name = sys.argv[1]
try:
    with open(file_name) as file:
        for line in file:
            split_line = line.split("#")[0]
            command = split_line.strip()
            if command == "":
                continue
            num = int(command, 2)
            print(num)
except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} file was not found")
    sys.exit()
