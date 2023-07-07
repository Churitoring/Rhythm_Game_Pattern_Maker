import msvcrt
import time
import os
import win32api
import pygame

def START_MAIN():
    print(f"DPC Frame Maker ver. 0.0.1")
    time.sleep(0.2)
    print(f"By Churitoring\n")
    time.sleep(0.2)
    print(f"Based on \'osu! Beatmap Maker\'(OBMC)\n")
    time.sleep(0.2)
    print(f"1: 4B(Key Sound: blank)")
    time.sleep(0.05)
    print(f"2: 5B(Key Sound: blank)")
    time.sleep(0.05)
    print(f"3: 6B(Key Sound: blank)")
    time.sleep(0.05)
    print(f"4: 8B(Key Sound: blank)")
    time.sleep(0.05)
    print(f"5: 4B(Key Sound: No.0000)")
    time.sleep(0.05)
    print(f"6: 5B(Key Sound: No.0000)")
    time.sleep(0.05)
    print(f"7: 6B(Key Sound: No.0000)")
    time.sleep(0.05)
    print(f"8: 8B(Key Sound: No.0000)")
    time.sleep(0.05)

def START_SEL_BF():
    if mode_input=="1":
        START_1BF()
    if mode_input=="2":
        START_2BF()
    if mode_input=="3":
        START_3BF()
    if mode_input=="4":
        START_4BF()
    if mode_input=="5":
        START_5BF()
    if mode_input=="6":
        START_6BF()
    if mode_input=="7":
        START_7BF()
    if mode_input=="8":
        START_8BF()

#blank
def START_1BF():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"3\">"
    key3="    <track idx=\"4\">"
    key4="    <track idx=\"5\">"
    key5="    <track idx=\"6\">"
    key6="    <track idx=\"9\">"

    b = False
    prev_time = win32api.GetTickCount()

    # Received 7 keys
    key_inputs = input("Please enter 7 keys.\nLeftSide,B,B,B,B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"■ □□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ ■□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□■□ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□■ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□□ ■  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}")
    time.sleep(31536000)

def START_2BF():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"3\">"
    key3="    <track idx=\"4\">"
    key4="    <track idx=\"5\">"
    key5="    <track idx=\"6\">"
    key6="    <track idx=\"7\">"
    key7="    <track idx=\"9\">"

    b = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\nLeftSide,B,B,(B,B),B,B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"■ □□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ ■□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □■□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key4 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key5 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□■□ □  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    key6 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□□■ □  T: {t}, ms: {a}")
                elif input_char == key_list[7]:
                    key7 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□□□ ■  T: {t}, ms: {a}")
                elif input_char == key_list[8]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"
    key7+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}\n{key7}")
    time.sleep(31536000)

def START_3BF():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"3\">"
    key3="    <track idx=\"4\">"
    key4="    <track idx=\"5\">"
    key5="    <track idx=\"6\">"
    key6="    <track idx=\"7\">"
    key7="    <track idx=\"8\">"
    key8="    <track idx=\"9\">"

    b = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\nLeftSide,B,B,B,B,B,B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"■ □□□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ ■□□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □■□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□■□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□□■□ □  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□□□■ □  T: {t}, ms: {a}")
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □□□□□□ ■  T: {t}, ms: {a}")
                elif input_char == key_list[8]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"
    key7+="\n    </track>"
    key8+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}\n{key7}\n{key8}")
    time.sleep(31536000)

def START_4BF():
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

    b = False
    prev_time = win32api.GetTickCount()

    # Received 11 keys
    key_inputs = input("Please enter 11 keys.\nLeftSide,LeftB,B,B,B,B,B,B,Right8B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"■ □ □□□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ ■ □□□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ ■□□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □■□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □□■□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □□□■□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □□□□■□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □□□□□■ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[8]:
                    key9 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □□□□□□ ■ □  T: {t}, ms: {a}")
                elif input_char == key_list[9]:
                    key10 += f"\n      <note tick=\"{t}\" ins=\"1\"/>"
                    print(f"□ □ □□□□□□ □ ■  T: {t}, ms: {a}")
                elif input_char == key_list[10]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"
    key7+="\n    </track>"
    key8+="\n    </track>"
    key9+="\n    </track>"
    key10+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}\n{key7}\n{key8}\n{key9}\n{key10}")

    time.sleep(31536000)

#No.0000
def START_5BF():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"3\">"
    key3="    <track idx=\"4\">"
    key4="    <track idx=\"5\">"
    key5="    <track idx=\"6\">"
    key6="    <track idx=\"9\">"

    b = False
    prev_time = win32api.GetTickCount()

    # Received 7 keys
    key_inputs = input("Please enter 7 keys.\nLeftSide,B,B,B,B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\"/>"
                    print(f"■ □□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ ■□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□■□ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□■ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□□ ■  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}")
    time.sleep(31536000)

def START_6BF():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"3\">"
    key3="    <track idx=\"4\">"
    key4="    <track idx=\"5\">"
    key5="    <track idx=\"6\">"
    key6="    <track idx=\"7\">"
    key7="    <track idx=\"9\">"

    b = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\nLeftSide,B,B,(B,B),B,B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\"/>"
                    print(f"■ □□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ ■□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □■□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key4 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key5 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□■□ □  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    key6 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□□■ □  T: {t}, ms: {a}")
                elif input_char == key_list[7]:
                    key7 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□□□ ■  T: {t}, ms: {a}")
                elif input_char == key_list[8]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"
    key7+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}\n{key7}")
    time.sleep(31536000)

def START_7BF():
    key1="    <track idx=\"2\">"
    key2="    <track idx=\"3\">"
    key3="    <track idx=\"4\">"
    key4="    <track idx=\"5\">"
    key5="    <track idx=\"6\">"
    key6="    <track idx=\"7\">"
    key7="    <track idx=\"8\">"
    key8="    <track idx=\"9\">"

    b = False
    prev_time = win32api.GetTickCount()

    # Received 9 keys
    key_inputs = input("Please enter 9 keys.\nLeftSide,B,B,B,B,B,B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\"/>"
                    print(f"■ □□□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ ■□□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □■□□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□■□□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□■□□ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□□■□ □  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□□□■ □  T: {t}, ms: {a}")
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □□□□□□ ■  T: {t}, ms: {a}")
                elif input_char == key_list[8]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"
    key7+="\n    </track>"
    key8+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}\n{key7}\n{key8}")
    time.sleep(31536000)

def START_8BF():
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

    b = False
    prev_time = win32api.GetTickCount()

    # Received 11 keys
    key_inputs = input("Please enter 11 keys.\nLeftSide,LeftB,B,B,B,B,B,B,Right8B,RightSide,End\n").strip()
    # Convert the input string into a list
    key_list = list(key_inputs)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Adjusting the tps
    tps = float(input("Please enter tps.\n"))
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Adjusting the start time
    a_input = input("Please enter the start time.\n(default: 0ms)\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        a = int(a_input)
    except ValueError:
        a = 0
    c=a+1
    
    elapsed_time=0
    while True:
        current_time = win32api.GetTickCount()
        elapsed_time = current_time - prev_time
        if elapsed_time >= 1:
            a += elapsed_time  # Add the elapsed time to a
            prev_time = current_time  # Update with the current time
        if b==False:
            a = c
        # If there is input
        t=round(a*tps/1000)
        if msvcrt.kbhit():
            # Read the input value and print it
            input_char = msvcrt.getch().decode()
            if input_char in key_list:
                if input_char == key_list[0]:
                    key1 += f"\n      <note tick=\"{t}\"/>"
                    print(f"■ □ □□□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[1]:
                    key2 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ ■ □□□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[2]:
                    key3 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ ■□□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[3]:
                    key4 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □■□□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[4]:
                    key5 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □□■□□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[5]:
                    key6 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □□□■□□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[6]:
                    key7 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □□□□■□ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[7]:
                    key8 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □□□□□■ □ □  T: {t}, ms: {a}")
                elif input_char == key_list[8]:
                    key9 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □□□□□□ ■ □  T: {t}, ms: {a}")
                elif input_char == key_list[9]:
                    key10 += f"\n      <note tick=\"{t}\"/>"
                    print(f"□ □ □□□□□□ □ ■  T: {t}, ms: {a}")
                elif input_char == key_list[10]:
                    break
                b=True
                sound_effect.play()

            # Do not print any input other than the received value
            elif input_char not in ["\r", "\n", "\t"]:
                pass
    
    key1+="\n    </track>"
    key2+="\n    </track>"
    key3+="\n    </track>"
    key4+="\n    </track>"
    key5+="\n    </track>"
    key6+="\n    </track>"
    key7+="\n    </track>"
    key8+="\n    </track>"
    key9+="\n    </track>"
    key10+="\n    </track>"

    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{key1}\n{key2}\n{key3}\n{key4}\n{key5}\n{key6}\n{key7}\n{key8}\n{key9}\n{key10}")

    time.sleep(31536000)

pygame.mixer.init(buffer=2)
sound_file = "sound.mp3"
sound_effect=pygame.mixer.Sound(sound_file)
os.system('cls' if os.name == 'nt' else 'clear')
START_MAIN()
mode_input=input(f"\n\nPlease enter numbers only.\n\n")
os.system('cls' if os.name == 'nt' else 'clear')
START_SEL_BF()