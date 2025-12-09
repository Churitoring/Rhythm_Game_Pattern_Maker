import msvcrt
import time
import os
import win32api
import pygame
import webbrowser

#Main Process
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_engine(key_list, handler_func, context):
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
    timeMS_input = input("Please enter the start time.\n(default: 0ms)\n")
    clear_screen()
    
    try:
        timeMS = int(timeMS_input)
    except ValueError:
        timeMS = 0
    
    customStartMS = timeMS + 1
    
    startNote = False
    prev_time = win32api.GetTickCount()
    context['startNote'] = startNote

    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time

        if elapsed_time >= 1:
            timeMS += elapsed_time
            prev_time = current_time
        
        if startNote == False:
            timeMS = customStartMS

        if sysBPM > 0:
            beat_interval = 60000 / (sysBPM * sysBeats)
            quotient = timeMS // beat_interval
            lower_multiple = beat_interval * quotient
            upper_multiple = beat_interval * (quotient + 1)

            if abs(timeMS - lower_multiple) <= abs(timeMS - upper_multiple):
                timeMStoBPM = round(lower_multiple)
            else:
                timeMStoBPM = round(upper_multiple)
        else:
            timeMStoBPM = timeMS
        
        if msvcrt.kbhit():
            try:
                input_char = msvcrt.getch().decode()
            except UnicodeDecodeError:
                continue

            if input_char in key_list:
                if not startNote:
                    startNote = True
                    context['startNote'] = True
                
                sound_effect.play()
                handler_func(input_char, timeMStoBPM, context)


def osu_engine(key_list, key_handler_func):
    clear_screen()
    
    spinnerLength_input = input("Please enter the spinner length.\n(default: 5000ms)\n")
    clear_screen()
    try:
        spinnerLength = int(spinnerLength_input)
    except ValueError:
        spinnerLength = 5000
        
    context = {
        'key_list': key_list,
        'key_handler_func': key_handler_func,
        'spinnerLength': spinnerLength
    }
    
    main_engine(key_list, _handler_osu, context)

def dpc_engine(key_count, input_msg, use_ins_attr):
    all_keys = list(dpc_key()) 
    tracks_initial = all_keys[:key_count]
    
    print(f"Please enter {key_count} keys.")
    key_inputs = input(input_msg + "\n")
    key_list = list(key_inputs)
    clear_screen()

    tps = float(input("Please enter tps.\n"))
    clear_screen()

    ins_str = ' ins="1"' if use_ins_attr else ""
    
    context = {
        'key_list': key_list,
        'tracks': tracks_initial,
        'tps': tps,
        'ins_str': ins_str
    }
    
    main_engine(key_list, _handler_dpc, context)

def rd_engine(mode):
    key_inputs = input("Please enter 4 keys. (Classic x 2, Oneshot x 2)\n")
    key_list = list(key_inputs)
    clear_screen()

    userBPM = input("Please enter BPM.\n")
    clear_screen()

    timeMS_input = input("Please enter the start time.\n(default: 0ms)\n")
    clear_screen()
    try:
        timeMS = int(timeMS_input)
    except ValueError:
        timeMS = 0
    
    rd_sysBPM = 60000 / round(float(userBPM), 2)
    customStartMS = timeMS + 1

    if mode == 1:
        key_configs = [
            {"type": "AddClassicBeat", "row": 0},
            {"type": "AddClassicBeat", "row": 1},
            {"type": "AddOneshotBeat", "row": 2},
            {"type": "AddOneshotBeat", "row": 3},
        ]
    else:
        key_configs = [
            {"type": "AddClassicBeat", "row": 0, "pulseType": "Wave", "tick": 1.333333},
            {"type": "AddClassicBeat", "row": 1, "pulseType": "Wave", "tick": 1.333333},
            {"type": "AddOneshotBeat", "row": 2, "pulseType": "Wave", "tick": 8},
            {"type": "AddOneshotBeat", "row": 3, "pulseType": "Wave", "tick": 8},
        ]

    context = {
        'key_list': key_list,
        'rd_sysBPM': rd_sysBPM,
        'key_configs': key_configs,
        'rd_version': mode
    }

    main_engine(key_list, _handler_rd, 120, 4, customStartMS, context)

def fnf_engine():
    key_inputs = input("Please enter 4 keys. (Left, Down, Up, Right)\n")
    key_list = list(key_inputs)
    clear_screen()

    context = {
        'key_list': key_list
    }

    main_engine(key_list, _handler_fnf, context)


def _handler_osu(key, current_time, context):
    func = context['key_handler_func']
    key_list = context['key_list']
    spinnerLength = context['spinnerLength']
    
    func(key, key_list, current_time, spinnerLength)

def _handler_dpc(key, current_time, context):
    key_list = context['key_list']
    idx = key_list.index(key)
    
    tick = round(current_time * context['tps'] / 1000)
    ins_str = context['ins_str']
    
    context['tracks'][idx] += f'\n      <note tick="{tick}"{ins_str}/>'
    
    clear_screen()
    output_str = ""
    for track_content in context['tracks']:
        output_str += f"{track_content}\n    </track>\n"
    print(output_str)

def _handler_rd(key, current_time, context):
    sysBPM = context['rd_sysBPM']
    
    gameBeat = int(current_time / sysBPM % 8) + 1
    gameBar = int(current_time / (sysBPM * 8)) + 1
    if context['rd_version'] == 2:
         gameBar = int(current_time / (sysBPM * 8))

    key_list = context['key_list']
    idx = key_list.index(key)
    
    config = context['key_configs'][idx]
    
    output_value = f'"y": {idx}, "type": "{config["type"]}", "row": {config["row"]}'
    
    if "pulseType" in config:
        output_value += f', "pulseType": "{config["pulseType"]}", "tick": {config["tick"]}'
    else:
        output_value += ', "pulseType": "Wave", "tick": 0'

    print(f'    {{ "bar": {gameBar}, "beat": {gameBeat}, {output_value} }},')

def _handler_fnf(key, current_time, context):
    key_list = context['key_list']
    idx = key_list.index(key)
    print(f"[{current_time},{idx},0],")


def key_catch(input_char, key_list, timeMStoBPM, spinnerLength):
    key_index = key_list.index(input_char)
    output_value = None

    match key_index:
        case 0: output_value = 0
        case 1: output_value = 57
        case 2: output_value = 114
        case 3: output_value = 171
        case 4: output_value = 228
        case 5: output_value = 285
        case 6: output_value = 342
        case 7: output_value = 399
        case 8: output_value = 456
        case 9: output_value = 512
        case 10: 
            print(f"256,192,{timeMStoBPM},12,0,{timeMStoBPM+spinnerLength},0:0:0:0:")

    if output_value is not None:
        print(f"{output_value},192,{timeMStoBPM},1,0,0:0:0:0:")

def key3(input_char, key_list, timeMStoBPM, spinnerLength):
    if input_char == key_list[0]:
        print(f"512,384,{timeMStoBPM},1,0,0:0:0:0:")
    elif input_char == key_list[1]:
        print(f"512,384,{timeMStoBPM},1,0,0:0:0:0:")
    elif input_char == key_list[2]:
        print(f"512,384,{timeMStoBPM},12,0,{timeMStoBPM+spinnerLength},0:0:0:0:")

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
    menu = [
        ("Rhythm Game Pattern Maker ver. 0.0.2", 0.2),
        ("By Churitoring\n", 0.2),
        ("1: osu!", 0.05),
        ("2: Rhythm Doctor (Beta Version)", 0.05),
        ("3: Friday Night Funkin' (Beta Version)", 0.05),
        ("4: DPC(DJMAX PATTERN-DESIGN CHALLENGE)", 0.05),
        ("\n\n0: Go To Youtube & Github Releases Page", 0.1),
        ("\n\nEXIT: Ctrl+C", 0.1)
    ]
    for text, delay in menu:
        print(text)
        time.sleep(delay)

    mode_input = input("\n\nPlease enter numbers only.\n\n")
    clear_screen()

    match mode_input:
        case "0": GITHUB()
        case "1": OSU()
        case "2": RD()
        case "3": FNF()
        case "4": DPC()
        case _: MAIN()


# OSU
def OSU():
    menu = [
        ("osu!\n", 0.2),
        ("1: Catch(BETA)", 0.05),
        ("2: Standard(BETA)", 0.1),
        ("\n\n0: Back To Home", 0.1)
    ]
    for text, delay in menu:
        print(text)
        time.sleep(delay)

    mode_inputOSU = input("\n\nPlease enter numbers only.\n\n")
    clear_screen()

    match mode_inputOSU:
        case "0": MAIN()
        case "1": osu_engine(list(input("Please enter 11 keys.\n(The last key is the spinner.)\n")), key_catch)
        case "2": OSU_Standard()
        case _: OSU()

# OSU - osu! Standard
def OSU_Standard():
    menu = [
    ("1: 2 Key Mode", 0.05),
    ("2: Keypad Mode(9 Keys)", 0.05),
    ("3: 41 key Mode", 0.05),
    ("4: Full Size Mode", 0.05),
    ("\n5: Setuped Keypad Mode(9 Keys)", 0.05),
    ("6: Setuped 41 key Mode", 0.05),
    ("7: Setuped Full Size Mode", 0.05)
    ]
    for text, delay in menu:
        print(text)
        time.sleep(delay)
    
    select_inputOSU = input("\n\nPlease enter numbers only.\n\n")
    clear_screen()

    match select_inputOSU:
        case "1": osu_engine(list(input("Please enter 3 keys.\n(The last key is the spinner.)\n")), key3)
        case "2": osu_engine(list(input("Please enter 10 keys.\n(The last key is the spinner.)\n")), key10)
        case "3": osu_engine(list(input("Please enter 41 keys.\n(The last key is the spinner.)\n")), key41)
        case "4": osu_engine(list(input("Please enter 46 keys.\n(The last key is the spinner.)\n")), key46)
        case "5": osu_engine(list("1234567890"), key10)
        case "6": osu_engine(list("234567890-wertyuiop[asdfghjkl;zxcvbnm,./1"), key41)
        case "7": osu_engine(list("1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./`"), key46)
        case _: OSU()

# Rhythm Doctor
def RD():
    menu = [
        ("Rhythm Doctor (Beta Version)\n", 0.2),
        ("1: All Note 0 Tick", 0.05),
        ("2: 1.3 Tick & 8 Tick", 0.1),
        ("\n\n0: Back To Home", 0.1)
    ]
    for text, delay in menu:
        print(text)
        time.sleep(delay)

    mode_inputRD = input("\n\nPlease enter numbers only.\n\n")
    clear_screen()

    match mode_inputRD:
        case "0": MAIN()
        case "1": rd_engine(1)
        case "2": rd_engine(2)
        case _: RD()

# FNF
def FNF():
    key_inputs = input("Please enter 4 keys. (Left, Down, Up, Right)\n")
    key_list = list(key_inputs)
    clear_screen()

    context = {
        'key_list': key_list
    }

    main_engine(key_list, _handler_fnf, context)

# DPC
def DPC():
    menu = [
        ("DPC(DJMAX PATTERN-DESIGN CHALLENGE)\n", 0.2),
        ("1: 4B(Key Sound: blank)", 0.05),
        ("2: 5B(Key Sound: blank)", 0.05),
        ("3: 6B(Key Sound: blank)", 0.05),
        ("4: 8B(Key Sound: blank)", 0.05),
        ("5: 4B(Key Sound: No.0000)", 0.05),
        ("6: 5B(Key Sound: No.0000)", 0.05),
        ("7: 6B(Key Sound: No.0000)", 0.05),
        ("8: 8B(Key Sound: No.0000)", 0.1),
        ("\n9: View Delete Note Command", 0.1),
        ("\n\n0: Back To Home", 0.1)
    ]
    for text, delay in menu:
        print(text)
        time.sleep(delay)

    mode_inputDPC = input("\n\nPlease enter numbers only.\n\n")
    clear_screen()

    match mode_inputDPC:
        case "0": MAIN()
        case "1": dpc_engine(6, "LeftSide,B,B,B,B,RightSide", True)
        case "2": dpc_engine(8, "LeftSide,B,B,(B,B),B,B,RightSide", True)
        case "3": dpc_engine(8, "LeftSide,B,B,B,B,B,B,RightSide", True)
        case "4": dpc_engine(10, "LeftSide,LeftB,B,B,B,B,B,B,Right8B,RightSide", True)
        case "5": dpc_engine(6, "LeftSide,B,B,B,B,RightSide", False)
        case "6": dpc_engine(8, "LeftSide,B,B,(B,B),B,B,RightSide", False)
        case "7": dpc_engine(8, "LeftSide,B,B,B,B,B,B,RightSide", False)
        case "8": dpc_engine(10, "LeftSide,LeftB,B,B,B,B,B,B,Right8B,RightSide", False)
        case "9": DPC_DELETENOTE()
        case _: DPC()

def DPC_DELETENOTE():
    clear_screen()
    print('      <note tick=".*" />')
    print('      <note tick=".*" ins="1" />')
    input(f"\n\n\n\n")
    clear_screen()
    DPC()


# Github
def GITHUB():
    webbrowser.open_new('https://www.youtube.com/@churitoring')
    webbrowser.open_new('https://github.com/Churitoring/Rhythm_Game_Pattern_Maker/releases')

    countdown_steps = [
        ("Open!\nBack to Home!\n3", 1),
        ("Open!\nBack to Home!\n2", 1),
        ("Open!\nBack to Home!\n1", 1)
    ]

    for text, delay in countdown_steps:
        clear_screen()
        print(text)
        time.sleep(delay)

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