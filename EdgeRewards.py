import os
import random
import time
import subprocess


def kill_edge():
    tasklist_output = subprocess.check_output('tasklist').splitlines()

    matches = [s for s in tasklist_output if b'Edge.exe' in s]

    pid_list = []
    for result in matches:
        pid_list.append(result.decode("utf-8").split()[1])

    taskkill_command = "taskkill /f /pid "
    for pid in pid_list:
        os.popen(taskkill_command + pid)


if __name__ == "__main__":
    dictionary = open("words.txt").read().splitlines()

    edge_string = "start shell:AppsFolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge"

    num_of_searches = int(150 / 5)

    for search in range(0, num_of_searches):
        time_to_sleep = random.randrange(30, 600)
        time.sleep(time_to_sleep)
        num_of_terms = random.randrange(1, 5)
        search_terms = random.sample(dictionary, num_of_terms)
        search_string = edge_string
        for term in search_terms:
            search_string += " " + term
        os.popen(search_string)

    kill_edge()
