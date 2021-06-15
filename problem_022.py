
# read file into list
with open ("problem_22.txt", "r") as myfile:
    # remove quotes arround names and split on comma
    names = myfile.read().replace('"','').split(",")

# sort list
names.sort()

value = 0

for index in range(0,len(names)) :
    tmp_val = 0

    for char in names[index]:
        tmp_val += ord(char)-64

    value += tmp_val*(index+1)

print(value)
