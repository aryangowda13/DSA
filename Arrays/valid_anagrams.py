# Check if two strings are anagrams of each other
def isAnagram(s, t):
    # If the lengths of the strings are not equal, they cannot be anagrams
    if len(s) != len(t):
        return False
    # Create a dictionary to count the occurrences of each character in the first string
    count = {}

    for char in s:
     # Increment the count for each character in the first string   
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
    
        count[char] -= 1

        if count[char] < 0:
            return False

    return True


s = "silent"
t = "listen"

print(isAnagram(s, t))