# from requests import get, Timeout

# import time

# for _ in range(15):
#     response = get("https://www.cloudflare.com/rate-limit-test/")
#     print(response.status_code)
#     time.sleep(6)

# try:
#     response = get("https://httpbin.org/delay/10", timeout=2)
# except Timeout:
#     response = get("https://httpbin.org/delay/10", timeout=9)
# finally:
#     print(response.status_code)
