import sys

if len(sys.argv) != 2:
    print("Invalid usage. Correct: vivaldi_restore_urls [source file path]")
    sys.exit(1)

file_name = sys.argv[1]

fhand = open(file_name, "r")
contents = fhand.read()
fhand.close()

urlList = []


fhand = open("./decoded/" + file_name + ".txt", "w")
fhand.writelines(urlList)
fhand.close()
