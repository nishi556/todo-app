tasks = []

while True:
    task = input("タスクを入力（exitで終了）：")
    if task == "exit":
        break
    tasks.append(task)

print("タスク一覧")
for t in tasks:
    print("-", t)