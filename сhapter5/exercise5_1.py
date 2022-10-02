import time

print(time.time())
def count_days():
    """Считает количество дней с 1 января 1970 по 
        31 декабря 2021 включительно.
    """
    n = 0
    for year in range(1970, 2022):
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                n = n + 365
            else:
                n = n + 366 
        else:
            n = n + 365
    return n

def count_this_year():
    #today is August, 6th
    n = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 5
    return n

def print_time():
    time_now = time.time()
    full_days = count_days() + count_this_year()
    time_days = full_days * 24 * 60 * 60
    today = time_now - time_days
    hours = int(today // 3600) + 3 #Moscow time 
    minutes = int((today % 3600) // 60)
    seconds =  int((today % 3600) % 60)
    print("Your time is up, my time is now: ", hours, ":", minutes, ":", seconds)

print_time() 
        