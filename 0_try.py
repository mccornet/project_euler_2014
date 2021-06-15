from os import rename, listdir

fnames = listdir('.')

for name in fnames :
    if name.startswith("problem_") and name.endswith(".py") :

        # start digit is name[7]
        i = 8

        while True :
            if name[i].isdigit() :
                i += 1
            else:
                break

        # we should have the segments now
        new_name = name[:8] + name[8:i].zfill(3) + name[-len(name)+i:]

        rename(name, new_name)





