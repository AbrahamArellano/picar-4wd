import picar_4wd as fc
import random
import time

speed = 10
back_speed = 2
back_time = 0.2
on_stop = False

def are_all_elements_equal_to_2(arr):
    for element in arr:
        if element != 2:
            return False
    return True

def stop_and_back():
    fc.stop()
    time.sleep(back_time)
    fc.backward(back_speed)
    time.sleep(back_time)
    fc.stop()

def main():
    global on_stop
    while True:
        # Distance of read - Threshold distance to avoid obstacles
        scan_list = fc.scan_step(30)
        if not scan_list:
            print("No scan")
            continue

        #  Maximum amount of reads is 10
        scan_read = scan_list[1:8]
        read_size = len(scan_read)
        print(scan_read)
        print(read_size)
        #if (read_size == 5 and tmp != [2,2,2,2,2]) or (read_size < 5 ):
        if (not are_all_elements_equal_to_2(scan_read)):
            choice = random.randrange(2)
            print("choice: ", choice)
            # if it is NOT first iteration. Go backwards when obstacle found.
            # On first iteration is better to assess 
            if not on_stop:
                stop_and_back()
                on_stop = True
            else:
                on_stop = False
                if choice == 0:
                    fc.turn_right(speed)
                    print("Right")
                else:
                    fc.turn_left(speed)
                    print("Left")
        else:
            on_stop = False
            fc.forward(speed)
            print("Forward")


if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
