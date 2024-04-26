import os
import requests
from time import sleep, time

def main():
    git_directory = os.getcwd()

    ret = requests.post("http://127.0.0.1:7315/create_job", json={"Repository_path": git_directory})
    
    if 299 < ret.status_code < 200:
        return
    ret_json = ret.json()
    if "Job_id" not in ret_json:
        return
    job_id = int(ret_json["Job_id"])
    
    print("Job started with id " + str(job_id))
    
    running = True
    time_start = time()
    while running and (time() - time_start) < 4000:
        ret = requests.post("http://127.0.0.1:7315/is_job_finished", json={"Job_id": job_id})
        if 300 <= ret.status_code < 200:
            return
        ret_json = ret.json()
        if "Log" in ret_json:
            log = ret_json["Log"]
            if log is not None:
               print(log)
        if "Job_done" not in ret_json:
            return
        if ret_json["Job_done"]:
            print("Job done")
            print("Error: " + str(ret_json["Error"]))
            if len(ret_json["Error"]) > 1:
                exit(-1)
            break
        sleep(5)

if __name__ == "__main__":
    main()