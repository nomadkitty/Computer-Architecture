# this won't close files for us
# try:
#     file = open("print8.ls8", 'r')
#     lines = file.read()
#     # print(lines)
import sys
​
#     raise Exception('hi')
# except Exception:
#     print(file.closed)
​
​
# try:
#     filename = sys.argv[1]
# except IndexError:
#     print('Error Message')
#     sys.exit()
​
​
if len(sys.argv) < 2:
    print("Please pass in a second filename: python3 in_and_out.py second_filename.py")
    sys.exit()
​
file_name = sys.argv[1]
try:
    # this will close files for us: with close automatically
    with open(file_name) as file:
        for line in file:
            split_line = line.split('#')[0]
            command = split_line.strip()
​
if command == '':
    continue
​
num = int(command, 2)
​
print(f'{num:8b} is {num}')

​
except FileNotFoundError:
    print(f'{sys.argv[0]}: {sys.argv[1]} file was not found')
    sys.exit()
