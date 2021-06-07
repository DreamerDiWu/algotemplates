{
    "Trie": {
        "input": "words: list[str], END mark, INFO, text to check",
        "output": "trie: dict, the INFO of text if text in words else None",
        "code": 
'''
trie = {}
for word in words:
    curr_root = trie 
    for c in word:
        curr_root = curr_root.setdefault(c, {})
    curr_root[END] = INFO 
curr_root = trie 
for c in text:
    if c in curr_root:
        curr_root = curr_root[c]
check_result = curr_root.get(END, None)
return trie, check_result
'''
    },
    "UnionFind": {
        "input": "n: int",
        "output": "class UF() with union, connected, count, find methods",
        "code": 
'''
class UF():
    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))

    def union(self, a ,b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b  （这里不要搞错成self.parent[a] = b)
            self.count -= 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)

    def count(self):
        return self.count

    def find(self, a):
        while a != self.parent[a]:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a
'''
    },
    "BFS": {
        "input": "source, target, edges(list of [ui, vi])",
        "output": "step of source -> target, if cannot reach return -1",
        "code": 
'''
adj = collections.defaultdict(list)
for u, v in edges:
    adj[u].append(v)
q = collections.deque([source])
visited = {source}
step = 0
while q:
    for i in range(len(q)):
        u = q.popleft()
        if u == target:
            return step
        for v in adj[u]:
            if v in visited:
                continue
            visited.add(v) 
            q.append(v)
    step += 1
return -1
'''
    },
    "BidirectionalBFS": {
        "input": "source, target, edges(list of [ui, vi])",
        "output": "step of source -> target, if cannot reach return -1",
        "code": 
'''
adj = collections.defaultdict(list)
for u, v in edegs:
    adj[u].append(v)
q1 = {source}
q2 = {target}
visited = set()
step = 0
while q1:
    temp = set()
    for u in q1:
        if u in q2:
            return step
        visited.add(u)
        for v in adj[u]:
            if v in visited:
                continue
            temp.add(v)
    step += 1
    q1, q2 = q2, temp
return -1
'''
    },
    "TopologySort": {
        "input": "n: int, edges(list of [ui, vi]) directional graph",
        "output": "'var=result': a list of topology sort, if cannot return []",
        "code": 
'''

indegree = [0] * n
adj = collections.defaultdict(list)
for u, v in edges:
    indegree[v] += 1
    adj[u].append(v)
q = collections.deque([i for i in range(n) if indegree[i] == 0])
result = []
while q:
    u = q.popleft()
    result.append(u)
    for v in adj[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)
if len(result) == n:
    return result
else:
    return []
'''
    },
    "Dijkstra": {
        "input": "n: int, source: int, edges = [[u, v, w]...]",
        "output": "'dist' which represents every node from source",
        "code": 
'''
dist = {i: float('Inf') for i in range(n)}
dist[source] = 0
adj = collections.defaultdict(list)
for u, v, w in edges:
    adj[u].append([v, w])
q = set(range(n))
def extract_min(q):
    u, d = -1, float('Inf')
    for i in q:
        if dist[i] < d:
            u, d = i, dist[i]
    if u != -1:
        q.remove(u)
    return u
while q:
    u, d = extract_min(q)
    if u == -1:
        break
    for v, w in adj[u]:
        dist[v] = min(dist[v], dist[u] + w)
'''   
    },
    "Dijkstra-pq": {
        "input": "n: int, source: int, edges = [[u, v, w]...]",
        "output": "dist of every node from source",
"code": 
'''
adj = collections.defaultdict(list)
for u, v, w in edges:
    adj[u].append([v, w])
dist = {i: float('Inf') for i in range(n)}
dist[source] = 0
visited = set()
pq = [[0, source]]
while pq:
    d, u = heapq.heappop(pq)
    if u in visited:
        continue
    visited.add(u)
    for v, w in adj[u]:
        dist[v] = min(dist[v], d + w)
        heapq.heappush(pq, [dist[v], v])
return dist
'''
    },
    "Bellman-Ford": {
        "input": "n: int, edges = [[u, v, w]...], source: int",
        "output": "dist of every node from source",
        "code": 
'''
dist = {i: float('Inf') for i in range(n)}
dist[source] = 0
for i in range(n-1):
    for u, v, w in edges:
        dist[v] = min(dist[v], dist[u] + w)
return dist
'''
    },
    "Bellman-Ford-K-path-length": {
        "input": "n: int, edges = [[u, v, w]...], source: int, K: int",
        "output": "dist of every node from source",
        "code": 
'''
dist = {i: float('Inf') for i in range(n)}
dist[source] = 0
for i in range(K):
    temp = dist.copy()
    for u, v, w in edges:
        temp[v] = min(dist[v], dist[u] + w)
    dist = temp
return dist
'''
    }
}
