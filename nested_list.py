# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([score, name])
ans = []
records.sort()        
least = records[0][0]
flag = False
for i in range(1,len(records)):
    if records[i][0] > least:
        flag = True
        for j in range(i, len(records)):
            if records[i][0] == records[j][0]:
                ans.append(records[j])
    if flag:
        break
if flag == False:
    print(records[0][1])
for i in range(len(ans)):
    print(ans[i][1])       