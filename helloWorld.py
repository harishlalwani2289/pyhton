import time

result = time.localtime(time.time())
print(time.time())
print(type(result))
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)