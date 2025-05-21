vowels = ['a', 'e', 'i', 'o', 'u', 'y'] 

def patternMatcher(pattern, source):
    string = ""
    for character in source:
        if character in vowels:
            string += "1"
        else:
            string += "0"

    count = 0
    patternLength = len(pattern)
    for i in range(len(string)):
        if string[i : i + patternLength] == pattern:
            count += 1
    return count

# pattern = "010"
# source = "amazing"
pattern = "11"
source = "aaaa"
print(patternMatcher(pattern, source))
