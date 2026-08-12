import threading
import time

def take_orders():
    for i in range(1,4):
        print(f"Taking order for #{i}")
        time.sleep(1)



def brew_chai():
    for i in range(1,4):
            print(f"Brewing chai for #{i}")
            time.sleep(2)


# Creating Threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()