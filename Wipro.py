#
# Your previous Java content is preserved below:
#
# /**
#
# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:
#
# Input: s = ""
# Output: 0
#
# */
#
# import java.io.*;
# import java.util.*;
#
# class Solution {
#   public static void main(String[] args) {
#     Solution obj = new Solution();
#     obj.lengthOfLongestSubstring("aabcashdbbad");
#   }
#
#   public int lengthOfLongestSubstring(String s) {
#     return 0;
#   }
# }
#

text = 'pwwkew'
start = 0
end = 0
letterDict = {}
maxLength = 0
length = 0
for letter in text:
    if letter in letterDict:
        letterDict = {}
        start = text.index(letter)
        end = text.index(letter)
        length = 1
        letterDict[letter] = 1
    else:
        letterDict[letter] = 1
        end = text.index(letter)
        length = length + 1
    if (length > maxLength):
        maxLength = length
        stringstart = start

print(maxLength)
print(text[stringstart:stringstart + maxLength:1])



