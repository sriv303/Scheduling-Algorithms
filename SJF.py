from JobClass import Job, joblist

p1 = Job(3,0) #creating job
p2 = Job(2,0)
p3 = Job(7,0)
p4 = Job(8,0)
p5 = Job(9,0)
p6 = Job(2,0)

jobl = joblist

jobl.sort(key = lambda x:x.burstTime)
print(*[x.burstTime for x in jobl])