from datetime import datetime
import time as t

start = t.time()
t.sleep(3)
end = t.time()
elapsed = end - start
now = datetime.now().strftime("%Y.%m.%d")
print("Elapsed time: " + t.strftime("%H:%M:%S.{}".format(str(elapsed % 1)[2:])[:9], t.gmtime(elapsed)))
print(now)
