from task1 import timecolc, urls,download_and_save,main
import threading

@timecolc
def main_threading():
    aray = []
    for url in urls:
        thread = threading.Thread(target=download_and_save, args=(url,))
        aray.append(thread)
        thread.start()
    
    for i in aray:
        i.join()

if __name__ == "__main__":
    main_threading()
    main()