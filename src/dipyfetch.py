import os
import platform
import sys
import psutil
import time
import cpuinfo

COLOR_CODES = {"black": 20,
               "red": 31,
               "green": 32,
               "yellow": 33,
               "blue": 34,
               "magenta": 35,
               "cyan": 36,
               "white": 37
               }



def clr_print(*args, color="black", **kwargs):
    text = ""
    for arg in args:
        text = text + " " + str(arg)
    text = text.replace(" ", "", 1)
    sys.stdout.write("\033[%sm%s\033[0m" % (COLOR_CODES[color], text))
    print(**kwargs)


labels = ["Operating System:",
          "Windows Build:",
          "Processor:",
          "CPU Architecture",
          "Memory Usage:"
         ]


output = [platform.system() + " " + platform.release() + " " + platform.win32_edition(),
          platform.version(),
          cpuinfo.get_cpu_info()["brand_raw"],
          platform.machine(),
          str(round(psutil.virtual_memory().used / 2**30, 1)) + " / " + str(round(psutil.virtual_memory().total / 2**30, 1)) +" GB"
         ]

def main():
    system = os.name
    match system:
        case nt:
            os.system('cls')
            label_color = "blue"
            output_color = "cyan"
            max_width = len(max(labels, key=len))
            for i in range(len(labels)):
                clr_print(labels[i].ljust(max_width), color=label_color, end='   ')
                clr_print(output[i], color=output_color)
            print()


if __name__ == "__main__":
    starttime = time.time()
    main()
    runtime = round(time.time() - starttime, 5)
    clr_print("Total time of execution:", runtime, "seconds", color='red')
    print('\n'*5)