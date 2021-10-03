from collections import deque
def solution(bridge_length, weight, truck_weights):
    #bridge_lenth = 다리의 길이 / 올라갈 수 있는 트럭의 갯수  1 이상 10,000 이하
    #weight = 다리가 버틸 수 있는 무게                      1 이상 10,000 이하
    #truck_weights = 트럭 각각의 무게 / 순서대로 건너야 함    길이 1 이상 10,000 이하, 1 이상 weight 이하
    #answer = 걸리는 최소 시간 (초)                        
    
    answer = 0
    queue=deque()
    for truck in truck_weights:        
        queue.append(truck)
    count=0
    q = queue.popleft()
    print(queue)
    

    """
    while(queue):
        current=queue.popleft()
        while(count<=weight):
            if queue[0]+current > weight:
                count+=1
                continue
            else:
                count+=1
                
        current=queue.popleft()
        
            
        answer+=1
        break
        """
    return answer
