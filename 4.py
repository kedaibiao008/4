import itertools

# 生成所有可能的组合
combinations = []
for first_char in 'abcdefghijklmnopqrstuvwxyz':
    for char_2 in 'abcdefghijklmnopqrstuvwxyz0123456789':
        for char_3 in 'abcdefghijklmnopqrstuvwxyz0123456789':
            for char_4 in 'abcdefghijklmnopqrstuvwxyz0123456789':
                combination = first_char + char_2 + char_3 + char_4
                combinations.append(combination)

# 过滤出符合条件的组合
filtered_combinations = [combo for combo in combinations if any(combo[i] == combo[i+1] for i in range(3))]

# 将符合条件的组合保存到文件
with open('4l.txt', 'w') as file:
    file.write('\n'.join(filtered_combinations))
