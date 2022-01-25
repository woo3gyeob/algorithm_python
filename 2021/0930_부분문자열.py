# 백준 16916 부분문자열
# https://www.acmicpc.net/problem/16916

whole_string = input()
part_string = input()
n = len(part_string)

def is_part_string():
    i = 0
    while i < len(whole_string) - n + 1:
        if whole_string[i] == part_string[0]:
            for j in range(i+1, i+n):
                if whole_string[j] != part_string[j-i]:
                    i = j-1
                    break
            else:
                return 1
        
        i += 1

    return 0

print(is_part_string())

################# KMP 알고리즘 ####################
def make_table(pattern):
    length = len(pattern)
    table = [0] * length
    j = 0

    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
            
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table


def kmp(parent, pattern):
    table = make_table(pattern)
    parent_length = len(parent)
    pattern_length = len(pattern)

    j = 0
    for i in range(parent_length):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == pattern_length - 1:
                return 1
            else:
                j += 1

    return 0


parent = input()
pattern = input()
print(kmp(parent, pattern))