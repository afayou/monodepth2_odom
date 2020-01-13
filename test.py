file = open("./splits/odom/test_files_09.txt", "r")
new_file = open("./splits/odom/test_files_09.txt", "w")
lines = file.readlines()
data = []
del_index = []
for row in lines:
    if '0' not in row or '1' not in row or '2' not in row or '3' not in row or '4' not in row or '5' not in row or \
            '6' not in row or '7' not in row or '8' not in row or '9' not in row or '10' not in row:
        new_file.write(row)
new_file.close()



