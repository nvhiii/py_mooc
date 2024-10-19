# The exercise template contains the function balanced_brackets which takes a string as its argument. It checks if the round brackets, or parentheses, within the string are balanced. That is, for each opening bracket ( there should be a closing bracket ), and all pairs of brackets should be matched in order, i.e. the bracket pairs must not be crossed.

# True
# False
# False
# False

# Please expand the function so that it also works with square brackets []. The function should also ignore all characters which are not brackets () or []. The different types of brackets must be matched correctly in order.

# Please have a look at the examples below::

# ok = balanced_brackets("([([])])")
# print(ok)

# ok = balanced_brackets("(python version [3.7]) please use this one!")
# print(ok)

# # this is no good, the closing bracket doesn't match
# ok = balanced_brackets("(()]")
# print(ok)

# # different types of brackets are mismatched
# ok = balanced_brackets("([bad egg)]")
# print(ok)

# NB: the function only needs to handle entirely nested brackets. The string (x + 1)(y + 1) should produce False as the brackets are not nested within each other.

# True
# True
# False
# False

def balanced_brackets(my_string: str):
    # first get rid of all non () or [] string charas
    paren = "()[]"
    valid = [chara for chara in my_string.strip() if chara in paren]
    new_str = "".join(valid)
    # valid_rounds = [chara for chara in new_str if chara in "()"]
    # valid_squares = [chara for chara in new_str if chara in "[]"]

    if len(new_str) == 0:
        return True
    if (new_str[0] == '(' and new_str[-1] == ')') or (new_str[0] == '[' and new_str[-1] == ']'):
        return balanced_brackets(my_string[1:-1])

    # remove first and last character
    return False