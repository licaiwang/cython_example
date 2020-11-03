import test
import test2
import org
import time

start = time.time()
p1 = org.find(20000)
print('Python: %.2f sec' % (time.time() - start))

start = time.time()
p1 = test.find(20000)
print('Cython without typing: %.2f sec' % (time.time() - start))

start = time.time()
p2 = test2.find(20000)
print('Cython with typing: %.2f sec' % (time.time() - start))