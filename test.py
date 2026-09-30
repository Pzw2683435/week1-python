with open("knowledge.md", "r", encoding="utf-8") as f:
    text = f.read()

# 先切块（你刚学过的）
chunk_size, overlap = 200, 50
chunks = []
start = 0
while start < len(text):
    end = start + chunk_size
    chunks.append(text[start:end])
    if end >= len(text):
        break
    start = end - overlap

# 提问
question = "为什么要用RAG"

# 给每一块打分：它和问题有多少共同的字
scored = []
for chunk in chunks:
    common = set(question) & set(chunk)     # 共同的字
    score = len(common)
    scored.append((score, chunk))

# 按分数从高到低排序
scored.sort(reverse=True)

# 只看前 3 名
for rank, (score, chunk) in enumerate(scored[:3], start=1):
    print(f"第{rank}名  得分 {score}")
    print(f"  {chunk[:50]}...")
    print()