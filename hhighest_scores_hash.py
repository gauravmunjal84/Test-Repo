scores = {}
result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split()
    scores[float(score)] = name
result_f.close()
for key in sorted(scores.keys(), reverse = True):
    print(scores[key]+ " : " +str(key))
#Test this comment
