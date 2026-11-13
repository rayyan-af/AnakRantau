# IMPLEMENTATION_PLAN.md

## Executive Summary
- **Product Name:** RantauHub
- **Tagline:** "Teman Pertama untuk Memulai Hidup di Perantauan."
- **Target Audience:** Mahasiswa baru luar kota, pelajar rantau, dan pekerja/first-jobbers yang baru pindah ke kota besar.
- **Core Value Proposition:** Platform digital terpadu untuk pendampingan pra-keberangkatan, penataan logistik kost, kalkulasi realistis biaya hidup, navigasi direktori terverifikasi, generator pesan darurat, dan forum tanya-jawab komunitas perantau.
- **Tech Stack:**
  - **Backend:** Python 3.12+, Django 5.x (Django ORM, Forms, Built-in Auth, Admin, Management Commands).
  - **Frontend:** Django Templates + Tailwind CSS + HTMX 1.9+ (asynchronous reactivity) + Alpine.js 3+ (micro-interactions).
  - **Database:** SQLite (local development) / 100% PostgreSQL schema compatible.
  - **Configuration:** `python-decouple` with `.env`.
  - **Design System:** Mobile-first, Indigo/Ocean Blue palette (`#2563eb` / `#1d4ed8`), neutral slate background (`#f8fafc`), modern Inter typography, soft shadows, rounded-3xl / rounded-2xl cards.

---

## Architecture & Modularity Rules
1. **The 150-Line Threshold (Strict Modularization):**
   - No Python file or template exceeds 150–200 lines of code.
   - All modules split into clean sub-packages: `models/`, `views/`, `forms/`, `services/`, `selectors/`.
2. **Layering Pattern (Thin Views, Fat Services/Selectors):**
   - Views act strictly as thin HTTP controllers.
   - Budget calculations and checklist syncing reside in `apps/survival_kit/services/`.
   - Complex directory filtering queries reside in `apps/directory/selectors/`.
   - WhatsApp message formatting and URL encoding in `apps/emergency/services/`.
3. **Custom User Model First:**
   - `apps.users.models.User` inheriting `AbstractUser` configured at `AUTH_USER_MODEL = 'users.User'` prior to initial migration.
4. **Data Integrity & Honesty Policy:**
   - Unverified initial demo data explicitly marked with UI badge `[Data Demo — Belum Diverifikasi]`.
5. **Data Isolation & Object Ownership Security:**
   - All user-sensitive data queries and mutations strictly isolated using `user=request.user` to prevent IDOR.
6. **No Premature Overhead:**
   - Clean, stable core stack without unnecessary external dependencies.

---

## Structured Task Tracking Table

| Task ID | Task Description | Priority | Status | Dependencies | Files Involved |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `FND-01` | Create IMPLEMENTATION_PLAN.md & living tracker | High | **Selesai** | - | `IMPLEMENTATION_PLAN.md` |
| `FND-02` | Initialize project skeleton, requirements, .env, base/dev settings | High | **Selesai** | FND-01 | `requirements.txt`, `.env.example`, `.env`, `manage.py`, `config/settings/**` |
| `AUTH-01` | Build custom User model, auth forms & views, and templates | High | **Selesai** | FND-02 | `apps/users/**`, `templates/users/**` |
| `SURV-01` | Survival Kit models, services, HTMX views, templates & seed command | High | **Selesai** | AUTH-01 | `apps/survival_kit/**`, `templates/survival_kit/**` |
| `DIR-01` | Essential directory models, selectors, HTMX views, templates & seed command | Medium | **Selesai** | SURV-01 | `apps/directory/**`, `templates/directory/**` |
| `EMER-01` | Emergency card, WhatsApp generator, BPJS & lost document guides | Medium | **Selesai** | DIR-01 | `apps/emergency/**`, `templates/emergency/**` |
| `COMM-01` | Community Q&A models, thread/reply/report views, templates & seed command | Medium | **Selesai** | EMER-01 | `apps/community/**`, `templates/community/**` |
| `QA-01` | Automated test suite, security audit, error pages (403, 404, 500) & README | High | **Selesai** | COMM-01 | `tests/**`, `templates/pages/**`, `README.md` |

---

## Phase Checklist & Definition of Done (DoD)

- [x] **Phase 1: Enterprise Foundation & Core Authentication**
  - Project directory structure initialized adhering to strict modular layout.
  - Settings split into `base.py`, `development.py`, and `production.py`.
  - Abstract `TimeStampedModel` created in `apps/common/models.py`.
  - Custom `User` model created and registered in `AUTH_USER_MODEL`.
  - Modular forms: `RegistrationForm`, `LoginForm`, `ProfileUpdateForm`.
  - Modular views: `views/auth.py`, `views/profile.py`.
  - Base layout (`base.html`), components (`navbar.html`, `footer.html`, `alert.html`), landing page (`home.html`), and dashboard (`dashboard.html`).
  - Initial migrations executed successfully.

- [x] **Phase 2: Survival Kit MVP (Checklist, Calculator, & Guides)**
  - Models: `ChecklistTemplate`, `UserChecklist`, `BudgetPlan`, `GuideArticle`.
  - Services: `checklist_service.py` (idempotent cloning & completion stats) and `budget_calculator.py` (pure calculation service).
  - HTMX dynamic checklist checkbox toggle with out-of-band progress bar updating.
  - Interactive budget calculator with live preview and save simulation feature.
  - Seed command `seed_survival_kit` providing 18 checklist templates and 3 practical guides.

- [x] **Phase 3: Essential Directory (Services & Filtering)**
  - Models: `EssentialPlace` and `FavoritePlace`.
  - Selector: `place_search.py` for multi-criteria querying (query, category, city, district).
  - HTMX live search input and category pills.
  - Verification badge display (`[Terverifikasi]` vs `[Data Demo — Belum Diverifikasi]`).
  - Place detail page with external Google Maps navigation links.
  - Bookmark favorite place toggle via HTMX.
  - Seed command `seed_directory` with initial places across Yogyakarta, Jakarta, and Bandung.

- [x] **Phase 4: Emergency & Information Center**
  - Mobile-first digital SOS Card displaying personal credentials, family contacts, and national emergency hotlines (110, 119, 113, 123, 165).
  - WhatsApp emergency message generator with URL encoding service (`wa_encoder.py`) and live preview.
  - Interactive BPJS Faskes 1 migration guide via Mobile JKN with official disclaimers.
  - Practical emergency protocol for lost KTP, ATM, or STNK.

- [x] **Phase 5: Moderated Community Q&A**
  - Models: `Thread`, `Reply`, and `Report`.
  - Filterable discussion forum with tags and categories.
  - Strict ownership permissions: only authors or staff can delete content or accept best answers.
  - Content reporting form feeding into Django Admin moderation queue.
  - Seed command `seed_community` providing sample active discussions and replies.

- [x] **Phase 6: Quality Assurance, Security Audit, & Documentation**
  - Friendly error templates: `403.html`, `404.html`, `500.html`.
  - Comprehensive automated test suite in `tests/` covering Auth, Data Isolation, Budget Calculator, Checklist Sync, Place Selector, Emergency Encoder, and Community Permissions (15/15 tests passing).
  - Production-ready `README.md` with step-by-step local setup instructions for Windows PowerShell and macOS/Linux Bash.
  - Task board updated to 100% Selesai.
