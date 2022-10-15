joblist = []
class Job: #job container
    def __init__(self, burstTime, arrivalTime):
        self.burstTime = burstTime
        self.arrivalTime = arrivalTime
        joblist.append(self)