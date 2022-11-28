# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
roman_values_in_dict = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        
        idx = 0
        while idx < len(s):
            if idx+1 < len(s) and roman_values_in_dict[s[idx+1]] > roman_values_in_dict[s[idx]]:
                answer = answer + (roman_values_in_dict[s[idx+1]] - roman_values_in_dict[s[idx]])
                idx = idx + 2
            else:
                answer = answer + roman_values_in_dict[s[idx]]
                idx = idx + 1
       
        return answer


if __name__ == "__main__":
    input_string = "III"
    
    answer = Solution().romanToInt(s=input_string)
    
    print(f"Roman: {input_string} is {answer} in Integer")
