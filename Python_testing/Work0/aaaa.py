def xxx():
    for i in range(0,11):
        print("开始操作")
        yield i  # 相当于return i，同时记录了上一次的执行位置，如果yield后面没有内容的话，就会返回none
        print("结束操作")
a= xxx()
# 只进行打印操作时，必须加next，不然不输出
print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# # 循环
# for c in a:
#     print(c)