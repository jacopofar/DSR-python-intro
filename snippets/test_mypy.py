def count_vowels(txt: str) -> int:
    total: int = 0
    for char in txt:
        if char in 'aeiouAEIOU':
            total += 1
    return total

print(count_vowels("hello"))
# this works even though the type is wrong
# and the comparison gives wrong results
print(count_vowels(['hel', 'lo']))
