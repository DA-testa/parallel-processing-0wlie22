def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)]  # initialize the threads with their indices and start times
    for i in range(m):
        # find the thread with the earliest finish time
        min_finish_time = threads[0][1]
        min_thread_index = 0
        for j in range(1, n):
            if threads[j][1] < min_finish_time:
                min_finish_time = threads[j][1]
                min_thread_index = j
        # add the job to the output with the thread index and start time
        output.append((min_thread_index, min_finish_time))
        # update the thread's finish time
        threads[min_thread_index] = (threads[min_thread_index][0], min_finish_time + data[i])
    return output

def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # run the parallel processing function
    result = parallel_processing(n, m, data)

    # print out the results
    for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
