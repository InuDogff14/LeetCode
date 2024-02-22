class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        joined_int = int(''.join(map(str, digits)))
        joined_int += 1
        return [int(digit) for digit in str(joined_int)]