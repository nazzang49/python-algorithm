tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
v = [False] * len(tickets)

ans = ['JFK'] # departure is fixed with JFK
def dfs(departure):
    ans.append(departure)
    for i in range(len(tickets)):
        if not v[i] and tickets[i][0] == departure:
            v[i] = True
            dfs(tickets[i][1])

for i in range(len(tickets)):
    if tickets[i][0] == 'JFK':
        v[i] = True
        dfs(tickets[i][1])
        break # answer is only one path

print(ans)