import sys

if len(sys.argv) != 2:
    print("Invalid usage. Correct: vivaldi_restore_urls [source file path]")
    sys.exit(1)

file_name = sys.argv[1]
