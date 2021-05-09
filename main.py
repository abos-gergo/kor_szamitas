import math
import time
import os

def clear_console():
    os.system('cls')

def draw_line():
    print('----------------------------------------------------------')

def kor_kerulet():
    print('Kör kerületszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Terület')
    print('2. Átmérő hossza')
    print('3. Sugár hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()
    if opcio == 1:
        terulet : float = 0
        while terulet <= 0:
            terulet : float = float(input('Adja meg a kör területét! (cm2)'))
            if terulet <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        radius = math.sqrt(terulet / math.pi)
        kerulet : float = 2 * radius * math.pi
        print(f'A kör kerülete: {kerulet} centiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        diameter : float = 0
        while diameter <= 0:
            diameter : float = float(input('Adja meg a kör ármérőjének hosszát! (cm)'))
            if diameter <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        radius = diameter / 2
        kerulet : float = 2 * radius * math.pi
        print(f'A kör kerülete: {kerulet} centiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 3:
        radius : float = 0
        while radius <= 0:
            radius : float = float(input('Adja meg a kör sugarának hosszát! (cm)'))
            if radius <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        kerulet : float = 2 * radius * math.pi
        print(f'A kör kerülete: {kerulet} centiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def kor_terulet():
    print('Kör területszámítása:')
    print('Melyik adatot ismeri?')
    print('1. Kerület')
    print('2. Átmérő hossza')
    print('3. Sugár hossza')
    opcio : int = int(input('Írd be az opció számát! '))
    draw_line()

    if opcio == 1:
        kerulet : float = 0
        while kerulet <= 0:
            kerulet : float = float(input('Adja meg a kör kerületét! (cm)'))
            if kerulet <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        radius : float = kerulet / (2 * math.pi)
        terulet : float = radius ** 2 * math.pi
        print(f'A kör területe: {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()

    elif opcio == 2:
        diameter : float = 0
        while diameter <= 0:
            diameter : float = float(input('Adja meg a kör átmérőjének hosszát! (cm)'))
            if diameter <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        radius : float = diameter / 2
        terulet : float = radius ** 2 * math.pi
        print(f'A kör területe: {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    elif opcio == 3:
        radius : float = 0
        while radius <= 0:
            radius : float = float(input('Adja meg a kör sugarának hosszát! (cm)'))
            if radius <= 0:
                print('Ez nem egy valós adat! Kérem adjon meg egy használhatót!')
                draw_line()
        terulet : float = radius ** 2 * math.pi
        print(f'A kör területe: {terulet} négyzetcentiméter')
        time.sleep(2)
        input('Nyomj "ENTER"-t a folytatáshoz!')
        clear_console()
    else:
        print('Ez az opció nem létezik! Visszatérés a program elejére...')
        time.sleep(2)
        clear_console()

def main():
    print("Program a kör kerületének és területének kiszámolására.")
    draw_line()
    while True:
        print('Mit szeretne tenni?')
        print('1. Kerület kiszámolása')
        print('2. Terület kiszámolása')
        print('3. Kilépés a programból')
        opcio : int = int(input('Adja meg az opció számát: '))
        draw_line()
        if opcio == 1:
            kor_kerulet()
        elif opcio == 2:
            kor_terulet()
        elif opcio == 3:
            print('Kilépés a programból...')
            quit()

if __name__ == "__main__":
    main()