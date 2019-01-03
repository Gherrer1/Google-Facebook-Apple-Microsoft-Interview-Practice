def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    table = {}
    for i in range(len(s1)):
        table[s1[i]] = table.get(s1[i], 0) + 1
        table[s2[i]] = table.get(s2[i], 0) - 1
    for count in table.values():
        if count != 0:
            return False
    return True

input1 = 'anagram'
input2 = 'nagaram'
print is_anagram(input1, input2) # expect True

input3 = 'rat'
input4 = 'car'
print is_anagram(input3, input4) # expect Flase