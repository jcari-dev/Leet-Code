class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        number = 0
        skip_next = False
        last_index = len(s) - 1
        for index, letter in enumerate(s):

            if skip_next:
                skip_next = False
                continue
            if letter in ["I", "X", "C"] and index != last_index:
                if letter == "I":
                    if s[index+1] == "V":
                        number += 4
                        skip_next = True
                        continue
                    if s[index+1] == "X":
                        number += 9
                        skip_next = True
                        continue
                if letter == "X":
                    if s[index+1] == "L":
                        number += 40
                        skip_next = True
                        continue
                    if s[index+1] == "C":
                        number += 90
                        skip_next = True
                        continue
                if letter == "C":
                    if s[index+1] == "D":
                        number += 400
                        skip_next = True
                        continue
                    if s[index+1] == "M":
                        number += 900
                        skip_next = True
                        continue
            number += roman_dictionary.get(letter)

        return number
