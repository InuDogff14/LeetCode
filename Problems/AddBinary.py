class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = int(a, 2) + int(b, 2)  # 二進数を整数に変換して和を計算
        return bin(sum)[2:]  # 二進数に変換し、先頭の '0b' を除去