import random, time



list_len = 2
while True:
    list_len += 1
    numbers = [random.randint(1, 100) for _ in range(list_len)]


    count = 0
        
    st = time.time()


    while True:
        random.shuffle(numbers)
        count += 1
        et = time.time()
        elapsed_time = et - st
        print(f"{list_len} elements - shuffled {count} times - time: {elapsed_time}")
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                break
        else:
            print(f'Execution time for {list_len} elements: {elapsed_time} seconds')
            time.sleep(5)
            break
