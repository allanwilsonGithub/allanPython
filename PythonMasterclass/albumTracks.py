imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

title, album, year, tracks = imelda

print("#" * 30)
print("Title: " + title + "\n" + "Album: " + album + "\n" + "Year: " + str(year) + "\n")
print("Tracks:")
for i in range(0, len(tracks)):
    print("\t" + str(tracks[i][0]) + "\t" + str(tracks[i][1]))