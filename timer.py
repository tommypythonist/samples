import time
from timeloop import Timeloop
from datetime import timedelta

tl = Timeloop()
@tl.job(interval=timedelta(seconds=2))
def sample_job_every_2s():
    print(f"2s job current time : {time.ctime()}")
   
   
if __name__ == "__main__":
    tl.start(block=True)