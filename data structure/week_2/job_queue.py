# python3
import heapq
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []

    pq = [ Worker(i) for i in range(n_workers)]
    for j in range(len(jobs)):
        f_thread = heapq.heappop(pq)
        result.append(AssignedJob(f_thread.id, f_thread.nextFreeTime))
        f_thread.nextFreeTime += jobs[j]
        heapq.heappush(pq, f_thread)
    return result

class Worker(object):
    def __init__(self, id):
        self.id = id
        self.nextFreeTime = 0
    def __lt__(self, other):
        if self.nextFreeTime == other.nextFreeTime:
            return self.id < other.id
        return self.nextFreeTime < other.nextFreeTime

 #   def __gt__(self, other):
  #      if self.nextFreeTime == other.nextFreeTime:
   #         return self.id > other.id
    #    return self.nextFreeTime > other.nextFreeTime


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
