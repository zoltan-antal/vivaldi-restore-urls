import sys

if len(sys.argv) != 2:
    print("Invalid usage. Correct: vivaldi_restore_urls [source file path]")
    sys.exit(1)

file_name = sys.argv[1]

fhand = open(file_name, "r")
contents = fhand.read()
fhand.close()

urlList = []

while True:
    if contents.find("urlForThumbnail") == -1:
        break

    start = contents.find("\"urlForThumbnail\"")
    start += 19

    contents = contents[start:]

    end = contents.find("\"vivaldi_tab_muted\"")
    if (end > 5000 or end == -1):
        end = contents.find("\"thumbnail\"")
    if (end > 5000 or end == -1):
        continue
    end -= 2

    print(contents[:end])

    urlList.append(contents[:end])
    urlList.append("\n")

    contents = contents[end:]

fhand = open("./decoded/" + file_name + ".txt", "w")
fhand.writelines(urlList)
fhand.close()

print("Succesfully executed. Find decoded files with URLs in dist folder.")
