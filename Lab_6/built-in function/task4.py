import time

def task4(delay, num):
    time.sleep(delay/1000)
    return pow(num, 0.5)

num = 25100
delay = 2123
print(f"Square root of {num} after {delay} milliseconds is {task4(delay, num)}")