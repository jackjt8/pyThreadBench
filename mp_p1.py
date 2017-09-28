from multiprocessing import Pool
import time
import matplotlib.pyplot as plt

def f(x):
    # do work
    return (x*x) - (x*x) ** (1/4-x) / 3

if __name__ == '__main__':
    # Need to set these...
    threads = 8
    repeat = 5
    workload = 10000000 #10,000,000
    #workload = 100000000 #100,000,000
    
    #total runtime
    totalruntime = time.time()
    
    #stores the timings of each run in a list-list
    timings = [[] for x in range(repeat)]
    
    # repeat a number of times
    for i in range(repeat):
        # Test multiple threads
        for n in range(threads):
            # start timing
            start = time.time()
            # create pool
            with Pool(n+1) as p:
                # do work
                temp = p.map(f, range(workload))
            # record timings
            timings[i].append(time.time() - start)
        # Wait before retesting
        time.sleep(5)
        
    # creates a list to store averages    
    avg = [] 
    # goes through timings and averages all results for n threads.
    for n in range(threads):
        temp = 0.0
        for i in range(repeat):
            temp += timings[i][n]
        temp = temp / repeat
        avg.append(temp)
    
    # plot avg time against threads and plot a minimum line.
    x = range(threads)
    setmin = [min(avg)] * threads
    plt.plot(x,avg, "o", label='Time taken for # threads')
    plt.plot(x, setmin, label='Fastest # of threads')
    plt.legend(loc='lower left')
    plt.xticks(range(threads))
    plt.ylim(ymin=0)
    plt.ylim(ymax=(round(max(avg))+1))
    plt.grid()
    plt.xlabel('Number of threads (offset by 1)')
    plt.ylabel('Average time in seconds')
    plt.suptitle('Effect of using pools to thread work averaged over %s runs.' % repeat)

    print('Time to complete tasks %s' % (time.time() - totalruntime))

