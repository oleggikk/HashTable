def addInHashTable(x: int):
    hash_table[x % hashLen].append(x)

def find(x: int):
    for now in hash_table[x % hashLen]:
        if now == x:
            return True
    return False

def delete(x):
    for i in range(len(hash_table[x % hashLen])):
        if x == hash_table[x % hashLen][i]:
            hash_table[x % hashLen][i] = hash_table[x % hashLen][-1]
            hash_table.pop(x % hashLen, hash_table[x % hashLen][-1])



print("input Hash Size: ")
hashLen = int(input())
hashKeys = []
for i in range(hashLen):
    hashKeys.append(i)
hash_table = dict.fromkeys(hashKeys)
print(hash_table)