# dictionary
    # {
    #   "小明": "18岁",
    #   "小芳": "20岁" 
    # }
    # iterable: list, dictionary, set
    # non-iterable: string, int, bool, tuple*
    # search: dic[key] => val
    # run time on search: O(1)


def WaitTime(lst):
    # key: friend number
    # val: [waitTime, ReceivedTime=-1]
    friends = {}
    timer = 0
    for type, num in lst:
        # 1. Receive
        # change ReceivedTime to current time
        if type == "R":
            if num in friends:
                friends[num][1] = timer
            else:
                friends[num] = [0, timer]
            timer += 1
        # 2. Send
        # change waitTime by current time - ReceivedTime
        # change ReceivedTime back to -1
        elif type == "S":
            friends[num][0] += timer - friends[num][1]
            friends[num][1] = -1
            timer += 1
        # 3. Wait
        # update timer
        else:
            num = int(num)
            timer += num - 1
    friends.sort()
    
    sorted_friends = sorted(friends.items())
    
    result = []
    for friend, val in sorted_friends:
        wait_time, ReceivedTime = val
        if ReceivedTime == -1:
            result.append((friend, wait_time))
        else:
            result.append((friend, -1))
    
    for i in range(len(result)):
        print(result[i][0] + " " + result[i][1])
            
def Take_input():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input())
    return lst

lst = Take_input()
WaitTime(lst)