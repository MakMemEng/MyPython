# データの取得
rock_star = []
with open('input/rock_star.csv', encoding='utf-8') as f:
    for row in f:
        name = row.strip()
        rock_star.append(name)
# 並び替え
sorted_rock_star = sorted(rock_star)
# 表示
print(sorted_rock_star[:5])
