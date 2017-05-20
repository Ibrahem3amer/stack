# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    #text = input('here')

    opening_brackets_stack = []
    # in case that unmatched char came in first place.
    #opening_brackets_stack.append('')
    empty = Bracket('',-1)
    opening_brackets_stack.append(empty)

    status = 'Success'
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opeining = Bracket(next, i)
            opening_brackets_stack.append(opeining)

        if next == ')' or next == ']' or next == '}':
            # first case: ]()
            #poping up from empty list
            if not Bracket.Match(opening_brackets_stack.pop(), next):
                status = i + 1
                break

    # Printing answer, write your code here
    #case {}(()
    if len(opening_brackets_stack) == 2 and status == 'Success':
        status = opening_brackets_stack[1].position + 1
    #case {}((
    elif len(opening_brackets_stack) > 2 and status == 'Success':
        status = opening_brackets_stack[len(opening_brackets_stack)-1].position + 1

    print(status)
