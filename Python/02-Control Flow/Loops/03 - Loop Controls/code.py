# -------------------------------
# Loop Control Statements
# -------------------------------

# break: exits the loop prematurely
print("========== BREAK Example ==========")
for i in range(10):
    if i == 5:
        break
    print(i)

# continue: skips the current iteration and continues with next
print("========== CONTINUE Example ==========")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass: null operation, does nothing but syntactically required
print("========== PASS Example ==========")
for i in range(5):
    if i == 3:
        pass
    print(i)

