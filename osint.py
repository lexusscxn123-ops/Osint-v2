import requests
from PIL import Image
from PIL.ExifTags import TAGS
import os

def banner():
    print("""
██╗     ███████╗██╗  ██╗██╗   ██╗███████╗
██║     ██╔════╝╚██╗██╔╝██║   ██║██╔════╝
██║     █████╗   ╚███╔╝ ██║   ██║███████╗
██║     ██╔══╝   ██╔██╗ ██║   ██║╚════██║
███████╗███████╗██╔╝ ██╗╚██████╔╝███████║
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝

        LEXUS OSINT TOOL
    """)

def username_osint():
    username = input("Kullanıcı adı: ")

    sites = {
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}"
    }

    print("\nSonuçlar:\n")

    for site, url in sites.items():
        r = requests.get(url)
        if r.status_code == 200:
            print(f"[+] {site}: {url}")
        else:
            print(f"[-] {site}: Bulunamadı")

def exif_osint():
    path = input("Fotoğraf yolu: ")

    if not os.path.exists(path):
        print("Dosya bulunamadı")
        return

    image = Image.open(path)
    exif = image._getexif()

    if not exif:
        print("EXIF veri yok")
        return

    print("\nEXIF DATA:\n")

    for tag, value in exif.items():
        tagname = TAGS.get(tag, tag)
        print(f"{tagname}: {value}")

def menu():
    while True:
        print("""
1 - Username OSINT
2 - Fotoğraf EXIF OSINT
3 - Çıkış
""")

        secim = input("Seçim: ")

        if secim == "1":
            username_osint()

        elif secim == "2":
            exif_osint()

        elif secim == "3":
            break

        else:
            print("Hatalı seçim")

banner()
menu()