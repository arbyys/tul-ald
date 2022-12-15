# ALD - semestrální práce 

## Adam Petříček

___

### Popis aplikace

Uživatel má na výběr z 15 možných trubek, které se použijí na generaci. Základně jsou vybrány všechny z nich. Při kliknutí na tlačítko "Vygenerovat pole" se spustí algoritmus, který generuje pole dokud není plné. Pokud na dané místo nelze umístit žádnou vhodnou dlaždici, místo se vyplní červeným křížkem.

### Popis algoritmu

Algoritmus nejdříve udělá seznam všech vybraných trubek, které jsou reprezentovány čtyřmi hodnotami `1` nebo `0`, jenž znamenají, zda trubka na tomto místě vychází z dlaždice ven, v pořadí nahoře, vpravo, dole, vlevo.

Př.: `0101` znamená, že trubka vychází z dlaždice vpravo a vlevo, což je tato trubka:

![Trubka](resources/2-example.png)

První trubku program vybere náhodně a umístí ji na náhodné místo v pracovní ploše. Při každé umístěné trubce si program ukládá všechny přilehlé prázdné dlaždice k této. Každé další místo (kromě prvního) vybírá program právě z tohoto pole přilehlých dlaždic. Program tedy začne na náhodném místě a z tohoto místa se šíří náhodně po přilehlých dlaždicích.

Jakmile algoritmus vybere vhodnou dlaždici na umístění trubky, musí ještě vybrat jakou trubku použije. Program zanalyzuje všechny okolní trubky a vytvoří masku, která reprezentuje, zda se v daném směru musí nacházet připojení (`1`), žádné připojení (`0`), nebo na tom nezáleží - je tam prázdno (`x`). Podle této masky projde pole možných trubek a vybere náhodnou, která splňuje všechny podmínky.