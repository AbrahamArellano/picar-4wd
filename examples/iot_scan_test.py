import picar_4wd as fc
import random
import time

speed = 30
back_speed = 5
back_time = 0.2

def main():
    start_v = True
    while True:
        scan_list = fc.scan_step(35)
        if not scan_list:
            continue

        tmp = scan_list[3:7]
        print(tmp)
#        if tmp != [2,2,2,2]:
#            choice = random.randrange(2)
#            print("choice: ", choice)
#            if not start_v:
#                fc.backward(back_speed)
#                time.sleep(back_time)
#            if choice == 0:
#                fc.turn_right(speed)
#            else:
#                fc.turn_left(speed)
#        else:
#            fc.forward(speed)

        start_v = False

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()
