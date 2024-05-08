#!/usr/bin/python3
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers

    count = number_of_subscribers("CallOfDutyMobile")
    print(count)