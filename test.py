file = open("./splits/odom/val_files.txt", "r")
new_file = open("./splits/odom/val_files_new.txt", "w")
lines = file.readlines()
index = []
for i in range(11):
    index.append(str(i))
print(index)
for row in lines:
    data = row.split()
    if str(data[1]) not in index:
        print(data[1])
        new_file.write(row)
new_file.close()



