def is_precedent(char1, char2):
    precedence_dictionary = {}
    precedence_dictionary['+'] = 1
    precedence_dictionary['-'] = 1
    precedence_dictionary['*'] = 2
    precedence_dictionary['/'] = 2
    precedence_dictionary['^'] = 3
    if precedence_dictionary[char1] > precedence_dictionary[char2]:
        return True
    else:
        return False

def infix_to_postfix(inp_exp):
    output_exp = ''
    operator_stack = []
    for character in inp_exp:
        if character.isalpha():
            output_exp += character
        elif character == '(' or not operator_stack:
            operator_stack.append(character)
        elif character == ')':
            while operator_stack[-1] != '(':
                output_exp += operator_stack.pop()
            operator_stack.pop()
        else:
            while operator_stack and operator_stack[-1] != '(' and is_precedent(operator_stack[-1], character):
                output_exp += operator_stack.pop()
            operator_stack.append(character)
    while operator_stack:
        output_exp += operator_stack.pop()
    return output_exp


print(infix_to_postfix('(a+b)*c+d^f'))
