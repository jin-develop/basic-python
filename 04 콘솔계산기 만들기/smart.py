# 5 + 5 * 10 = 순차적으로 계산을 하게 만들기

operator = ["+", "-", "*", "/", "="]
user_input = "5 + 5 * 10"

string_list = []
lop = 0

for i, s in enumerate(user_input):
    if s in operator:
        if user_input[lop:i].strip() != "":
            string_list.append(user_input[lop:i])
            string_list.append(s)
            lop = i + 1

print(string_list)



