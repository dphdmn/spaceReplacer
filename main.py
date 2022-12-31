counterchar = ' '
replacedchar = '/'
counterconst = 5
with open("input.txt", 'r') as f:
    lines = f.readlines()
newlines = []
for line in lines:
    chars = list(line)
    newline = ""
    cntr = 0
    checked = False
    for c in chars:
        addc = c
        if c == counterchar:
            cntr = cntr + 1
            checked = False
        if cntr % counterconst == 0 and cntr != 0 and not checked:
            addc = replacedchar
            checked = True
        newline = newline + addc
    newlines.append(newline)
with open("output.txt", 'w') as f:
    f.writelines(newlines)
