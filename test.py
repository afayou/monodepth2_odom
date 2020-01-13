file = open("./splits/odom/test_files_10.txt", "r")
new_file = open("./splits/odom/test_files_10_new.txt", "w")
lines = file.readlines()
index = []
for i in range(12):
    index.append(str(i))
print(index)
for row in lines:
    data = row.split()
    if str(data[1]) not in index:
        print(data[1])
        new_file.write(row)
new_file.close()



