text = input("Enter an IP address: ")

# 123.456.789.123

segments = 1
count = 0
current_segment = 1

for i in range(0, len(text)):
    if text[i] == "." and i != 0 and i != len(text)-1:
        segments += 1
    if text[i] in "0123456789":
        count += 1
    elif text[i] == ".":
        print("Segment {0} has {1} characters.".format(str(current_segment), str(count)))
        count = 0
        current_segment += 1
    if i == len(text)-1:
        print("Segment {0} has {1} characters.".format(str(current_segment), str(count)))

print("There are {0} segments".format((str(segments))))
