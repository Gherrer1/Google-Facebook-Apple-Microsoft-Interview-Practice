def partition_labels(string):
    retVal = []
    last = {}
    for i in range(len(string) - 1, -1, -1):
        if last.get(string[i]) == None:
            last[string[i]] = i
    start_index = 0
    target = string[0]
    for i in range(0, len(string)):
        letter = string[i]
        if i == last[target]:
            distance = i + 1 - start_index
            retVal.append(distance)
            start_index = i + 1
            if start_index < len(string):
                target = string[start_index]
            continue
        elif last[letter] > last[target]:
            target = letter
    return retVal

input1 = 'ababcbacadefegdehijhklij'
print partition_labels(input1) # expect [9, 7, 8]
input2 = 'abc'
print partition_labels(input2) # expect [1, 1, 1]
input3 = 'agljdlghdha'
print partition_labels(input3) # expect [11]
input4 = 'abbccddeefafhhiijjkkf'
print partition_labels(input4) # expect [21]