class Queue(object):
    def __init__(self, max_size):
        self.max_size = max_size
        self.curr_size = 0
        self.q = []

    def add(self, new):
        if self.curr_size+1 > self.max_size:
            del self.q[0]
            self.curr_size -= 1
        self.q.append(new)
        self.curr_size += 1

with open("09.in", "r") as file:
    q = Queue(25)
    for l in file:
        l = int(l.strip())
        if q.curr_size == 25:
            found = False
            for i in q.q:
                if l-i in q.q:
                    found = True
                else:
                    pass
            if not found:
                print(l)
                break

        q.add(l)

