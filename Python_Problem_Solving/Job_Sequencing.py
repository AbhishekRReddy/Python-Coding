'''
https://www.codingninjas.com/codestudio/problems/job-sequencing-problem_1169460?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
'''

def jobScheduling(jobs):
    
    jobs.sort(key = lambda x : x[1],reverse = True)
    maxi = max(jobs, key = lambda x:x[0])[0]
    tracker = {i:-1 for i in range(maxi)}
    profit = 0
    for job in jobs:
        x = job[0]
        while x > 0:
            x -= 1
            if tracker[x] == -1:
                tracker[x] = 1
                profit += job[1]
                break
    return profit
