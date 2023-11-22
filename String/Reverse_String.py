class Solution:
    def reverseString(s: list[str]) -> None:
        return s[::-1]
        


string = [char for char in input().split(",")]
print(Solution.reverseString(string))