class RecentCounter:
    def __init__(self):
        self.queue=[]
        self.sz=0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.sz+=1
        range=t-3000
        while self.queue[0]<range:
            self.queue.pop(0)
            self.sz-=1 
            
        return self.sz
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

tests=[
    [
        (["RecentCounter","ping","ping","ping","ping"],
        [[],[1],[100],[3001],[3002]]),
        [None,1,2,3,3]
    ],
    [
        (["RecentCounter","ping","ping","ping","ping","ping"],
        [[],[642],[1849],[4921],[5936],[5957]]),
        [None,1,2,3,3]
    ]
]