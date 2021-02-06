from time import sleep
import _thread as thread

class Sync:
    def __init__(self):
        self.global_sync = 0

    def get_global_sync(self):
        return self.global_sync

    def set_global_sync(self):
        self.global_sync += 1
        print("sync.set_global_sync: updated global_sync")
        if self.global_sync > 100:
            self.global_sync = 0

def update_sync(sync, time):
    while True:
        sleep(time)
        sync.set_global_sync()

class Sync_handler:
    def __init__(self, sync, time):
        self.sync_thread = thread.start_new_thread(update_sync, (sync, time))
