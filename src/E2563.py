count = int(input())
papers = [[0]*100 for i in range(100)]
result = 0

# for i in range(paper):
#     papers[i] = list(map(int, input().split()))
#
# for i in range(paper):
#     for j in range(i+1, paper):
#         if papers[i][0] < papers[j][0] < papers[i][0] + 10:
#             x = papers[i][0] + 10 - papers[j][0]
#             if papers[i][1] < papers[j][1] < papers[i][1] + 10:
#                 y = (papers[i][1] + 10) - papers[j][1]
#                 result += x * y
#             elif papers[j][1] < papers[i][1] < papers[j][1] + 10:
#                 y = (papers[j][1] + 10) - papers[i][1]
#                 result += x * y
#         if papers[j][0] < papers[i][0] < papers[j][0] + 10:
#             x = papers[j][0] + 10 - papers[i][0]
#             if papers[i][1] < papers[j][1] < papers[i][1] + 10:
#                 y = (papers[i][1] + 10) - papers[j][1]
#                 result += x * y
#             elif papers[j][1] < papers[i][1] < papers[j][1] + 10:
#                 y = (papers[j][1] + 10) - papers[i][1]
#                 result += x * y
#
# print(paper*100 - result)

for i in range(count):
    paper = list(map(int, input().split()))
    for j in range(10):
        for k in range(10):
            papers[paper[0] + j][paper[1] + k] = 1

for i in range(100):
    for j in range(100):
        result += papers[i][j]

print(result)