import msvcrt
import time
import os
import win32api
import pygame
import webbrowser

#Main Process
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def adjusting_the_bpm():
    userBPM = input("Please enter BPM. (default: Do not use automatic arrangement)\n")
    try:
        sysBPM = round(float(userBPM), 2)
    except ValueError:
        sysBPM = 0
        sysBeats = 4
        
    if sysBPM > 0:
        userBeats = input("\nPlease enter Beat. Type: 1/n. (default: 4)\n")
        try:
            sysBeats = int(userBeats)
            if sysBeats == 0: sysBeats = 4
        except ValueError:
            sysBeats = 4
    clear_screen()
    return sysBPM, sysBeats

def adjust_start_time():
    global timeMS
    timeMS_input = input("Please enter the start time.\n(default: 0ms)\n")
    clear_screen()
    try:
        timeMS = int(timeMS_input)
    except ValueError:
        timeMS = 0
    customStartMS = timeMS + 1
    return customStartMS

def update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats):
    global timeMS
    current_time = win32api.GetTickCount()
    elapsed_time = current_time - prev_time

    if elapsed_time >= 1:
        timeMS += elapsed_time  # Add the elapsed time
        prev_time = current_time  # Update with the current time
    if startNote == False:
        timeMS = customStartMS

    if sysBPM > 0:
        quotient = timeMS // (60000 / (sysBPM * sysBeats))
        lower_multiple = (60000 / (sysBPM * sysBeats)) * quotient
        upper_multiple = (60000 / (sysBPM * sysBeats)) * (quotient + 1)

        if abs(timeMS - lower_multiple) <= abs(timeMS - upper_multiple):
            timeMStoBPM = round(lower_multiple)
        else:
            timeMStoBPM = round(upper_multiple)
    else:
        timeMStoBPM = timeMS
    
    return timeMStoBPM, prev_time

def key10(input_char, key_list, timeMStoBPM, spinnerLength):
    index = key_list.index(input_char)
    output_value = (index % 3) * 256
    output_value2 = 384 - ((index // 3) * 192)

    if input_char != key_list[9]:
        print(f"{output_value},{output_value2},{timeMStoBPM},1,0,0:0:0:0:")
    else:
        print(f"256,192,{timeMStoBPM},12,0,{timeMStoBPM+spinnerLength},0:0:0:0:")

def key41(input_char, key_list, timeMStoBPM, spinnerLength):
    index = key_list.index(input_char)
    output_value = (index % 10) * 57
    output_value2 = (index // 10) * 128

    if input_char != key_list[40]:
        print(f"{output_value},{output_value2},{timeMStoBPM},1,0,0:0:0:0:")
    else:
        print(f"256,192,{timeMStoBPM},12,0,{timeMStoBPM+spinnerLength},0:0:0:0:")

def key46(input_char, key_list, timeMStoBPM, spinnerLength):
    output_value = 0
    output_value2 = 0
    
    # 1st column
    if input_char in key_list[:12]:
        output_value = 46 * key_list.index(input_char)
    # 2nd column
    elif input_char in key_list[12:24]:
        output_value = 23 + 46 * (key_list.index(input_char) - 12)
        output_value2 = 128
    # 3rd column
    elif input_char in key_list[24:35]:
        output_value = 23 + 46 * (key_list.index(input_char) - 24)
        output_value2 = 256
    # 4th column
    elif input_char in key_list[35:45]:
        output_value = 46 * (key_list.index(input_char) - 35) + 46
        output_value2 = 384
    if input_char == key_list[45]:
        print(f"256,192,{timeMStoBPM},12,0,{timeMStoBPM + spinnerLength},0:0:0:0:")
    else:
        print(f"{output_value},{output_value2},{timeMStoBPM},1,0,0:0:0:0:")

def dpc_key():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"10\">"
    key3="    <track idx=\"3\">"
    key4="    <track idx=\"4\">"
    key5="    <track idx=\"5\">"
    key6="    <track idx=\"6\">"
    key7="    <track idx=\"7\">"
    key8="    <track idx=\"8\">"
    key9="    <track idx=\"11\">"
    key10="    <track idx=\"9\">"
    return key1, key2, key3, key4, key5, key6, key7, key8, key9, key10

# SELECT
def MAIN():
    print("Rhythm Game Pattern Maker ver. 0.0.1")
    time.sleep(0.2)
    print("By Churitoring\n")
    time.sleep(0.2)
    print("1: osu!")
    time.sleep(0.05)
    print("2: Rhythm Doctor (Beta Version)")
    time.sleep(0.05)
    print("3: Friday Night Funkin' (Beta Version)")
    time.sleep(0.05)
    print("4: DPC(DJMAX PATTERN-DESIGN CHALLENGE)")
    time.sleep(0.05)
    print("\n\n0: Go To Youtube & Github Releases Page")
    time.sleep(0.1)
    print("\n\nEXIT: Ctrl+C")
    time.sleep(0.1)

    MAIN_SELECT()

def MAIN_SELECT():
    mode_input=input(f"\n\nPlease enter numbers only.\n\n")
    clear_screen()
    if mode_input=="0":
        GITHUB()
    elif mode_input=="1":
        OSU()
    elif mode_input=="2":
        RD()
    elif mode_input=="3":
        FNF()
    elif mode_input=="4":
        DPC()
    else : MAIN()


# OSU
def OSU():
    print("osu!\n")
    time.sleep(0.2)
    print("1: Mania 1K")
    time.sleep(0.05)
    print("2: Mania 2K")
    time.sleep(0.05)
    print("3: Mania 3K")
    time.sleep(0.05)
    print("4: Mania 4K")
    time.sleep(0.05)
    print("5: Mania 5K")
    time.sleep(0.05)
    print("6: Mania 6K")
    time.sleep(0.05)
    print("7: Mania 7K")
    time.sleep(0.05)
    print("8: Mania 8K")
    time.sleep(0.05)
    print("9: Mania 9K")
    time.sleep(0.05)
    print("10: Mania Co-op 5K")
    time.sleep(0.05)
    print("11: Mania Co-op 6K")
    time.sleep(0.05)
    print("12: Mania Co-op 7K")
    time.sleep(0.05)
    print("13: Mania Co-op 8K")
    time.sleep(0.05)
    print("14: Mania Co-op 9K")
    time.sleep(0.05)
    print("15: Taiko")
    time.sleep(0.05)
    print("\n16: Catch(BETA)")
    time.sleep(0.05)
    print("17: Standard(BETA)")
    time.sleep(0.1)
    print("\n\n0: Back To Home")
    time.sleep(0.1)
    OSU_SEL()

def OSU_SEL():
    mode_inputOSU=input(f"\n\nPlease enter numbers only.\n\n")
    clear_screen()

    if mode_inputOSU=="0":
        MAIN()
    elif mode_inputOSU=="1":
        OSU_1()
    elif mode_inputOSU=="2":
        OSU_2()
    elif mode_inputOSU=="3":
        OSU_3()
    elif mode_inputOSU=="4":
        OSU_4()
    elif mode_inputOSU=="5":
        OSU_5()
    elif mode_inputOSU=="6":
        OSU_6()
    elif mode_inputOSU=="7":
        OSU_7()
    elif mode_inputOSU=="8":
        OSU_8()
    elif mode_inputOSU=="9":
        OSU_9()
    elif mode_inputOSU=="10":
        OSU_10()
    elif mode_inputOSU=="11":
        OSU_11()
    elif mode_inputOSU=="12":
        OSU_12()
    elif mode_inputOSU=="13":
        OSU_13()
    elif mode_inputOSU=="14":
        OSU_14()
    elif mode_inputOSU=="15":
        OSU_15()
    elif mode_inputOSU=="16":
        OSU_16()
    elif mode_inputOSU=="17":
        print("1: 2 Key Mode")
        time.sleep(0.05)
        print("2: Keypad Mode(9 Keys)")
        time.sleep(0.05)
        print("3: 41 key Mode")
        time.sleep(0.05)
        print("4: Full Size Mode")
        time.sleep(0.05)
        print("\n5: Setuped Keypad Mode(9 Keys)")
        time.sleep(0.05)
        print("6: Setuped 41 key Mode")
        time.sleep(0.05)
        print("7: Setuped Full Size Mode")
        time.sleep(0.05)

        select_inputOSU=input(f"\n\nPlease enter numbers only.\n\n")
        clear_screen()

        if select_inputOSU=="1":
            OSU_17_1()
        if select_inputOSU=="2":
            OSU_17_2()
        if select_inputOSU=="3":
            OSU_17_3()
        if select_inputOSU=="4":
            OSU_17_4()
        if select_inputOSU=="5":
            OSU_17_5()
        if select_inputOSU=="6":
            OSU_17_6()
        if select_inputOSU=="7":
            OSU_17_7()
        else : OSU()
    else : OSU()

# OSU - mania     
def OSU_1():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 1 key
    key_inputs = input("Please enter one key.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 256
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_2():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 2 keys
    key_inputs = input("Please enter 2 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()
    

    # Adjusting the start time
    customStartMS = adjust_start_time()
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 128
                elif input_char == key_list[1]:
                    output_value = 384
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_3():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 3 keys
    key_inputs = input("Please enter 3 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 85
                elif input_char == key_list[1]:
                    output_value = 256
                elif input_char == key_list[2]:
                    output_value = 426
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_4():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 4 keys
    key_inputs = input("Please enter 4 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 64
                elif input_char == key_list[1]:
                    output_value = 192
                elif input_char == key_list[2]:
                    output_value = 320
                elif input_char == key_list[3]:
                    output_value = 448
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_5():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 5 keys
    key_inputs = input("Please enter 5 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 51
                elif input_char == key_list[1]:
                    output_value = 153
                elif input_char == key_list[2]:
                    output_value = 256
                elif input_char == key_list[3]:
                    output_value = 358
                elif input_char == key_list[4]:
                    output_value = 460
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_6():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 6 keys
    key_inputs = input("Please enter 6 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 42
                elif input_char == key_list[1]:
                    output_value = 128
                elif input_char == key_list[2]:
                    output_value = 213
                elif input_char == key_list[3]:
                    output_value = 298
                elif input_char == key_list[4]:
                    output_value = 384
                elif input_char == key_list[5]:
                    output_value = 469
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_7():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 7 keys
    key_inputs = input("Please enter 7 keys.")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 36
                elif input_char == key_list[1]:
                    output_value = 109
                elif input_char == key_list[2]:
                    output_value = 182
                elif input_char == key_list[3]:
                    output_value = 256
                elif input_char == key_list[4]:
                    output_value = 329
                elif input_char == key_list[5]:
                    output_value = 402
                elif input_char == key_list[6]:
                    output_value = 475
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_8():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 8 keys
    key_inputs = input("Please enter 8 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 32
                elif input_char == key_list[1]:
                    output_value = 96
                elif input_char == key_list[2]:
                    output_value = 160
                elif input_char == key_list[3]:
                    output_value = 224
                elif input_char == key_list[4]:
                    output_value = 288
                elif input_char == key_list[5]:
                    output_value = 352
                elif input_char == key_list[6]:
                    output_value = 416
                elif input_char == key_list[7]:
                    output_value = 480
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_9():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()
    

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 28
                elif input_char == key_list[1]:
                    output_value = 85
                elif input_char == key_list[2]:
                    output_value = 142
                elif input_char == key_list[3]:
                    output_value = 199
                elif input_char == key_list[4]:
                    output_value = 256
                elif input_char == key_list[5]:
                    output_value = 312
                elif input_char == key_list[6]:
                    output_value = 369
                elif input_char == key_list[7]:
                    output_value = 426
                elif input_char == key_list[8]:
                    output_value = 483
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_10():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 10 keys
    key_inputs = input("Please enter 10 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 25
                elif input_char == key_list[1]:
                    output_value = 76
                elif input_char == key_list[2]:
                    output_value = 128
                elif input_char == key_list[3]:
                    output_value = 179
                elif input_char == key_list[4]:
                    output_value = 230
                elif input_char == key_list[5]:
                    output_value = 281
                elif input_char == key_list[6]:
                    output_value = 332
                elif input_char == key_list[7]:
                    output_value = 384
                elif input_char == key_list[8]:
                    output_value = 435
                elif input_char == key_list[9]:
                    output_value = 486
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_11():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 12 keys
    key_inputs = input("Please enter 12 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 21
                elif input_char == key_list[1]:
                    output_value = 64
                elif input_char == key_list[2]:
                    output_value = 106
                elif input_char == key_list[3]:
                    output_value = 149
                elif input_char == key_list[4]:
                    output_value = 192
                elif input_char == key_list[5]:
                    output_value = 234
                elif input_char == key_list[6]:
                    output_value = 277
                elif input_char == key_list[7]:
                    output_value = 320
                elif input_char == key_list[8]:
                    output_value = 362
                elif input_char == key_list[9]:
                    output_value = 405
                elif input_char == key_list[10]:
                    output_value = 448
                elif input_char == key_list[11]:
                    output_value = 490
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_12():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 14 keys
    key_inputs = input("Please enter 14 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 18
                elif input_char == key_list[1]:
                    output_value = 54
                elif input_char == key_list[2]:
                    output_value = 91
                elif input_char == key_list[3]:
                    output_value = 128
                elif input_char == key_list[4]:
                    output_value = 164
                elif input_char == key_list[5]:
                    output_value = 201
                elif input_char == key_list[6]:
                    output_value = 237
                elif input_char == key_list[7]:
                    output_value = 274
                elif input_char == key_list[8]:
                    output_value = 310
                elif input_char == key_list[9]:
                    output_value = 347
                elif input_char == key_list[10]:
                    output_value = 384
                elif input_char == key_list[11]:
                    output_value = 420
                elif input_char == key_list[12]:
                    output_value = 457
                elif input_char == key_list[13]:
                    output_value = 493
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_13():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 16 keys
    key_inputs = input("Please enter 16 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 16
                elif input_char == key_list[1]:
                    output_value = 48
                elif input_char == key_list[2]:
                    output_value = 80
                elif input_char == key_list[3]:
                    output_value = 112
                elif input_char == key_list[4]:
                    output_value = 144
                elif input_char == key_list[5]:
                    output_value = 176
                elif input_char == key_list[6]:
                    output_value = 208
                elif input_char == key_list[7]:
                    output_value = 240
                elif input_char == key_list[8]:
                    output_value = 272
                elif input_char == key_list[9]:
                    output_value = 304
                elif input_char == key_list[10]:
                    output_value = 336
                elif input_char == key_list[11]:
                    output_value = 368
                elif input_char == key_list[12]:
                    output_value = 400
                elif input_char == key_list[13]:
                    output_value = 432
                elif input_char == key_list[14]:
                    output_value = 464
                elif input_char == key_list[15]:
                    output_value = 496
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_14():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 18 keys
    key_inputs = input("Please enter 18 keys.\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 14
                elif input_char == key_list[1]:
                    output_value = 42
                elif input_char == key_list[2]:
                    output_value = 71
                elif input_char == key_list[3]:
                    output_value = 99
                elif input_char == key_list[4]:
                    output_value = 128
                elif input_char == key_list[5]:
                    output_value = 156
                elif input_char == key_list[6]:
                    output_value = 184
                elif input_char == key_list[7]:
                    output_value = 213
                elif input_char == key_list[8]:
                    output_value = 241
                elif input_char == key_list[9]:
                    output_value = 270
                elif input_char == key_list[10]:
                    output_value = 298
                elif input_char == key_list[11]:
                    output_value = 327
                elif input_char == key_list[12]:
                    output_value = 355
                elif input_char == key_list[13]:
                    output_value = 384
                elif input_char == key_list[14]:
                    output_value = 412
                elif input_char == key_list[15]:
                    output_value = 440
                elif input_char == key_list[16]:
                    output_value = 469
                elif input_char == key_list[17]:
                    output_value = 497
                print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                startNote=True
                sound_effect.play()

# OSU - Beta Version
def OSU_15():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\n(Red Red Blue Blue BigRed BigRed BigBlue BigBlue Spinner)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    print(f"256,192,{timeMStoBPM},5,0,0:0:0:0:")
                elif input_char == key_list[1]:
                    print(f"256,192,{timeMStoBPM},5,0,0:0:0:0:")
                elif input_char == key_list[2]:
                    print(f"256,192,{timeMStoBPM},1,2,0:0:0:0:")
                elif input_char == key_list[3]:
                    print(f"256,192,{timeMStoBPM},1,2,0:0:0:0:")
                elif input_char == key_list[4]:
                    print(f"256,192,{timeMStoBPM},1,4,0:0:0:0:")
                elif input_char == key_list[5]:
                    print(f"256,192,{timeMStoBPM},1,4,0:0:0:0:")
                elif input_char == key_list[6]:
                    print(f"256,192,{timeMStoBPM},1,6,0:0:0:0:")
                elif input_char == key_list[7]:
                    print(f"256,192,{timeMStoBPM},1,6,0:0:0:0:")
                elif input_char == key_list[8]:
                    print(f"512,384,{timeMStoBPM},12,0,{timeMStoBPM+spinnerLength},0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_16():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 11 keys
    key_inputs = input("Please enter 11 keys.\n(The last key is the spinner.)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 0
                elif input_char == key_list[1]:
                    output_value = 57
                elif input_char == key_list[2]:
                    output_value = 114
                elif input_char == key_list[3]:
                    output_value = 171
                elif input_char == key_list[4]:
                    output_value = 228
                elif input_char == key_list[5]:
                    output_value = 285
                elif input_char == key_list[6]:
                    output_value = 342
                elif input_char == key_list[7]:
                    output_value = 339
                elif input_char == key_list[8]:
                    output_value = 456
                elif input_char == key_list[9]:
                    output_value = 512
                if input_char!=key_list[10]:
                    print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")
                if input_char==key_list[10]:
                    print(f"256,192,{timeMStoBPM},12,0,{timeMS+spinnerLength},0:0:0:0:")
                startNote=True
                sound_effect.play()

# OSU - osu! Standard
def OSU_17_1():
    startNote = False
    s = 0
    prev_time = win32api.GetTickCount()

    # Received 3 keys
    key_inputs = input("Please enter 3 keys.\n(The last key is the spinner.)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    print(f"512,384,{timeMStoBPM},1,0,0:0:0:0:")
                elif input_char == key_list[1]:
                    print(f"512,384,{timeMStoBPM},1,0,0:0:0:0:")
                elif input_char == key_list[2]:
                    print(f"512,384,{timeMStoBPM},12,0,{timeMStoBPM+spinnerLength},0:0:0:0:")
                startNote=True
                sound_effect.play()

def OSU_17_2():
    startNote = False
    prev_time = win32api.GetTickCount()
    
    # Received 10 keys
    key_inputs = input("Please enter 10 keys.\n(The last key is the spinner.)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                key10(input_char, key_list, timeMStoBPM, spinnerLength)
                startNote=True
                sound_effect.play()

def OSU_17_3():
    startNote = False
    prev_time = win32api.GetTickCount()
    
    # Received 41 keys
    key_inputs = input("Please enter 41 keys.\n(The last key is the spinner.)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                key41(input_char, key_list, timeMStoBPM, spinnerLength)
                startNote=True
                sound_effect.play()

def OSU_17_4():
    startNote = False
    prev_time = win32api.GetTickCount()
    
    # Received 46 keys
    key_inputs = input("Please enter 46 keys.\n(The last key is the spinner.)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                key46(input_char, key_list, timeMStoBPM, spinnerLength)
                startNote=True
                sound_effect.play()

def OSU_17_5():
    startNote = False
    prev_time = win32api.GetTickCount()
    
    key_list = list("1234567890")
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                key10(input_char, key_list, timeMStoBPM, spinnerLength)
                startNote=True
                sound_effect.play()

def OSU_17_6():
    startNote = False
    prev_time = win32api.GetTickCount()
    
    key_list = list("234567890-wertyuiop[asdfghjkl;zxcvbnm,./1")
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)

        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                key41(input_char, key_list, timeMStoBPM, spinnerLength)
                startNote=True
                sound_effect.play()

def OSU_17_7():
    startNote = False
    prev_time = win32api.GetTickCount()

    key_list = list("1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./`")

    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    # Adjusting the spinner length
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                key46(input_char, key_list, timeMStoBPM, spinnerLength)
                startNote=True
                sound_effect.play()

# Rhythm Doctor
def RD():
    print("Rhythm Doctor (Beta Version)\n")
    time.sleep(0.2)
    print("1: All Note 0 Tick")
    time.sleep(0.05)
    print("2: 1.3 Tick & 8 Tick")
    time.sleep(0.1)
    print("\n\n0: Back To Home")
    time.sleep(0.1)
    RD_SEL()

def RD_SEL():
    mode_inputRD=input(f"\n\nPlease enter numbers only.\n\n")
    clear_screen()
    if mode_inputRD=="0":
        MAIN()
    if mode_inputRD=="1":
        RD_1()
    elif mode_inputRD=="2":
        RD_2()
    else : RD()
 
def RD_1():
    global timeMS
    startNote = False
    prev_time = win32api.GetTickCount()
    # Received 4 key
    key_inputs = input("Please enter 4 keys. (Classic x 2, Oneshot x 2)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Received BPM
    userBPM = input("Please enter BPM.\n")
    clear_screen()

    # Adjusting the start time
    timeMS_input = input("Please enter the start time.\n(default: 0ms)\n")
    clear_screen()
    try:
        timeMS = int(timeMS_input)
    except ValueError:
        timeMS = 0
    customStartMS = timeMS + 1

    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            timeMS += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
            sysBPM=60000/round(float(userBPM),2)
            gameBeat = int(timeMS/sysBPM%8)+1
            gameBar = int(timeMS/(sysBPM*8))+1
        if startNote==0:
            timeMS = customStartMS
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = '"y": 0, "type": "AddClassicBeat", "row": 0'
                elif input_char == key_list[1]:
                    output_value = '"y": 1, "type": "AddClassicBeat", "row": 1'
                elif input_char == key_list[2]:
                    output_value = '"y": 2, "type": "AddOneshotBeat", "row": 2'
                elif input_char == key_list[3]:
                    output_value = '"y": 3, "type": "AddOneshotBeat", "row": 3'
                print(f'	{{ "bar": {gameBar}, "beat": {gameBeat}, {output_value}, "pulseType": "Wave", "tick": 0 }},')
                startNote=True
                sound_effect.play()

def RD_2():
    global timeMS
    startNote = False
    prev_time = win32api.GetTickCount()
    # Received 4 key
    key_inputs = input("Please enter 4 keys. (Classic x 2, Oneshot x 2)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Received BPM
    userBPM = input("Please enter BPM.\n")
    clear_screen()

    # Adjusting the start time
    timeMS_input = input("Please enter the start time.\n(default: 0ms)\n")
    clear_screen()
    try:
        timeMS = int(timeMS_input)
    except ValueError:
        timeMS = 0
    customStartMS = timeMS + 1

    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            timeMS += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
            sysBPM=60000/round(float(userBPM),2)
            gameBeat = int(timeMS/sysBPM%8)+1
            gameBar = int(timeMS/(sysBPM*8))
        if startNote==0:
            timeMS = customStartMS
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = '"y": 0, "type": "AddClassicBeat", "row": 0, "pulseType": "Wave", "tick": 1.333333'
                elif input_char == key_list[1]:
                    output_value = '"y": 1, "type": "AddClassicBeat", "row": 1, "pulseType": "Wave", "tick": 1.333333'
                elif input_char == key_list[2]:
                    output_value = '"y": 2, "type": "AddOneshotBeat", "row": 2, "pulseType": "Wave", "tick": 8'
                elif input_char == key_list[3]:
                    output_value = '"y": 3, "type": "AddOneshotBeat", "row": 3, "pulseType": "Wave", "tick": 8'
                print(f'	{{ "bar": {gameBar}, "beat": {gameBeat}, {output_value} }},')
                startNote=True
                sound_effect.play()

# FNF
def FNF():
    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 4 keys
    key_inputs = input("Please enter 4 keys. (Left, Down, Up, Right)\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        
        # If there is input
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    output_value = 0
                elif input_char == key_list[1]:
                    output_value = 1
                elif input_char == key_list[2]:
                    output_value = 2
                elif input_char == key_list[3]:
                    output_value = 3
                print(f"[{timeMStoBPM},{output_value},0],")
                startNote=True
                sound_effect.play()


# DPC
def DPC():
    print("DPC(DJMAX PATTERN-DESIGN CHALLENGE)\n")
    time.sleep(0.2)
    print("1: 4B(Key Sound: blank)")
    time.sleep(0.05)
    print("2: 5B(Key Sound: blank)")
    time.sleep(0.05)
    print("3: 6B(Key Sound: blank)")
    time.sleep(0.05)
    print("4: 8B(Key Sound: blank)")
    time.sleep(0.05)
    print("5: 4B(Key Sound: No.0000)")
    time.sleep(0.05)
    print("6: 5B(Key Sound: No.0000)")
    time.sleep(0.05)
    print("7: 6B(Key Sound: No.0000)")
    time.sleep(0.05)
    print("8: 8B(Key Sound: No.0000)")
    time.sleep(0.1)
    print("\n9: View Delete Note Command")
    time.sleep(0.1)
    print("\n\n0: Back To Home")
    time.sleep(0.1)
    DPC_SEL()

def DPC_SEL():
    mode_inputDPC=input(f"\n\nPlease enter numbers only.\n\n")
    clear_screen()
    if mode_inputDPC=="0":
        MAIN()
    elif mode_inputDPC=="1":
        DPC_1()
    elif mode_inputDPC=="2":
        DPC_2()
    elif mode_inputDPC=="3":
        DPC_3()
    elif mode_inputDPC=="4":
        DPC_4()
    elif mode_inputDPC=="5":
        DPC_5()
    elif mode_inputDPC=="6":
        DPC_6()
    elif mode_inputDPC=="7":
        DPC_7()
    elif mode_inputDPC=="8":
        DPC_8()
    elif mode_inputDPC=="9":
        DPC_DELETENOTE()
    else : DPC()

def DPC_DELETENOTE():
    clear_screen()
    print('      <note tick=".*" />')
    print('      <note tick=".*" ins="1" />')
    input(f"\n\n\n\n")
    clear_screen()
    DPC()

# DPC - blank
def DPC_1():
    key1, key2, key3, key4, key5, key6, _, _, _, _ = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 6 keys
    key_inputs = input("Please enter 6 keys.\nLeftSide,B,B,B,B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()

    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>")

def DPC_2():
    key1, key2, key3, key4, key5, key6, key7, _, _, _ = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 8 keys
    key_inputs = input("Please enter 8 keys.\nLeftSide,B,B,(B,B),B,B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()
    
    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()

    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()
    
    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[4]:
                    key4 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[5]:
                    key5 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[6]:
                    key6 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[7]:
                    key7 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n{key7}\n    </track>\n")

def DPC_3():
    key1, key2, key3, key4, key5, key6, key7, key8, _, _ = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 8 keys
    key_inputs = input("Please enter 8 keys.\nLeftSide,B,B,B,B,B,B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n{key7}\n    </track>\n{key8}\n    </track>\n")

def DPC_4():
    key1, key2, key3, key4, key5, key6, key7, key8, key9, key10 = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 10 keys
    key_inputs = input("Please enter 10 keys.\nLeftSide,LeftB,B,B,B,B,B,B,Right8B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[8]:
                    key9 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                elif input_char == key_list[9]:
                    key10 += f"\n      <note tick=\"{tick}\" ins=\"1\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n{key7}\n    </track>\n{key8}\n    </track>\n{key9}\n    </track>\n{key10}\n    </track>\n")

# DPC - No.0000
def DPC_5():
    key1, key2, key3, key4, key5, key6, _, _, _, _ = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 6 keys
    key_inputs = input("Please enter 6 keys.\nLeftSide,B,B,B,B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{tick}\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n")

def DPC_6():
    key1, key2, key3, key4, key5, key6, key7, _, _, _ = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 8 keys
    key_inputs = input("Please enter 8 keys.\nLeftSide,B,B,(B,B),B,B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[4]:
                    key4 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[5]:
                    key5 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[6]:
                    key6 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[7]:
                    key7 += f"\n      <note tick=\"{tick}\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n{key7}\n    </track>\n")

def DPC_7():
    key1, key2, key3, key4, key5, key6, key7, key8, _, _ = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 8 keys
    key_inputs = input("Please enter 8 keys.\nLeftSide,B,B,B,B,B,B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()
    
    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{tick}\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n{key7}\n    </track>\n{key8}\n    </track>\n")

def DPC_8():
    key1, key2, key3, key4, key5, key6, key7, key8, key9, key10 = dpc_key()

    startNote = False
    prev_time = win32api.GetTickCount()

    # Received 10 keys
    key_inputs = input("Please enter 10 keys.\nLeftSide,LeftB,B,B,B,B,B,B,Right8B,RightSide\n")
    # Convert the input string into a list
    key_list = list(key_inputs)
    clear_screen()

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    clear_screen()
    
    # Adjusting the BPM
    sysBPM, sysBeats = adjusting_the_bpm()

    # Adjusting the start time
    customStartMS = adjust_start_time()

    while True:
        timeMStoBPM, prev_time = update_time(prev_time, startNote, customStartMS, sysBPM, sysBeats)
        # If there is input
        tick=round(timeMStoBPM*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[8]:
                    key9 += f"\n      <note tick=\"{tick}\"/>"
                elif input_char == key_list[9]:
                    key10 += f"\n      <note tick=\"{tick}\"/>"
                startNote=True
                sound_effect.play()
                clear_screen()
                print(f"{key1}\n    </track>\n{key2}\n    </track>\n{key3}\n    </track>\n{key4}\n    </track>\n{key5}\n    </track>\n{key6}\n    </track>\n{key7}\n    </track>\n{key8}\n    </track>\n{key9}\n    </track>\n{key10}\n    </track>\n")


# Github
def GITHUB():
    webbrowser.open_new('https://www.youtube.com/@churitoring')
    webbrowser.open_new('https://github.com/Churitoring/Rhythm_Game_Pattern_Maker/releases')
    clear_screen()
    print("Open!\nBack to Home!\n3")
    time.sleep(1)
    clear_screen()
    print("Open!\nBack to Home!\n2")
    time.sleep(1)
    clear_screen()
    print("Open!\nBack to Home!\n1")
    time.sleep(1)
    clear_screen()
    MAIN()

# MAIN
pygame.mixer.init(buffer=2)
sound_file = "sound.mp3"
sound_effect=pygame.mixer.Sound(sound_file)
timeMS = 0
clear_screen()
MAIN()
print("IF YOU READ THIS PLEASE TELL ME")
time.sleep(31536000)