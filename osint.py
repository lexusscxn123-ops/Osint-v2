#!/usr/bin/env python3
import os
import json
import urllib.request
import urllib.parse
import socket
import dns.resolver
import whois

# ------------------- BANNER -------------------
def banner():
    os.system("clear" if os.name == "posix" else "cls")
    b = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║     ██╗     ███████╗██╗  ██╗██╗   ██╗███████╗    ██████╗ ███████╗███╗   ██╗ ║
║     ██║     ██╔════╝╚██╗██╔╝██║   ██║██╔════╝    ██╔══██╗██╔════╝████╗  ██║ ║
║     ██║     █████╗   ╚███╔╝ ██║   ██║███████╗    ██████╔╝█████╗  ██╔██╗ ██║ ║
║     ██║     ██╔══╝   ██╔██╗ ██║   ██║╚════██║    ██╔══██╗██╔══╝  ██║╚██╗██║ ║
║     ███████╗███████╗██╔╝ ██╗╚██████╔╝███████║    ██║  ██║███████╗██║ ╚████║ ║
║     ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ║
║                                                                              ║
║                    LEXUS OSINT FRAMEWORK - BY LEXUS.                         ║
║                                    OSINT Tool v2.0                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
    print(b)

# 1. IP SORGULA (ip-api.com)
def ip_api(ip):
    print("\n[*] IP sorgulaniyor...")
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"
        req = urllib.request.Request(url, headers={'User-Agent': 'Lexus-OSINT'})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
        
        if data.get('status') == 'success':
            return f"""
┌─────────────────────────────────────────────┐
│ IP BILGILERI                                 │
├─────────────────────────────────────────────┤
│ IP          : {data.get('query', '-')}
│ Ulke        : {data.get('country', '-')} ({data.get('countryCode', '-')})
│ Sehir       : {data.get('city', '-')}
│ Bolge/Ilce  : {data.get('regionName', '-')}
│ Posta Kodu  : {data.get('zip', '-')}
│ Koordinat   : {data.get('lat', '-')}, {data.get('lon', '-')}
│ Zaman       : {data.get('timezone', '-')}
│ ISP         : {data.get('isp', '-')}
│ Organizasyon: {data.get('org', '-')}
│ AS          : {data.get('as', '-')}
└─────────────────────────────────────────────┘"""
        else:
            return f"[!] Hata: {data.get('message', 'Bilinmiyor')}"
    except Exception as e:
        return f"[!] Hata: {str(e)}"

# 2. EMAIL VERI SIZINTISI (demo)
def email_breach_api(email):
    print("\n[*] Email sizinti kontrolu yapiliyor...")
    demo_siteler = [
        "Adobe (2013) - 153M kullanici",
        "LinkedIn (2016) - 164M kullanici",
        "Dropbox (2012) - 68M kullanici",
        "Twitter (2018) - 5.4M kullanici",
        "Canva (2019) - 137M kullanici"
    ]
    siteler_str = ""
    for s in demo_siteler:
        siteler_str += f"\n  • {s}"
    
    return f"""
┌─────────────────────────────────────────────┐
│ EMAIL SIZINTI BILGILERI                      │
├─────────────────────────────────────────────┤
│ Email       : {email}
│ Domain      : {email.split('@')[-1]}
│ Sizinti Sayisi: {len(demo_siteler)} veritabaninda bulundu
│                                              │
│ Bulundugu Sizintiler:{siteler_str}
│                                              │
│ [!] NOT: Demo veridir. Gercek API icin      │
│     leak-lookup.com veya HIBP               │
└─────────────────────────────────────────────┘"""

# 3. USERNAME SOSYAL MEDYA
def username_social_api(username):
    print("\n[*] Sosyal medya araniyor...")
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Pinterest": f"https://pinterest.com/{username}",
        "Twitch": f"https://twitch.tv/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}"
    }
    
    sonuc = f"""
┌─────────────────────────────────────────────┐
│ SOSYAL MEDYA ARAMA: {username}                │
├─────────────────────────────────────────────┤"""
    
    for platform, url in platforms.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=5) as r:
                if r.status == 200:
                    sonuc += f"\n│ ✓ {platform:<12} : VAR                               │"
                else:
                    sonuc += f"\n│ ✗ {platform:<12} : YOK                               │"
        except:
            sonuc += f"\n│ ✗ {platform:<12} : YOK                               │"
    
    sonuc += """
└─────────────────────────────────────────────┘"""
    return sonuc

# 4. TELEFON NUMARASI (demo)
def phone_api(phone):
    print("\n[*] Telefon numarasi sorgulaniyor...")
    return f"""
┌─────────────────────────────────────────────┐
│ TELEFON BILGILERI                            │
├─────────────────────────────────────────────┤
│ Numara      : {phone}
│ Ulke        : Turkiye (+90)
│ Gecerli     : Evet (demo)
│ Operator    : Turkcell/Vodafone/TurkTelekom
│ Tip         : Mobil
│ Lokasyon    : Istanbul (demo)
│                                              │
│ [!] NOT: Demo veridir. Gercek API icin      │
│     numverify.com ucretsiz key alinabilir   │
└─────────────────────────────────────────────┘"""

# 5. DOMAIN WHOIS
def domain_whois_api(domain):
    print("\n[*] Domain whois sorgulaniyor...")
    try:
        w = whois.whois(domain)
        name_servers = ', '.join(w.name_servers) if w.name_servers else '-'
        return f"""
┌─────────────────────────────────────────────┐
│ DOMAIN WHOIS BILGILERI                       │
├─────────────────────────────────────────────┤
│ Domain      : {domain}
│ Registrar   : {w.registrar if w.registrar else '-'}
│ Kayit Tarihi: {w.creation_date if w.creation_date else '-'}
│ Bitis Tarihi: {w.expiration_date if w.expiration_date else '-'}
│ Guncelleme  : {w.updated_date if w.updated_date else '-'}
│ Name Server : {name_servers}
│ Status      : {w.status if w.status else '-'}
└─────────────────────────────────────────────┘"""
    except Exception as e:
        return f"[!] Hata: {str(e)}"

# 6. DNS SORGULAMA
def dns_api(domain):
    print("\n[*] DNS kayitlari sorgulaniyor...")
    result = f"""
┌─────────────────────────────────────────────┐
│ DNS KAYITLARI: {domain}                       │
├─────────────────────────────────────────────┤"""
    
    record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']
    for rt in record_types:
        try:
            answers = dns.resolver.resolve(domain, rt)
            records = [str(r) for r in answers]
            record_str = ', '.join(records[:3])
            if len(records) > 3:
                record_str += f" +{len(records)-3} more"
            result += f"\n│ {rt:<4} : {record_str:<40}│"
        except:
            result += f"\n│ {rt:<4} : {'-':<40}│"
    
    result += """
└─────────────────────────────────────────────┘"""
    return result

# 7. SUBNET/CIDR
def subnet_api(ip_cidr):
    print("\n[*] Subnet hesaplaniyor...")
    try:
        import ipaddress
        net = ipaddress.ip_network(ip_cidr, strict=False)
        hosts = list(net.hosts())
        first_host = str(hosts[0]) if hosts else '-'
        last_host = str(hosts[-1]) if hosts else '-'
        return f"""
┌─────────────────────────────────────────────┐
│ SUBNET BILGILERI                             │
├─────────────────────────────────────────────┤
│ Network     : {net.network_address}
│ Broadcast   : {net.broadcast_address}
│ Netmask     : {net.netmask}
│ CIDR        : {net.prefixlen}
│ Host Sayisi : {net.num_addresses}
│ IP Araligi  : {first_host} - {last_host}
└─────────────────────────────────────────────┘"""
    except Exception as e:
        return f"[!] Hata: {str(e)}"

# 8. KENDI IP
def my_ip_api():
    try:
        req = urllib.request.Request('https://api.ipify.org?format=json', headers={'User-Agent': 'Lexus'})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read().decode())
            return data.get('ip', 'bilinmiyor')
    except:
        return socket.gethostbyname(socket.gethostname())

# MENU
def menu():
    banner()
    print("""
╔════════════════════════════════════════════════════════════════════╗
║                         OSINT MODULLERI                            ║
╠════════════════════════════════════════════════════════════════════╣
║  1. IP Sorgula (Konum, ISP, Koordinat)                             ║
║  2. Email Sizinti Kontrolu (Veritabani sorgulama)                  ║
║  3. Username Sosyal Medya Ara (9+ platform)                        ║
║  4. Telefon Numarasi Sorgula                                       ║
║  5. Domain Whois Sorgula                                           ║
║  6. DNS Kayitlari Sorgula (A, MX, NS, TXT, SOA)                    ║
║  7. Subnet/CIDR Hesaplama                                          ║
║  8. Kendi IP'mi Goster                                             ║
║  0. Cikis                                                          ║
╚════════════════════════════════════════════════════════════════════╝
""")

# MAIN
def main():
    while True:
        menu()
        secim = input("\n[LEXUS@OSINT]$ ").strip()
        
        if secim == "1":
            ip = input("IP adresi: ")
            print(ip_api(ip))
        elif secim == "2":
            email = input("Email adresi: ")
            print(email_breach_api(email))
        elif secim == "3":
            username = input("Kullanici adi (nick): ")
            print(username_social_api(username))
        elif secim == "4":
            phone = input("Telefon numarasi (+905551234567): ")
            print(phone_api(phone))
        elif secim == "5":
            domain = input("Domain (example.com): ")
            print(domain_whois_api(domain))
        elif secim == "6":
            domain = input("Domain: ")
            print(dns_api(domain))
        elif secim == "7":
            cidr = input("CIDR (192.168.1.0/24): ")
            print(subnet_api(cidr))
        elif secim == "8":
            my_ip = my_ip_api()
            print(f"\n┌─────────────────────────────────────────────┐\n│ KENDI IP M: {my_ip:<35} │\n└─────────────────────────────────────────────┘")
        elif secim == "0":
            print("\n[+] Lexus OSINT kapatiliyor... Gule gule!")
            break
        else:
            print("\n[!] Gecersiz secim! 0-8 arasi girin.")
        
        input("\n[Enter] ile devam...")

if __name__ == "__main__":
    main()
