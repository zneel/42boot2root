import os
import subprocess
import itertools

def generate_combi():
    digits = "0123456789"
    all_combi = [" ".join(combination) for combination in itertools.product(digits, repeat=6)]
    return all_combi

combinations = generate_combi()

with open("/dev/null", "w") as devnull:
        for i in range(10*10*10*10*10*10):
                process = subprocess.Popen(["/home/laurie/bomb"], stdin=subprocess.PIPE, stdout=devnull, stderr=devnull)
                output, error = process.communicate("Public speaking is very easy.\n1 2 6 24 120 720\n0 q 777\n9\n/ %+-!\n"+combinations[i]+"\n".encode("utf-8"))
                process.wait()
                if process.returncode == 0:
                        print("Solution found: Public speaking is very easy.\n1 2 6 24 120 720\n0 q 777\n9\n/ %+-!\n"+combinations[i]+"\n")
                        exit(0)