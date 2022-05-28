class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total_result = 0
        prev_value = 0
        array_of_romans = [i for i in s]
        for roman in array_of_romans:
            current_value = roman_int[roman]
            if current_value > prev_value:
                total_result += current_value - prev_value
                total_result -= prev_value
            else:
                total_result +=current_value
            prev_value = current_value
        return total_result