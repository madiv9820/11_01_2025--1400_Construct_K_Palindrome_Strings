from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If the length of the string `s` is less than `k`, 
        # it's impossible to form `k` palindromic substrings.
        # Hence, we return True because we can always construct 1 or more palindromes 
        # as long as the string length is greater than or equal to `k`.
        if len(s) < k: 
            return True

        # Count the number of characters in `s` that appear an odd number of times.
        # We use Counter to get the frequency of each character in the string.
        # Then we sum the number of odd frequencies by checking each frequency value.
        # (1 if the frequency is odd, otherwise 0).
        letters_With_Odd_Count = sum(1 if freq & 1 else 0 for freq in Counter(s).values())
        
        # A palindrome can have at most one character with an odd frequency.
        # If the number of characters with an odd frequency is less than or equal to `k`, 
        # it means we can form `k` palindromic substrings, so we return True.
        return letters_With_Odd_Count <= k