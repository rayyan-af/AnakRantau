"""
Script to generate the complete, professional project report document:
Laporan_Proyek_Website.docx for RantauHub.
Following exact standards of SMK Negeri 1 Kota Bengkulu (PPLG)
and modeled after the Snap-to-Pocket Cheat Sheet reference document.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

DOC_PATH = r"d:\RantauHub\Laporan_Proyek_Website.docx"
ASSETS_DIR = r"d:\RantauHub\report_assets"

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Set inner padding for table cell in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    """Set background color of a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_cell_borders(cell, top="CCCCCC", bottom="CCCCCC", left=None, right=None, sz="4"):
    """Set borders of a cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    borders = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
    for b_name, b_val in borders.items():
        if b_val:
            node = OxmlElement(f'w:{b_name}')
            node.set(qn('w:val'), 'single')
            node.set(qn('w:sz'), sz)
            node.set(qn('w:space'), '0')
            node.set(qn('w:color'), b_val)
            tcBorders.append(node)
        else:
            node = OxmlElement(f'w:{b_name}')
            node.set(qn('w:val'), 'none')
            tcBorders.append(node)
    tcPr.append(tcBorders)

def style_table(table, col_widths, headers, data, header_bg="1E3A8A", alt_bg="F8FAFC"):
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # Format Header Row
    hdr_cells = table.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].text = title
        set_cell_shading(hdr_cells[i], header_bg)
        set_cell_margins(hdr_cells[i], top=140, bottom=140, left=160, right=160)
        set_cell_borders(hdr_cells[i], top="1E3A8A", bottom="1E3A8A", left="1E3A8A", right="1E3A8A", sz="6")
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15
        for run in p.runs:
            run.font.name = "Times New Roman"
            run.font.size = Pt(10)
            run.font.bold = True
            run.font.color.rgb = RGBColor(255, 255, 255)

    # Make header repeat across pages
    trPr = table.rows[0]._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

    # Format Data Rows
    for r_idx, row_data in enumerate(data):
        row_cells = table.add_row().cells
        bg_color = alt_bg if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row_data):
            row_cells[c_idx].text = str(val)
            set_cell_shading(row_cells[c_idx], bg_color)
            set_cell_margins(row_cells[c_idx], top=100, bottom=100, left=150, right=150)
            set_cell_borders(row_cells[c_idx], top="E2E8F0", bottom="E2E8F0", left="E2E8F0", right="E2E8F0", sz="4")
            p = row_cells[c_idx].paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            # Center column 0 if it's short code or number
            if c_idx == 0 and len(str(val)) <= 6:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for run in p.runs:
                run.font.name = "Times New Roman"
                run.font.size = Pt(9.5)
                run.font.color.rgb = RGBColor(30, 41, 59)

    # Set column widths
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

def add_styled_heading(doc, text, level):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    if level == 1:
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = RGBColor(15, 23, 42)
    elif level == 2:
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = RGBColor(30, 41, 59)
    elif level == 3:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(text)
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)
        run.font.bold = True
        run.font.color.rgb = RGBColor(51, 65, 85)
    return p

def add_body_paragraph(doc, text, space_after=6, line_spacing=1.35, align=WD_ALIGN_PARAGRAPH.JUSTIFY):
    p = doc.add_paragraph()
    p.alignment = align
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    run = p.add_run(text)
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)
    run.font.color.rgb = RGBColor(30, 41, 59)
    return p

def add_figure(doc, img_path, caption, width=Inches(6.0)):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(10)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=width)

    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(2)
    p_cap.paragraph_format.space_after = Pt(12)
    run_cap = p_cap.add_run(caption)
    run_cap.font.name = "Times New Roman"
    run_cap.font.size = Pt(10)
    run_cap.font.italic = True
    run_cap.font.bold = True
    run_cap.font.color.rgb = RGBColor(71, 85, 105)

def build_document():
    doc = docx.Document()

    # Page Margins: Kiri 4 cm, Atas 3 cm, Kanan 3 cm, Bawah 3 cm
    sec = doc.sections[0]
    sec.top_margin = Cm(3.0)
    sec.bottom_margin = Cm(3.0)
    sec.left_margin = Cm(4.0)
    sec.right_margin = Cm(3.0)
    sec.page_width = Cm(21.0)  # A4
    sec.page_height = Cm(29.7)

    # -------------------------------------------------------------
    # 1. IDENTITAS DOKUMEN (HALAMAN SAMPUL / COVER)
    # -------------------------------------------------------------
    p_cover_title = doc.add_paragraph()
    p_cover_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cover_title.paragraph_format.space_before = Pt(20)
    p_cover_title.paragraph_format.space_after = Pt(4)
    run1 = p_cover_title.add_run("LAPORAN PROYEK\nPENGEMBANGAN WEBSITE\n")
    run1.font.name = "Times New Roman"
    run1.font.size = Pt(18)
    run1.font.bold = True
    run1.font.color.rgb = RGBColor(15, 23, 42)

    run_app = p_cover_title.add_run("RANTAUHUB\n")
    run_app.font.name = "Times New Roman"
    run_app.font.size = Pt(24)
    run_app.font.bold = True
    run_app.font.color.rgb = RGBColor(30, 58, 138)  # Deep Navy Blue

    run_sub = p_cover_title.add_run("Platform Digital Terpadu Pendamping dan Pemandu Adaptasi\nMahasiswa serta Pekerja Perantau di Indonesia")
    run_sub.font.name = "Times New Roman"
    run_sub.font.size = Pt(11.5)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(71, 85, 105)

    # Logo SMKN 1 Kota Bengkulu
    logo_path = os.path.join(ASSETS_DIR, "logo_smkn1.png")
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(30)
        p_logo.paragraph_format.space_after = Pt(35)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(2.5))
    else:
        # Fallback space if logo missing
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(80)

    # Author and Supervisor
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(20)
    p_meta.paragraph_format.space_after = Pt(2)
    p_meta.paragraph_format.line_spacing = 1.25

    r_auth_label = p_meta.add_run("Disusun oleh:\n")
    r_auth_label.font.name = "Times New Roman"
    r_auth_label.font.size = Pt(11)

    r_auth_val = p_meta.add_run("Zakia Kurnia Putri\n\n")
    r_auth_val.font.name = "Times New Roman"
    r_auth_val.font.size = Pt(12)
    r_auth_val.font.bold = True

    r_adv_label = p_meta.add_run("Guru Pembimbing:\n")
    r_adv_label.font.name = "Times New Roman"
    r_adv_label.font.size = Pt(11)

    r_adv_val = p_meta.add_run("Reza Resinta, S.Kom\n\n")
    r_adv_val.font.name = "Times New Roman"
    r_adv_val.font.size = Pt(12)
    r_adv_val.font.bold = True

    # Institution and Year
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(15)
    p_inst.paragraph_format.space_after = Pt(0)
    p_inst.paragraph_format.line_spacing = 1.2

    r_inst = p_inst.add_run("PROGRAM KEAHLIAN PENGEMBANGAN PERANGKAT LUNAK DAN GIM\nSMK NEGERI 1 KOTA BENGKULU\nTAHUN AJARAN 2026/2027")
    r_inst.font.name = "Times New Roman"
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True
    r_inst.font.color.rgb = RGBColor(15, 23, 42)

    doc.add_page_break()

    # -------------------------------------------------------------
    # KATA PENGANTAR
    # -------------------------------------------------------------
    add_styled_heading(doc, "KATA PENGANTAR", level=1)

    add_body_paragraph(doc, "Puji syukur ke hadirat Tuhan Yang Maha Esa atas limpahan rahmat, taufik, serta hidayah-Nya, sehingga Dokumen Laporan Proyek Pengembangan Website \"RantauHub: Platform Digital Terpadu Pendamping dan Pemandu Adaptasi Mahasiswa serta Pekerja Perantau di Indonesia\" ini dapat diselesaikan dengan baik dan tepat waktu. Laporan ini disusun sebagai bentuk dokumentasi teknis, pertanggungjawaban akademis, serta deskripsi menyeluruh mengenai analisis kebutuhan, perancangan arsitektur, implementasi kode sumber, dan pengujian sistem pada program keahlian Pengembangan Perangkat Lunak dan Gim (PPLG) SMK Negeri 1 Kota Bengkulu.")

    add_body_paragraph(doc, "RantauHub dikembangkan secara khusus untuk menjawab realitas tantangan yang dihadapi oleh jutaan generasi muda Indonesia saat menempuh pendidikan atau memulai karier di kota perantauan baru, khususnya di Daerah Istimewa Yogyakarta. Tantangan adaptasi kultural, kebingungan mengurus administrasi dan relokasi fasilitas kesehatan (BPJS Faskes 1), kesulitan menjaga disiplin finansial bulanan tanpa boncos, hingga kepanikan ketika menghadapi keadaan darurat medis atau kriminalitas di kamar kost tanpa keluarga menjadi landasan utama perancangan sistem ini.")

    add_body_paragraph(doc, "Dalam implementasi fisiknya, website RantauHub dibangun menggunakan kerangka kerja backend Python dan Django 5.x yang mengadopsi pola arsitektur modern Thin Views / Fat Services guna menjamin modularitas dan kemudahan pemeliharaan kode. Pada lapisan antarmuka (frontend), sistem mengintegrasikan perpaduan teknologi responsif Tailwind CSS dari CDN, HTMX untuk interaksi asinkronus parsial yang cepat tanpa beban Single Page Application (SPA), serta Alpine.js untuk manajemen status reaktif lokal pada komponen modal dan navigasi. Seluruh data transaksi, profil perantau, perencanaan anggaran, checklist adaptasi, dan 88 titik fasilitas esensial terkurasi dikelola secara efisien melalui Object-Relational Mapping (ORM) Django berbasis relasional SQLite3.")

    add_body_paragraph(doc, "Penyusunan laporan dan keberhasilan pengembangan proyek ini tidak terlepas dari bimbingan, dorongan, serta bantuan berbagai pihak. Penulis menyampaikan rasa hormat dan ucapan terima kasih yang setulus-tulusnya kepada:\n"
                            "1. Bapak/Ibu Kepala SMK Negeri 1 Kota Bengkulu yang telah memfasilitasi sarana dan prasarana pembelajaran berbasis industri;\n"
                            "2. Ibu Reza Resinta, S.Kom, selaku Guru Pembimbing yang senantiasa meluangkan waktu memberikan arahan teknis, validasi struktur program, serta standar mutu kode perangkat lunak;\n"
                            "3. Bapak dan Ibu Dewan Guru Program Keahlian Pengembangan Perangkat Lunak dan Gim (PPLG) atas ilmu dan fondasi rekayasa logika pemrograman yang telah diajarkan;\n"
                            "4. Orang tua dan keluarga tercinta atas doa, motivasi, dan dukungan moril serta materiil yang tiada henti; serta\n"
                            "5. Rekan-rekan seperjuangan angkatan 2026/2027 yang senantiasa saling bertukar gagasan dalam pengujian dan penyempurnaan sistem.")

    add_body_paragraph(doc, "Penulis menyadari sepenuhnya bahwa laporan dan sistem perangkat lunak yang dibangun ini masih memiliki ruang untuk penyempurnaan, baik dalam cakupan data wilayah direktori di luar Daerah Istimewa Yogyakarta maupun implementasi gateway pesan darurat dua arah skala nasional. Oleh sebab itu, kritik dan saran yang konstruktif dari pembaca sangat diharapkan demi penyempurnaan di masa mendatang. Semoga laporan ini dapat memberikan manfaat nyata bagi pembaca, dunia pendidikan vokasi, serta masyarakat luas.")

    # Signature
    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(20)
    p_sig.paragraph_format.space_after = Pt(0)
    r_sig = p_sig.add_run("Bengkulu, November 2026\n\n\n\nPenulis,")
    r_sig.font.name = "Times New Roman"
    r_sig.font.size = Pt(11)

    doc.add_page_break()

    # -------------------------------------------------------------
    # DAFTAR ISI, DAFTAR GAMBAR, DAFTAR TABEL
    # -------------------------------------------------------------
    add_styled_heading(doc, "DAFTAR ISI", level=1)
    toc_items = [
        ("KATA PENGANTAR", "ii"),
        ("DAFTAR ISI", "iii"),
        ("DAFTAR GAMBAR", "iv"),
        ("DAFTAR TABEL", "iv"),
        ("BAB I PENDAHULUAN", "1"),
        ("   1.1 Latar Belakang", "1"),
        ("   1.2 Rumusan Masalah", "2"),
        ("   1.3 Tujuan Pengembangan", "2"),
        ("   1.4 Manfaat Pengembangan", "2"),
        ("   1.5 Ruang Lingkup", "3"),
        ("BAB II LANDASAN TEORI", "4"),
        ("   2.1 Arsitektur Web dan Model Client–Server", "4"),
        ("   2.2 HTML5, CSS3, Tailwind CSS, dan JavaScript", "4"),
        ("   2.3 HTMX dan Interaktivitas Reaktif Modern", "5"),
        ("   2.4 Alpine.js untuk Deklaratif Komponen Antarmuka", "5"),
        ("   2.5 Bahasa Pemrograman Python dan Framework Django", "5"),
        ("   2.6 Basis Data Relasional SQLite dan Django ORM", "6"),
        ("   2.7 Pola Arsitektur Layanan (Thin Views / Fat Services Architecture)", "6"),
        ("   2.8 Pengujian Perangkat Lunak (Django Automated Testing)", "7"),
        ("BAB III ANALISIS DAN PERANCANGAN SISTEM", "8"),
        ("   3.1 Analisis Sistem", "8"),
        ("   3.2 Analisis Kebutuhan", "8"),
        ("   3.3 Arsitektur Sistem", "9"),
        ("   3.4 Alur Kerja Pemrosesan", "10"),
        ("   3.5 Perancangan Data", "11"),
        ("   3.6 Rancangan Antarmuka", "12"),
        ("BAB IV IMPLEMENTASI DAN PENGUJIAN", "13"),
        ("   4.1 Lingkungan dan Teknologi", "13"),
        ("   4.2 Struktur Program", "13"),
        ("   4.3 Implementasi Antarmuka", "14"),
        ("   4.4 Implementasi Modul Autentikasi dan Profil Perantau (apps/users)", "17"),
        ("   4.5 Implementasi Modul Survival Kit: Checklist, Budget, dan Panduan (apps/survival_kit)", "17"),
        ("   4.6 Implementasi Modul Direktori DIY dan Pusat Respons Darurat (apps/directory & emergency)", "18"),
        ("   4.7 Endpoint Backend / Route Sistem", "19"),
        ("   4.8 Skenario Pemeriksaan", "20"),
        ("   4.9 Batasan Implementasi", "21"),
        ("BAB V PENUTUP", "22"),
        ("   5.1 Kesimpulan", "22"),
        ("   5.2 Saran Pengembangan", "22"),
        ("DAFTAR PUSTAKA", "23"),
        ("LAMPIRAN: PANDUAN SINGKAT PENGGUNAAN", "24"),
    ]

    for title, page in toc_items:
        p_toc = doc.add_paragraph()
        p_toc.paragraph_format.space_before = Pt(0)
        p_toc.paragraph_format.space_after = Pt(3)
        p_toc.paragraph_format.line_spacing = 1.15
        r_t = p_toc.add_run(title)
        r_t.font.name = "Times New Roman"
        r_t.font.size = Pt(10.5)
        if title.startswith("BAB") or title in ["KATA PENGANTAR", "DAFTAR ISI", "DAFTAR GAMBAR", "DAFTAR TABEL", "DAFTAR PUSTAKA", "LAMPIRAN: PANDUAN SINGKAT PENGGUNAAN"]:
            r_t.font.bold = True

        dots_count = max(5, 75 - len(title))
        r_dots = p_toc.add_run(" " + "." * dots_count + " ")
        r_dots.font.name = "Times New Roman"
        r_dots.font.size = Pt(10)
        r_dots.font.color.rgb = RGBColor(148, 163, 184)

        r_p = p_toc.add_run(page)
        r_p.font.name = "Times New Roman"
        r_p.font.size = Pt(10.5)
        if title.startswith("BAB"):
            r_p.font.bold = True

    p_space = doc.add_paragraph()
    p_space.paragraph_format.space_before = Pt(12)

    # DAFTAR GAMBAR
    add_styled_heading(doc, "DAFTAR GAMBAR", level=2)
    figures = [
        ("Gambar 3.1  Diagram Alur Arsitektur Sistem RantauHub", "9"),
        ("Gambar 4.1  Halaman Beranda Utama RantauHub", "14"),
        ("Gambar 4.2  Dashboard Personal dan Checklist Adaptasi Perantau", "15"),
        ("Gambar 4.3  Simulasi Kalkulator Finansial dan Rasio Dana Darurat", "15"),
        ("Gambar 4.4  Direktori Fasilitas Esensial Yogyakarta dan Filter Kategori", "16"),
        ("Gambar 4.5  Pusat Bantuan Darurat SOS dan WhatsApp Message Generator", "16"),
    ]
    for title, page in figures:
        p_fig = doc.add_paragraph()
        p_fig.paragraph_format.space_before = Pt(0)
        p_fig.paragraph_format.space_after = Pt(3)
        p_fig.paragraph_format.line_spacing = 1.15
        r_t = p_fig.add_run(title)
        r_t.font.name = "Times New Roman"
        r_t.font.size = Pt(10.5)

        dots_count = max(5, 75 - len(title))
        r_dots = p_fig.add_run(" " + "." * dots_count + " ")
        r_dots.font.name = "Times New Roman"
        r_dots.font.size = Pt(10)
        r_dots.font.color.rgb = RGBColor(148, 163, 184)

        r_p = p_fig.add_run(page)
        r_p.font.name = "Times New Roman"
        r_p.font.size = Pt(10.5)

    p_space2 = doc.add_paragraph()
    p_space2.paragraph_format.space_before = Pt(12)

    # DAFTAR TABEL
    add_styled_heading(doc, "DAFTAR TABEL", level=2)
    tables = [
        ("Tabel 3.1  Kebutuhan Fungsional Website RantauHub", "8"),
        ("Tabel 3.2  Skema Struktur Entitas Basis Data Relasional", "11"),
        ("Tabel 4.1  Teknologi dan Komponen Perangkat Lunak Proyek", "13"),
        ("Tabel 4.2  Struktur Direktori dan Tanggung Jawab Modul Program", "13"),
        ("Tabel 4.3  Daftar Lengkap Endpoint Backend dan Route Sistem", "19"),
        ("Tabel 4.4  Skenario Pemeriksaan dan Pengujian Fitur", "20"),
    ]
    for title, page in tables:
        p_tbl = doc.add_paragraph()
        p_tbl.paragraph_format.space_before = Pt(0)
        p_tbl.paragraph_format.space_after = Pt(3)
        p_tbl.paragraph_format.line_spacing = 1.15
        r_t = p_tbl.add_run(title)
        r_t.font.name = "Times New Roman"
        r_t.font.size = Pt(10.5)

        dots_count = max(5, 75 - len(title))
        r_dots = p_tbl.add_run(" " + "." * dots_count + " ")
        r_dots.font.name = "Times New Roman"
        r_dots.font.size = Pt(10)
        r_dots.font.color.rgb = RGBColor(148, 163, 184)

        r_p = p_tbl.add_run(page)
        r_p.font.name = "Times New Roman"
        r_p.font.size = Pt(10.5)

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB I PENDAHULUAN
    # -------------------------------------------------------------
    add_styled_heading(doc, "BAB I\nPENDAHULUAN", level=1)

    add_styled_heading(doc, "1.1 Latar Belakang", level=2)
    add_body_paragraph(doc, "Fenomena mobilitas penduduk antardaerah di Indonesia, khususnya perpindahan pelajar, mahasiswa, dan tenaga kerja muda menuju kota-kota pusat pendidikan serta ekonomi, merupakan bagian penting dari dinamika sosial nasional. Daerah Istimewa Yogyakarta (DIY), sebagai salah satu kota pelajar dan kebudayaan terkemuka di Indonesia, setiap tahunnya menerima puluhan ribu mahasiswa baru dari berbagai pelosok nusantara, mulai dari pulau Sumatra, Kalimantan, Sulawesi, hingga Papua. Meskipun demikian, fase awal perpindahan ke kota baru kerap menghadirkan disorientasi dan tekanan adaptasi yang signifikan bagi anak rantau.")

    add_body_paragraph(doc, "Permasalahan yang dihadapi oleh anak rantau bersifat multidimensional. Pertama, aspek kesiapan logistik dan dokumen administrasi; banyak perantau baru tidak mengetahui dokumen krusial apa saja yang wajib dibawa (seperti legalisir ijazah, fotokopi Kartu Keluarga, dan kartu BPJS) serta perlengkapan dasar kost yang esensial, sehingga menimbulkan pengeluaran mendadak yang tidak perlu. Kedua, aspek literasi finansial; transisi dari pengelolaan uang oleh orang tua menjadi pengelolaan mandiri seringkali berujung pada \"sindrom akhir bulan\" atau kondisi defisit akut karena tidak adanya simulasi alokasi biaya hidup (sewa kost, konsumsi harian, transportasi, dan dana darurat). Ketiga, keterbatasan informasi spasial lokal; perantau kerap kesulitan menemukan fasilitas penting dengan harga terjangkau di sekitar domisili baru mereka, seperti Puskesmas rujukan BPJS (Faskes 1), klinik 24 jam, warteg murah, binatu (laundry) kiloan, dan bengkel motor terpercaya. Terakhir dan paling kritis, kesiapan dalam menghadapi situasi darurat; ketika seorang perantau jatuh sakit parah di kamar kost sendirian, mengalami kecelakaan, atau kehilangan dokumen KTP dan kartu ATM, mereka seringkali panik dan tidak memiliki akses cepat ke nomor panggilan darurat resmi maupun cara mengabari keluarga secara ringkas dan presisi.")

    add_body_paragraph(doc, "Berdasarkan permasalahan nyata tersebut, dikembangkanlah website RantauHub. RantauHub dirancang sebagai platform pendamping digital komprehensif yang mengintegrasikan panduan persiapan (Survival Kit), kalkulator simulasi anggaran bulanan presisi, direktori terkurasi 88 fasilitas esensial di Yogyakarta yang terverifikasi, serta pusat bantuan respons darurat (Emergency Center) yang dilengkapi generator pesan darurat WhatsApp otomatis. Proyek ini dibangun sebagai wujud konkret implementasi kompetensi keahlian Pengembangan Perangkat Lunak dan Gim (PPLG) yang menggabungkan rekayasa backend berorientasi layanan, basis data relasional, antarmuka modern yang responsif, serta pengujian perangkat lunak otomatis.")

    add_styled_heading(doc, "1.2 Rumusan Masalah", level=2)
    add_body_paragraph(doc, "Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam pengembangan proyek website RantauHub adalah sebagai berikut:\n"
                            "1. Bagaimana merancang dan membangun platform website adaptasi terpadu yang mampu mendampingi perantau baru dalam mengelola logistik, finansial, dan pemetaan fasilitas di kota tujuan?\n"
                            "2. Bagaimana mengimplementasikan sistem kalkulator anggaran bulanan berbasis presisi angka desimal tinggi (Decimal) yang mampu menganalisis status surplus/defisit serta rasio kecukupan dana darurat perantau secara akurat?\n"
                            "3. Bagaimana merancang direktori fasilitas esensial terkurasi khusus wilayah Daerah Istimewa Yogyakarta yang mendukung pencarian multi-kriteria dan pemfilteran kategori berbasis pertukaran DOM parsial menggunakan HTMX tanpa pemuatan ulang halaman?\n"
                            "4. Bagaimana membangun pusat respons darurat yang mampu menyajikan nomor panggilan darurat nasional serta menghasilkan pesan darurat WhatsApp otomatis yang terenkripsi dan terhubung langsung ke kontak keluarga melalui skema click-to-chat?")

    add_styled_heading(doc, "1.3 Tujuan Pengembangan", level=2)
    add_body_paragraph(doc, "Tujuan yang hendak dicapai melalui perancangan dan implementasi website RantauHub ini meliputi:\n"
                            "1. Mengembangkan website RantauHub dengan kerangka kerja Django 5.x yang menerapkan pola arsitektur Thin Views / Fat Services guna memisahkan logika presentasi dan aturan bisnis secara modular.\n"
                            "2. Menyediakan fitur Survival Checklist dengan sinkronisasi template otomatis dan status periksa mandiri yang terisolasi aman untuk setiap akun pengguna.\n"
                            "3. Menyediakan modul Kalkulator Anggaran Finansial yang secara cerdas memproyeksikan pengeluaran makan bulanan, total beban biaya hidup, sisa saldo, dan evaluasi kelayakan rasio dana darurat perantau.\n"
                            "4. Membangun sistem Direktori Fasilitas Esensial berisi 88 lokasi terverifikasi di wilayah Yogyakarta (Puskesmas, Rumah Sakit, Klinik 24 Jam, Apotek, Warteg, Laundry, Bengkel, dan Perpustakaan) dengan fitur penanda favorit personal.\n"
                            "5. Mengintegrasikan Pusat Respons Darurat (Emergency Center) yang mencakup Kartu Identitas Darurat, panduan pindah faskes BPJS Kesehatan melalui Mobile JKN, protokol penanganan kehilangan dokumen resmi, serta generator pesan WhatsApp darurat.")

    add_styled_heading(doc, "1.4 Manfaat Pengembangan", level=2)
    add_body_paragraph(doc, "Pengembangan website RantauHub diharapkan mampu memberikan manfaat yang nyata bagi berbagai pihak:\n"
                            "1. Bagi Pengguna (Mahasiswa dan Pekerja Perantau):\n"
                            "   Membantu mempercepat proses adaptasi di kota perantauan, meminimalkan risiko tertinggalnya barang bawaan penting, mencegah kegagalan manajemen keuangan bulanan, memudahkan penemuan faskes dan layanan esensial murah di Yogyakarta, serta memberikan rasa tenang karena memiliki instrumen keselamatan darurat terpadu.\n"
                            "2. Bagi Pelajar, Satuan Pendidikan, dan Masyarakat:\n"
                            "   Menjadi contoh nyata inovasi produk digital berbasis kebutuhan riil masyarakat yang dapat diakses oleh publik, sekaligus memperlihatkan kemampuan siswa SMK program keahlian PPLG dalam memecahkan permasalahan sosial melalui rekayasa perangkat lunak.\n"
                            "3. Bagi Penulis (Pengembang):\n"
                            "   Mengembangkan kompetensi teknis dalam pemanfaatan kerangka kerja Django skala profesional, penerapan prinsip clean code dan service-oriented pattern, implementasi UI modern berbasis Tailwind CSS, HTMX, dan Alpine.js, pengelolaan skema data relasional, serta penulisan automated unit test yang disiplin.")

    add_styled_heading(doc, "1.5 Ruang Lingkup", level=2)
    add_body_paragraph(doc, "Untuk menjaga ketajaman analisis dan menjamin bahwa seluruh isi dokumen sesuai dengan kode program aktual di dalam workspace, batasan sistem (ruang lingkup) ditetapkan secara jujur dan transparan sebagai berikut:\n"
                            "1. Cakupan Geografis Direktori: Modul direktori fasilitas esensial dalam rilis ini secara spesifik berfokus pada wilayah Daerah Istimewa Yogyakarta (Kabupaten Sleman, Kota Yogyakarta, dan Kabupaten Bantul) dengan total 88 lokasi terkurasi di 12 kategori fasilitas publik.\n"
                            "2. Arsitektur Basis Data: Sistem menggunakan mesin basis data relasional SQLite3 lokal melalui Django ORM untuk lingkungan pengembangan dan pengujian, tanpa mengimplementasikan replikasi basis data multi-master.\n"
                            "3. Integrasi Komunikasi Darurat: Generator pesan darurat mengandalkan protokol resmi WhatsApp Click-to-Chat URL (https://wa.me/<nomor>?text=<pesan_terencode>) yang mengeksekusi aplikasi WhatsApp lokal milik pengguna, bukan melalui WhatsApp Business Cloud API berbayar.\n"
                            "4. Dependensi Frontend Eksternal: Lembar gaya antarmuka Tailwind CSS, pustaka HTMX 1.9.10, dan pustaka Alpine.js 3.13.5 dimuat melalui Content Delivery Network (CDN) publik, sehingga tampilan antarmuka interaktif membutuhkan koneksi internet pada browser pengguna.\n"
                            "5. Rasionalisasi Modul Komunitas: Sesuai dengan hasil refaktorisasi arsitektur perangkat lunak terkini pada proyek, modul komunitas pengguna dan forum publik telah sepenuhnya dieliminasi dari basis kode guna memfokuskan platform secara ketat pada modul utilitas bertahan hidup (Survival Kit), direktori faskes esensial, dan modul darurat dengan standar privasi tinggi.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB II LANDASAN TEORI
    # -------------------------------------------------------------
    add_styled_heading(doc, "BAB II\nLANDASAN TEORI", level=1)

    add_styled_heading(doc, "2.1 Arsitektur Web dan Model Client–Server", level=2)
    add_body_paragraph(doc, "Aplikasi web modern beroperasi di atas paradigma client-server, di mana peramban web (client) bertindak sebagai antarmuka pengguna yang berinteraksi melalui jaringan komputer dengan server aplikasi menggunakan protokol Hypertext Transfer Protocol (HTTP) atau versi terenkripsinya (HTTPS). Dalam model ini, klien mengirimkan permintaan (HTTP Request) yang memuat metode tertentu seperti GET (pengambilan data) atau POST (pengiriman data), dan server memproses permintaan tersebut untuk kemudian mengembalikan respons (HTTP Response) berupa kode status, metadata header, dan tubuh konten berupa dokumen HTML, data JSON, atau berkas biner.")

    add_body_paragraph(doc, "Django mengimplementasikan variasi arsitektur Model-View-Controller (MVC) yang diadaptasi menjadi pola Model-View-Template (MVT). Pada pola MVT Django:\n"
                            "• Model: Merupakan representasi struktur data dan aturan integritas tabel basis data yang didefinisikan sebagai kelas Python.\n"
                            "• View: Bertindak sebagai controller atau pengatur logika presentasi yang menerima HTTP request, berinteraksi dengan model atau service layer, dan menentukan template apa yang akan dirender.\n"
                            "• Template: Merupakan berkas presentasi antarmuka (biasanya HTML) yang disisipi tag sintaksis Django Template Language (DTL) untuk menyuntikkan data dinamis secara aman sebelum dikirimkan ke peramban.")

    add_styled_heading(doc, "2.2 HTML5, CSS3, Tailwind CSS, dan JavaScript", level=2)
    add_body_paragraph(doc, "HTML5 (Hypertext Markup Language versi 5) menyediakan fondasi semantik untuk menstrukturkan konten dokumen web, seperti penggunaan elemen <header>, <nav>, <main>, <section>, dan <footer> yang mendukung keterbacaan kode dan standar aksesibilitas web. CSS3 (Cascading Style Sheets level 3) bertanggung jawab atas tata letak visual, tipografi, warna, dan transisi animasi responsif.")

    add_body_paragraph(doc, "Dalam proyek RantauHub, antarmuka dikembangkan menggunakan Tailwind CSS. Tailwind CSS adalah kerangka kerja CSS berbasis utilitas (utility-first) yang menyediakan kelas-kelas CSS atomik siap pakai (misalnya flex, items-center, bg-blue-600, rounded-xl, shadow-md). Pendekatan ini memungkinkan perancangan tata letak antarmuka modern, konsisten, dan responsif secara langsung pada berkas template HTML tanpa perlu menuliskan ratusan baris aturan CSS kustom yang rentan terhadap konflik penamaan (class name collision). JavaScript murni (Vanilla JS) digunakan secara minimalis pada berkas static/js/main.js untuk mendukung manipulasi DOM lokal dan penanganan event peramban.")

    add_styled_heading(doc, "2.3 HTMX dan Interaktivitas Reaktif Modern", level=2)
    add_body_paragraph(doc, "HTMX (High-power Tools for HTML) adalah pustaka JavaScript modern berukuran sangat ringkas (~14 KB) yang memperluas kemampuan dasar elemen HTML standar. Melalui atribut kustom berbasis HTML seperti hx-get, hx-post, hx-target, hx-swap, dan hx-trigger, elemen HTML biasa seperti <div>, <button>, atau <input> dapat melakukan panggilan AJAX asinkronus ke server backend.")

    add_body_paragraph(doc, "Keunggulan utama arsitektur Hypermedia-Driven Application (HDA) yang ditawarkan oleh HTMX adalah kemampuannya menerima potongan fragmen HTML (HTML partials) langsung dari Django Views, kemudian menyuntikkannya ke bagian tertentu dari Document Object Model (DOM) tanpa memuat ulang seluruh halaman peramban (full page reload). Pendekatan ini secara drastis mengurangi beban overhead peramban, mengeliminasi kebutuhan penulisan API JSON yang rumit untuk operasi antarmuka sederhana, serta menjaga seluruh logika rendering tetap terpusat di sisi server (Server-Side Rendering).")

    add_styled_heading(doc, "2.4 Alpine.js untuk Deklaratif Komponen Antarmuka", level=2)
    add_body_paragraph(doc, "Alpine.js adalah kerangka kerja JavaScript reaktif yang ringan dan deklaratif, dirancang khusus untuk menangani interaktivitas mikro pada antarmuka web, seperti pembukaan dialog modal, pengelolaan dropdown menu, tab switcher, dan penutupan toast alert. Berbeda dengan kerangka kerja SPA besar seperti React atau Vue yang membutuhkan build step (bundler) yang kompleks, Alpine.js disematkan langsung pada atribut elemen HTML (seperti x-data, x-show, x-cloak, x-transition, dan @click). Pada RantauHub, Alpine.js berkolaborasi secara harmonis dengan Tailwind CSS dan HTMX untuk menyajikan interaksi pengguna yang mulus dan elegan.")

    add_styled_heading(doc, "2.5 Bahasa Pemrograman Python dan Framework Django", level=2)
    add_body_paragraph(doc, "Python adalah bahasa pemrograman tingkat tinggi yang mengutamakan keterbacaan kode (clean syntax), produktivitas pengembang, dan fleksibilitas berorientasi objek. Versi Python 3.12+ yang digunakan pada proyek ini menyediakan performa eksekusi bytecode yang lebih cepat dan dukungan pengetikan statis (type hinting) yang matang.")

    add_body_paragraph(doc, "Django 5.x merupakan kerangka kerja web kelas industri berbasis Python yang menganut filosofi \"batteries-included\". Django menyediakan infrastruktur komprehensif bawaan, meliputi modul autentikasi pengguna terenkripsi, sistem manajemen sesi (session framework), proteksi keamanan terintegrasi terhadap serangan umum (Cross-Site Request Forgery/CSRF, Cross-Site Scripting/XSS, SQL Injection, dan Clickjacking), serta sistem routing URL yang bersih dan modular.")

    add_styled_heading(doc, "2.6 Basis Data Relasional SQLite dan Django ORM", level=2)
    add_body_paragraph(doc, "Basis data relasional (RDBMS) mengorganisasikan data ke dalam tabel-tabel terstruktur yang saling berelasi melalui kunci utama (Primary Key) dan kunci asing (Foreign Key). SQLite3 adalah mesin basis data relasional berbasis berkas lokal yang mandiri (self-contained), tanpa server (serverless), dan tanpa konfigurasi rumit, menjadikannya standar ideal untuk pengembangan, portabilitas sistem, dan pengujian perangkat lunak.")

    add_body_paragraph(doc, "Django Object-Relational Mapping (ORM) menjembatani interaksi antara kode berorientasi objek Python dan tabel relasional basis data. Melalui Django ORM, pengembang dapat mendefinisikan skema tabel menggunakan kelas Python (django.db.models.Model), melakukan migrasi skema basis data secara otomatis melalui perintah makemigrations dan migrate, serta mengeksekusi operasi manipulasi data (CRUD) menggunakan sintaksis QuerySet yang aman dari ancaman SQL Injection.")

    add_styled_heading(doc, "2.7 Pola Arsitektur Layanan (Thin Views / Fat Services Architecture)", level=2)
    add_body_paragraph(doc, "Dalam pengembangan perangkat lunak berbasis Django skala profesional, anti-pola \"Fat Views\" (menuliskan seluruh logika bisnis, validasi, dan manipulasi data di dalam fungsi view) sangat dihindari karena menyebabkan kode sulit diuji dan dipelihara. RantauHub secara ketat menerapkan pola desain Thin Views / Fat Services.")

    add_body_paragraph(doc, "Dalam pola arsitektur ini:\n"
                            "1. Layer Controller (Views): Dibatasi secara ketat di bawah 150 baris kode per berkas. Tugas view hanya menerima HTTP request, melakukan validasi awal masukan, memanggil service atau selector yang relevan, dan mengembalikan respons HTTP atau template HTML.\n"
                            "2. Layer Services (Logika Bisnis): Berada di dalam sub-direktori services/ pada masing-masing aplikasi (misalnya apps/survival_kit/services/budget_calculator.py dan checklist_service.py). Layer ini memuat fungsi-fungsi murni untuk kalkulasi matematis, manipulasi status, dan integrasi eksternal.\n"
                            "3. Layer Selectors (Pengambilan Data): Berada di dalam sub-direktori selectors/ (misalnya apps/directory/selectors/place_search.py). Layer ini bertugas membungkus query pencarian data yang kompleks menggunakan Q objects dan filter kriteria multi-parameter.")

    add_styled_heading(doc, "2.8 Pengujian Perangkat Lunak (Django Automated Testing)", level=2)
    add_body_paragraph(doc, "Pengujian perangkat lunak adalah disiplin verifikasi dan validasi untuk memastikan bahwa kode program berperilaku sesuai dengan spesifikasi fungsional yang telah ditentukan. Kerangka kerja pengujian otomatis Django (dibangun di atas modul standar unittest Python) menyediakan kelas django.test.TestCase.")

    add_body_paragraph(doc, "Kelas TestCase secara otomatis membuat basis data pengujian sementara yang terisolasi untuk setiap sesi pengujian, menjalankan migrasi skema, mengeksekusi metode-metode uji, dan melakukan rollback basis data pada akhir sesi pengujian. Melalui pengujian otomatis berbasis assertion (seperti assertEqual, assertTrue, dan assertIn), stabilitas fitur inti seperti registrasi pengguna, kalkulasi surplus anggaran, sinkronisasi checklist, pencarian direktori, dan encoding nomor WhatsApp dapat diverifikasi secara objektif dan berulang.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB III ANALISIS DAN PERANCANGAN SISTEM
    # -------------------------------------------------------------
    add_styled_heading(doc, "BAB III\nANALISIS DAN PERANCANGAN SISTEM", level=1)

    add_styled_heading(doc, "3.1 Analisis Sistem", level=2)
    add_body_paragraph(doc, "Analisis sistem bertujuan untuk memetakan alur interaksi pengguna, mengidentifikasi titik kegagalan adaptasi perantau baru, serta merumuskan kebutuhan fungsional dan teknis yang harus dipenuhi oleh platform RantauHub. Sistem dirancang untuk melayani dua jenis pengguna: pengguna umum (tamu/guest) yang membutuhkan akses cepat ke informasi fasilitas esensial dan panduan darurat, serta pengguna terdaftar (authenticated user) yang memiliki akses ke dashboard personal, penyimpanan checklist adaptasi tersinkronisasi, kalkulator anggaran bulanan, dan penyimpanan fasilitas favorit.")

    add_styled_heading(doc, "3.2 Analisis Kebutuhan", level=2)
    add_body_paragraph(doc, "Kebutuhan fungsional sistem mencerminkan seluruh kemampuan teknis yang disediakan oleh kode program aktual di dalam workspace RantauHub. Rincian kebutuhan fungsional disajikan pada Tabel 3.1.")

    # Tabel 3.1 Kebutuhan Fungsional
    p_tbl_lbl = doc.add_paragraph()
    p_tbl_lbl.paragraph_format.space_before = Pt(8)
    p_tbl_lbl.paragraph_format.space_after = Pt(4)
    r_tl = p_tbl_lbl.add_run("Tabel 3.1 Kebutuhan Fungsional Website RantauHub")
    r_tl.font.name = "Times New Roman"
    r_tl.font.size = Pt(10.5)
    r_tl.font.bold = True

    t31_headers = ["Kode", "Modul Sistem", "Deskripsi Kebutuhan Fungsional Aktual"]
    t31_widths = [Inches(1.0), Inches(2.2), Inches(3.4)]
    t31_data = [
        ("F-01", "Autentikasi & Akun", "Menyediakan registrasi pengguna dengan profil domisili (kota asal, kota tujuan, kecamatan tujuan, dan instansi kampus/kantor)."),
        ("F-02", "Autentikasi & Akun", "Mengautentikasi pengguna melalui login aman, manajemen sesi, dan pengakhiran sesi (logout) dengan redirection yang tepat."),
        ("F-03", "Profil & Dashboard", "Menyediakan halaman profil untuk memperbarui data kontak darurat keluarga serta dashboard ringkasan progres adaptasi."),
        ("F-04", "Checklist Adaptasi", "Menyinkronkan template bawaan checklist perantau (dokumen, kost, akademik, kesehatan) secara otomatis saat pengguna mengakses modul."),
        ("F-05", "Checklist Adaptasi", "Mengubah status selesai/belum (toggle) item checklist secara asinkronus menggunakan HTMX dengan pembaruan progress bar instan."),
        ("F-06", "Checklist Adaptasi", "Memungkinkan pengguna menambahkan tugas atau barang bawaan khusus secara mandiri ke dalam checklist personal mereka."),
        ("F-07", "Kalkulator Anggaran", "Melakukan kalkulasi alokasi finansial bulanan dengan presisi Decimal, mendeteksi status Surplus/Defisit, dan menghitung rasio dana darurat."),
        ("F-08", "Panduan Survival", "Menyajikan artikel panduan adaptasi kehidupan mandiri yang dikelompokkan ke dalam kategori terstruktur dengan indikator waktu baca."),
        ("F-09", "Direktori Fasilitas", "Menampilkan direktori terkurasi 88 fasilitas esensial di Yogyakarta yang dikelompokkan ke dalam 12 kategori spesifik."),
        ("F-10", "Direktori Fasilitas", "Menyediakan pencarian multi-kriteria berbasis nama lokasi, kategori fasilitas, dan filter kecamatan/kota menggunakan selector Django."),
        ("F-11", "Direktori Fasilitas", "Menyediakan fitur simpan/favoritkan lokasi fasilitas esensial personal bagi pengguna yang telah masuk ke dalam sistem."),
        ("F-12", "Pusat Respons Darurat", "Menyajikan Kartu Darurat Nasional, panduan pindah faskes BPJS, protokol kehilangan dokumen, serta generator pesan WhatsApp SOS terformat."),
    ]
    tbl_31 = doc.add_table(rows=1, cols=3)
    style_table(tbl_31, t31_widths, t31_headers, t31_data)

    add_styled_heading(doc, "Kebutuhan Nonfungsional", level=3)
    add_body_paragraph(doc, "Selain kebutuhan fungsional, sistem RantauHub memenuhi sejumlah kebutuhan nonfungsional kritis:\n"
                            "1. Kemudahan Penggunaan (Usability): Antarmuka dirancang dengan pendekatan mobile-first, navigasi intuitif, kontras warna yang nyaman di mata, dan umpan balik visual instan (toast dan status badges).\n"
                            "2. Integritas dan Keamanan Data (Security): Kata sandi pengguna diamankan menggunakan algoritma hashing PBKDF2 bawaan Django. Seluruh formulir POST dilindungi token CSRF guna mencegah serangan pemalsuan permintaan antar-situs.\n"
                            "3. Isolasi Data (Data Isolation): Sistem menjamin bahwa item checklist kustom dan data perencanaan finansial milik seorang pengguna tidak dapat diakses atau diubah oleh pengguna lain melalui validasi kepemilikan sesi di service layer.\n"
                            "4. Efisiensi dan Performa: Pemanfaatan HTMX meminimalkan pertukaran data melalui jaringan karena hanya fragmen HTML parsial yang ditransmisikan, menghasilkan interaksi yang gesit bahkan pada koneksi internet seluler terbatas.")

    add_styled_heading(doc, "3.3 Arsitektur Sistem", level=2)
    add_body_paragraph(doc, "Arsitektur sistem RantauHub memadukan interaksi empat lapisan utama yang saling terisolasi secara logis, yaitu Lapisan Klien / Peramban, Lapisan Pengaturan Server & Routing Django, Lapisan Logika Bisnis & Layanan (Services), serta Lapisan Basis Data Relasional SQLite. Struktur alur arsitektur disajikan pada Gambar 3.1.")

    add_figure(doc, os.path.join(ASSETS_DIR, "gambar_3_1_arsitektur.png"), "Gambar 3.1 Diagram Alur Arsitektur Sistem RantauHub")

    add_styled_heading(doc, "3.4 Alur Kerja Pemrosesan", level=2)
    add_body_paragraph(doc, "Alur kerja pemrosesan data pada sistem RantauHub dirancang secara terstruktur dan efisien. Berikut adalah rincian lima alur kerja operasional utama:\n\n"
                            "1. Alur Registrasi dan Personalisasi Pengguna:\n"
                            "   Pengguna mengisi formulir pendaftaran pada rute /auth/register/ dengan menyertakan nama pengguna, email, kata sandi, serta informasi domisili (kota asal, kota tujuan perantauan, dan kampus/kantor). Data divalidasi oleh RegistrationForm. Jika valid, akun disimpan ke tabel User dan sistem secara otomatis mengautentikasi pengguna menuju halaman dashboard.\n\n"
                            "2. Alur Pengelolaan Checklist Adaptasi Mandiri:\n"
                            "   Saat pengguna membuka menu Checklist (/survival/checklist/), service sync_user_checklists() memeriksa apakah seluruh template bawaan dari ChecklistTemplate telah disalin ke relasi UserChecklist milik pengguna bersangkutan. Pengguna dapat mengetuk kotak centang pada suatu item tugas, yang kemudian memicu request AJAX hx-post ke rute /survival/checklist/toggle/<id>/. Layanan toggle_checklist_item_service() memvalidasi kepemilikan data, mengubah status penyelesaian, menghitung ulang persentase progres total, dan mengembalikan potongan HTML kartu tugas yang langsung diperbarui pada antarmuka.\n\n"
                            "3. Alur Simulasi Anggaran Finansial:\n"
                            "   Pengguna memasukkan parameter keuangan bulanan melalui formulir di rute /survival/budget/ (uang saku, sewa kost, konsumsi harian, transportasi, internet, dan alokasi tabungan darurat). Saat formulir dikirimkan, view memanggil layanan calculate_budget(). Layanan ini mengevaluasi total biaya makan sebulan (konsumsi harian × 30 hari), menjumlahkan seluruh beban pengeluaran, menghitung sisa saldo bebas, mengklasifikasikan status keuangan menjadi 'Surplus' atau 'Defisit', serta mengevaluasi apakah rasio tabungan darurat telah mencapai batas ideal (≥10% dari uang saku).\n\n"
                            "4. Alur Penelusuran Direktori Fasilitas Esensial:\n"
                            "   Pengguna mengetikkan kata kunci pencarian atau memilih pil filter kategori pada rute /directory/. Peramban mengirimkan parameter pencarian melalui permintaan HTTP GET. Fungsi selector search_places() mengonstruksikan query Django ORM berbasis objek Q(name__icontains=query) | Q(district__icontains=query) serta filter kategori. Sebanyak 88 data fasilitas terverifikasi difilter secara instan dan disajikan kembali ke antarmuka.\n\n"
                            "5. Alur Pembuatan Pesan Bantuan Darurat WhatsApp:\n"
                            "   Pada rute /emergency/whatsapp-generator/, pengguna memilih jenis situasi darurat (sakit medis, kecelakaan, tindak kejahatan, atau bencana), memasukkan titik lokasi terkini, dan rincian bantuan yang dibutuhkan. Fungsi layanan generate_emergency_whatsapp_message() memformat teks darurat dengan tag visual tegas (*...*, 📍, ℹ️), menormalkan format nomor telepon kontak keluarga (mengubah awalan '08' menjadi standar internasional '628'), melakukan URL-encoding pada seluruh isi pesan, dan menghasilkan tautan resmi https://wa.me/62... yang dapat langsung dibuka oleh pengguna.")

    add_styled_heading(doc, "3.5 Perancangan Data", level=2)
    add_body_paragraph(doc, "Perancangan skema data sistem RantauHub diorganisasikan ke dalam model-model relasional yang bersih, terindeks, dan mematuhi kaidah normalisasi basis data. Seluruh entitas diturunkan dari kelas dasar TimeStampedModel untuk mencatat waktu pembuatan (created_at) dan pembaruan terakhir (updated_at) secara otomatis. Struktur tabel data dirangkum pada Tabel 3.2.")

    # Tabel 3.2 Struktur Entitas Basis Data
    p_tbl32_lbl = doc.add_paragraph()
    p_tbl32_lbl.paragraph_format.space_before = Pt(8)
    p_tbl32_lbl.paragraph_format.space_after = Pt(4)
    r_t32l = p_tbl32_lbl.add_run("Tabel 3.2 Skema Struktur Entitas Basis Data Relasional RantauHub")
    r_t32l.font.name = "Times New Roman"
    r_t32l.font.size = Pt(10.5)
    r_t32l.font.bold = True

    t32_headers = ["Entitas Model", "Atribut / Kolom Utama", "Tipe Data & Batasan", "Fungsi & Keterangan Relasi"]
    t32_widths = [Inches(1.2), Inches(2.0), Inches(1.8), Inches(2.2)]
    t32_data = [
        ("User (Kustom)", "username, email, password\norigin_city, target_city\ntarget_district, campus_or_office\nemergency_contact_name\nemergency_contact_phone", "CharField / EmailField\nCharField(100)\nCharField(100)\nCharField(100)\nCharField(20)", "Menyimpan kredensial autentikasi pengguna, profil daerah asal dan tujuan rantau, serta kontak darurat keluarga."),
        ("ChecklistTemplate", "category, title, description\nis_essential", "CharField(choices)\nCharField(200)\nTextField, BooleanField", "Katalog master tugas/barang bawaan standar untuk perantau (dokumen, kost, akademik, kesehatan)."),
        ("UserChecklist", "user_id, template_id\ncustom_title, is_completed\ncompleted_at", "ForeignKey(User)\nForeignKey(Template, null)\nCharField(200), Boolean\nDateTimeField(null)", "Menyimpan status centang personal pengguna terhadap template bawaan atau tugas kustom mandiri."),
        ("BudgetPlan", "user_id, monthly_allowance\nrent_cost, food_daily\ntransport_monthly, internet_cost\ncampus_work_cost, personal_cost\nemergency_reserve", "OneToOneField(User)\nDecimalField(12, 2)\nDecimalField(12, 2)\nDecimalField(12, 2)\nDecimalField(12, 2)", "Menyimpan parameter kalkulasi alokasi finansial perantau dengan presisi desimal mata uang rupiah."),
        ("GuideArticle", "title, slug, category\nexcerpt, content\nreading_time_minutes", "CharField(200), SlugField\nCharField(choices)\nTextField, TextField\nPositiveIntegerField", "Menyimpan artikel panduan bertahan hidup mandiri, tips kost, dan etika adaptasi budaya lokal."),
        ("EssentialPlace", "name, category, city\ndistrict, address\ngoogle_maps_url, phone_number\nprice_range, is_verified, notes", "CharField(150), CharField\nCharField(100), CharField\nTextField, URLField\nCharField(50), Boolean\nTextField", "Menyimpan master data 88 fasilitas esensial DIY di 12 kategori publik terverifikasi."),
        ("FavoritePlace", "user_id, place_id\ncreated_at", "ForeignKey(User)\nForeignKey(EssentialPlace)\nDateTimeField(auto_now_add)", "Menyimpan relasi bookmark penanda lokasi fasilitas favorit yang disimpan oleh pengguna terdaftar."),
    ]
    tbl_32 = doc.add_table(rows=1, cols=4)
    style_table(tbl_32, t32_widths, t32_headers, t32_data)

    add_styled_heading(doc, "3.6 Rancangan Antarmuka", level=2)
    add_body_paragraph(doc, "Perancangan antarmuka RantauHub berorientasi pada kemudahan navigasi, kejelasan informasi, dan kenyamanan visual bagi perantau yang mengakses website melalui gawai telepon pintar (smartphone) maupun komputer jinjing (laptop). Filosofi desain yang diterapkan adalah clean, empathetic, and responsive interface.")

    add_body_paragraph(doc, "Palet warna antarmuka didominasi oleh warna biru tua (Deep Navy #1E3A8A dan Royal Blue #2563EB) yang merepresentasikan kepercayaan, profesionalisme, dan kestabilan. Sebagai aksen fungsional, sistem menggunakan warna hijau zamrud (#10B981) untuk status keberhasilan, verifikasi, dan surplus keuangan, warna kuning amber (#F59E0B) untuk peringatan saldo menipis, serta warna merah tegas (#EF4444) untuk seluruh modul panggilan darurat dan peringatan krisis medis. Tata letak elemen disusun secara modular menggunakan grid dan flexbox responsif dari Tailwind CSS.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB IV IMPLEMENTASI DAN PENGUJIAN
    # -------------------------------------------------------------
    add_styled_heading(doc, "BAB IV\nIMPLEMENTASI DAN PENGUJIAN", level=1)

    add_styled_heading(doc, "4.1 Lingkungan dan Teknologi", level=2)
    add_body_paragraph(doc, "Implementasi proyek RantauHub dibangun di atas tumpukan teknologi (tech stack) berbasis Python dan web modern yang terintegrasi secara modular. Rincian teknologi dan perannya dalam pengembangan sistem dirangkum pada Tabel 4.1.")

    # Tabel 4.1 Teknologi dan Komponen Proyek
    p_tbl41_lbl = doc.add_paragraph()
    p_tbl41_lbl.paragraph_format.space_before = Pt(8)
    p_tbl41_lbl.paragraph_format.space_after = Pt(4)
    r_t41l = p_tbl41_lbl.add_run("Tabel 4.1 Teknologi dan Komponen Perangkat Lunak Proyek RantauHub")
    r_t41l.font.name = "Times New Roman"
    r_t41l.font.size = Pt(10.5)
    r_t41l.font.bold = True

    t41_headers = ["Komponen", "Teknologi / Pustaka", "Peran dan Tanggung Jawab dalam Sistem"]
    t41_widths = [Inches(1.5), Inches(2.2), Inches(3.5)]
    t41_data = [
        ("Bahasa Pemrograman", "Python 3.12+", "Bahasa utama untuk seluruh logika server, kalkulasi finansial, dan pengujian."),
        ("Kerangka Backend", "Django 5.0.x", "Menyediakan routing URL, ORM basis data, otentikasi akun, CSRF guard, dan template engine."),
        ("Basis Data", "SQLite 3", "Penyimpanan relasional lokal untuk pengguna, checklist, kalkulator anggaran, dan direktori."),
        ("Penggayaan Antarmuka", "Tailwind CSS (via CDN)", "Kerangka kerja CSS utility-first untuk menyusun desain antarmuka modern dan responsif."),
        ("Interaktivitas AJAX", "HTMX 1.9.10", "Menangani pembaruan DOM parsial asinkronus (toggle checklist, filter direktori, live preview WA)."),
        ("Manajemen State UI", "Alpine.js 3.13.5", "Pustaka JavaScript mikro-reaktif untuk membuka/menutup modal, menu dropdown, dan tab."),
        ("Konfigurasi Sistem", "python-decouple", "Mengelola parameter rahasia dan konfigurasi lingkungan melalui berkas .env secara aman."),
        ("Pengolahan Citra", "Pillow 12.3.0", "Validasi dan penanganan berkas avatar foto profil pengguna pada model User."),
        ("Arsitektur Kode", "Thin Views / Fat Services", "Pola pemisahan logika bisnis ke service layer agar controller views tetap ringkas (<150 baris)."),
        ("Pengujian Otomatis", "Django Test Runner (unittest)", "Eksekusi automated test suite untuk memastikan keandalan modul autentikasi, survival, dan direktori."),
    ]
    tbl_41 = doc.add_table(rows=1, cols=3)
    style_table(tbl_41, t41_widths, t41_headers, t41_data)

    add_styled_heading(doc, "4.2 Struktur Program", level=2)
    add_body_paragraph(doc, "Struktur direktori proyek RantauHub diorganisasikan ke dalam modul aplikasi lokal (local apps) yang mandiri di bawah direktori apps/, konfigurasi terpusat pada config/, berkas aset statis pada static/, serta berkas template antarmuka pada templates/. Struktur fisik program disajikan pada Tabel 4.2.")

    # Tabel 4.2 Struktur Direktori Program
    p_tbl42_lbl = doc.add_paragraph()
    p_tbl42_lbl.paragraph_format.space_before = Pt(8)
    p_tbl42_lbl.paragraph_format.space_after = Pt(4)
    r_t42l = p_tbl42_lbl.add_run("Tabel 4.2 Struktur Direktori dan Tanggung Jawab Modul Program")
    r_t42l.font.name = "Times New Roman"
    r_t42l.font.size = Pt(10.5)
    r_t42l.font.bold = True

    t42_headers = ["Lokasi Berkas / Folder", "Tanggung Jawab dan Isi Modul"]
    t42_widths = [Inches(2.4), Inches(4.8)]
    t42_data = [
        ("config/settings/base.py, dev.py", "Konfigurasi inti Django, pendaftaran installed apps, middleware, template DTL, dan zona waktu Asia/Jakarta."),
        ("config/urls.py", "Root URL routing yang memetakan modul auth/, survival/, directory/, emergency/, dan error handlers."),
        ("apps/common/", "Model dasar abstrak TimeStampedModel, view halaman beranda/tentang, template tags bersama, dan error views."),
        ("apps/users/", "Kustomisasi model User (AbstractUser), formulir login/registrasi/profil, dan view dashboard perantau."),
        ("apps/survival_kit/models/", "Definisi entitas ChecklistTemplate, UserChecklist, BudgetPlan, dan GuideArticle."),
        ("apps/survival_kit/services/", "Logika murni kalkulator anggaran (budget_calculator.py) dan sinkronisasi checklist (checklist_service.py)."),
        ("apps/survival_kit/views/", "Controller tipis untuk manajemen checklist, simulasi anggaran, dan pembacaan artikel panduan."),
        ("apps/directory/models/", "Model master EssentialPlace (12 kategori fasilitas DIY) dan penanda bookmark FavoritePlace."),
        ("apps/directory/selectors/", "Query selector pencarian multi-kriteria lokasi (place_search.py) berbasis Q objects."),
        ("apps/emergency/views/", "Controller kartu identitas darurat (card.py), generator WA (whatsapp_generator.py), dan panduan BPJS."),
        ("apps/emergency/services/", "Logika normalisasi nomor telepon 62 dan encoding string pesan WhatsApp (wa_encoder.py)."),
        ("templates/ (base, pages, partials)", "Struktur template antarmuka modular Django, komponen kartu, modal Alpine, dan fragmen swap HTMX."),
        ("static/css/, static/js/", "Lembar gaya tambahan dan skrip JavaScript minimal untuk penanganan event antarmuka peramban."),
        ("tests/ (test_auth, survival, dir, emg)", "Rangkaian 12 automated unit tests yang memverifikasi seluruh fungsi kritis sistem."),
    ]
    tbl_42 = doc.add_table(rows=1, cols=2)
    style_table(tbl_42, t42_widths, t42_headers, t42_data)

    add_styled_heading(doc, "4.3 Implementasi Antarmuka", level=2)
    add_body_paragraph(doc, "Dokumentasi tangkapan layar antarmuka berikut ini memperlihatkan hasil implementasi visual halaman utama, dashboard perantau, simulasi kalkulator finansial, direktori fasilitas esensial, serta pusat respons darurat pada website RantauHub.")

    add_figure(doc, os.path.join(ASSETS_DIR, "gambar_4_1_beranda.png"), "Gambar 4.1 Tampilan Beranda Utama RantauHub")
    add_figure(doc, os.path.join(ASSETS_DIR, "gambar_4_2_dashboard_checklist.png"), "Gambar 4.2 Tampilan Dashboard Personal dan Checklist Adaptasi Perantau")
    add_figure(doc, os.path.join(ASSETS_DIR, "gambar_4_3_kalkulator_budget.png"), "Gambar 4.3 Tampilan Simulasi Kalkulator Finansial dan Rasio Dana Darurat")
    add_figure(doc, os.path.join(ASSETS_DIR, "gambar_4_4_direktori_fasilitas.png"), "Gambar 4.4 Tampilan Direktori Fasilitas Esensial Yogyakarta dan Filter Kategori")
    add_figure(doc, os.path.join(ASSETS_DIR, "gambar_4_5_emergency_sos.png"), "Gambar 4.5 Tampilan Pusat Bantuan Darurat SOS dan WhatsApp Message Generator")

    add_styled_heading(doc, "4.4 Implementasi Modul Autentikasi dan Profil Perantau (apps/users)", level=2)
    add_body_paragraph(doc, "Modul pengguna diimplementasikan melalui model User yang meng-extend AbstractUser Django. Kustomisasi ini menambahkan field spesifik rantau meliputi origin_city, target_city, target_district, campus_or_office, emergency_contact_name, dan emergency_contact_phone. Alur autentikasi memisahkan formulir registrasi dan login secara bersih pada apps/users/forms/auth.py dengan validasi kata sandi ganda dan sanitasi input.")

    add_body_paragraph(doc, "Halaman dashboard (dashboard_view) bertindak sebagai pusat ringkasan bagi perantau setelah berhasil login. Dashboard memanggil progress checklist pengguna melalui checklist_service, membaca data perencanaan anggaran terbaru, serta menampilkan kartu ringkas kontak darurat yang tersimpan pada profil pengguna. Rute profil dan dashboard diproteksi menggunakan dekorator @login_required guna menjamin bahwa pengguna yang belum terautentikasi akan dialihkan secara otomatis ke halaman login.")

    add_styled_heading(doc, "4.5 Implementasi Survival Kit: Checklist, Budget, dan Panduan (apps/survival_kit)", level=2)
    add_body_paragraph(doc, "Modul Survival Kit menjadi instrumen utama dalam memandu kesiapan perantau baru melalui tiga sub-fitur terpadu:\n"
                            "1. Sistem Checklist Adaptasi (apps/survival_kit/services/checklist_service.py):\n"
                            "   Layanan sync_user_checklists() menjamin sinkronisasi otomatis antara tabel master ChecklistTemplate dan tabel personal UserChecklist. Setiap item memiliki kategori (dokumen penting, perlengkapan kost, akademik & kerja, atau kesehatan & darurat). Saat pengguna melakukan centang, endpoint /survival/checklist/toggle/<id>/ dieksekusi secara asinkronus via HTMX, memperbarui status is_completed, mencatat completed_at, dan menghitung persentase kesiapan perantau secara instan.\n\n"
                            "2. Kalkulator Anggaran Finansial (apps/survival_kit/services/budget_calculator.py):\n"
                            "   Perhitungan finansial diimplementasikan sebagai fungsi murni berbasis tipe Decimal bawaan Python guna mencegah kesalahan pembulatan angka floating-point. Fungsi menghitung pengeluaran konsumsi bulanan (food_daily × 30), total pengeluaran dari delapan pos alokasi biaya, sisa saldo, status kelayakan ('Surplus' jika sisa saldo ≥ 0, 'Defisit' jika sebaliknya), serta rasio alokasi dana darurat terhadap uang saku dengan evaluasi ambang batas aman (≥ 10%).\n\n"
                            "3. Panduan Bertahan Hidup (Guide Articles):\n"
                            "   Menyajikan artikel literasi adaptasi budaya, tips hemat belanja bahan makanan, serta etika hidup bertetangga di Yogyakarta. Sistem menghitung estimasi waktu baca (reading_time_minutes) berdasarkan rasio panjang konten teks.")

    add_styled_heading(doc, "4.6 Implementasi Direktori DIY dan Pusat Respons Darurat (apps/directory & emergency)", level=2)
    add_body_paragraph(doc, "Modul direktori memuat 88 titik fasilitas esensial terkurasi khusus wilayah Daerah Istimewa Yogyakarta. Ke-88 lokasi tersebut dikelompokkan ke dalam 12 kategori publik spesifik: Puskesmas (Faskes 1), Klinik Pratama/24 Jam, Rumah Sakit Umum & IGD, Apotek 24 Jam, Warung Makan / Warteg Hemat, Laundry Kiloan, Minimarket, Fotokopi & Print Center, Coworking Space & Kafe Belajar, Bengkel Motor, Perpustakaan Publik, serta Pasar Tradisional. Pencarian data ditangani oleh apps/directory/selectors/place_search.py menggunakan query dinamis Q objects yang memungkinkan pencarian simultan pada nama tempat, alamat, dan kecamatan.")

    add_body_paragraph(doc, "Modul darurat (Emergency Center) menyajikan empat fungsi keselamatan terpadu:\n"
                            "1. Kartu Panggilan Darurat Nasional: Akses cepat ke nomor darurat 110 (Kepolisian), 119 (Gawat Darurat Medis SPGDT), 113 (Pemadam Kebakaran), 115 (Basarnas), 123 (PLN Gangguan Listrik Kost), dan 165 (BPJS Kesehatan Care Center).\n"
                            "2. Generator Pesan Darurat WhatsApp (apps/emergency/services/wa_encoder.py): Layanan otomatis yang menyusun pesan krisis terstruktur sesuai pilihan situasi (sakit, kecelakaan, kejahatan, bencana, atau tersesat), menormalkan nomor telepon keluarga menjadi format internasional 628..., melakukan URL encoding melalui urllib.parse.quote(), dan menghasilkan tautan https://wa.me/62... yang langsung membuka obrolan WhatsApp dengan pesan terisi rapi.\n"
                            "3. Panduan Pindah Faskes BPJS: Petunjuk praktis 4 langkah pemindahan faskes tingkat 1 ke puskesmas kota perantauan menggunakan aplikasi Mobile JKN tanpa perlu datang ke kantor cabang.\n"
                            "4. Protokol Kehilangan Dokumen: Langkah terstruktur pengurusan Surat Tanda Penerimaan Laporan Kehilangan (STPLK) di Polsek setempat ketika perantau kehilangan KTP, STNK, atau kartu ATM.")

    add_styled_heading(doc, "4.7 Endpoint Backend / Route Sistem", level=2)
    add_body_paragraph(doc, "Seluruh rute URL dan endpoint backend yang diimplementasikan pada proyek RantauHub terdaftar secara rapi dan modular. Rincian seluruh endpoint disajikan pada Tabel 4.3.")

    # Tabel 4.3 Endpoint Backend
    p_tbl43_lbl = doc.add_paragraph()
    p_tbl43_lbl.paragraph_format.space_before = Pt(8)
    p_tbl43_lbl.paragraph_format.space_after = Pt(4)
    r_t43l = p_tbl43_lbl.add_run("Tabel 4.3 Daftar Lengkap Endpoint Backend dan Route Sistem RantauHub")
    r_t43l.font.name = "Times New Roman"
    r_t43l.font.size = Pt(10.5)
    r_t43l.font.bold = True

    t43_headers = ["Endpoint / URL Route", "Metode HTTP", "Fungsi dan Logika Pengolahan"]
    t43_widths = [Inches(2.6), Inches(1.2), Inches(3.4)]
    t43_data = [
        ("/", "GET", "Menampilkan halaman beranda utama (home) dengan hero banner dan fitur unggulan."),
        ("/about/", "GET", "Menampilkan halaman informasi tentang platform RantauHub dan panduan umum."),
        ("/dashboard/", "GET", "Menampilkan dashboard personal perantau dengan progres checklist dan kontak darurat."),
        ("/auth/register/", "GET, POST", "Memproses formulir pendaftaran akun baru dengan data domisili asal dan tujuan."),
        ("/auth/login/", "GET, POST", "Memvalidasi kredensial pengguna dan menginisialisasi sesi login terenkripsi."),
        ("/auth/logout/", "GET, POST", "Mengakhiri sesi login pengguna dan mengalihkan kembali ke halaman utama."),
        ("/auth/profile/", "GET, POST", "Menampilkan dan memperbarui data profil perantau serta kontak darurat keluarga."),
        ("/survival/checklist/", "GET", "Menampilkan daftar checklist adaptasi dan menyinkronkan template bawaan."),
        ("/survival/checklist/toggle/<id>/", "POST", "Mengubah status centang item checklist via HTMX dan menghitung progres."),
        ("/survival/checklist/add/", "POST", "Menambahkan item tugas atau barang bawaan baru secara kustom."),
        ("/survival/budget/", "GET, POST", "Menghitung simulasi alokasi anggaran bulanan, status surplus/defisit, dan rasio darurat."),
        ("/survival/guides/", "GET", "Menampilkan daftar artikel panduan bertahan hidup mandiri di perantauan."),
        ("/survival/guides/<slug>/", "GET", "Menampilkan rincian isi artikel panduan berdasarkan slug pengenal unik."),
        ("/directory/", "GET", "Menampilkan katalog 88 fasilitas esensial DIY dengan pencarian dan filter kategori."),
        ("/directory/<pk>/", "GET", "Menampilkan rincian detail fasilitas esensial, alamat, jam buka, dan peta lokasi."),
        ("/directory/<pk>/favorite/", "POST", "Menandai atau menghapus fasilitas dari daftar simpan/favorit pengguna."),
        ("/emergency/card/", "GET", "Menampilkan kartu identitas darurat personal dan daftar nomor darurat nasional."),
        ("/emergency/whatsapp-generator/", "GET, POST", "Membuat pesan darurat terformat dan menghasilkan link URL resmi https://wa.me/."),
        ("/emergency/bpjs-guide/", "GET", "Menampilkan panduan 4 langkah migrasi Faskes 1 BPJS melalui aplikasi Mobile JKN."),
        ("/emergency/lost-document/", "GET", "Menampilkan panduan protokol pengurusan dokumen penting yang hilang di perantauan."),
    ]
    tbl_43 = doc.add_table(rows=1, cols=3)
    style_table(tbl_43, t43_widths, t43_headers, t43_data)

    add_styled_heading(doc, "4.8 Skenario Pemeriksaan", level=2)
    add_body_paragraph(doc, "Pemeriksaan fungsionalitas dan keandalan sistem RantauHub dilakukan melalui automated unit testing terstruktur yang dijalankan melalui perintah python manage.py test. Seluruh 12 skenario pengujian unit test dinyatakan lulus 100% (OK). Rincian skenario pemeriksaan dirangkum pada Tabel 4.4.")

    # Tabel 4.4 Skenario Pengujian Fitur
    p_tbl44_lbl = doc.add_paragraph()
    p_tbl44_lbl.paragraph_format.space_before = Pt(8)
    p_tbl44_lbl.paragraph_format.space_after = Pt(4)
    r_t44l = p_tbl44_lbl.add_run("Tabel 4.4 Skenario Pemeriksaan dan Pengujian Fitur RantauHub")
    r_t44l.font.name = "Times New Roman"
    r_t44l.font.size = Pt(10.5)
    r_t44l.font.bold = True

    t44_headers = ["No.", "Skenario Pengujian", "Perilaku yang Diharapkan / Bukti Hasil Pengujian"]
    t44_widths = [Inches(0.6), Inches(2.8), Inches(3.8)]
    t44_data = [
        ("1", "Registrasi akun pengguna baru (test_registration)", "Server merespons kode 302 redirect dan entitas pengguna baru tersimpan sukses di basis data."),
        ("2", "Autentikasi login dan logout (test_login_and_logout)", "Login pengguna terverifikasi, sesi aktif dibuat, dan saat logout sesi dihapus dengan kode 302."),
        ("3", "Proteksi rute privat tanpa login (test_protected_routes)", "Mengakses /dashboard/ dan /auth/profile/ tanpa sesi diarahkan otomatis ke /auth/login/ (status 302)."),
        ("4", "Pembaruan profil & kontak darurat (test_profile_update)", "Data kota tujuan dan kontak darurat keluarga berhasil diperbarui dan tersimpan permanen di basis data."),
        ("5", "Simulasi anggaran status Surplus (test_budget_surplus)", "Layanan menghitung total biaya secara presisi, menghasilkan sisa saldo Rp 200.000, status 'Surplus', dan rasio 10%."),
        ("6", "Simulasi anggaran status Defisit (test_budget_deficit)", "Saat beban melebihi uang saku, sisa saldo bernilai negatif dan layanan menetapkan status finansial 'Defisit'."),
        ("7", "Sinkronisasi template checklist (test_checklist_sync)", "Template master otomatis disalin ke UserChecklist saat akun baru pertama kali mengakses modul checklist."),
        ("8", "Toggle checklist dan persentase progres (test_checklist_progress)", "Menandai item selesai berhasil mengubah status, completed_at terisi, dan progres meningkat menjadi 100%."),
        ("9", "Isolasi data checklist antar pengguna (test_data_isolation)", "User B dicegah memodifikasi item milik User A (layanan mengembalikan None dan data tidak berubah)."),
        ("10", "Pencarian direktori kata kunci (test_search_query)", "Selector place_search dengan query 'Depok' berhasil menyaring fasilitas yang berlokasi di kecamatan tersebut."),
        ("11", "Pemfilteran direktori kategori (test_search_category)", "Selector dengan filter category='warteg_hemat' hanya mengembalikan lokasi berkategori warteg murah."),
        ("12", "Encoding pesan darurat WhatsApp (test_wa_encoding)", "Nomor 0812... dinormalkan menjadi 62812..., pesan diformat rapi, dan tautan wa.me terbuat secara valid."),
    ]
    tbl_44 = doc.add_table(rows=1, cols=3)
    style_table(tbl_44, t44_widths, t44_headers, t44_data)

    add_styled_heading(doc, "4.9 Batasan Implementasi", level=2)
    add_body_paragraph(doc, "Berdasarkan analisis kode sumber aktual, terdapat beberapa batasan teknis pada implementasi sistem saat ini:\n"
                            "1. Mesin Basis Data: Penggunaan SQLite3 sangat ideal untuk tahap pengembangan dan pengujian lokal, namun memiliki keterbatasan konkurensi penulisan tinggi (database-level locking) jika dioperasikan pada beban jutaan pengguna simultan.\n"
                            "2. Ketergantungan Aset CDN: Pustaka Tailwind CSS, HTMX, dan Alpine.js dimuat secara langsung melalui Content Delivery Network eksternal; pada kondisi server/klien luring (offline) total, lembar gaya dan interaktivitas asinkronus tidak dapat dimuat.\n"
                            "3. Batasan Wilayah Direktori: Data fasilitas publik saat ini baru mencakup 88 titik terverifikasi di wilayah Daerah Istimewa Yogyakarta; kota-kota perantauan besar lainnya (seperti Bandung, Surabaya, Malang, dan Jabodetabek) belum diintegrasikan.\n"
                            "4. Tautan Pesan WhatsApp Satu Arah: Fitur generator pesan darurat mengandalkan tautan browser wa.me yang mengeksekusi aplikasi WhatsApp di sisi klien, sehingga sistem backend tidak memiliki mekanisme konfirmasi otomatis apakah pesan tersebut telah terkirim atau terbaca oleh penerima.\n"
                            "5. Penghitungan Anggaran Berbasis Periode Tunggal: Modul kalkulator anggaran memproyeksikan pengeluaran dalam siklus satu bulan berjalan, belum menyediakan pencatatan riwayat arus kas harian secara berkesinambungan (expense tracker harian).")

    doc.add_page_break()

    # -------------------------------------------------------------
    # BAB V PENUTUP
    # -------------------------------------------------------------
    add_styled_heading(doc, "BAB V\nPENUTUP", level=1)

    add_styled_heading(doc, "5.1 Kesimpulan", level=2)
    add_body_paragraph(doc, "Berdasarkan keseluruhan tahapan analisis, perancangan, implementasi kode sumber, dan pengujian sistem pada proyek pengembangan website RantauHub, dapat ditarik beberapa kesimpulan pokok:\n"
                            "1. Platform RantauHub berhasil dibangun menggunakan kerangka kerja Python dan Django 5.x dengan menerapkan arsitektur MVT yang dipadukan dengan pola Thin Views / Fat Services, menghasilkan kode sumber yang rapi, terisolasi, mudah dipelihara, dan memiliki modularitas tinggi.\n"
                            "2. Integrasi antarmuka modern yang memadukan utilitas Tailwind CSS, pertukaran fragmen DOM asinkronus HTMX, dan manajemen komponen deklaratif Alpine.js terbukti mampu menghadirkan pengalaman pengguna yang gesit dan reaktif tanpa kompleksitas arsitektur Single Page Application (SPA).\n"
                            "3. Fitur Survival Checklist berhasil menyediakan panduan persiapan adaptasi perantau secara terstruktur dengan sinkronisasi template otomatis dan isolasi keamanan data antar-akun pengguna.\n"
                            "4. Fitur Kalkulator Anggaran Finansial mampu melakukan analisis proyeksi biaya hidup bulanan dengan presisi Decimal yang tinggi, memberikan indikasi visual status Surplus/Defisit secara akurat, serta mengevaluasi kecukupan rasio dana darurat perantau.\n"
                            "5. Direktori Fasilitas Esensial berhasil memetakan 88 titik lokasi publik terverifikasi di wilayah Daerah Istimewa Yogyakarta ke dalam 12 kelompok kategori esensial dengan dukungan pencarian multi-kriteria berbasis Q objects yang cepat.\n"
                            "6. Pusat Respons Darurat (Emergency Center) memberikan solusi kesiapsiagaan krisis melalui penyediaan nomor darurat nasional resmi, panduan migrasi faskes BPJS via Mobile JKN, protokol dokumen hilang, serta generator pesan WhatsApp otomatis yang telah terenkripsi rapi.\n"
                            "7. Seluruh fungsionalitas inti telah divalidasi melalui 12 automated unit tests dengan tingkat kelulusan 100%, menegaskan bahwa implementasi sistem berjalan stabil dan sesuai dengan spesifikasi kebutuhan yang dirumuskan.")

    add_styled_heading(doc, "5.2 Saran Pengembangan", level=2)
    add_body_paragraph(doc, "Demi penyempurnaan dan pengembangan berkelanjutan platform RantauHub pada masa yang akan datang, diajukan beberapa saran pengembangan teknis:\n"
                            "1. Migrasi ke Basis Data Enterprise: Mengganti mesin SQLite3 dengan PostgreSQL pada lingkungan produksi guna mendukung konkurensi data tingkat tinggi, replikasi data, dan fitur pencarian teks penuh (Full-Text Search) yang lebih canggih.\n"
                            "2. Penerapan Progressive Web App (PWA): Menambahkan berkas Web App Manifest dan Service Workers agar data checklist dan direktori fasilitas yang telah dimuat dapat diakses secara luring (offline) saat perantau mengalami kendala koneksi internet.\n"
                            "3. Bundling Berkas Statis Lokal: Mengompilasi Tailwind CSS menggunakan Tailwind CLI dan menyimpan pustaka HTMX serta Alpine.js secara lokal pada direktori static/ guna mengeliminasi ketergantungan pada jaringan CDN pihak ketiga.\n"
                            "4. Ekspansi Cakupan Direktori Nasional: Memperluas database fasilitas esensial ke kota-kota tujuan pendidikan dan industri besar lainnya di Indonesia, seperti Bandung, Surabaya, Malang, Surakarta, Semarang, dan Jabodetabek.\n"
                            "5. Integrasi API Gateway Komunikasi: Mengintegrasikan layanan SMS gateway atau WhatsApp Business API resmi untuk pengiriman notifikasi darurat langsung dari sisi server ketika pengguna menekan tombol SOS dalam situasi darurat akut.\n"
                            "6. Pengembangan Modul Buku Kas Harian: Mengembangkan kalkulator anggaran bulanan menjadi fitur pelacak pengeluaran harian (daily expense tracker) berbasis grafik visual untuk memantau realisasi anggaran secara real-time.")

    doc.add_page_break()

    # -------------------------------------------------------------
    # DAFTAR PUSTAKA
    # -------------------------------------------------------------
    add_styled_heading(doc, "DAFTAR PUSTAKA", level=1)

    references = [
        "[1] Django Software Foundation. \"Django Documentation (Version 5.0).\" https://docs.djangoproject.com/en/5.0/ (diakses November 2026).",
        "[2] Python Software Foundation. \"Python 3.12 Documentation.\" https://docs.python.org/3.12/ (diakses November 2026).",
        "[3] Tailwind Labs Inc. \"Tailwind CSS Documentation.\" https://tailwindcss.com/docs (diakses November 2026).",
        "[4] Big Sky Software. \"HTMX — High Power Tools for HTML.\" https://htmx.org/docs/ (diakses November 2026).",
        "[5] Alpine.js Development Team. \"Alpine.js Documentation.\" https://alpinejs.dev/ (diakses November 2026).",
        "[6] SQLite Consortium. \"SQLite Documentation and Query Language Reference.\" https://www.sqlite.org/docs.html (diakses November 2026).",
        "[7] BPJS Kesehatan Republik Indonesia. \"Panduan Layanan Peserta Jaminan Kesehatan Nasional (JKN) dan Aplikasi Mobile JKN.\" Jakarta: BPJS Kesehatan, 2024.",
        "[8] Kementerian Kesehatan Republik Indonesia. \"Sistem Penanggulangan Gawat Darurat Terpadu (SPGDT) Call Center 119.\" Jakarta: Kemenkes RI, 2023.",
        "[9] Kode Sumber Proyek RantauHub: config/settings/base.py, apps/users/, apps/survival_kit/, apps/directory/, apps/emergency/, dan apps/common/. Repositori Lokal Workspace, 2026.",
        "[10] Dokumentasi Rangkaian Pengujian Otomatis RantauHub: tests/test_auth.py, tests/test_survival_kit.py, tests/test_directory.py, dan tests/test_emergency.py, 2026.",
    ]

    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.space_before = Pt(0)
        p_ref.paragraph_format.space_after = Pt(6)
        p_ref.paragraph_format.line_spacing = 1.15
        p_ref.paragraph_format.left_indent = Inches(0.4)
        p_ref.paragraph_format.first_line_indent = Inches(-0.4)
        r = p_ref.add_run(ref)
        r.font.name = "Times New Roman"
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(30, 41, 59)

    doc.add_page_break()

    # -------------------------------------------------------------
    # LAMPIRAN: PANDUAN SINGKAT PENGGUNAAN
    # -------------------------------------------------------------
    add_styled_heading(doc, "LAMPIRAN: PANDUAN SINGKAT PENGGUNAAN", level=1)

    steps = [
        ("Langkah 1: Mengakses Website RantauHub",
         "Buka peramban web modern (Google Chrome, Mozilla Firefox, Microsoft Edge, atau Safari) pada komputer atau ponsel pintar Anda. Masukkan alamat URL lokal http://127.0.0.1:8000/ pada bilah alamat untuk membuka halaman beranda utama RantauHub."),

        ("Langkah 2: Melakukan Pendaftaran Akun dan Login",
         "Tekan tombol 'Daftar' pada bilah navigasi kanan atas. Isi formulir pendaftaran dengan nama pengguna, email aktif, kata sandi, kota asal (misalnya: Bengkulu), kota tujuan (misalnya: Yogyakarta), kecamatan domisili kost (misalnya: Depok), dan nama kampus atau kantor (misalnya: UGM). Setelah berhasil, masuk ke sistem menggunakan menu 'Masuk'."),

        ("Langkah 3: Membuka Dashboard dan Memperbarui Kontak Darurat",
         "Setelah berhasil masuk, Anda akan diarahkan ke halaman Dashboard personal. Klik menu 'Profil' untuk melengkapi informasi nama kontak darurat keluarga (misalnya: Ayah/Ibu) beserta nomor telepon aktif mereka. Data ini akan otomatis disinkronkan ke seluruh modul bantuan darurat."),

        ("Langkah 4: Memeriksa dan Menandai Checklist Adaptasi (Survival Kit)",
         "Buka menu 'Survival Kit' lalu pilih 'Checklist Adaptasi'. Sistem akan memuat daftar barang bawaan dan tugas esensial (dokumen asli, perlengkapan kamar kost, kebutuhan akademik, dan obat-obatan). Ketuk kotak centang pada setiap tugas yang telah Anda selesaikan; persentase kesiapan hidup mandiri Anda akan bertambah secara otomatis secara real-time."),

        ("Langkah 5: Menambahkan Tugas Kustom Mandiri",
         "Jika terdapat perlengkapan khusus yang ingin Anda catat secara pribadi, gulir ke bagian bawah formulir checklist, ketikkan judul barang/tugas pada kolom 'Tambah Tugas Kustom', lalu tekan tombol 'Tambah'. Tugas baru akan langsung disematkan ke daftar periksa Anda."),

        ("Langkah 6: Melakukan Simulasi Anggaran Bulanan",
         "Pilih submenu 'Kalkulator Anggaran'. Masukkan nominal uang saku bulanan, biaya sewa kost, estimasi makan harian, transportasi, internet, dan tabungan darurat yang diinginkan. Tekan tombol 'Hitung Anggaran'. Perhatikan kartu hasil analisis di sisi kanan: pastikan status keuangan Anda menunjukkan 'SURPLUS' dan rasio tabungan darurat mencapai minimal 10% agar keuangan Anda tetap sehat."),

        ("Langkah 7: Menjelajahi Direktori Fasilitas Esensial Yogyakarta",
         "Buka menu 'Direktori Fasilitas'. Ketikkan nama tempat atau kecamatan (misalnya: 'Depok', 'Sleman', atau 'Sardjito') pada kolom pencarian cepat, atau klik salah satu pil kategori fasilitas (Puskesmas, Klinik 24 Jam, Rumah Sakit, Warteg Hemat, Laundry, dll.). Anda dapat menekan tautan 'Buka di Google Maps' untuk mendapatkan petunjuk arah navigasi atau menekan ikon bintang untuk menyimpan tempat tersebut ke daftar favorit Anda."),

        ("Langkah 8: Memanfaatkan Pusat Respons Darurat (Emergency Center)",
         "Dalam situasi krisis, buka menu 'Pusat Darurat':\n"
         "• Untuk panggilan darurat resmi: Ketuk langsung tombol panggil pada nomor 110 (Polisi), 119 (Ambulans), atau 113 (Damkar).\n"
         "• Untuk mengabari keluarga: Buka submenu 'WhatsApp Darurat', pilih jenis situasi (misalnya 'Darurat Medis / Sakit Parah'), konfirmasi lokasi keberadaan Anda saat ini, lalu tekan tombol 'Kirim Pesan via WhatsApp'. Aplikasi WhatsApp akan terbuka otomatis dengan draf pesan darurat yang rapi dan siap dikirimkan kepada kontak darurat Anda."),
    ]

    for title, desc in steps:
        add_styled_heading(doc, title, level=3)
        add_body_paragraph(doc, desc, space_after=8, line_spacing=1.2)

    # Final Save
    doc.save(DOC_PATH)
    print(f"Document saved successfully at: {DOC_PATH}")
    file_size = os.path.getsize(DOC_PATH)
    print(f"File size: {file_size:,} bytes ({file_size/1024:.2f} KB)")

if __name__ == "__main__":
    build_document()

