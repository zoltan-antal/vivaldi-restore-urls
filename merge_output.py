import os
import time

file_names = sorted(os.listdir("./dist"))
file_names = list(filter(lambda file_name: file_name.find("merged") == -1, file_names))

urls = set()

for file_name in file_names:
    with open("./dist/" + file_name, "r") as fhand:
        for line in fhand:
            urls.add(line)

fhand = open("./dist/" + "merged-" + str(time.time()) + ".txt", "w")
fhand.writelines(urls)
fhand.close()

print("Succesfully executed. Find merged with all URLs in dist folder.")
