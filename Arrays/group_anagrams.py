# importing List from typing module for type hinting
from typing import List

class Solution:
    # Function to group anagrams from a list of strings
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Creating a dictionary to hold groups of anagrams
        groups = {}

        for s in strs:
            # Sorting the string to create a key for the anagram group
            key = ''.join(sorted(s))

            if key not in groups:
                # If the key is not in the dictionary, initialize it with an empty list
                groups[key] = []
             # Appending the original string to the corresponding anagram group
            groups[key].append(s)

        return list(groups.values())

    # Input
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Create object and call function
solution = Solution()
answer = solution.groupAnagrams(strs)

# Print output
print(answer)
    