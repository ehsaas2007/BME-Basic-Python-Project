sequence = input("Enter DNA Sequence: ").upper()

a_count = 0

t_count = 0

g_count = 0

c_count = 0

for letter in sequence:
    if letter == "A":
        a_count += 1
        
    if letter == "T":
        t_count+= 1
        
    if letter == "G":
        g_count += 1
        
    if letter == "C":
        c_count += 1
        
length = len(sequence)

at_content = ((a_count + t_count) / length) * 100

gc_content = ((g_count + c_count) / length) * 100

print("-----------------")
print("DNA SEQUENCE REPORT")
print('-----------------')

print("Length", length)

print()

print("A Count: ", a_count)
print("T Count: ", t_count)
print("G Count: ", g_count)
print("C Count: ", c_count)

print()
print("GC Content: ", round(gc_content, 2), "%")
print()
print("AT Content: ", round(at_content, 2), "%") 






















        
        
    