import os
import time
from subprocess import Popen

if __name__ == "__main__":
    sleep_count = 1
    keep_waiting = True

    while keep_waiting is True:
        time.sleep(sleep_count)
        sleep_count = sleep_count * 2

        if os.path.exists("./output.txt") is True:
            keep_waiting = False
            break

    run_model = Popen("source ~/.profile && cd ParisWindstormModel && oasislmf model run --config oasislmf_mdk.json", shell=True)
    run_model.wait()
