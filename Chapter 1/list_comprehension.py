#Regular List

result = []

for i in range(0,21):
    if i % 2 == 0:
        result.append(i)
print(result)

# List creation using List Comprehensive syntax
results=[i for i in range(0,21) if i % 2 == 0]
print(results)

'''Both should create a new List, but way of creating a list is different
the comprehensive syntax is more compact
Rules: first define the iterator variable, i 
        then write the for loop as usual,
        at the end, use the condition when i should be added to new List '''