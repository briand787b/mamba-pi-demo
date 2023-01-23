#!/usr/bin/env python3

import httpx

def main():
    r = httpx.get('https://www.mallofgeorgiaford.com/used-inventory/index.htm?bodyStyle=Truck&normalDriveLine=4WD&internetPrice=10000-40000')
    print(f'{r.text}')

if __name__ == '__main__':
    main()
