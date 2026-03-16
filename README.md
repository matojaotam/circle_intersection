# Kružnice – průnik dvou kružnic

## Popis projektu

Cílem projektu je vytvořit Python program, který zjistí, zda se dvě kružnice protínají, a pokud ano, kolik mají průniků. Program pracuje se dvěma kružnicemi definovanými jejich středem `(x, y)` a poloměrem `r`.

Program:

* vypočítá vzdálenost mezi středy kružnic,
* porovná ji se součtem a rozdílem poloměrů,
* rozhodne, zda mají kružnice **0, 1 nebo 2 průniky**,
* vrátí výsledek ve formě slovníku,
* vypíše výsledek do terminálu,
* vykreslí obě kružnice do grafu pomocí knihovny `matplotlib`.

## Struktura projektu

Projekt je rozdělen do tří souborů:

### `circle_stats.py`

Obsahuje matematické funkce:

* `radius_sum(r1, r2)` – vrátí součet poloměrů
* `euclid_distance(x1, y1, x2, y2)` – vypočítá Euklidovskou vzdálenost mezi dvěma body
* `has_intersection(circle_1, circle_2)` – určí, zda se kružnice protínají a kolik mají průniků

Výstup funkce je slovník například:

```
{"is_intersection": True, "intersections_count": 2}
```

### `circles_intersection_draw.py`

Obsahuje funkci:

* `draw_data(circle_1, circle_2)`

Tato funkce vykreslí obě kružnice do grafu pomocí knihovny `matplotlib`.

### `circle_intersection.py`

Hlavní skript programu, který:

* definuje dvě kružnice,
* zavolá funkci `has_intersection`,
* vypíše výsledek do terminálu,
* zavolá funkci pro vykreslení kružnic.

## Matematický princip

Nejdříve se vypočítá vzdálenost mezi středy kružnic:

```
d = √((x2-x1)^2 + (y2-y1)^2)
```

Poté se porovnává s:

```
r_sum = r1 + r2
r_diff = |r1 - r2|
```

Možné situace:

| Podmínka           | Výsledek                       |
| ------------------ | ------------------------------ |
| d > r1 + r2        | kružnice se neprotínají        |
| d = r1 + r2        | jeden průnik (dotyk zvenku)    |
| r_diff < d < r_sum | dva průniky                    |
| d = r_diff         | jeden průnik (dotyk zevnitř)   |
| d < r_diff         | jedna kružnice je uvnitř druhé |

## Instalace závislostí

Pro vykreslení grafu je potřeba nainstalovat knihovnu:

```
pip install matplotlib
```

nebo

```
uv add matplotlib
```

## Spuštění programu

Program spustíš příkazem:

```
python circle_intersection.py
```

Po spuštění program vypíše informaci o průniku kružnic a zobrazí graf s jejich vykreslením.
