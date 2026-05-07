import threading 
import requests
import time

def download(url):
    print(f"Starting download from the {url}")
    resp = requests.get(url)
    print(f"Finished download from the {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg"
]

start = time.time()

threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url,))
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()

end = time.time()

print(f"Total Time : {end - start:.2f}")
