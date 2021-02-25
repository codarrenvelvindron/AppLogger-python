import AppLogger
import time

logger = AppLogger.Logger("audit")

def my_sleeper_func():
    print ("This function sleeps for 5 seconds")
    logger.write (action="SLEEP", data="5_seconds")
    time.sleep(5)

def my_printer_func():
    print ("This function prints text for 10 iterations")
    for counter in range (1,11):
        logger.write(action="COUNT_TEXT", data=('count_to_(%d)' % counter))
        print (counter)

my_sleeper_func()
my_printer_func()
