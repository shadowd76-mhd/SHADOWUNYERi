import random

def rastgele_yuruyus_simulasyonu_2D(adim_sayisi):
    """
    Belirtilen adım sayısı kadar 2D düzlemde rastgele yürüyüş simülasyonu yapar.
    
    Args:
        adim_sayisi (int): Simülasyonun kaç adım süreceği.
        
    Returns:
        tuple: Son (x, y) koordinatları ve tüm rotayı içeren liste.
    """
    x, y = 0, 0  # Başlangıç koordinatları (Orijin)

    # Yürünen tüm noktaları kaydetmek için (x, y) koordinatlarından oluşan bir liste
    yol = [(x, y)] 

    # Mümkün olan dört yön: (x değişimi, y değişimi)
    # (0, 1) = Yukarı, (0, -1) = Aşağı, (1, 0) = Sağ, (-1, 0) = Sol
    yonler = [(0, 1), (0, -1), (1, 0), (-1, 0)]  

    print(f"Başlangıç: ({x}, {y})")

    for i in range(adim_sayisi):
        # Rastgele bir yön seç
        dx, dy = random.choice(yonler)

        # Konumu güncelle
        x += dx
        y += dy
        
        # Yeni konumu yola ekle
        yol.append((x, y))

    print("-" * 30)
    print(f"Toplam {adim_sayisi} adım sonunda ulaşılan son konum: ({x}, {y})")
    print(f"Başlangıçtan uzaklık (Öklid): {(x**2 + y**2)**0.5:.2f}")
    
    # Tüm rotayı görmek isterseniz aşağıdaki satırın yorumunu kaldırın:
    # print("Yürüyüş Rotası:", yol) 
    
    return x, y, yol

# Simülasyonu 100 adım için çalıştır
rastgele_yuruyus_simulasyonu_2D(adim_sayisi=100)  
# ...existing code...
import random
from typing import List, Tuple, Optional
import math

def rastgele_yuruyus_simulasyonu_2D(adim_sayisi: int,
                                   seed: Optional[int] = None,
                                   verbose: bool = True) -> Tuple[int, int, List[Tuple[int, int]]]:
    """
    Belirtilen adım sayısı kadar 2D düzlemde rastgele yürüyüş simülasyonu yapar.

    Args:
        adim_sayisi (int): Simülasyonun kaç adım süreceği.
        seed (Optional[int]): Rastgelelik için isteğe bağlı seed.
        verbose (bool): True ise kısa sonuçları yazdırır.

    Returns:
        tuple: Son (x, y) koordinatları ve tüm rotayı içeren liste.
    """
    if seed is not None:
        random.seed(seed)

    x, y = 0, 0
    yol: List[Tuple[int, int]] = [(x, y)]
    yonler = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    if verbose:
        print(f"Başlangıç: ({x}, {y})")

    for _ in range(adim_sayisi):
        dx, dy = random.choice(yonler)
        x += dx
        y += dy
        yol.append((x, y))

    uzaklik = math.hypot(x, y)

    if verbose:
        print("-" * 30)
        print(f"Toplam {adim_sayisi} adım sonunda ulaşılan son konum: ({x}, {y})")
        print(f"Başlangıçtan uzaklık (Öklid): {uzaklik:.2f}")

    return x, y, yol

def ciz(yol: List[Tuple[int, int]], show: bool = True, filepath: Optional[str] = None) -> None:
    try:
        import matplotlib.pyplot as plt
    except Exception:
        return

    xs, ys = zip(*yol)
    plt.figure(figsize=(6,6))
    plt.plot(xs, ys, '-o', markersize=3, linewidth=1)
    plt.plot(xs[0], ys[0], 'go', label='Başlangıç')
    plt.plot(xs[-1], ys[-1], 'ro', label='Bitiş')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    if filepath:
        plt.savefig(filepath, bbox_inches='tight')
    if show:
        plt.show()
# ...existing code...
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="2D rastgele yürüyüş simülasyonu")
    parser.add_argument("--adim", type=int, default=100, help="Adım sayısı")
    parser.add_argument("--seed", type=int, default=None, help="Rastgele seed")
    parser.add_argument("--plot", action="store_true", help="Rotayı çiz")
    args = parser.parse_args()

    _, _, yol = rastgele_yuruyus_simulasyonu_2D(adim_sayisi=args.adim, seed=args.seed, verbose=True)
    if args.plot:
        ciz(yol)
# ...existing code...