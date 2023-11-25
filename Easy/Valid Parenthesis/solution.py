class Solution:
    def isValid(self, s: str) -> bool:

        first = s[0]

        if first == "}" or first == ")" or first == "]":
            return False

        stack = []

        for letter in s:

            if letter == "{" or letter == "(" or letter == "[":
                stack.append(letter)

            if letter == "}" or letter == ")" or letter == "]":
                if not stack:
                    return False
                if letter == "}" and (stack[-1], letter) == ("{", "}"):
                    stack.pop()
                elif letter == ")" and (stack[-1], letter) == ("(", ")"):
                    stack.pop()
                elif letter == "]" and (stack[-1], letter) == ("[", "]"):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
