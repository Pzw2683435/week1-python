with open("knowledge.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"总共有 {len(lines)} 行")
print(f"第 1 行是：{lines[0]}")
print(f"第 2 行是：{lines[1]}")
headings = [line for line in lines if line.startswith("#")]
print(f"有 {len(headings)} 个标题")
for h in headings[:5]:
    print(h.strip())