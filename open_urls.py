import sys
import webbrowser
import time

if len(sys.argv) != 3:
    print("Invalid usage. Correct: open_urls [source file path] [seconds delay]")
    sys.exit(1)

file_name = sys.argv[1]
sleep_seconds = int(sys.argv[2])

with open(file_name, "r") as fhand:
    for line in fhand:
        url = line.strip()
        webbrowser.open_new_tab(url)
        time.sleep(sleep_seconds)

print("Successfully executed. All URLs have been opened.")
