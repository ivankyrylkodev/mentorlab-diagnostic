lines = 0
empty_lines = 0
words = 0
longest_line = 0

file_name = input('File name: ')
f = open(file_name, encoding="utf-8")

if len(f.read()) > 0:
    for line in f:
        lines += 1
        print(lines)
        if line.strip() == '':
            empty_lines += 1
        words += len(line.split())
        longest_line = max(longest_line, len(line))

        print("Lines: " + str(lines))
        print("Empty lines: " + str(empty_lines))
        print("Words: " + str(words))
        print("Longest line: " + str(longest_line) + " characters")
else:
    print("The file is empty.")


