
def comparison(string_one, string_two):
    if isinstance(string_one, str) and isinstance(string_two, str):    
        if string_one == string_two:
            return 1
        else:
            if string_two =='learn':
               return 3
            else:
                if len(string_one) > len(string_two):
                    return 2
    else:
        return 0


print(comparison(1244, 123))
print(comparison('привет', 'привет'))
print(comparison('приветики', 'привет'))
print(comparison('привет', 'learn'))
print(comparison('привет', 123))
print(comparison('learn', 'привет'))
print(comparison('learn', 'learn'))