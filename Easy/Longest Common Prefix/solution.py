from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]

        prefixes = {}

        largest = 0
        response = ""
        for word in strs:
            for index, _ in enumerate(word):
                prefix = word[:index+1]
                if prefix in prefixes:
                    prefixes.get(prefix)

                    prefixes[prefix] += 1
                else:
                    prefixes[prefix] = 1

                if prefixes[prefix] > largest:
                    largest = prefixes[prefix]

                if prefixes[prefix] == largest and largest > 1:
                    response = prefix
        if not response:
            return ""
        elif prefixes[response] == len(strs):
            return response
        else:
            return ""
