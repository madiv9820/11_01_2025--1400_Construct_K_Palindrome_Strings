#include <string>
#include <numeric>
using namespace std;

class Solution {
public:
    bool canConstruct(string s, int k) {
        // If the length of string `s` is less than `k`, it is impossible to form `k` substrings
        // (since we need at least one character for each substring)
        if(s.length() < k) return false;

        // Array to count the occurrences of each letter in the string (there are 26 lowercase letters)
        int letterCount[26] = {0};

        // Loop through the string and count how many times each character appears
        for(const char& ch: s) ++letterCount[ch-'a'];

        // Variable to count how many letters have an odd number of occurrences
        int letter_With_Odd_Count = 0;

        // Loop through the letter counts and check how many letters have an odd count
        for(int i = 0; i < 26; ++i) {
            // If the letter count is odd, increment the odd count
            if(letterCount[i] & 1) ++letter_With_Odd_Count;
        }

        // A palindrome can have at most one letter with an odd frequency (for the center of the palindrome)
        // To divide the string into `k` palindromic substrings, we need at most `k` odd-count letters
        return letter_With_Odd_Count <= k;
    }
};