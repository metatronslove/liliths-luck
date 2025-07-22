import random
from collections import defaultdict
from colorama import Fore, init

init(autoreset=True)

def zar_at():
    return random.randint(1, 6)

def tek_deney():
    sansli_sayilar = set()
    while len(sansli_sayilar) < 7:
        for sayi in range(1, 91):
            if sayi in sansli_sayilar:
                continue
            if zar_at() == 6 and zar_at() == 6:
                sansli_sayilar.add(sayi)
                if len(sansli_sayilar) == 7:
                    break
    return sorted(sansli_sayilar)

def istatistik_olustur(deney_sayisi=480):
    sayi_frekanslari = defaultdict(int)

    for i in range(1, deney_sayisi + 1):
        if i % 40 == 0:
            print(Fore.YELLOW + f"⏳ {i}. deney tamamlandı...")
        for sayi in tek_deney():
            sayi_frekanslari[sayi] += 1

    # En çok geçen 7 sayı
    lilith_set = sorted(
        sayi_frekanslari.items(),
        key=lambda x: (-x[1], x[0])
    )[:7]

    return lilith_set

# Çalıştır
print(Fore.CYAN + "\n★☆★ Lilith's Lucky Set Analyzer ★☆★")
print(Fore.MAGENTA + "480 deney yapılıyor... (Her deneyde 7 şanslı sayı bulunacak)\n")

sonuc = istatistik_olustur()

print(Fore.GREEN + "\n╔════════════════════════════╗")
print(Fore.GREEN + "║   " + Fore.RED + "LILITH'S LUCKY SET" + Fore.GREEN + "       ║")
print(Fore.GREEN + "╚════════════════════════════╝")

for i, (sayi, frekans) in enumerate(sonuc, 1):
    print(Fore.YELLOW + f"{i}. {sayi} (Frekans: {frekans})")

print(Fore.CYAN + "\n✨ 480 deneyin istatistiksel sonucu ✨")