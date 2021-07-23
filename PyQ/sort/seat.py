book = {}
with open('input/book.csv','r', encoding='utf-8') as f:
    for row in f:
        # データの取得
        columns = row.rstrip().split(',')
        name = columns[0]
        seat = columns[1]
        
        # 辞書の作成
        book[seat] = name
        
# 並び替え
book_seat = sorted(book.items())

# 表示
for seat, name in book_seat:
    print(seat, name)