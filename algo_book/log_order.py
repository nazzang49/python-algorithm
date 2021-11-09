logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

letters = []
digits = []

for log in logs:
    if log.split()[1].isdigit(): # isdigit => str(1) possible
        digits.append(log)
    else:
        letters.append(log)

letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # double key => first and second rule
print(letters + digits)