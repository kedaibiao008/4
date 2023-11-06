import itertools

# 生成所有可能的组合
combinations = []
for first_char in 'abcdefghijklmnopqrstuvwxyz':
    for chars234 in itertools.product('abcdefghijklmnopqrstuvwxyz0123456789', repeat=3):
        combination = first_char + ''.join(chars234)
        combinations.append(combination)

# 过滤符合条件的组合
filtered_combinations = [comb for comb in combinations if any(comb[i] == comb[i+1] == comb[i+2] for i in range(2))]

# 将符合条件的组合保存到文件
with open('4l.txt', 'w') as file:
    for comb in filtered_combinations:
        file.write(comb + '\n')

print(f'已保存 {len(filtered_combinations)} 个符合条件的组合到 4l.txt 文件.')
