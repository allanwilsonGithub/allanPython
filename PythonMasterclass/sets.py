string = "Here we go again on our own!"
print(string)

setString = set(string)
print(setString)
vowels = set("a" "e" "i" "o" "u")
print(vowels)
setString.difference_update(vowels)
print(setString)
extras = set("!" " ")
setString.difference_update(extras)
print(setString)
