# 🎓 BUKU PANDUAN PRESENTASI & DOKUMENTASI TEKNIS RANTAUHUB
> **Panduan Komprehensif Presentasi untuk Guru, Penguji, dan Audiens**  
> *Dari Konsep Dasar, Latar Belakang Masalah, Arsitektur Sistem, Bedah Kode Sumber, hingga Panduan Menjawab Pertanyaan Penguji (Defense Q&A).*

---

## 📑 DAFTAR ISI
1. [BAB 1: Latar Belakang & Mengapa RantauHub Dibuat](#bab-1-latar-belakang--mengapa-rantauhub-dibuat)
2. [BAB 2: Nilai Produk & Alur Pengguna (User Journey)](#bab-2-nilai-produk--alur-pengguna-user-journey)
3. [BAB 3: Keputusan Teknologi & Desain Arsitektur](#bab-3-keputusan-teknologi--desain-arsitektur)
4. [BAB 4: Bedah Kode Sumber (Dari Logika Dasar hingga Rumit)](#bab-4-bedah-kode-sumber-dari-logika-dasar-hingga-rumit)
5. [BAB 5: Kualitas & Keamanan (Automated Testing & Security)](#bab-5-kualitas--keamanan-automated-testing--security)
6. [BAB 6: Skrip Presentasi Langkah-Demi-Langkah (Siap Pakai)](#bab-6-skrip-presentasi-langkah-demi-langkah-siap-pakai)
7. [BAB 7: Panduan Menjawab Pertanyaan Guru / Juri (Q&A Defense)](#bab-7-panduan-menjawab-pertanyaan-guru--juri-qa-defense)

---

## BAB 1: Latar Belakang & Mengapa RantauHub Dibuat

### 1.1 Masalah Nyata di Lapangan (Problem Statement)
Setiap tahunnya, ratusan ribu pelajar, mahasiswa baru, dan pencari kerja muda di Indonesia berpindah ke kota-kota besar (seperti Yogyakarta, Jakarta, Bandung, Surabaya, Malang) untuk menuntut ilmu atau bekerja.

Namun, fase awal transisi perantauan ini sering kali dipenuhi oleh **5 Masalah Kritis**:
1. **Kekacauan Logistik Pra-Keberangkatan:** Dokumen legal penting (KK, KTP, ijazah legalisir, pas foto) atau obat pribadi sering tertinggal di kampung halaman, memicu biaya kirim ekspres dan hambatan administrasi kampus/kantor.
2. **Kebutaan Finansial (Financial Blind Spot):** Banyak anak rantau mengalami defisit uang saku di pertengahan bulan pertama karena tidak pernah memperhitungkan biaya makan 30 hari secara riil, biaya fotokopi, iuran sampah kost, atau dana darurat.
3. **Ketidaktahuan Layanan Kesehatan & Fasilitas Terdekat:** Saat jatuh sakit di kamar kost, anak rantau kebingungan mencari Puskesmas atau Apotek 24 jam terdekat, dan belum mengetahui cara memindahkan Faskes BPJS Kesehatan dari daerah asal.
4. **Kepanikan saat Situasi Darurat:** Saat mengalami kecelakaan, sakit berat sendirian di malam hari, atau kehilangan dompet/ATM, anak rantau tidak memiliki kontak darurat keluarga yang mudah diakses dan tidak tahu nomor kepolisian/ambulans setempat.
5. **Keterasingan Sosial (Isolation):** Sulit mencari informasi lokal tepercaya yang hanya diketahui oleh sesama anak rantau (misalnya warung makan murah higienis atau rute angkot termurah).

### 1.2 Solusi: RantauHub
**RantauHub** hadir sebagai platform web terpadu dengan tagline:
> *"Teman Pertama untuk Memulai Hidup di Perantauan."*

RantauHub tidak hanya sekadar website direktori, melainkan sebuah **sistem pendampingan digital** terstruktur dari hari keberangkatan hingga kehidupan sehari-hari di perantauan.

---

## BAB 2: Nilai Produk & Alur Pengguna (User Journey)

RantauHub dibagi ke dalam **5 Modul Fungsional Utama**:

```
[ PENGGUNA BARU ]
       │
       ▼
[ Registrasi & Pengaturan Kota Asal ➔ Kota Tujuan ]
       │
       ├───────────────────────────────────────────────┐
       ▼                                               ▼
[ 1. SURVIVAL CHECKLIST ]                    [ 2. KALKULATOR ANGGARAN ]
- Dokumen Wajib                              - Pemasukan vs Pengeluaran
- Perlengkapan Kost                          - Simulasi Makan 30 Hari
- Progres Centang Asynchronous (HTMX)        - Rasio Tabungan Darurat
       │                                               │
       ├───────────────────────────────────────────────┤
       ▼                                               ▼
[ 3. DIREKTORI LAYANAN PENTING ]             [ 4. PUSAT DARURAT (SOS) ]
- Puskesmas & Apotek 24 Jam                  - Kartu Darurat Digital Mobile-First
- Warteg Hemat & Laundry Kiloan              - Generator Pesan WA Sekali Klik
- Badge Verifikasi & Peta Google Maps        - Panduan Alih BPJS Mobile JKN
       │                                               │
       └───────────────────────┬───────────────────────┘
                               ▼
                   [ 5. KOMUNITAS & DISKUSI ]
                   - Tanya Jawab Rekomendasi Lokal
                   - Penanda Jawaban Terbaik
                   - Sistem Pelaporan Konten
```

---

## BAB 3: Keputusan Teknologi & Desain Arsitektur

Saat mempresentasikan website ini kepada guru/penguji, jelaskan alasan mengapa teknologi ini dipilih secara rasional:

| Komponen | Pilihan Teknologi | Alasan Rekayasa (Engineering Rationale) |
| :--- | :--- | :--- |
| **Backend Framework** | **Python Django 5.x** | *Batteries-included*: Dilengkapi sistem autentikasi kelas enterprise, ORM aman dari SQL Injection, sistem migrasi otomatis, dan antarmuka Django Admin yang mempermudah operasional verifikasi data. |
| **Frontend Strategy** | **Django Templates + HTMX + Tailwind CSS** | **Mengapa bukan React/Vue SPA?** Menghilangkan *over-engineering*. HTMX memberikan kecepatan dan interaktivitas reaktif (seperti toggle checklist dan live search) langsung dari server (*Server-Driven UI*), tanpa membebani browser dengan bundle JavaScript ratusan megabyte dan tanpa perlu mengelola state API ganda. |
| **Micro-Interactions** | **Alpine.js 3+** | Digunakan sangat minimalis dan terisolasi untuk interaksi sisi klien murni (toggle mobile menu hamburger, modal dialog, dan transisi UI). |
| **Database** | **SQLite (Dev) ➔ PostgreSQL (Prod)** | Skema database dirancang 100% kompatibel antar database relasional. SQLite memudahkan pengujian dan portabilitas lokal tanpa instalasi server database berat. |
| **Konfigurasi** | **python-decouple (`.env`)** | Memisahkan konfigurasi sensitif (*Secret Key*, status *Debug*) dari kode sumber (*Twelve-Factor App Methodology*). |

### 3.1 Aturan Emas Arsitektur (Golden Architecture Rules)
1. **The 150-Line Threshold (Modularisasi Ketat):**
   Tidak ada satu pun file Python atau template HTML yang melebihi 150–200 baris. Seluruh logika dipecah ke dalam folder modul: `models/`, `views/`, `forms/`, `services/`, dan `selectors/`.
2. **Pola Pemisahan Tanggung Jawab (*Separation of Concerns*):**
   - **Views (Controller Tipis):** Hanya menerima request HTTP, memvalidasi form, memanggil service, dan merender HTML/HTMX.
   - **Services (Logika Bisnis Gemuk):** Seluruh kalkulasi matematika keuangan dan manipulasi progres disimpan di `apps/survival_kit/services/` dan `apps/emergency/services/`.
   - **Selectors (Query Teroptimasi):** Logika pencarian data direktori kompleks disimpan terisolasi di `apps/directory/selectors/`.
3. **Data Isolation (Pencegahan IDOR):**
   Setiap data checklist atau simulasi anggaran milik pengguna diikat secara mutlak dengan filter `user=request.user`. Pengguna lain tidak dapat mengakses atau memodifikasi ID milik orang lain.
4. **Data Integrity & Honesty Policy:**
   Seluruh data demo atau fasilitas yang belum diverifikasi fisik oleh tim wajib memiliki penanda visual eksplisit: `[Data Demo — Belum Diverifikasi]`.

---

## BAB 4: Bedah Kode Sumber (Dari Logika Dasar hingga Rumit)

Gunakan bagian ini untuk menunjukkan kode asli saat sesi tanya-jawab teknis:

### 4.1 Tingkat Dasar: Custom User Model
**File:** `apps/users/models/user.py`
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    origin_city = models.CharField(max_length=100, blank=True, verbose_name="Kota Asal")
    target_city = models.CharField(max_length=100, blank=True, verbose_name="Kota Tujuan Rantau")
    target_district = models.CharField(max_length=100, blank=True, verbose_name="Kecamatan / Area Tujuan")
    campus_or_office = models.CharField(max_length=150, blank=True, verbose_name="Kampus / Tempat Kerja")
    emergency_contact_phone = models.CharField(max_length=30, blank=True, verbose_name="No. HP Kontak Darurat")
    emergency_contact_name = models.CharField(max_length=100, blank=True, verbose_name="Nama Kontak Darurat")

    @property
    def has_completed_profile(self):
        return bool(self.origin_city and self.target_city)
```
- **Penjelasan untuk Penguji:**
  *Kita tidak menggunakan model User bawaan Django secara mentah, melainkan mewarisi `AbstractUser` sejak hari pertama. Ini memungkinkan sistem menyimpan atribut perantauan (kota asal, kota tujuan, nomor darurat keluarga) dalam satu tabel terpusat tanpa perlu melakukan query join tambahan ke tabel profil terpisah.*

---

### 4.2 Tingkat Menengah: Reaktivitas Asynchronous Tanpa Reload (HTMX)
**File:** `templates/survival_kit/partials/checklist_item_row.html` & `apps/survival_kit/views/checklist.py`

Saat pengguna menekan tombol centang pada item checklist, browser **TIDAK** memuat ulang seluruh halaman (no full page reload):

```html
<button 
  type="button"
  hx-post="{% url 'survival_kit:toggle_item' item.id %}"
  hx-target="#checklist-item-{{ item.id }}"
  hx-swap="outerHTML"
  class="w-6 h-6 rounded-lg ...">
  ...
</button>
```

Dan pada View (`views/checklist.py`):
```python
@login_required
def toggle_item_view(request, item_id):
    if request.method == 'POST':
        item = toggle_checklist_item_service(request.user, item_id)
        progress = get_user_checklist_progress(request.user)
        if request.headers.get('HX-Request'):
            return render(request, 'survival_kit/partials/checklist_item_row.html', {
                'item': item,
                'progress': progress,
            })
    return redirect('survival_kit:checklist')
```
- **Penjelasan untuk Penguji:**
  *HTMX mengirimkan request HTTP POST di latar belakang. Django hanya merender potongan kecil HTML (`checklist_item_row.html`) dan mengganti elemen lama melalui atribut `hx-swap="outerHTML"`. Hebatnya lagi, dengan fitur `hx-swap-oob="true"` (Out of Band Swap), progress bar di bagian atas halaman ikut ter-update secara otomatis tanpa reload!*

---

### 4.3 Tingkat Rumit: Layanan Perhitungan Murni (Pure Service Layer)
**File:** `apps/survival_kit/services/budget_calculator.py`

Logika kalkulasi dipisahkan dari controller/view agar bersifat independen dan mudah diuji (*100% unit-testable*):

```python
from decimal import Decimal

def calculate_budget(monthly_allowance=Decimal('0'), rent_cost=Decimal('0'), food_daily=Decimal('0'), ...):
    allowance = Decimal(str(monthly_allowance or 0))
    rent = Decimal(str(rent_cost or 0))
    f_daily = Decimal(str(food_daily or 0))
    food_monthly = f_daily * Decimal('30')  # Simulasi konsumsi 30 hari
    ...
    living_expenses = rent + food_monthly + transport + internet + campus + personal
    total_expenses = living_expenses + emergency
    remaining_balance = allowance - total_expenses

    if allowance > Decimal('0'):
        emergency_ratio = round((emergency / allowance) * 100, 1)
        savings_health = 'Sehat (≥10%)' if emergency_ratio >= 10 else 'Kurang (<10%)'
    else:
        emergency_ratio = Decimal('0')
        savings_health = 'Belum Ada Pemasukan'

    if remaining_balance >= Decimal('0'):
        financial_status = 'Surplus'
        advice = 'Keuangan Anda seimbang dan aman. Pertahankan disiplin pengeluaran harian!'
    else:
        financial_status = 'Defisit'
        advice = 'Pengeluaran melebihi pemasukan. Kurangi pos makan harian atau cari kosan lebih hemat.'

    return { ... }
```
- **Penjelasan untuk Penguji:**
  *Kami menggunakan tipe data `Decimal` bukan `float` untuk mencegah kesalahan floating-point aritmatika mata uang. Fungsi ini menerima angka dan mengembalikan status surplus/defisit, rasio kesehatan dana darurat, dan saran aksi taktis secara deterministik.*

---

### 4.4 Tingkat Lanjut: Keamanan URL Encoding & Generator Pesan Darurat
**File:** `apps/emergency/services/wa_encoder.py`

```python
import urllib.parse

def generate_emergency_whatsapp_message(user_name, situation_type, current_location, details="", phone_number=""):
    situations = {
        'sakit': '🚨 DARURAT MEDIS / SAKIT PARAH',
        'kecelakaan': '⚠️ KECELAKAAN LALU LINTAS',
        'kriminal': '⛔ TINDAK KEJAHATAN / PERAMPOKAN',
        ...
    }
    ...
    # Normalisasi format telepon Indonesia: 08xx -> 628xx
    clean_phone = "".join(filter(str.isdigit, str(phone_number or "")))
    if clean_phone.startswith("0"):
        clean_phone = "62" + clean_phone[1:]

    raw_message = "\n".join(lines)
    encoded_text = urllib.parse.quote(raw_message)

    whatsapp_url = f"https://wa.me/{clean_phone}?text={encoded_text}" if clean_phone else f"https://wa.me/?text={encoded_text}"
    return {
        'raw_text': raw_message,
        'whatsapp_url': whatsapp_url,
        ...
    }
```
- **Penjelasan untuk Penguji:**
  *Fitur ini mengonversi teks darurat lengkap dengan koordinat titik lokasi pengguna ke format URL-encoded yang mematuhi standar RFC 3986. Ketika tombol ditekan di ponsel, aplikasi WhatsApp langsung terbuka dengan pesan pra-terisi tanpa perlu mengetik satu huruf pun saat kondisi panik.*

---

### 4.5 Tingkat Lanjut: Optimasi Pencarian Kompleks (*Selector Pattern*)
**File:** `apps/directory/selectors/place_search.py`

```python
from django.db.models import Q
from apps.directory.models.place import EssentialPlace

def search_places(query=None, category=None, city=None, district=None, is_verified=None):
    qs = EssentialPlace.objects.all()

    if query:
        q = query.strip()
        qs = qs.filter(
            Q(name__icontains=q) |
            Q(address__icontains=q) |
            Q(district__icontains=q) |
            Q(city__icontains=q)
        )

    if category and category != 'all':
        qs = qs.filter(category=category)

    if city and city != 'all':
        qs = qs.filter(city__iexact=city.strip())
    ...
    return qs.order_by('-is_verified', 'name')
```
- **Penjelasan untuk Penguji:**
  *Logika query tidak dikotori di dalam View. Menggunakan objek `Q` dari Django ORM untuk menghasilkan query SQL `OR` yang efisien. Prioritas pengurutan selalu mendahulukan tempat yang memiliki status `is_verified=True` agar masyarakat mendapatkan rekomendasi paling sahih terlebih dahulu.*

---

## BAB 5: Kualitas & Keamanan (Automated Testing & Security)

Website ini dilengkapi pengujian otomatis (*Unit & Integration Testing*) di folder `tests/`:

```text
tests/
├── test_auth.py           # Uji registrasi, login, proteksi rute tertutup
├── test_survival_kit.py   # Uji kalkulator anggaran & isolasi data checklist (Anti-IDOR)
├── test_directory.py      # Uji filter selector pencarian & penanda badge verifikasi
├── test_emergency.py      # Uji encoding pesan WhatsApp & sanitasi nomor HP
└── test_community.py      # Uji pembuatan thread, reply, hak akses, & pelaporan
```

### Eksekusi Hasil Pengujian:
```bash
python manage.py test tests
```
**Hasil:**
```text
Creating test database for alias 'default'...
Found 15 test(s).
System check identified no issues (0 silenced).
...............
----------------------------------------------------------------------
Ran 15 tests in 11.479s

OK
Destroying test database for alias 'default'...
```
✅ **15 dari 15 test lulus 100% tanpa kegagalan.**

---

## BAB 6: Skrip Presentasi Langkah-Demi-Langkah (Siap Pakai)

Gunakan skrip berbicara berikut saat tampil di depan guru atau audiens:

### 1. Pembukaan (1 Menit)
> *"Selamat pagi/siang Bapak/Ibu guru dan rekan-rekan sekalian. Hari ini saya bangga mempresentasikan proyek web aplikasi bernama **RantauHub**, dengan tagline **'Teman Pertama untuk Memulai Hidup di Perantauan'**.*
> 
> *Website ini dibangun menggunakan Python Django 5, Tailwind CSS, dan HTMX. RantauHub hadir untuk menjawab satu pertanyaan penting: **Bagaimana seorang anak muda yang baru pertama kali merantau ke kota besar bisa bertahan hidup dengan aman, mandiri, dan terencana?**"*

### 2. Demonstrasi Fitur (3–4 Menit)
> *"Mari kita lihat alur penggunaannya secara langsung:*
> 1. ***Landing Page & Registrasi:*** *Pengguna mendaftar dan memasukkan kota asal dan kota tujuan rantau mereka.*
> 2. ***Survival Checklist:*** *Pengguna mendapatkan daftar barang bawaan wajib dan dokumen legal. Perhatikan saat saya mencentang item ini: tidak ada reload halaman sama sekali. Angka progres dan progress bar di atas langsung berubah berkat teknologi HTMX.*
> 3. ***Kalkulator Anggaran Realistis:*** *Anak rantau sering kehabisan uang di bulan pertama. Di sini, sistem menghitung otomatis simulasi makan harian selama 30 hari ditambah sewa kos dan kuota internet. Jika saldo minus, sistem memberi peringatan 'Defisit' dan memberikan saran berhemat.*
> 4. ***Direktori Layanan Terdekat:*** *Jika anak rantau sakit atau butuh makan murah, mereka bisa memfilter Puskesmas, Apotek 24 jam, atau Warteg hemat. Seluruh data yang belum diverifikasi diberi badge penanda transparan demi kejujuran informasi.*
> 5. ***Kartu Darurat Digital (SOS):*** *Inilah fitur keselamatan kami. Menampilkan nomor penting polisi 110 dan ambulans 119 yang bisa ditelepon langsung, serta generator pesan WhatsApp otomatis yang siap kirim saat kondisi genting.*
> 6. ***Forum Komunitas:*** *Tempat bertanya rekomendasi kost dan transportasi kepada sesama perantau, dengan fitur penandaan jawaban terbaik dan sistem pelaporan konten.*"

### 3. Aspek Teknis & Penutup (1 Menit)
> *"Dari sisi rekayasa perangkat lunak, kode RantauHub dibangun dengan standar modular enterprise: tidak ada file yang melebihi 150 baris, memisahkan logika bisnis ke dalam Service Layer murni, dan telah melewati 15 pengujian otomatis dengan tingkat kelulusan 100%.*
> 
> *Demikian pengantar dari saya, saya persilakan kepada Bapak/Ibu guru untuk memberikan masukan maupun pertanyaan. Terima kasih."*

---

## BAB 7: Panduan Menjawab Pertanyaan Guru / Juri (Q&A Defense)

Berikut daftar pertanyaan yang paling sering ditanyakan oleh guru atau penguji beserta jawaban terbaiknya:

### Q1: "Mengapa kamu memilih Django dan HTMX, bukan React atau Next.js?"
**Jawaban:**
> *"Pemilihan Django + HTMX didasarkan pada prinsip **Efisiensi dan Maintainability**. Pada aplikasi seperti RantauHub yang kaya akan data transaksional dan form, membuat REST API terpisah dengan Single Page Application (SPA) seperti React akan memicu 'Overhead': kita harus menduplikasi validasi form di backend dan frontend, serta mengelola state sinkronisasi yang rumit.*
> 
> *Dengan HTMX, kita mempertahankan arsitektur **Server-Driven UI**: Django merender potongan HTML bersih secara langsung, memberikan pengalaman cepat tanpa reload seperti aplikasi SPA, namun dengan ukuran transfer data yang sangat kecil dan SEO-friendly."*

---

### Q2: "Bagaimana jika ada data nomor telepon atau alamat klinik yang salah? Siapa yang bertanggung jawab?"
**Jawaban:**
> *"Di RantauHub kami menerapkan **Data Integrity & Honesty Policy**. Kami secara eksplisit menolak mencantumkan nomor palsu seolah-olah resmi. Setiap data awal yang baru dimasukkan wajib memiliki badge `[Data Demo — Belum Diverifikasi]`.*
> 
> *Hanya Administrator melalui Django Admin yang dapat mengubah status menjadi `[Terverifikasi]` setelah dilakukan pengecekan fisik atau konfirmasi nomor hotline resmi. Ini melindungi pengguna dari informasi yang menyesatkan."*

---

### Q3: "Bagaimana sistem menjamin keamanan data pengguna agar tidak bisa diubah oleh pengguna lain (Anti-IDOR)?"
**Jawaban:**
> *"Kami menerapkan prinsip **Data Isolation & Object Ownership Security**. Pada setiap controller/service (misalnya saat mengubah status checklist atau menghapus thread), kami tidak hanya mencari data berdasarkan ID item, melainkan selalu menyertakan filter `user=request.user`.*
> 
> *Jika seorang pengguna mencoba mengubah ID checklist milik orang lain melalui inspect element atau manipulasi HTTP request, sistem database Django akan otomatis menghasilkan error `404 Not Found` atau menolak operasi tersebut. Hal ini juga telah kami buktikan kelulusannya pada unit test `test_data_isolation_checklist`."*

---

### Q4: "Apakah aplikasi ini bisa di-deploy ke server online dan diakses publik?"
**Jawaban:**
> *"Sangat siap. Kami telah memisahkan file konfigurasi menjadi `base.py`, `development.py`, dan `production.py`. Seluruh environment key rahasia dikelola lewat file `.env`.*
> 
> *Skema database yang saat ini menggunakan SQLite dirancang 100% kompatibel dengan PostgreSQL tanpa perlu mengubah satu baris pun kode model Django. Untuk aset statis seperti CSS dan JavaScript, kami telah mengonfigurasi `STATIC_ROOT` dan `STATICFILES_DIRS` sehingga siap disajikan melalui Nginx atau WhiteNoise."*

---

*Dokumentasi ini disusun secara lengkap dan siap Anda gunakan sebagai bahan materi cetak maupun presentasi visual.*
