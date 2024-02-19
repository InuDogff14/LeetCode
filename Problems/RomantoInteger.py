class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        prev_value = 0
        roman_dict = {
        "I": 1, "V": 5, 'X': 10, 'L': 50,
         'C': 100, 'D': 500, 'M': 1000
        }

        for char in reversed(s):
            int_val = roman_dict[char]
            if int_val < prev_value:
                total -= int_val
            else:
                total += int_val
            prev_value = int_val

        return total