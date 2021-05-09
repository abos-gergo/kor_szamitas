Függvények:
    clear_console (5-6 sor):
    - Törli a console eddigi sorait, egy blank console-t eredményez.
    - Azért használom, mert így átláthatóbb marad a console a második, vagy sokadik számításnál.

    draw_line (8-9 sor):
    - Egy kötőjelekből álló sort ír ki.
    - Azért használok vonalakat, hogy átláthatóbbak legyenek a sorok.

    kor_kerulet (11-61 sor):
    - Az egyik fő függvény (a 2 közül). Egy kör kerületét tudja kiszámolni.
    - A kerületet ki tudja számolni 3 különböző adatból is (kör területe, átmérő hossza, sugár hossza).
    - Egy menüvel kezdődik a függvény, ahol ki tudjuk választani, hogy melyik adatból szeretnénk megkapni a kerületet. Az opció számát kell beírni az input-ba.
    - Amennyiben nem létező opciót ad meg a felhasználó, egy hibaüzenet után a függvénynek vége, és visszatér a main ágba. (Így lényegében újrakezdődik a program)
    - Miután kiválasztottuk, hogy melyik adatot ismerjük, a program bekéri az adatot cm-ben (vagy adott esetben cm2-ben)
    - Egy ellenőrző ciklus nézi, hogy a felhasználó használható adatot adott-e meg. Amennyiben nem, egy hibaüzenet után ismét bekéri az adatot.
    - 0, vagy annál kisebb számok nem megfelelőek a számoláshoz, így azt kiszűri a rendszer. Ha viszont üresen adjuk be az inputot, a program hibát fog jelezni, és megáll a program. (ezt nem tudtam kiszűrni)
    - Miután megkapta a program az adatot, kiszámolja, majd kiírja az eredményt.
    - Két másodpercet vár, hogy a felhasználónak egyértelmű legyen, melyik sorban van az eredmény, majd csak utána ír ki újabb üzenetet.
    - Az ENTER gomb lenyomásával folytatódik a program, így a felhasználó addig látja az eredményét, ameddig szeretné.
    - Az ENTER után törlődnek a console előzményei, majd végetér a függvény, visszatérve így a main ágba.

    kor_terulet (63-114 sor):
    - Az egyik fő függvény (a 2 közül). Egy kör területét tudja kiszámolni.
    - A területet ki tudja számolni 3 különböző adatból is (kör kerülete, átmérő hossza, sugár hossza).
    - Egy menüvel kezdődik a függvény, ahol ki tudjuk választani, hogy melyik adatból szeretnénk megkapni a területet. Az opció számát kell beírni az input-ba.
    - Amennyiben nem létező opciót ad meg a felhasználó, egy hibaüzenet után a függvénynek vége, és visszatér a main ágba. (Így lényegében újrakezdődik a program)
    - Miután kiválasztottuk, hogy melyik adatot ismerjük, a program bekéri az adatot cm-ben (vagy adott esetben cm2-ben)
    - Egy ellenőrző ciklus nézi, hogy a felhasználó használható adatot adott-e meg. Amennyiben nem, egy hibaüzenet után ismét bekéri az adatot.
    - 0, vagy annál kisebb számok nem megfelelőek a számoláshoz, így azt kiszűri a rendszer. Ha viszont üresen adjuk be az inputot, a program hibát fog jelezni, és megáll a program. (ezt nem tudtam kiszűrni)
    - Miután megkapta a program az adatot, kiszámolja, majd kiírja az eredményt.
    - Két másodpercet vár, hogy a felhasználónak egyértelmű legyen, melyik sorban van az eredmény, majd csak utána ír ki újabb üzenetet.
    - Az ENTER gomb lenyomásával folytatódik a program, így a felhasználó addig látja az eredményét, ameddig szeretné.
    - Az ENTER után törlődnek a console előzményei, majd végetér a függvény, visszatérve így a main ágba.

    main (116-132 sor):
    - A függvényben egy végtelen ismétlés van, ami biztosítja, hogy a felhasználónak ne kelljen kétszer elindítania a programot, ha kétszer is akar számolni.
    - Egy menü van a függvényben, ahol ki tudjuk választani, hogy mit akarunk kiszámolni. (kerületet, vagy területet)
    - A menüben van egy "Kilépés a programból" opció, ami quit parancs segítségével bezárja a programot, ha már nem szeretnénk használni.
    - Miután kiválasztottuk a kívánt opciót, az ahhoz tartozó függvény lesz meghívva, a további kód ott fog lefutni.
    - Ha a futtatott függvénynek vége, a main ágban az ismétlésnek köszönhetően visszatér a program az elejére, így ki tudunk számolni még valamit, ha úgy szeretnénk.