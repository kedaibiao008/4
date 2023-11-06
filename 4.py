import itertools

# 定义满足条件的字符集
characters = "abcdefghijklmnopqrstuvwxyz0123456789"

# 用于存储满足条件的数据
output_data = []

def generate_combinations(prefix, length):
    if length == 0:
        output_data.append(prefix)
        return
    for char in characters:
        generate_combinations(prefix + char, length - 1)

# 生成所有可能的组合
generate_combinations("", 4)

# 过滤并保存符合条件的组合
filtered_data = [combo for combo in output_data if (combo[0].islower() and combo.count('b') == 3) or (combo[0].islower() and combo.count('a') == 3)]

# 输出数据到文件
with open("4l.txt", "w") as file:
    file.write("\n".join(filtered_data))

print(f"已生成并保存 {len(filtered_data)} 条数据到 4l.txt 文件。")
