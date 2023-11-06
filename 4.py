import itertools

# 定义字符集
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# 用于存储满足条件的数据
output_data = []

# 生成所有可能的组合
combinations = itertools.product(characters, repeat=4)

for combo in combinations:
    combo_str = ''.join(combo)
    if (combo_str[0] == 'a' and combo_str[1:].count('b') == 3) or (combo_str[0] == 'a' and combo_str[1:].count('a') == 3):
        output_data.append(combo_str)

# 输出数据到文件
with open("4l.txt", "w") as file:
    file.write("\n".join(output_data))

print(f"已生成并保存 {len(output_data)} 条数据到 4l.txt 文件。")
