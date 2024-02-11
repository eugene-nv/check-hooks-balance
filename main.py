def hooks_balance(string: str) -> bool or str:
    '''The function checks the balance of parentheses in a string.'''

    start_hooks = '{[('
    finish_hooks = '}])'

    result = []

    for hook in string:
        if hook in start_hooks:
            result.append(hook)
        elif hook in finish_hooks:
            if hook == ']' and '[' in result:
                result.remove('[')
            elif hook == ')' and '(' in result:
                result.remove('(')
            elif hook == '}' and '{' in result:
                result.remove('{')
            else:
                result.append(hook)

    if string == '':
        return 'String is empty'
    else:
        if result == []:
            return 'Hooks is balanced'
        elif result != []:
            return 'Hooks is not balanced'


