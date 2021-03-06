# AppLogger-python
- Author: Codarren Velvindron
- Licence: MIT
- Date: 25/02/2021

## Logging/Auditing facility for your python application

## Introduction
- Easy to use: Just import, instantiate and write to logs
- Simple: By using an ***action*** and a ***data*** variable, where action is the bulk action and data can be more detailed !
- Customizable: set the logs to any extension and use your own separator
- Log variable changes: it is possible, check the example .py file

## Initialization
### Import library
- Create a new .py file
```python
import AppLogger
```

## Create a new object
```python
logger = AppLogger.Logger("nameoflog", 'separator', 'extension' )
```
Where 'nameoflog' can be anything, eg. audit, test.

separator and extension are optional parameters.

It will automatically create a new folder in current directory named nameoflog_logs

And the log name in that directory will be called 'nameoflog'_date.log

## Customizing
### Format the log to a csv
Here, we are making it a .csv with a ; as separator
```python
logger = AppLogger.Logger("myapp", ';', '.csv' )
```

## Usage Example
It can log right before the action is happening.

Or you may put it after, if you so desire.
```python
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
```
### my_sleeper_func

Here, we have a function that is sleeping for 5 seconds.

The first variable will be an **action**, where we say that the action is a sleep.

The second variable will be **data**, where we can put more details about the action.

### my_printer_func
Here, we are printing text by looping from 1 to 10.

**action** is used to show that we are simply doing a "COUNT_TEXT"

**data** is used to print a text and log the variable ***counter*** for each iteration !

This is useful if you want to know how the variables are changing and to log that as well.

## Log output
log name here will be: audit_logs/audit_25022021.log

```txt
2021-02-25 19:28:51.883253 SLEEP 5_seconds
2021-02-25 19:28:56.887445 COUNT_TEXT count_to_(1)
2021-02-25 19:28:56.887537 COUNT_TEXT count_to_(2)
2021-02-25 19:28:56.887591 COUNT_TEXT count_to_(3)
2021-02-25 19:28:56.887640 COUNT_TEXT count_to_(4)
2021-02-25 19:28:56.887687 COUNT_TEXT count_to_(5)
2021-02-25 19:28:56.887731 COUNT_TEXT count_to_(6)
2021-02-25 19:28:56.887777 COUNT_TEXT count_to_(7)
2021-02-25 19:28:56.887822 COUNT_TEXT count_to_(8)
2021-02-25 19:28:56.887867 COUNT_TEXT count_to_(9)
2021-02-25 19:28:56.887911 COUNT_TEXT count_to_(10)
```

## Possible limitations
- In high volume environments, logging to file might limit performance.
- This is mostly aimed at hobbyist projects, not production environments

## Contributions
- If you found an issue, or have a cool improvement, send me a pull request !
