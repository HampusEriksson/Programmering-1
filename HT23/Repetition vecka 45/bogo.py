import random, time

def bogo_sort(numbers):
    count = 0
    
    st = time.time()
    
   
    while True:
        random.shuffle(numbers)
        count += 1
        et = time.time()
        elapsed_time = et - st
        print(f"Shuffled {count} - time: {elapsed_time}")
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                break
        else:
            print('Execution time:', elapsed_time, 'seconds')
            break


numbers = [random.randint(1, 100) for _ in range(100)]

bogo_sort(numbers)