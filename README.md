# 🦾 LEXUS OSINT - Advanced OSINT Framework

![Version](https://img.shields.io/badge/version-3.0-red)
![Python](https://img.shields.io/badge/python-3.7+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

> **LEXUS OSINT** - API tabanlı, logsuz, adminsiz, tamamen terminal üzerinde çalışan profesyonel OSINT aracı.

## 📌 Özellikler

| Modül | Açıklama | API |
|-------|----------|-----|
| 🌐 IP Sorgulama | Ülke, şehir, ilçe, koordinat, ISP, AS bilgisi | ip-api.com |
| 📧 Email Sızıntı | Email'in sızdırıldığı veritabanları (demo) | Leak-Lookup |
| 👤 Username OSINT | 9+ sosyal medya platformunda hesap kontrolü | HTTP Request |
| 📱 Telefon OSINT | Numara doğrulama, operatör, lokasyon (demo) | Numverify |
| 🌍 Domain Whois | Domain kayıt bilgileri, name server, tarihler | python-whois |
| 🔍 DNS Sorgulama | A, AAAA, MX, NS, TXT, SOA kayıtları | dnspython |
| 🕸️ Subnet/CIDR | Ağ hesaplama, IP aralığı, broadcast | ipaddress |
| 🆔 Kendi IP | Harici IP adresini göster | ipify.org |

## 🚀 Kurulum

```bash
# Repoyu klonla
git clone https://github.com/lexus/lexus-osint.git
cd lexus-osint

# Gereksinimleri kur
pip install -r requirements.txt

# Çalıştır
python lexus-osint.py
