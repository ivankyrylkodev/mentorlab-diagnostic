lines = 0
empty_lines = 0
words = 0
longest_line = 0
comment_lines = 0

file_name = input('File name: ')
with open(file_name, encoding="utf-8") as f:
    for line in f:
        lines += 1
        if line.strip() == '':
            empty_lines += 1
        if line.strip().startswith("#"):
            comment_lines += 1
        else:
            words += len(line.split())
        longest_line = max(longest_line, len(line.replace("\n", "")))



if lines > 0:
    print("Lines: " + str(lines))
    print("Empty lines: " + str(empty_lines))
    print("Comment lines: " + str(comment_lines))
    print("Words: " + str(words))
    print("Longest line: " + str(longest_line) + " characters")
else:
    print("The file is empty.")