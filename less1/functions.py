def get_sum(one, two, delimiter='&'):
    fraza = one + delimiter + two
    return fraza

s = get_sum('learn', 'python').upper()
print(s)