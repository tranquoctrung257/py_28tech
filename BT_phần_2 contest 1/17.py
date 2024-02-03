c = input()
if c.islower(): # in ra true nếu là chữ in thường
    print("LOWER")
elif c.isupper(): # in ra true nếu là chữ in hoa
    print("UPPER")
elif c.isdigit(): # in ra true nếu là số
    print("DIGIT")
else: # in ra kí tự đặc biệt
    print("SPECIAL")