from JobClass import Job, joblist

p1 = Job(3,0) #creating job
p2 = Job(2,1)
p3 = Job(7,2)
p4 = Job(8,3)
p5 = Job(9,6)
p6 = Job(2, 5)

jobl = joblist

jobl.sort(key=lambda x: x.arrivalTime) #sorting jobl based on arrivalTime
print(*[x.arrivalTime for x in jobl])

def WaitingTime(orderlist): #prints out waiting time for each joib
    elapsed = 0
    for i in range(0, len(orderlist)): #makes sure to start first job at 0
        if i == 0:
            print(elapsed)
        else:
            elapsed += orderlist[i-1].burstTime #adds previous burstTime
            print(elapsed)
    return elapsed #returns total time elapsed after all jobs complete

totalElapsed = WaitingTime(jobl)

def AverageWaitingTime(totalWaitTime):
    return round(totalWaitTime/len(jobl), 2)
    #calculates avg wait by finding total time elapsed and dividing by no. jobs

print(AverageWaitingTime(totalElapsed))