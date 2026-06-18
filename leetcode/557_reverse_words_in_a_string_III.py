# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, reverse each word, and join them back
        return " ".join([word[::-1] for word in s.split(" ")])
