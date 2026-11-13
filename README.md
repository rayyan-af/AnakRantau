# RantauHub 🇮🇩
> **"Teman Pertama untuk Memulai Hidup di Perantauan."**

RantauHub adalah platform digital terpadu berbasis Python Django yang mendampingi mahasiswa, pelajar, dan first-jobbers yang baru pertama kali merantau ke kota besar di Indonesia.

---

## 🌟 Fitur Utama

1. **Survival Checklist Terstruktur:**
   - Checklist barang bawaan wajib, dokumen legal, hari pertama di kost, dan adaptasi bulan pertama.
   - Status centang tersimpan instan via **HTMX** tanpa reload halaman.
   - Dukungan penambahan item custom pribadi.

2. **Simulasi Anggaran & Biaya Hidup:**
   - Kalkulator biaya hidup perantau dengan breakdown sewa kos, makan harian 30 hari, transportasi, kuota, dan rasio dana darurat.
   - Deteksi otomatis status keuangan (*Surplus* / *Defisit*) dan saran penghematan taktis.
   - Fitur simpan rencana anggaran bulanan.

3. **Direktori Layanan Penting & Terverifikasi:**
   - Navigasi puskesmas, klinik 24 jam, apotek, warteg hemat, dan laundry kiloan terjangkau.
   - Filter instan kota dan kategori via HTMX.
   - Kebijakan Integritas Data: Badge penanda eksplisit `[Terverifikasi]` vs `[Data Demo — Belum Diverifikasi]`.
   - Fitur bookmark tempat favorit.

4. **Pusat Darurat & SOS (Emergency Center):**
   - **Kartu Darurat Digital (SOS Card):** Tampilan mobile-first data identitas, kontak keluarga, dan panggilan darurat bebas pulsa (Polisi 110, Ambulans 119, Damkar 113, PLN 123, BPJS 165).
   - **Generator Pesan Darurat WhatsApp:** Pesan darurat otomatis siap kirim via `wa.me` dan salin ke clipboard.
   - **Panduan Pindah Faskes BPJS Kesehatan:** Langkah alih faskes via aplikasi Mobile JKN ke Puskesmas kota rantau.
   - **Protokol Kehilangan Dokumen:** Prosedur darurat saat KTP, ATM, atau STNK hilang di perantauan.

5. **Forum Diskusi Komunitas:**
   - Forum tanya-jawab perantau dengan kategori `#InfoKost`, `#Transportasi`, `#KulinerHemat`, `#Akademik`.
   - Penandaan jawaban paling membantu (*Accepted Answer*).
   - Sistem pelaporan konten tidak pantas (*Moderation Report Queue*).

---

## 🛠️ Tech Stack & Arsitektur

- **Backend:** Python 3.12+, Django 5.x (ORM, Built-in Auth, Admin, Management Commands).
- **Frontend:** Django Templates + Tailwind CSS + HTMX 1.9+ (reaktivitas asynchronous) + Alpine.js 3+ (interaksi mikro UI).
- **Database:** SQLite (Default lokal) / PostgreSQL ready.
- **Konfigurasi:** `python-decouple` membaca variabel lingkungan dari `.env`.
- **Standar Arsitektur:**
  - *150-Line Threshold:* Kode modular terpecah rapi.
  - *Thin Views, Fat Services/Selectors:* Logika bisnis di `services/`, query filter di `selectors/`.
  - *Data Isolation:* Seluruh mutasi dan query sensitif terikat pada `request.user`.

---

## 🚀 Panduan Instalasi Lokal

### A. Windows (PowerShell)

1. **Clone atau buka repositori:**
   ```powershell
   cd D:\RantauHub
   ```

2. **Buat dan aktifkan Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Konfigurasi Environment:**
   Salin `.env.example` menjadi `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```

5. **Jalankan Migrasi Database:**
   ```powershell
   python manage.py migrate
   ```

6. **Semai Data Awal (Checklist, Direktori, Akun Demo):**
   ```powershell
   python manage.py seed_survival_kit
   python manage.py seed_directory
   python manage.py seed_demo_user
   python manage.py seed_community
   ```

7. **Jalankan Server Pengembang:**
   ```powershell
   python manage.py runserver
   ```
   Buka peramban di: `http://127.0.0.1:8000/`

---

### B. macOS / Linux (Bash)

1. **Clone dan masuk ke direktori:**
   ```bash
   cd RantauHub
   ```

2. **Buat dan aktifkan Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Konfigurasi Environment:**
   ```bash
   cp .env.example .env
   ```

5. **Jalankan Migrasi Database:**
   ```bash
   python3 manage.py migrate
   ```

6. **Semai Data Awal:**
   ```bash
   python3 manage.py seed_survival_kit
   python3 manage.py seed_directory
   python3 manage.py seed_demo_user
   python3 manage.py seed_community
   ```

7. **Jalankan Server:**
   ```bash
   python3 manage.py runserver
   ```

---

## 🔑 Akun Demo Siap Pakai

| Peran | Username | Password | Keterangan |
|---|---|---|---|
| **Administrator** | `admin` | `admin123` | Akses penuh ke Django Admin di `/admin/` |
| **Anak Rantau (User)** | `anakrantau` | `rantau123` | Akun demo mahasiswa rantau Padang → Yogyakarta |

---

## 🧪 Menjalankan Pengujian Otomatis

Untuk memastikan seluruh alur autentikasi, isolasi data, kalkulator anggaran, dan search selector berjalan dengan valid:

```bash
python manage.py test tests
```

---

## 🎓 Panduan Presentasi & Ujian (Defense Guide)

Untuk mempresentasikan proyek ini kepada guru, dosen, atau penguji, silakan buka file:
👉 **[PANDUAN_PRESENTASI.md](PANDUAN_PRESENTASI.md)**

File tersebut memuat:
- Latar belakang & masalah nyata anak rantau di lapangan.
- Keputusan arsitektur (Mengapa Django + HTMX + Tailwind, bukan React SPA).
- Bedah kode sumber mendalam dari logika dasar hingga rumit.
- Skrip presentasi langkah-demi-langkah siap pakai.
- Kunci jawaban untuk pertanyaan tersulit dari guru/penguji (Q&A Defense Cheat Sheet).

---

## 📄 Lisensi
Dilisensikan di bawah lisensi MIT. Dibangun untuk kemajuan dan ketenangan hidup seluruh pejuang rantau di Indonesia.
