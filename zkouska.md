# ALD zkouška - poznámky

### 1. Vnější a vnitřní paměť

- bruh

___

### 2. Datové typy a jejich rozdělení

- pojmenování pro množinu hodnot a sadu operací
- **dělení:**
    - jednoduché (int)
        - mají definovanou rovnost, nerovnost, porovnávání (>, <=, ...)
        - v paměti je uložena přímo hodnota
        - **ordinální**
            - hodnota má předchůdce a následovníka
            - pozici lze číselně ohodnotit
            - např. integer, boolean
            - dále interval, enum
        - **neordinální**
            - např. reálná čísla
            - ztráta přesnosti při převodu na ordinální
    - strukturované (pole)
    - abstraktní (FIFO, halda)
- konstanty - nelze měnit za běhu, na rozdíl od proměnných (jinak mají vše stejné)
___

### 3. Strukturované DT, co víte o polích a řetězcích

- skupina jednodušších dat. typů
- poskytují prostředky pro práci s prvky
- typicky string, array
- **array:**
    - pevný počet položek stejného typu
    - rozlišuje je index (unique)
    - existuje jednoznačné přiřazení index -> položka
    - index pole = ordinální typ (většinou int)
    - lze udělat dynamické pole - buď pointer, nebo přímá podpora jazyku
    - pole indexované řetězcem = mapa / tabulka
- **string**
    - pole charů (znaků)
    - OOP jazyky mají String jako třídu
    - lze k němu přistupovat buď:
        - pomocí pointerů
            - `\0` jako konec - v C
        - jako k poli
        - objektově

___

### 4. ADT - co to je, které znáte, výhody, zákl. operace nad ADT kontejnery

- implementačně nezávislá specifikace struktury dat s výčtem povolených operací
- jejich počet položek se může za běhu měnit
- používají se, když přestanou stačit základní typy
- často implementovány nativně v jazyku nebo v knihovnách
- výhody:
    - snadné používání pomocí metod
    - implementace je programátorovi skryta
- všechny lze označit jako kontejnery
- vyžadované operace:
    - vytvoření prázdného (init)
    - zjištění počtu prvků (size)
    - přístup k prvku (top)
    - vložení prvku (insert)
    - odstranění prvku (pop)
    - vymazání všech prvků (clear)
- známé ADT:
    - ukazatel (pointer)
    - zásobník (stack, LIFO)
    - fronta (queue, FIFO)
    - tabulka (map)
    - seznam (list)
    - strom (tree)
    - množina (set)

___

### 5. Kritéria pro rozčlenění ADT, typ ukazatel
- kritéria:
    - statické / dynamické (v závislosti na počet prvků)
    - homogenní / nehomogenní (různost prvků)
    - lineární / nelineární (existence bezprostředního následníka)
        - lineární = pole, nelineární = stromg
- **ukazatel (pointer):**
    - základním stavebním kamenem v C pro dynamické datové struktury
    - uchovává adresu prvku z paměti
    - adresa může ukazovat do libovolné části paměti (i do paměti, která nám nepatří)
    - typ ukazatele určuje jeho datový typ (velikost, jak daleko od adresy čte)

___

### 6. Popište LIFO, FIFO - vše o co nich víte
- **LIFO:**
    - zásobník
    - homogenní, lineární, dynamický
    - odebírání z vrcholu, vkládání na vrchol
    - odložení informace, výběr v opačném pořadí
    - lze implementovat pomocí pole nebo linked-listu
    - operace: create, push, pop, top
- **FIFO:**
    - homogenní, lineární, dynamický
    - odebírání z vrcholu, vkládání na spod
    - fronta v obchodě
    - lze implementovat pomocí pole nebo linked-listu
    - operace: create, push, pop, top

___

### 7. Popište Kruhový buffer - princip, vlastnosti,možnost použití atd.

- speciální příklad FIFO
- vyrovnávací pamět
- obsahuje fixní pole a dva ukazatele:
    1) ukazatel na první obsazený prvek
    2) ukazatel na první volný prvek
- při odebrání prvku se ikrementuje first a původní first se uvolní
- celý proces je v kruhu
- čtení i odstranění má O(1)

___

### 8. Popište ADT Seznam, rozdíl oproti LIFO (resp. FIFO)

- homogenní, lineární, dynamický
- zobecnění LIFO a FIFO
- data lze přidávat a odebírat kamkoliv
- definujeme ukazovátko na místo, se kterým prvkem zrovna chceme pracovat
- **Linked-list**
    - nejčastější implementace seznamu
    - prvky nejsou v paměti za sebou, ale jsou náhodně rozmístěny s odkazy na další / předchozí prvek
    - jednosměrný / dopředný / obousměrný / kruhový
    - operace: create, insert, remove, isEmpty, search, size, clear
    - oproti poli má pomalejší indexování, ale rychlejší vkládání / mazání

___

### 9. Popište ADT Heap - princip, vlastnosti,možnost použití

- halda
- strom, který splňuje vlastnosti haldy
- pokud B je potomek A, poté:
    - h(A) >= h(B) = max-heap
    - nebo
    - h(A) <= h(B) = min-heap
- v kořenu je vždy prvek s největší (nejmenší) hodnotou
- chová se jako prioritní fronta
- lze použít i binární haldu
    - u ní se přidává pomocí vložení nového prvku na spodní úroveň haldy
    - pokud není na správném místě, prohodí se s příslušným rodičem a proces se opakuje
___

### 10. Popište ADT Dynamické pole, srovnání, princip, výhody atd.

- implementováno jazykem, datový kontejner nad polem
- eliminuje nedostatek pole - fixní velikost
- vnitřně implementováno jako pole fixní délky 
- při naplnění kapacity se vytvoří nové pole (cca 2x větší)
- do něj se prvky překopírují a původní se dealokují
- opačný postup (uvolnění paměti) při velké neobsazenosti
___

### 11. ADT Množina - co o něm víte

- nemá garanci pořadí prvků
- má garanci jedinečnosti prvků
- implementována jako seznam bez reference na aktuální prvek
- při přidání nového prvku se musí hlídat unikátnost
- není efektivní
- efektivnější způsob - hashovací tabulka

___

### 12. Definice algoritmu, jeho vlastnosti

- postup, jak řešit daný problém, abychom dospěli od vstupních dat k požadovanému výsledku
- skládá se z jednotlivých přesně definovaných kroků (příkazů)
- vlastnosti:
    - hromadnost - pracuje nad obecnou množinou dat
        - problémy se liší pouze vstupními hodnotami
        - není pouze pro jeden problém, ale na mnoho problémů
    - determinovanost - každý stav je jednoznačně určen z předchozího
        - je pevně zaručeno, jaký další krok bude následovat
        - neobsahuje žádné (pseudo)náhodné křižovatky
    - konečnost - pro konečnou množinu dat dojde k výsledku (v rozumném čase)
        - musíme brát do úvahy množství dat a potřebný čas na provedení jednotlivých kroků
    - korektnost
        - výpočet končí správným výsledkem
- dělení:
    - iterativní / rekurzivní
    - deterministické / nedeterministické
        - deterministické - má v každém kroku jedinou možnost, jak pokračovat
    - sériové / paralelní / distribuovaný
___

### 13. Co víte o složitosti algoritmu ?

- rychlost strojů se měří v FLOPS (floating point operations per second)
- asymptotická složitost = algoritmu jednoznačně přiřazená rostoucí funkce, charakterizující počet operací algoritmu v závislosti na rostoucím rozsahu vstupních dat
- chceme, aby funkce byla co nejpomaleji rostoucí
- vypočteme ji pomocí sečtení všech elementárních operací, jako např:
    - porovnání dvou hodnot
    - aritmetické operace
    - přesun v paměti
- výpočet lze zjednodušit pomocí počítání pouze operací nad daty
- indexování v poli: O(N)
- vyhledávání v seřazeném poli, půlení intervalu: O(log2(N))
- seřazení pole merge-sortem: O(N*log(N))
- problém obchodního cestujícího: O(2^N)
- složitosti lze pojmenovat - konstatní, logaritmická, kvadratická, exponencionální, faktoriálová...
- amortizovaná složitost:
    - určuje složitost jako průměr v sekvenci nejhoršch případů
    - je zaručená
    - příklad u dynamického pole - musí se brát do úvahy realokace i vkládání na index a to zprůměrovat
___

### 14. Co víte o rekurzi a backtracingu?

- **rekurze** = program volá sám sebe
- použít rekurzi není vždy vhodné
    - každé vyvolání podprogramu způsobí mnoho nežádoucích kroků jako:
        - uložení proměnných do zásobníku
        - předání parametru a návratové adresy
        - skok do podprogramu
        - uvolnění lok. proměnných
        - návrat z podprogramu
- rekurze vždy jde převést do iterativní podoby
    - dělá to i kompilátor
- rekurzi lze optimalizovat:
    - zefektivnit opakované volání se stejným vstupem
    - ukládání spočítaných mezivýsledků
    - hashovací tabulka
- **backtracking**
- prohledávání s návratem
- pokud se dostaneme do stavu, kde nelze pokračovat dále, vrátíme se do předchozího stavu a zkusíme jiné řešení
- typický příklad - problém pěti dam, ALD semestrálka

___

### 15. Sorting - co to je, jejich dělení podle typu dat, BogoSort, zajíci a želvy

- chceme data seřadit (uspořádat) dle určitého pravidla
- dělení podle dat:
    - vnitřní - pro data, která lze uchovat v RAM
    - vnější - pro rozsáhlá data, které se načítají z disku
- další dělení:
    - stabilní / nestabilní
        - podle schopnosti zachovat pořadí strukturovaných záznamů se stjným klíčem
        - z většiny algoritmů lze udělat stabilní pomocí další datové struktury
    - přirozený / nepřirozený
        - podle rychlosti na datech, která už jsou skoro nebo úplně seřazená
- **BogoSort**
    - teoretický algoritmus, nejhorší možné řešení
    - zkouší náhodné pořadí prvků dokud nejsou seřazeny
    - O(N*N!)
- **zajíci a želvy**
    - probém, že vysoké hodnoty probublají na svou pozici rychle, ale nízké hodnoty se posunou pouze o jednu pozici za iteraci
    - vyskytuje se u BubbleSortu, řeší ho CoctailSort
___

### 16. Popište princip ShakerSortu a HeapSortu

- **ShakerSort**
    - vylepšení BubbleSortu
    - řazení pole v obou směrech
    - řeší problém zajíců a želv
    - hlavní iterační cyklus proběhne jen n/2 krát
    - složitost: O(N^2)
- **HeapSort**
    - řazení binární haldou
    - složitost: O(N * log N)
    - v průměru pomalejší než QuickSort, horší možnost paralelizace
    - při využití vstupního pole pro haldu, nemá žádné další paměťové nároky
    - vhodnější pro rozsáhlé kolekce neznámých dat
    - nejdříve se vybere z vytvořené haldy vezme kořen (první prvek posloupnosti)
    - halda se rekonstruuje ze zbývajících uzlů
    - nový kořen se umístí na začátek posloupnosti a proces se opakuje

___

### 17. Popište princip SelectSortu a BubbleSortu

- **SelectSort**
    - řazení výběrem
    - složitost: O(N^2)
    - snadná implementace
    - vnitřní, nestabilní, nepřirozený
    - z nesetříděné posloupnosti vybere vždy nejmenší prvek a umístí ho na konec již setříděné posloupnosti
- **BubbleSort**
    - správné prvky probublávají na konec (začátek) množiny
    - složitost: nejhorší O(N^2), nejlepší O(N)
    - vnitřní, stabilní, přirozený
    - pomalejší než InsertSort
    - obsahuje problém zajíců a želv
    - dva sousední prvky se porovnávají a v případě nutnosti se prohodí
___

### 18. Popište princip InsertSortu a QuickSortu

- **InsertSort**
    - jednoduchá implementace
    - efektivní na malých množinách
    - složitost: nejhorší O(N^2), nejlepší O(N)
    - dokáže řadit nové prvky, co přicházejí na vstup
    - vnitřní i vnější, stabilní, přirozený
    - dobrý na testování seřazenosti dat
    - pracuje na principu vkládání prvku na správné místo
        - na to využívá pomocný prvek (většinou nultý prvek posloupnosti)
    - každý prvek posouvá doleva (porovnává se všemi, co potká), dokud není na své správné pozici
- **QuickSort**
    - využívá princip Rozděl a Panuj
    - pracuje s vybraným pivotem
        - může být první / poslední prvek
        - náhodný prvek
        - medián pole
    - podle výběru pivota se určí složitost algoritmu
    - složitost: nejhorší O(N^2), průměrná O(N * log(n))
    - na (pseudo)náhodných datech průměrně nejrychlejší z obecných algoritmů
    - vnitřní, nestabilní, nepřirozený
    - rekurzivní
    - princip:
        - zvolí pivota
        - pole se projde zleva, dokud nenarazíme na větší prvek než pivot
        - pole se projde zprava, dokud nenarazíme na menší prvek než pivot
        - tyto dva prvky vyměníme
        - postup se opakuje
___

### 19. Popište princip MergeSortu a CombSortu

- **MergeSort**
    - využívá princip Rozděl a Panuj
    - složitost: O(N * log(N))
    - paralelizovatelný, vyšší výkon na sekvečních médiích
    - vyšší paměťové nároky - potřebuje odkládácí ADT
    - implicitní řazení v některých jazycích
    - princip:
        - rozdělí množinu na dvě podmnožiny
        - rekurzivně (MergeSortem) seřadí každou vzniklou množinu
        - obě seřazené množiny sloučí
- **CombSort**
    - vylepšení BubbleSortu
    - řeší problém zajíců a želv
    - zavádí přírůstek (který se postupně snižuje)
    - neporovnávají se prvky přímo vedle sebe, ale prvky s mezerou o hodnotě přírůstku
    - na konci je z něj klasický BubbleSort
    - díky skoku se eliminují želvy
___

### 20. Vyhledávání, oč jde, zákl. pojmy, rozdíl mezi lieárním a binárním vyhledáváním

- hledání klíče `k` v množině `S`
- klíč k = query / dotaz
- množina S = search space / prohledávaný prostor
- podle typu prostoru zvolíme vhodný algoritmus
- dělení prostoru:
    - statický
        - velikost v čase je konstantní
        - změna vytvoří jeho novou verzi
        - př.: telefonní seznam, kniha
    - dynamický
        - velikost se v čase mění
        - náročnější implementace
        - př.: většina ADT
- dělení vyhledávání:
    - lineární:
        - jednoduchá implementace
        - postupné procházení všech prvků, dokud nenajdeme daný klíč
        - složitost: O(N)
        - pracuje na obecné - neseřazené množině
    - binární
        - půlení intervalu
        - prostor musí být uspořádaný
        - složitost: O(log(n))
    - binární dělení se vyplatí až když hledáme opakovaně několik různých hodnot
___

### 21. Binární a interpolační vyhledávání

- binární vyhledávání - data se musí nejprve seřadit
- poté se jede z vrchu a při každém kroku se nám množina výsledků vydělí dvěma
- **interpolační vyhledávání**
    - varianta binárního vyledávání
    - pro případy, kdy jsou hodnoty kromě seřazenosti také rovnoměrně rozložené
    - podle vzorce se odhaduje pozice prvku
    - příklad - vyhledávání ve slovníku

___

### 22. Binární vyhledávací stromy - vlastnosti, metody procházení, vkládání a odstranění prvku

- druh binárního stromu
- každý uzel má vlevo menší hodnotu než je on sám a vpravo větší hodnotu než je on sám
- vhodný pro hledání určitého klíče, nebo minima / maxima
- efektivní pro online řazení (realtime)
- při vkládání prvku nejdříve najdeme rodiče a poté vložíme doleva nebo doprava
- musíme implementovat vyhledávací metodu
- pokud chceme uzel odstranit a má potomky, musíme potomky vhodně přemístit

___

### 23. Vyvažování stromů - co to je, proč to je, co je bal a rotace

- vyvážený strom má hloubku log2(N)
- složitost vyhledávání v něm je tedy log(N)
- naopak nevyvážený strom se rozšiřuje pouze do jedné strany
- stromy chceme vyvážit pro větší efektivitu operací
- bal = faktor vyváženosti 
    - `bal(u) = h[l] - h[r]`
    - bal vyváženého stromu je -1, 0 nebo 1
- stromy se vyvažují pomocí rotací
- autovyvažující stromy
    - hloubka levého a pravého podstromu se liší max o 1
- při přidávání nového prvku:
    - kontroluje se bal všech jeho předků směrem ke kořeni
    - pokud bal je jiný než -1, 0, 1, musíme provést příslušnou rotaci
        - pokud bal(P) = 2 a bal(L) = 1: **R rotace**
        - pokud bal(P) = 2 a bal(L) = -1: **LR rotace**
        - pokud bal(P) = -2 a bal(R) = 1: **RL rotace**
        - pokud bal(P) = -2 a bal(R) = -1: **L rotace**

___

### 24. Hashování - základní terminologie, princip, asociativní a adresní vyhledávání, hašovací funkce + kolize

- hash = otisk
- asociativiní vyhledávání
    - používá se např. binární strom
    - hledá se určitý klíč postupným porovnáváním
    - složitost: O(log(n))
- adresní vyhledávání
    - klíč je přímo adresou v paměti
    - počet klíču určuje velikost indexu
    - složitost: O(1)
- pomocí hashování lze adresu vypočítat z hledaného klíče
- hashování je kompromis mezi rychlostí a spotřebou paměti
- při hashování vstup projde určitou hashovací funkcí
- je nutné vyřešit kolize - pro různé vstupy nám vyjde stejný výstup
- hashovací funkce je zobrazení z množiny klíčů K do množiny adres A
- ideální hashovací funkce je co nejrychlejší, využívá rovnoměrně adresní prostor a generuje minimum kolizí
- je lepší se s kolizemi smířit a efektivně je řešit, než hledat funkci, která negeneruje kolize
- kryptografická hashovací funkce 
    - velmi výpočetně náročné, chovají se jako ideální hashovací funkce
    - vždy je jednosměrná - nelze určit vstup podle výstupu
    - pro dva různé vstupy budou vždy dva různé výstupy

___

### 25. Zřetězené hashování, otevřené hashování, linear probing, double hashing - principy, výhody/nevýhody atd.

- **zřetězené hashování:**
- adresy v tabulce obsahují lineární seznamy
- při kolizi prvek zůstává na své pozici, přidá se na konec seznamu
- při hledání musíme navíc ještě procházet seznam na příslušné pozici
- **otevřené hashování:**
- při kolizi pomocí určité metody prohledáváme další prvky, dokud nenarazíme na volný prvek
- při vyhledávání prvku používáme stejnou metodu
- metody:
    - linear probing
        - prvek vložíme o n pozic dál na další volnou pozici
    - double hashing
        - použije se druhá hashovací funkce

___

### 26. Prohledávání řetězců - terminologie, princip, přirozené prohledávání, KMP, chybová funkce

- hledám vzor P uvnitř textu T
- textové editory, vyhledávání na webu...
- podřetězec - `S[i:j]`
- prefix - `S[O:i]`
- suffix - `S[j:m-1]`
- **přirozené vyhledávání:**
    - postupně procházíme celý řetězec a testujeme, zda na pozici nezačíná hledaný řetězec
    - složitost: nejhorší O(m*n), průměrná O(m+n)
    - je rychlý, pokud je abeceda textu velká
    - pomalý pro malou abecedu - binární soubory
    - lze zrychlit pomocí eliminace opakovaného procházení již prohledaných částí
- **KMP (Knuth-Morris-Pratt)**
    - stejný princip jako u přirozeného
    - složitost: O(m+n)
    - nikdy se nevrací ve vstupním textu
        - vhodné pro sekvenční zpracování velkého množství dat
    - pokud se vyskytne neshoda mezi textem a vzorem:
        - hledáme maximální možný posun, aby se nemusely porovnávat části řetězce znovu
        - posun = délka největšího prefixu `P[O:j-1]`, který je suffixem `P[1:j-1]`
    - analýzu prefixů a suffixů lze provést předem
- chybová funkce:
    - délka nejdelšího prefixu `P[0:k]`, který je zároveň suffixem P[1:k]
___

### 27. Prohledávání řetězců - Boyer-Moore, Rabin-Karp - princip, srovnání

- **Boye-Moore**
    - hledáme zrcadlově
    - hledáme, aby se charakter z prohledávaného textu shodoval s posledním charakterem hledané fráze
    - složitost: nejhorší O(n*m + A)
    - rychlý pro velkou, pomalý pro malou abecedu
        - v případě totožné abecedy je B-M rychlejší než přirozené
    - nejdříve musíme udělat preprocesing všech znaků hledané fráze
        - pro každý znak určíme jeho nejvyšší index v hledané frázi
        - pro všechny ostatní znaky to bude délka hledané fráze
    - začneme vyhledávat na znaku, který se nachází stejně daleko od začátku prohledávaného textu, jako je délka hledané fráze
    - pokud se znaky neshodují, přeskočíme dopředu o příslušnou hodnotu z tabulky určenou preprocesingem
    - jakmile najdeme shodu, postupujeme v opačném směru charakter po charakteru
        - pokud najdeme neshodu, znovu přeskočíme dopředu
- **Rabin-Karp**
    - využívá princip hashování
    - vypočte hash pro hledanou frázi a pro každý podřetězec prohledávaného textu, který má stejnou délku jako hledaná fráze
    - poté procházíme hashe všech podřetězců a porovnáváme je s hashem hledané fráze
        - v případě shody ještě manuálně musíme ověřit tyto dva řetězce - ochrana proti kolizím
    - je nutno zvolit vhodnout hashovací fci
        - prvočíslo q (velikost hashovacího prostoru)
            - čím větší, tím menší pravděpodobnost kolizí
        - základ d
        - nenumerické znaky se převedou na čísla pomocí ascii tabulky
        - lze využít hornerovo schéma 
    - pomalejší než KMP
    - lze rozšířit na vyhledávání více vzorů najednou
    - efektivní v detekci plagiátů