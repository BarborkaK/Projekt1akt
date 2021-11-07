from task_template import TEXTS

uzivatele = {"bob": "123" , "ann": "pass123" , "mike": "password123" , "liz": "pass123"}
oddelovac = 40 * "-"

text1 = TEXTS[0]
text2 = TEXTS[1]
text3 = TEXTS[2]
jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
print(oddelovac)
if uzivatele.get(jmeno) == heslo:
    print(f"Vítej v aplikaci, {jmeno}")
    print("Máme tři texty k analyzování.....: ")
    print(oddelovac)
else:
    print('Heslo, nebo uživatelské jméno je špatně!')
    quit()
vlozeni_cisla_textu = int(input("Vyber číslo textu(1-3) k analyzování...: "))
print(oddelovac)
if vlozeni_cisla_textu == 1:
    vybrany_text = text1
    print(text1)
    print(oddelovac)
elif vlozeni_cisla_textu == 2:
    vybrany_text = text2
    print(text2)
    print(oddelovac)
elif vlozeni_cisla_textu == 3:
    vybrany_text = text3
    print(text3)
    print(oddelovac)
else:
    print("Tato možnost neexistuje... konec... ")
    quit()
    print(oddelovac)
vybrany_text = text

# slovnik_textu = {}
cista_slova = [slovo.strip(",.\n") for slovo in vybrany_text.rstrip(' ').split(" ")]

# while '' in cista_slova:
#     cista_slova.remove('')

pocet_slov = len(cista_slova)
slova_zacinajici_na_velka_pismena = [slovo for slovo in cista_slova if slovo.istitle()]
pocet_slov_na_velka_pism = len(slova_zacinajici_na_velka_pismena)
slova_z_velkych_pismen = [slovo for slovo in cista_slova if slovo.isupper()]
pocet_slov_z_velkych_pism = len(slova_z_velkych_pismen)
slova_psana_malými_pismeny = [slovo for slovo in cista_slova if slovo.islower()]
pocet_slov_malymi = len(slova_psana_malými_pismeny)
pouze_cisla = [slovo for slovo in cista_slova if slovo.isnumeric()]
pocet_cisel = len(pouze_cisla)
cisla_z_cisel = [int(i) for i in pouze_cisla]
soucet_cisel = 0
for cislo in cisla_z_cisel:
    soucet_cisel += cislo
print(f"Ve vybraném textu je {pocet_slov} slov")
print(f"{pocet_slov_na_velka_pism} slov začíná na velká písmena")
print(f"{pocet_slov_z_velkych_pism} slov je psáno pouze velkými písmeny")
print(f"{pocet_slov_malymi} slov je psáno pouze malými písmeny")
print(f"{pocet_cisel} slov jsou čísla")
print(f"{soucet_cisel} je součet všech čísel")
print(oddelovac)
print(oddelovac)

dict_delek = {}
for slovo in cista_slova:
    delka_slova = len(slovo)
    if delka_slova in dict_delek.keys():
        dict_delek[delka_slova] += 1
    else:
        dict_delek[delka_slova] = 1

# print("Délka\nslov:|", "Výskyty:".ljust(15), "| Počet:")
print("Délka\nslov:|", f" {'Výskyty:' : <13}  {'| Počet:'}")
print(oddelovac)
poradi = [cislo for cislo in range(1,max(dict_delek.keys()) + 1)]

for delka_slov in poradi:
    opakovani = dict_delek[delka_slov]
    print(f"{delka_slov : <4} | {opakovani*'*' : <15} | {opakovani}")


