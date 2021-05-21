
# state[i] : 현재 i 건물에 있을 경우의 수 
# 초기값(0초): 출발지가 정보관이므로 state[0] = 1
# 0: 정보, 1: 전산,  2: 미래, 3: 신앙, 4: 한경, 5: 진리
# 6: 학생회관, 7: 형님 
state = [1]+[0]*7

# adj[i] : i 건물과 인접한 건물리스트 
adj = [ [1, 2], [2, 3, 0], [3, 1, 0, 4], 
        [1, 2, 4, 5], [2,3,5,7], [3,4,6], 
        [5,7], [4,6]]

def f(i, cur_state):
    # 현재에서 1분이 지났을때 i 건물에 있을 경우의 수
    # == 현재 i 건물과 인접한 건물들의 경우의 수 합 
    return sum(cur_state[v] for v in adj[i])%1000000007

def nxt(state):
    nstate = [f(i, state) for i in range(8)] 
    return nstate

D = int(input())
for _ in range(D):
    state = nxt(state)

print(state[0])
