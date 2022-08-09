V rámci toho programu som sa snažil nechať počítač riešiť hru Battleships pomocou nasledujúcich algoritmov:
- DFS
- Backtracking aloritmus s využím heuristiky LCV (Least Constraining Value)
- Backtracking aloritmus s využím heuristiky MRV (Minimum Remaining Values)

Súčasťou programu je jednoduché GUI, ktoré umožňuje vykresliť niekoľko polí rozmerov 3x3, 6x6, 10x10, zvoliť algoritmus, ktorým chceme problém vyriešiť ako aj slider, ktorého posúvaním nastavujeme rýchlosť hľadania rišenie. Je možnosť zvoliť je typ poľa "Unsolavable", čo sposobí výkreslenie poľa o veľkosti 3x3, ktoré nemá riešenie. Ná záver hľadania (buď keď program našiel riešenie alebo keď prešiel všetky možnosti a riešenie nenašiel) dostaneme hlásanie o tom koľko krokov algoritmus vykonal, koľko stavov expandoval a aký čas mu to trvalo. Pre pokračovanie môžeme zvoliť ktorýkoľvek typ poľa, čím sa nám vytvoré nová prázdna plocha alebo len zvoliť jeden z algoritmov a proces hľadania sa spustí odznova.
