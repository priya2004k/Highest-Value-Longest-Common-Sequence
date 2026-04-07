# Question 1 Code
import matplotlib.pyplot as plt 
from hvlcs import HighestValueLongestCommonSequence, parse_input
import time

labels = [] 
times = []

for i in range(1, 12):
    f = f"tests/test{i}.in"
    A, B, value = parse_input(f)

    start = time.perf_counter()
    HighestValueLongestCommonSequence(A, B, value)
    final = time.perf_counter()
    test_time = final - start

    label = f"{i}"
    
    labels.append(label)
    times.append(test_time)

plt.figure(figsize=(12,5))
plt.bar(range(1,12), times, tick_label=labels)
plt.xlabel("Test Case")
plt.ylabel("Runtime (s)")
plt.title("HVLCS Test Runtime Analysis")
plt.tight_layout()
plt.savefig("runtimes.png", dpi=300)
