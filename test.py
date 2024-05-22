def naive_replace_char(original_string, target_char, replacement_char):
    result = ''
    for char in original_string:
        if char == target_char:
            result += replacement_char
        else:
            result += char
    return result

# Example usage:
original = "hello world"
target = "o"
replacement = "x"
#print(naive_replace_char(original, target, replacement))

test = "ali"
print(test[0]+="j")