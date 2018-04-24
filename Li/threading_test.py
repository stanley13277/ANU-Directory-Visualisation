import threading,time

t_start = time.time()


class Datacollection(threading.Thread):
    def run(self):
        with open("Uni_ID.txt") as f:
            for i in f:
                print(threading.currentThread().getName())
                print('the thread way take %s s' % (t_end - t_start))


x = Datacollection(name = "stsge")
x.start()
t_end = time.time()