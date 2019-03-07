

class Node:
    def __init__(self, weight):
        self.weight = weight
        self.status = 0


def solution(bridge_length, weight, truck_wheights):
    ing_trucks = []
    trucks = []
    ing_wheight = 0
    answer = 0
    for truck_wheight in truck_wheights:
        trucks.append(Node(truck_wheight))
    while True:
        if len(trucks) == 0 and len(ing_trucks) == 0:
            break
        if len(ing_trucks) != 0 and ing_trucks[0].status == bridge_length:
            # 다리를 빠져 나가는 중. 이때는 중량에서 제외된다.
            ing_wheight -= ing_trucks[0].weight
            ing_trucks.pop(0)
        if len(trucks) != 0 and ing_wheight + trucks[0].weight <= weight:
            # truck 이 다리에 새로 오르는 경우
            ing_trucks.append(trucks[0])
            ing_wheight += trucks[0].weight
            trucks.pop(0)
        for truck in ing_trucks:
            truck.status += 1
        answer += 1
    return answer


def test_solution():
    assert solution(2, 10, [7]) == 3
    assert solution(2, 10, [7, 4, 5, 6]) == 8
    assert solution(100, 100, [10]) == 101
    assert solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 110


test_solution()

n, bridge_length, weight = map(int, input().split())
truck_weights = list(map(int, input().split()))
print(solution(bridge_length, weight, truck_weights))
