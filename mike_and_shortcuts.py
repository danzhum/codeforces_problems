def calculate_energy(p1, p2):
    return p2-p1

def solution(num_intersections, shortcuts):

    if num_intersections == 1:
        return 0

    energies = []

    distances = [-1]*num_intersections
    distances[0] = 0
    q = []
    q.append(0)

    while len(q) > 0:
        print("Before q", q)
        k = q[0]
        q = q[1:]
        print("After q", q)

        if k+1 <= num_intersections-1 and distances[k+1] == -1:
            distances[k+1] = distances[k]+1
            q.append(k+1)
        if distances[shortcuts[k]] == -1:
            distances[shortcuts[k]] = distances[k] + 1
            q.append(shortcuts[k])

    return distances

    # graph = {}
    # for i in range(1, len(shortcuts)+1):
    #     graph[i] = []
    #     graph[i].append(i)
    #     if i != len(shortcuts):
    #         graph[i].append(i+1)
    #     if shortcuts[i-1] != i and shortcuts[i-1] not in graph[i]:
    #         graph[i].append(shortcuts[i-1])
    # print(graph)

    # for i in range(num_intersections):
    #     energies.append()

    return energies


inputData = []
while True:
    
    data = input()
    inputData.append(data)
    if len(inputData) == 2:
        break

print(inputData)

print("Done")
N = int(inputData[0])
shortCuts = []

for i in inputData[1]:
    if i != " ":
        shortCuts.append(int(i)-1)
print(shortCuts)
print(solution(N, shortCuts))

output = solution(N, shortCuts)
print("Output: ", output)
for s in output:
    print(s)