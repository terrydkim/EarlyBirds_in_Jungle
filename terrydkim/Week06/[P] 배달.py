import heapq
def dijkstra(graph,distance):
    heap = []
    heapq.push(heap,(0,1))

def solution(N, road, K):
    INF = int(1e9)
    graph = [[]for i in range(N+1)]
    distance=[INF]*(N+1)
    for i in road:
        a, b, c = i
        graph[a].append((b,c))
        graph[b].append((a,c))
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return 