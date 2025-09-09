# El Football - Toko Perlengkapan Sepak Bola
## Tugas Individu PBP - Kelas C - 2406431510 - Muhammad Azka Awliya 

Aplikasi dapat diakses melalui tautan berikut: https://muhammad-azka41-elfootball.pbp.cs.ui.ac.id/ \
Nama Aplikasi: El Football

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

,,,
Formasi Empat Tiga Dua Satu Komando
,,,

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

## 3. Jelaskan peran settings.py dalam proyek Django!

**settings.py** adalah pusat konfigurasi proyek dan mendefinisikan cara kerja proyek (database, apps, keamanan, lokasi, template, dan lain sebagainya). Perannya meliputi:

**INSTALLED_APPS**: daftar aplikasi (app) yang aktif dalam proyek — Django akan memuatnya (migrations, admin, template lookup).

**DATABASES**: konfigurasi koneksi database.

**TEMPLATES**: pengaturan engine template, direktori DIRS, context processors.

**MIDDLEWARE**: middleware stack yang memproses request/response (security, session, csrf, dll).

**STATIC & MEDIA**: lokasi file statis HTML dan file upload media.

**DEBUG & ALLOWED_HOSTS**: mode pengembangan/production dan host yang diperbolehkan untuk melayani request.

**SECRET_KEY**: kunci kriptografi untuk session dan security — harus dirahasiakan (jangan commit ke repo publik).

**LOGGING / EMAIL / AUTHENTICATION BACKENDS**: berbagai konfigurasi lain untuk logging, email, otentikasi, dsb.

## 4. Bagaimana cara kerja migrasi database di Django?

a. ***Definisikan model di models.py**. Model adalah kelas Python yang mewakili tabel DB.

b. **Buat migration**: python manage.py makemigrations
    - Django mendeteksi perubahan pada model dan membuat file migration (mis. 0001_initial.py) yang berisi operasi (CreateModel, AddField, AlterField, dsb).
    - Migration adalah file Python yang mendeskripsikan transformasi skema.

c. **Terapkan migration**: python manage.py migrate
    - Django menjalankan operasi migration terhadap database target, membuat/ubah tabel sesuai instruksi migration.
    - Riwayat migration disimpan di tabel django_migrations sehingga Django tahu migrasi mana yang sudah diterapkan.

d. **Mengubah model later**: buat perubahan pada models.py, jalankan makemigrations lagi (membuat migration baru seperti 0002_auto...), lalu migrate untuk menerapkannya.

e. **Operasi lanjutan**: ada operasi lanjutan seperti RunPython untuk melakukan data migration, squashmigrations untuk menggabungkan banyak migration menjadi satu, dan rollback memakai migrate app_name migration_name.

## 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

a. **“Batteries-included”**: banyak fitur built-in (ORM, admin site, autentikasi, forms, i18n, dsb) sehingga fokus belajar pada konsep web tanpa harus memilih banyak library eksternal.

b. **ORM**: memudahkan interaksi DB tanpa SQL mentah pada tahap awal.

c. **Admin otomatis**: CRUD untuk model bisa langsung tersedia lewat admin, berguna untuk prototyping dan belajar.

d. **Arsitektur jelas (MTV)**: memaksa pemisahan concerns — Model (data), Template (UI), View (logika) — konsep yang mudah dipahami dan berlaku di framework lain juga.

e. **Dokumentasi & komunitas besar**: banyak tutorial, plugin, dan sumber belajar.

f. **Keamanan**: banyak fitur keamanan standar tersedia (CSRF protection, XSS protection, password hashing).

g. **Skalabilitas & produksi-ready**: proyek kecil cepat dibuat, dan framework ini mampu digunakan di proyek besar juga.

h. **Konsistensi**: Django punya konvensi dan struktur proyek yang konsisten sehingga memudahkan pemula mengikuti best practices.

## 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

Selama tutorial 1, asisten dosen turut membantu saya dalam menghadapi suatu permasalahan terutama pada migrasi data. Dari situ saya belajar bahwa setiap penambahan data, diperlukan migrasi basis data setiap perubahan berkala. Asisten dosen membantu saya dengan bahasa yang mudah dipahami, step-by-step, dan well structured. Namun saya memiliki saran untuk menambahkan section khusus untuk mengatasi beberapa error yang biasanya terjadi pada mahasiswa. Sejauh ini, kinerja asisten dosen sudah cukup baik. Terima kasih tim asisten dosen dan tim dosen.