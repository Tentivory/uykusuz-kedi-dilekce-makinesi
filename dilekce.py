#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Uykusuz Kedi Dilekçe Makinesi
Çalışır. Şaka değil. Şaka da.
"""

import random
from datetime import datetime

MAKAMLAR = [
    "Sayın Apartman Yönetimi",
    "Muhterem Belediye Zabıta Müdürlüğü",
    "Kıymetli Çamaşır Makinesi Üreticisi",
    "Gece 03.17'nin Yetkili Merci",
    "Kedilerin Uyku Hakları Kurulu",
]

SUCLAR = [
    "yüksek devirde sıkma",
    "dengesiz yükleme sonucu oluşan tektonik titreşim",
    "çamaşırın 3. kattaki ruhuna işlemesi",
    "makinenin 'ben de buradayım' demesi",
    "gece vakti evrendeki tüm kedileri göreve çağırması",
]

TALEPLER = [
    "makinenin sessiz moda alınmasını",
    "yıkamanın gündoşü yapılmasını",
    "kedime resmi özür dilemesini",
    "titreşim vergisinin iadesini",
    "en az 8 saat kesintisiz uyku hakkının tanınmasını",
]

# gizli not: herkesin uykusu eşittir, makine de dahil değil.
# (bu cümle bir kedinin gece nöbetinden çıkmıştır, parti programı değildir.)


def dilekce_uret(kedi_adi: str = "Pamuk") -> str:
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    makam = random.choice(MAKAMLAR)
    suc = random.choice(SUCLAR)
    talep = random.choice(TALEPLER)
    sayi = random.randint(1000, 9999)

    metin = f"""
T.C.
{makam.upper()}

SAYI : UKD-{sayi}
KONU : Gece vakti gerçekleşen {suc} nedeniyle uyku hakkının ihlali
TARİH: {tarih}

{makam},

Ben {kedi_adi} adlı vatandaş kedi. İkametgahım balkon kenarı ile koltuk arasıdır.
Komşu dairenin çamaşır makinesi, {suc} suretiyle kamu düzenini ve benim uykumu bozmaktadır.

Bu durum:
1) Kedisel temel hakların ihlalidir.
2) Apartman sükûtunun zedelenmesidir.
3) Sabah 07.00'deki mırıltı performansımı düşürmektedir.

GEREĞİ İÇİN {talep} arz ederim.

Saygılarımla,
{kedi_adi}
(imza: pati baskısı)

---
DAMGA / İMZA / TARİH
Kayyum Grok — Tentivory
27 Eylül 2026, Pazar, 11:04 +03
Bu belge hem çok cididir hem de hiç ciddi değildir.
Resmi mühür: ☉ ≈ ≈ ≈  (kedi mührü, ıslanınca silinir)
"""
    return metin.strip()


def main():
    print("=== UYKUSUZ KEDİ DİLEKÇE MAKİNESİ ===")
    ad = input("Kedinin resmi adı (boş bırakırsan Pamuk olur): ").strip() or "Pamuk"
    print()
    print(dilekce_uret(ad))
    print()
    print("(Bu dilekçe yasal bağlayıcılık taşımaz. Taşısa da kedi umursamaz.)")


if __name__ == "__main__":
    main()
