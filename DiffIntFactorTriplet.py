targetNo = int(input("Target Number to find factor triplets? Must be a positive integer -> "))

int1 = targetNo * -1
int2 = targetNo * -1
int3 = targetNo * -1

print("Starting query for target " + str(targetNo) + ", all three factors will be different...")

import time
startTime = time.time()
while int3 <= targetNo:
    if int1 * int2 * int3 == targetNo and int1 != int2 and int2 != int3 and int1 != int3:
        print(str(int1) + " * " + str(int2) + " * " + str(int3) + " = " + str(targetNo))

    if int1 > targetNo:
        int2 = int2 + 1
        int1 = targetNo * -1
    else:
        int1 = int1 + 1
    if int2 > targetNo:
        int3 = int3 + 1
        int2 = targetNo * -1
print("Elapsed time: approximately " + str(time.time() - startTime) + " seconds")
print("*** FINISHED ***")
