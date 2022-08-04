#!/usr/bin/python

import subprocess
from time import sleep

fixed = []
full_list = []

check = True
while check:
    try:
        is_mpv = subprocess.run(['pgrep', 'mpv'], capture_output=True)
        mpv_check = subprocess.run(['xdotool', 'search', 'mpv'], capture_output = True)
        out = mpv_check.stdout.decode('utf-8').splitlines()
        for i in out:
            naaame = subprocess.run(['xdotool', 'getwindowname', i ], capture_output = True)
            namee = naaame.stdout.decode('utf-8')
            namee = namee.split()[-1]
            if namee == 'mpv':
                print(namee)
                if namee not in full_list:
                    full_list.append(i)
        for i in full_list:
            if i not in out:
                if full_list:
                    full_list.remove(i)
                if fixed:
                    fixed.remove(i)

        #print(len(full_list))
        #print(len(out))
        #print(out)
        #print(full_list, 'FULL LIST')
        #print(fixed, 'added')

        if is_mpv.returncode == 0:

            if len(full_list) != 0:
                last = full_list[-1]
                #print(last)
                if last not in fixed:
                    for i in full_list:
                        if i not in fixed:
                            get_id = subprocess.run(f'bspc query -N -n {i}.tiled', shell = True, capture_output = True)
                            if  get_id.returncode == 0:
                                vid = get_id.stdout.decode('utf-8').split() [0]
                                switch = subprocess.run(f'bspc node {vid} -t floating ; xdotool windowmove {last} 928 145', shell = True)
                                #switch = subprocess.run(f'bspc node {vid} -t floating  -v 450 -124', shell = True)
                                fixed.append(last)

        #else:
        #    sleep(1)

        sleep(0.05)
    except KeyboardInterrupt:
        check = False
        exit()




