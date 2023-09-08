import sys

if len(sys.argv) != 2:
    print("Invalid usage. Correct: vivaldi_restore_urls [source file path]")
    sys.exit(1)

file_name = sys.argv[1]

fhand = open(file_name, "r")
contents = fhand.read()
fhand.close()

urls = set()

while True:
    if contents.find("urlForThumbnail") == -1:
        break

    start = contents.find("\"urlForThumbnail\"")
    start += 19

    contents = contents[start:]

    end = contents.find("\"")
    if (end > 5000 or end == -1):
        continue

    url = contents[:end]
    print(url)

    urls.add(url + "\n")

    contents = contents[end:]

fhand = open("./dist/" + file_name + ".txt", "w")
fhand.writelines(urls)
fhand.close()

print("Succesfully executed. Find decoded files with URLs in dist folder.")
