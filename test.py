grades = {
    "数学": 85,
    "英语": 92,
    "Python": 78
}

# 补两句：算出平均分并打印
# 提示：sum(grades.values()) 求和，len(grades) 算个数
total=sum(grades.values())
num=len(grades)
ave=total/num
print(f"{ave:.2f}")