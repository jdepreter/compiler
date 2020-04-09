import re

string = "hello\\nworld"


def replace(m):
    t_1 = m.string[m.regs[0][0]]
    t_2 = m.string[m.regs[0][1] - 1]
    print("h" + t_1 + t_2 + "elp")
    return

temp = re.sub(r'\\.', replace, string)
print(temp)