from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    visited=[False]*len(words)
    answer=0

    queue=deque([begin])  
    while queue:        
        v=queue.pop()
        if v==target:
            break
        for i in range(len(words)):
            if visited[i]==False and diff(words[i],v)==True:
                queue.append(words[i])
                visited[i]=True
        answer+=1    
    return answer

def diff(first,second):
    count=0
    for i in range(len(first)):
        if first[i]==second[i]:
            continue
        else:
            count+=1
        if count>=2:
            return False 
    return True  

"""
def dfs(current,tickets,used,answer):
    for i in range(len(tickets)):
        for j in range(len(tickets)):
            if (current==tickets[i][0] and used[i]==0):
                print(tickets[i]," 사용")
                used[i]=1
                answer.append(tickets[i][1])
                current=tickets[i][1]
                dfs(tickets[0],tickets,used,answer)"""