import time

def main():
    start = time.time()
    time.sleep(1)
    end = time.time()
    print(int(end - start))

if __name__ == '__main__':
    main()