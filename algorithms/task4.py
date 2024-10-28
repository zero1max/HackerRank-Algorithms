n = int(input())
scores = set()
dict = {}
for x in range(n):
    name = input()
    score = float(input())
    scores.add(score)
    dict[name] = score

scores = list(scores)
scores.sort()

names = []
for k, v in dict.items():
    if v == scores[1]:
        names.append(k)

names.sort()
for x in names:
    print(x)

