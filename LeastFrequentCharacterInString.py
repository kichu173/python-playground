string = "pythonprogramming"
freq = {} # dictionary
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)

leastFrequentChar =  []
for i in freq:
    if freq[i] == 1:
        leastFrequentChar.append(i)

print("Least Frequent Character in the string is:")
print(leastFrequentChar) # ['y', 't', 'h', 'a', 'i']