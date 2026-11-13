"""
Generate high quality diagrams and mockup illustrations for RantauHub project report.
"""
import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = r"d:\RantauHub\report_assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

FONT_REG = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

def get_font(bold=False, size=16):
    font_path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        return ImageFont.load_default()

def draw_header_bar(draw, width, title="RantauHub - Platform Digital Anak Rantau", url="https://rantauhub.id"):
    draw.rectangle([(0, 0), (width, 50)], fill="#1E3A8A")
    draw.text((25, 14), title, fill="#FFFFFF", font=get_font(True, 16))
    draw.text((width - 320, 16), "Home   Checklist   Anggaran   Direktori   Darurat", fill="#93C5FD", font=get_font(False, 13))

def create_architecture_diagram():
    w, h = 1200, 520
    im = Image.new("RGB", (w, h), "#F8FAFC")
    draw = ImageDraw.Draw(im)

    # Title box
    draw.rectangle([(40, 20), (w - 40, 75)], fill="#1E3A8A", outline="#172554", width=2)
    draw.text((60, 32), "DIAGRAM ALUR ARSITEKTUR SISTEM RANTAUHUB (CLIENT - SERVER - SERVICES - DATABASE)", fill="#FFFFFF", font=get_font(True, 18))

    # 4 Columns
    cols = [
        {
            "title": "1. LAPISAN KLIEN / BROWSER",
            "color": "#2563EB",
            "bg": "#EFF6FF",
            "items": [
                "• Antarmuka Pengguna Responsif",
                "• Tailwind CSS (Utility-first styling)",
                "• HTMX 1.9.10 (AJAX interaktif & partial DOM swap)",
                "• Alpine.js 3.13.5 (State & modal reaktif)",
                "• Pengiriman formulir HTTP & AJAX",
            ]
        },
        {
            "title": "2. DJANGO WEB SERVER & ROUTING",
            "color": "#0D9488",
            "bg": "#F0FDFA",
            "items": [
                "• Django 5.0 Core Framework & WSGI",
                "• Security Middleware (CSRF, XSS, Clickjacking)",
                "• URL Routing (config/urls.py & app urls)",
                "• Thin Controllers / Class & Function Views",
                "• Django Template Engine (MVT Pattern)",
            ]
        },
        {
            "title": "3. LOGIKA BISNIS & LAYANAN",
            "color": "#D97706",
            "bg": "#FFFBEB",
            "items": [
                "• checklist_service (Sinkronisasi & isolasi data)",
                "• budget_calculator (Kalkulasi Decimal, surplus/defisit)",
                "• place_search (Multi-criteria Q object selector)",
                "• wa_encoder (Sanitasi nomor 62 & URL schema wa.me)",
                "• Pemisahan tanggung jawab (Fat Services)",
            ]
        },
        {
            "title": "4. BASIS DATA & PENYIMPANAN",
            "color": "#4F46E5",
            "bg": "#EEF2FF",
            "items": [
                "• SQLite3 Relational Database Engine",
                "• Django ORM (Model & Migrasi skema)",
                "• Entitas User, Checklist, Budget, Guide",
                "• Entitas Direktori (88 Titik Fasilitas DIY)",
                "• Penyimpanan Berkas Statis & Media",
            ]
        }
    ]

    col_w = 260
    col_gap = 25
    start_x = 45
    start_y = 110
    card_h = 350

    for i, col in enumerate(cols):
        cx = start_x + i * (col_w + col_gap)
        # Card outer
        draw.rounded_rectangle([(cx, start_y), (cx + col_w, start_y + card_h)], radius=12, fill=col["bg"], outline=col["color"], width=2)
        # Header banner
        draw.rounded_rectangle([(cx, start_y), (cx + col_w, start_y + 45)], radius=10, fill=col["color"])
        draw.text((cx + 12, start_y + 12), col["title"], fill="#FFFFFF", font=get_font(True, 12))

        # Items
        cur_y = start_y + 65
        for item in col["items"]:
            draw.text((cx + 15, cur_y), item, fill="#1E293B", font=get_font(False, 12))
            cur_y += 50

        # Draw connecting arrow between cards
        if i < 3:
            arrow_x = cx + col_w + 3
            arrow_y = start_y + card_h // 2
            draw.polygon([(arrow_x, arrow_y - 8), (arrow_x + 18, arrow_y), (arrow_x, arrow_y + 8)], fill="#64748B")
            draw.line([(arrow_x - 5, arrow_y), (arrow_x + 10, arrow_y)], fill="#64748B", width=4)

    out_p = os.path.join(ASSETS_DIR, "gambar_3_1_arsitektur.png")
    im.save(out_p)
    print("Saved:", out_p)

def create_mockup_home():
    w, h = 1200, 680
    im = Image.new("RGB", (w, h), "#FFFFFF")
    draw = ImageDraw.Draw(im)

    # Topbar
    draw_header_bar(draw, w)

    # Hero section
    draw.rectangle([(0, 50), (w, 360)], fill="#F0F7FF")
    # Badge
    draw.rounded_rectangle([(w//2 - 160, 75), (w//2 + 160, 105)], radius=15, fill="#DBEAFE", outline="#93C5FD")
    draw.text((w//2 - 140, 82), "🚀 Sahabat Terpercaya Perantau di Indonesia", fill="#1D4ED8", font=get_font(True, 12))

    # Main Hero Title
    draw.text((w//2 - 380, 125), "Adaptasi Nyaman, Hidup Terencana di Kota Rantau", fill="#1E3A8A", font=get_font(True, 28))
    draw.text((w//2 - 420, 180), "Panduan lengkap persiapan keberangkatan, manajemen anggaran bulanan tanpa boncos,", fill="#475569", font=get_font(False, 16))
    draw.text((w//2 - 350, 210), "serta direktori fasilitas esensial terverifikasi untuk mahasiswa dan pekerja.", fill="#475569", font=get_font(False, 16))

    # CTA Buttons
    draw.rounded_rectangle([(w//2 - 210, 260), (w//2 - 20, 310)], radius=8, fill="#2563EB")
    draw.text((w//2 - 180, 275), "Mulai Checklist", fill="#FFFFFF", font=get_font(True, 15))

    draw.rounded_rectangle([(w//2 + 10, 260), (w//2 + 200, 310)], radius=8, fill="#FFFFFF", outline="#CBD5E1", width=2)
    draw.text((w//2 + 35, 275), "Cari Fasilitas Esensial", fill="#1E293B", font=get_font(True, 14))

    # Feature grid title
    draw.text((w//2 - 140, 385), "FITUR UTAMA RANTAUHUB", fill="#1E3A8A", font=get_font(True, 18))

    # 4 Feature Cards
    f_cards = [
        ("📋 Survival Checklist", "Daftar bawaan dokumen, perlengkapan kost, akademik, & darurat.", "#EFF6FF", "#3B82F6"),
        ("💰 Kalkulator Anggaran", "Simulasi pengeluaran bulanan, indikator surplus, & rasio darurat.", "#ECFDF5", "#10B981"),
        ("📍 Direktori Fasilitas", "88 lokasi faskes, laundry, warteg, & bengkel terverifikasi di DIY.", "#FEF3C7", "#F59E0B"),
        ("🚨 Pusat Respons Darurat", "Kartu identitas darurat & pesan WhatsApp otomatis sekali klik.", "#FEE2E2", "#EF4444"),
    ]

    card_w = 260
    gap = 20
    start_x = 50
    for i, (title, desc, bg, accent) in enumerate(f_cards):
        cx = start_x + i * (card_w + gap)
        draw.rounded_rectangle([(cx, 430), (cx + card_w, 640)], radius=10, fill=bg, outline=accent, width=2)
        draw.text((cx + 15, 450), title, fill="#0F172A", font=get_font(True, 14))
        # Word wrap desc
        lines = [desc[:35], desc[35:]] if len(desc) > 35 else [desc]
        dy = 490
        for ln in lines:
            draw.text((cx + 15, dy), ln.strip(), fill="#334155", font=get_font(False, 12))
            dy += 22
        # Mini action tag
        draw.rounded_rectangle([(cx + 15, 580), (cx + card_w - 15, 615)], radius=6, fill=accent)
        draw.text((cx + 60, 592), "Buka Modul →", fill="#FFFFFF", font=get_font(True, 12))

    out_p = os.path.join(ASSETS_DIR, "gambar_4_1_beranda.png")
    im.save(out_p)
    print("Saved:", out_p)

def create_mockup_dashboard_checklist():
    w, h = 1200, 680
    im = Image.new("RGB", (w, h), "#F8FAFC")
    draw = ImageDraw.Draw(im)

    draw_header_bar(draw, w, title="RantauHub - Dashboard & Checklist Adaptasi")

    # Welcome Banner
    draw.rounded_rectangle([(50, 70), (w - 50, 160)], radius=10, fill="#1E3A8A")
    draw.text((80, 85), "Halo, Zakia Kurnia Putri! 👋", fill="#FFFFFF", font=get_font(True, 22))
    draw.text((80, 120), "Kota Asal: Bengkulu  ➜  Kota Rantau: Yogyakarta (Depok, Sleman) | Kampus/Kantor: UGM", fill="#93C5FD", font=get_font(False, 14))

    # Left: Checklist Progress & Category Tabs
    draw.rounded_rectangle([(50, 180), (750, 650)], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.text((75, 200), "Daftar Periksa Adaptasi Perantau (Survival Checklist)", fill="#1E293B", font=get_font(True, 16))

    # Progress bar
    draw.text((75, 235), "Progres Kesiapan: 75% (6 dari 8 tugas selesai)", fill="#2563EB", font=get_font(True, 13))
    draw.rounded_rectangle([(75, 260), (720, 275)], radius=7, fill="#E2E8F0")
    draw.rounded_rectangle([(75, 260), (560, 275)], radius=7, fill="#10B981")

    # Category pills
    cats = ["Semua", "Dokumen Penting (4/4)", "Perlengkapan Kost (2/3)", "Akademik & Kerja (0/1)"]
    px = 75
    for i, c in enumerate(cats):
        bg = "#2563EB" if i == 0 else "#F1F5F9"
        txt_c = "#FFFFFF" if i == 0 else "#475569"
        draw.rounded_rectangle([(px, 295), (px + len(c)*8 + 20, 325)], radius=15, fill=bg)
        draw.text((px + 12, 303), c, fill=txt_c, font=get_font(True, 11))
        px += len(c)*8 + 30

    # Checklist items
    items = [
        ("☑", "KTP Elektronik Asli & Fotokopi 5 Lembar", "Dokumen Asli", True),
        ("☑", "Kartu Keluarga (KK) & Akta Kelahiran Legalisir", "Dokumen Asli", True),
        ("☑", "Kartu BPJS Kesehatan Aktif (Siap Pindah Faskes)", "Kesehatan", True),
        ("☑", "Sprei, Bantal, dan Guling Cadangan", "Perlengkapan Kost", True),
        ("☑", "Stopkontak Kabel Panjang & Colokan Tiga", "Kebutuhan Kost", True),
        ("☐", "Peralatan Mandi & Ember Lipat Portable", "Perlengkapan Kost", False),
        ("☐", "Surat Keterangan Bebas Narkoba / Skck", "Akademik/Kerja", False),
    ]

    iy = 345
    for box, title, tag, checked in items:
        bg = "#F8FAFC" if not checked else "#F0FDF4"
        bdr = "#E2E8F0" if not checked else "#BBF7D0"
        draw.rounded_rectangle([(75, iy), (720, iy + 38)], radius=6, fill=bg, outline=bdr)
        icon_c = "#10B981" if checked else "#94A3B8"
        draw.text((90, iy + 8), box, fill=icon_c, font=get_font(True, 16))
        txt_c = "#334155" if not checked else "#166534"
        draw.text((120, iy + 10), title, fill=txt_c, font=get_font(False, 13))
        # Tag
        draw.rounded_rectangle([(600, iy + 8), (705, iy + 30)], radius=4, fill="#E2E8F0")
        draw.text((610, iy + 11), tag, fill="#475569", font=get_font(False, 10))
        iy += 42

    # Right Column: Quick Status & Emergency Card Preview
    draw.rounded_rectangle([(775, 180), (1150, 400)], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.text((800, 200), "Ringkasan Finansial Bulan Ini", fill="#1E293B", font=get_font(True, 15))
    draw.text((800, 235), "Total Alokasi:", fill="#64748B", font=get_font(False, 13))
    draw.text((950, 235), "Rp 2.500.000", fill="#0F172A", font=get_font(True, 13))
    draw.text((800, 265), "Sewa Kost:", fill="#64748B", font=get_font(False, 13))
    draw.text((950, 265), "Rp 850.000", fill="#0F172A", font=get_font(True, 13))
    draw.text((800, 295), "Estimasi Makan:", fill="#64748B", font=get_font(False, 13))
    draw.text((950, 295), "Rp 900.000", fill="#0F172A", font=get_font(True, 13))
    draw.rounded_rectangle([(800, 335), (1120, 380)], radius=6, fill="#DCFCE7", outline="#86EFAC")
    draw.text((820, 348), "STATUS: SURPLUS (Sisa: Rp 250.000)", fill="#166534", font=get_font(True, 13))

    # Emergency Contact Card
    draw.rounded_rectangle([(775, 420), (1150, 650)], radius=10, fill="#FEF2F2", outline="#FECACA", width=1)
    draw.text((800, 440), "🚨 Kontak Darurat Tersimpan", fill="#991B1B", font=get_font(True, 15))
    draw.text((800, 480), "Nama Kontak: Ayah (Kurniawan)", fill="#7F1D1D", font=get_font(False, 13))
    draw.text((800, 510), "Nomor Darurat: 0812-7890-4321", fill="#7F1D1D", font=get_font(True, 14))
    draw.text((800, 545), "Rumah Sakit Terdekat:", fill="#7F1D1D", font=get_font(False, 12))
    draw.text((800, 565), "RSUP Dr. Sardjito (UGM) - IGD 24 Jam", fill="#991B1B", font=get_font(True, 12))

    draw.rounded_rectangle([(800, 595), (1120, 635)], radius=6, fill="#EF4444")
    draw.text((840, 606), "Buka Emergency Center →", fill="#FFFFFF", font=get_font(True, 13))

    out_p = os.path.join(ASSETS_DIR, "gambar_4_2_dashboard_checklist.png")
    im.save(out_p)
    print("Saved:", out_p)

def create_mockup_budget():
    w, h = 1200, 650
    im = Image.new("RGB", (w, h), "#F8FAFC")
    draw = ImageDraw.Draw(im)

    draw_header_bar(draw, w, title="RantauHub - Kalkulator Anggaran Finansial Perantau")

    # Title
    draw.text((50, 75), "Simulasi Pengelolaan Anggaran & Deteksi Boncos Bulanan", fill="#1E3A8A", font=get_font(True, 22))
    draw.text((50, 110), "Gunakan kalkulator presisi Decimal ini untuk memetakan alokasi biaya hidup dan menjaga dana darurat.", fill="#64748B", font=get_font(False, 14))

    # Form Box (Left)
    draw.rounded_rectangle([(50, 150), (600, 620)], radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw.text((75, 175), "Parameter Pengeluaran Bulanan", fill="#0F172A", font=get_font(True, 16))

    inputs = [
        ("Uang Saku / Pemasukan Bulanan (Rp)", "3.000.000"),
        ("Biaya Sewa Kost (Rp / bulan)", "800.000"),
        ("Biaya Makan Harian (Rp / hari)", "40.000"),
        ("Transportasi & Bensin (Rp / bulan)", "200.000"),
        ("Internet & Paket Data (Rp / bulan)", "100.000"),
        ("Keperluan Kuliah / Kerja (Rp / bulan)", "100.000"),
        ("Kebutuhan Pribadi & Hiburan (Rp / bulan)", "100.000"),
        ("Alokasi Tabungan Darurat (Rp / bulan)", "300.000"),
    ]

    fy = 215
    for label, val in inputs:
        draw.text((75, fy), label, fill="#475569", font=get_font(False, 11))
        draw.rounded_rectangle([(75, fy + 18), (575, fy + 42)], radius=5, fill="#F8FAFC", outline="#CBD5E1")
        draw.text((90, fy + 24), val, fill="#0F172A", font=get_font(True, 12))
        fy += 49

    # Result Box (Right)
    draw.rounded_rectangle([(630, 150), (1150, 620)], radius=10, fill="#FFFFFF", outline="#CBD5E1", width=1)
    draw.text((660, 175), "Hasil Analisis Finansial & Rasio Darurat", fill="#0F172A", font=get_font(True, 16))

    # Status Banner
    draw.rounded_rectangle([(660, 215), (1120, 285)], radius=8, fill="#DCFCE7", outline="#86EFAC", width=2)
    draw.text((680, 228), "STATUS: SURPLUS FINANSIAL", fill="#15803D", font=get_font(True, 16))
    draw.text((680, 255), "Keuangan Anda sehat! Sisa saldo dapat dialokasikan ke tabungan investasi.", fill="#166534", font=get_font(False, 12))

    # Metric Cards
    metrics = [
        ("Total Pemasukan", "Rp 3.000.000", "#EFF6FF", "#1D4ED8"),
        ("Total Pengeluaran", "Rp 2.800.000", "#FFF7ED", "#C2410C"),
        ("Sisa Saldo Bebas", "Rp 200.000", "#F0FDF4", "#15803D"),
        ("Rasio Dana Darurat", "10.0 % (Aman)", "#FAF5FF", "#7E22CE"),
    ]

    my = 305
    for title, val, bg, text_c in metrics:
        draw.rounded_rectangle([(660, my), (1120, my + 55)], radius=6, fill=bg)
        draw.text((680, my + 10), title, fill="#64748B", font=get_font(False, 12))
        draw.text((680, my + 28), val, fill=text_c, font=get_font(True, 16))
        my += 65

    # Recommendation Box
    draw.rounded_rectangle([(660, 535), (1120, 605)], radius=6, fill="#F1F5F9")
    draw.text((680, 545), "💡 Tips Cerdas Anak Rantau:", fill="#334155", font=get_font(True, 12))
    draw.text((680, 568), "Alokasi makan bulanan Rp 1.200.000 (Rp 40.000/hari) sudah ideal untuk Yogyakarta.", fill="#475569", font=get_font(False, 11))
    draw.text((680, 586), "Pertahankan rasio tabungan darurat minimal 10% setiap awal bulan.", fill="#475569", font=get_font(False, 11))

    out_p = os.path.join(ASSETS_DIR, "gambar_4_3_kalkulator_budget.png")
    im.save(out_p)
    print("Saved:", out_p)

def create_mockup_directory():
    w, h = 1200, 680
    im = Image.new("RGB", (w, h), "#F8FAFC")
    draw = ImageDraw.Draw(im)

    draw_header_bar(draw, w, title="RantauHub - Direktori Fasilitas Esensial Yogyakarta")

    # Title & Search
    draw.text((50, 70), "Direktori Fasilitas Esensial Yogyakarta (88 Titik Terkurasi)", fill="#1E3A8A", font=get_font(True, 22))
    draw.text((50, 105), "Temukan Faskes BPJS, Warteg hemat, laundry kiloan, klinik 24 jam, dan perpustakaan di DIY.", fill="#64748B", font=get_font(False, 13))

    # Search Bar
    draw.rounded_rectangle([(50, 135), (w - 50, 185)], radius=8, fill="#FFFFFF", outline="#CBD5E1", width=2)
    draw.text((75, 148), "🔍 Cari nama fasilitas, kecamatan (Depok, Gondokusuman), atau jenis faskes...", fill="#94A3B8", font=get_font(False, 14))
    draw.rounded_rectangle([(w - 180, 140), (w - 60, 180)], radius=6, fill="#2563EB")
    draw.text((w - 150, 152), "Cari Data", fill="#FFFFFF", font=get_font(True, 13))

    # Category Pills Filter Bar (Actual 12 categories from models)
    pills = [
        ("Semua (88)", True),
        ("Puskesmas (Faskes 1)", False),
        ("Klinik Pratama / 24 Jam", False),
        ("Rumah Sakit & IGD", False),
        ("Apotek 24 Jam", False),
        ("Warteg / Warung Hemat", False),
        ("Laundry Kiloan", False),
        ("Bengkel Motor", False),
    ]

    draw.text((50, 205), "KELOMPOK:", fill="#64748B", font=get_font(True, 11))
    px = 135
    for label, active in pills:
        bg = "#DBEAFE" if active else "#FFFFFF"
        bdr = "#3B82F6" if active else "#E2E8F0"
        txt_c = "#1D4ED8" if active else "#475569"
        pw = len(label) * 8 + 22
        draw.rounded_rectangle([(px, 200), (px + pw, 228)], radius=14, fill=bg, outline=bdr)
        draw.text((px + 11, 206), label, fill=txt_c, font=get_font(True, 11))
        px += pw + 10

    # 3 Place Cards Grid
    places = [
        {
            "name": "Puskesmas Depok I Sleman",
            "cat": "Puskesmas (Faskes 1)",
            "cat_color": "#10B981",
            "loc": "Jl. Ring Road Utara, Maguwoharjo, Depok, Sleman",
            "phone": "(0274) 487845",
            "badge": "[Terverifikasi]",
            "price": "Gratis (BPJS) / Rp 10.000",
            "maps": "Buka di Google Maps ↗"
        },
        {
            "name": "RSUP Dr. Sardjito (UGM)",
            "cat": "Rumah Sakit Umum & IGD 24 Jam",
            "cat_color": "#EF4444",
            "loc": "Jl. Kesehatan No. 1, Sekip, Sinduadi, Mlati, Sleman",
            "phone": "(0274) 631190",
            "badge": "[Terverifikasi]",
            "price": "Faskes Rujukan Lanjutan BPJS",
            "maps": "Buka di Google Maps ↗"
        },
        {
            "name": "Warteg Barokah Pogung Baru",
            "cat": "Warung Makan / Warteg Hemat",
            "cat_color": "#F59E0B",
            "loc": "Jl. Pogung Baru Blok F No. 12, Sleman",
            "phone": "0813-9876-5432",
            "badge": "[Terverifikasi]",
            "price": "Rp 10.000 - Rp 18.000 / porsi",
            "maps": "Buka di Google Maps ↗"
        },
        {
            "name": "Klinik Pratama Korpri DIY 24 Jam",
            "cat": "Klinik Pratama / 24 Jam",
            "cat_color": "#06B6D4",
            "loc": "Jl. Kenari No. 14, Semaki, Umbulharjo, Kota Yogyakarta",
            "phone": "(0274) 589765",
            "badge": "[Terverifikasi]",
            "price": "Faskes 1 BPJS & Umum",
            "maps": "Buka di Google Maps ↗"
        },
        {
            "name": "Super Wash Laundry Pandega Marta",
            "cat": "Laundry Kiloan",
            "cat_color": "#8B5CF6",
            "loc": "Jl. Pandega Marta No. 28, Caturtunggal, Depok",
            "phone": "0857-1122-3344",
            "badge": "[Terverifikasi]",
            "price": "Rp 6.000 / kg (One Day)",
            "maps": "Buka di Google Maps ↗"
        },
        {
            "name": "Grhatama Pustaka DIY",
            "cat": "Perpustakaan & Ruang Belajar",
            "cat_color": "#6366F1",
            "loc": "Janti, Banguntapan, Bantul, D.I. Yogyakarta",
            "phone": "(0274) 453629",
            "badge": "[Terverifikasi]",
            "price": "Gratis (WiFi Kencang & AC)",
            "maps": "Buka di Google Maps ↗"
        }
    ]

    card_w = 345
    card_h = 185
    start_x = 50
    start_y = 250

    for idx, p in enumerate(places):
        col = idx % 3
        row = idx // 3
        cx = start_x + col * (card_w + 32)
        cy = start_y + row * (card_h + 20)

        draw.rounded_rectangle([(cx, cy), (cx + card_w, cy + card_h)], radius=8, fill="#FFFFFF", outline="#E2E8F0", width=1)
        # Category strip
        draw.rounded_rectangle([(cx + 12, cy + 12), (cx + 180, cy + 32)], radius=4, fill=p["cat_color"])
        draw.text((cx + 18, cy + 15), p["cat"], fill="#FFFFFF", font=get_font(True, 9))

        # Verified badge
        draw.text((cx + card_w - 95, cy + 14), p["badge"], fill="#10B981", font=get_font(True, 10))

        # Place name
        draw.text((cx + 12, cy + 42), p["name"], fill="#0F172A", font=get_font(True, 13))

        # Address & phone
        draw.text((cx + 12, cy + 70), "📍 " + p["loc"][:42], fill="#475569", font=get_font(False, 10))
        draw.text((cx + 12, cy + 92), "📞 " + p["phone"] + "  |  💵 " + p["price"], fill="#64748B", font=get_font(False, 10))

        # Action bar
        draw.line([(cx + 12, cy + 130), (cx + card_w - 12, cy + 130)], fill="#F1F5F9", width=1)
        draw.text((cx + 14, cy + 145), p["maps"], fill="#2563EB", font=get_font(True, 11))
        # Fav star
        draw.text((cx + card_w - 90, cy + 145), "⭐ Simpan", fill="#F59E0B", font=get_font(True, 11))

    out_p = os.path.join(ASSETS_DIR, "gambar_4_4_direktori_fasilitas.png")
    im.save(out_p)
    print("Saved:", out_p)

def create_mockup_emergency():
    w, h = 1200, 680
    im = Image.new("RGB", (w, h), "#F8FAFC")
    draw = ImageDraw.Draw(im)

    draw_header_bar(draw, w, title="RantauHub - Pusat Darurat & Emergency WhatsApp Generator")

    # Banner
    draw.rounded_rectangle([(50, 70), (w - 50, 140)], radius=8, fill="#991B1B")
    draw.text((75, 85), "PUSAT BANTUAN DARURAT (EMERGENCY CENTER)", fill="#FFFFFF", font=get_font(True, 20))
    draw.text((75, 115), "Akses cepat nomor darurat nasional dan generator pesan SOS terformat langsung ke WhatsApp keluarga.", fill="#FCA5A5", font=get_font(False, 13))

    # Left: National Hotline Cards
    draw.rounded_rectangle([(50, 160), (450, 650)], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.text((75, 185), "Panggilan Darurat Bebas Pulsa", fill="#0F172A", font=get_font(True, 15))

    hotlines = [
        ("Polisi (Kamtibmas & Kejahatan)", "110", "#EF4444"),
        ("Ambulans / Gawat Darurat Medis (SPGDT)", "119", "#DC2626"),
        ("Pemadam Kebakaran (Damkar & Rescue)", "113", "#EA580C"),
        ("Basarnas (Pencarian & Penyelamatan)", "115", "#0284C7"),
        ("PLN (Gangguan Listrik Kost)", "123", "#F59E0B"),
        ("BPJS Kesehatan Care Center", "165", "#059669"),
    ]

    hy = 225
    for name, num, col in hotlines:
        draw.rounded_rectangle([(75, hy), (425, hy + 55)], radius=6, fill="#FEF2F2", outline="#FCA5A5")
        draw.text((90, hy + 10), name[:35], fill="#1E293B", font=get_font(False, 11))
        draw.text((90, hy + 28), "Tekan Panggilan: ", fill="#64748B", font=get_font(False, 10))
        draw.text((180, hy + 26), num, fill=col, font=get_font(True, 15))
        # Call pill
        draw.rounded_rectangle([(340, hy + 14), (410, hy + 42)], radius=12, fill=col)
        draw.text((355, hy + 20), "Hubungi", fill="#FFFFFF", font=get_font(True, 10))
        hy += 68

    # Right: WhatsApp Generator Form & Live Preview
    draw.rounded_rectangle([(475, 160), (1150, 650)], radius=10, fill="#FFFFFF", outline="#E2E8F0", width=1)
    draw.text((505, 185), "Generator Pesan Darurat WhatsApp (wa.me Schema)", fill="#0F172A", font=get_font(True, 15))

    # Form inputs preview
    draw.text((505, 220), "Nama Pengirim: Zakia Kurnia Putri", fill="#475569", font=get_font(False, 12))
    draw.text((505, 245), "Jenis Situasi: 🚨 DARURAT MEDIS / SAKIT PARAH", fill="#DC2626", font=get_font(True, 12))
    draw.text((505, 270), "Lokasi Saat Ini: Kost Pondok Melati No. 4, Karangmalang, Sleman", fill="#475569", font=get_font(False, 12))
    draw.text((505, 295), "Nomor Kontak Tujuan: 0812-7890-4321 (Dikonversi ke 6281278904321)", fill="#0F172A", font=get_font(True, 12))

    # WhatsApp Message Preview Box (mimic WhatsApp bubble)
    draw.rounded_rectangle([(505, 330), (1120, 560)], radius=10, fill="#DCF8C6", outline="#86EFAC")
    draw.text((525, 345), "*🚨 DARURAT MEDIS / SAKIT PARAH*", fill="#065F46", font=get_font(True, 13))
    draw.text((525, 370), "Halo, saya *Zakia Kurnia Putri* (Anak Rantau RantauHub).", fill="#1F2937", font=get_font(False, 12))
    draw.text((525, 395), "Saya membutuhkan pertolongan mendesak saat ini.", fill="#1F2937", font=get_font(False, 12))
    draw.text((525, 420), "📍 *Lokasi Saya Sekarang:* Kost Pondok Melati No. 4, Karangmalang, Sleman", fill="#1F2937", font=get_font(True, 12))
    draw.text((525, 450), "ℹ️ *Kondisi / Keterangan:* Mengalami demam tinggi dan sesak napas butuh antar ke faskes.", fill="#1F2937", font=get_font(False, 12))
    draw.text((525, 485), "Tolong segera hubungi saya atau kirim bantuan ke titik lokasi di atas.", fill="#1F2937", font=get_font(False, 12))
    draw.text((525, 515), "_(Pesan otomatis dibuat melalui RantauHub Emergency Center)_", fill="#4B5563", font=get_font(False, 10))

    # Click-to-chat CTA
    draw.rounded_rectangle([(505, 580), (1120, 630)], radius=8, fill="#25D366")
    draw.text((680, 595), "💬 Kirim Pesan via WhatsApp Sekarang (https://wa.me/62812...)", fill="#FFFFFF", font=get_font(True, 14))

    out_p = os.path.join(ASSETS_DIR, "gambar_4_5_emergency_sos.png")
    im.save(out_p)
    print("Saved:", out_p)

if __name__ == "__main__":
    create_architecture_diagram()
    create_mockup_home()
    create_mockup_dashboard_checklist()
    create_mockup_budget()
    create_mockup_directory()
    create_mockup_emergency()
    print("All report assets generated successfully!")

