งาน Backend TOC<br>
สำหรับฝ่าย Backend<br>
หากยังไม่เคย clone ลงไปเลย วิธี clone มีดังนี้<br>
สร้าง Folder ลงเครื่องตัวเองโดยใชั  git clone https://github.com/stsnx/temple_of_TOC.git<br>
โปรเจกต์นี้ใช้ module เพิ่มดังนี้<br>
    django-cors-headers<br>
วิธีติดตั้งคือ เข้าไปที่โปรเจกต์ เปิด terminal แล้วใช้<br>
pip install django-cors-headers<br>
แล้วไปแก้ที่ setting ดังนี้<br>
CORS_ALLOWED_ORIGINS = [<br>
    'http://localhost:3000',<br>
]<br>
INSTALLED_APPS = [<br>
    'django.contrib.admin',<br>
    'django.contrib.auth',<br>
    'django.contrib.contenttypes',<br>
    'django.contrib.sessions',<br>
    'django.contrib.messages',<br>
    'django.contrib.staticfiles',<br>
    'rest_framework',<br>
    'rest_framework.authtoken',<br>
    'temple_api',<br>
    ***'corsheaders',<br>
]<br>

MIDDLEWARE = [<br>
    'django.middleware.security.SecurityMiddleware',<br>
    'django.contrib.sessions.middleware.SessionMiddleware',<br>
    'django.middleware.common.CommonMiddleware',<br>
    'django.middleware.csrf.CsrfViewMiddleware',<br>
    'django.contrib.auth.middleware.AuthenticationMiddleware',<br>
    'django.contrib.messages.middleware.MessageMiddleware',<br>
    'django.middleware.clickjacking.XFrameOptionsMiddleware',<br>
    ***'corsheaders.middleware.CorsMiddleware',<br>
    ***'django.middleware.common.CommonMiddleware',<br>
]<br>
2.1. ช้าก่อน!!! หากเคย clone ไปแล้ว อย่าลืม pull ก่อนจะแบกอะไรด้วย โดยใช้<br>
 git pull origin main<br>
เมื่อเรียบร้อยแล้วฝากแบกด้วย<br>
เมื่อแบกเสร็จแล้วอยากจะ push ขึ้นมาที่นี่ ให้ทำดังนี้ git remote add originhttps://github.com/stsnx/temple_of_TOC.git  (เพื่ม remote repository)<br>
git pull origin (pull remote repository)<br>
git add .<br>
git commit -m "comment" ใน "comment" ไว้ใส่คำอธิบายว่าทำอะไรมา<br>
git checkout -b abcd โดย abcd คือชื่อ branch ใหม่ถ้ายังไม่มี หรือ git checkout abcd กรณีมี branch แล้ว<br>
*** สามารถตรวจสอบ branch ได้ด้วย git branch -v***<br>
git push -u origin abcd (push to remote repository)<br>
ห้าม push ขี้น Main โดยเด็ดขาด ใคร push ขี้น Main กูตีมือหัก<br>
เมื่อ push ขี้นมาแล้ว ให้เข้าไปที่ github brouser แล้ว ไปที่ Compare & Pull request<br>
ไปเรียกเจ้าของ repo นี้มาดูแล้วให้มัน merge<br>
สุดท้ายนี้<br>
แ บ ก ด้ ว ย ค รั บ<br>
<br>
สำหรับฝ่าย Frontend<br>
API ที่มีของ backend มีอันเดียวคือ<br>
POST /api/gettemple<br>
body{<br>
    "responseType": "blob",<br>
    "body": [],<br>
}<br>
โดยใน body จะเป็นจังหวัดที่ต้องการเรียกโดย<br>
ROY แทนจังหวัดร้อยเอ็ด<br>
RAN แทนจังหวัดระนอง<br>
RAY แทนจังหวัดระยอง<br>
YAL แทนจังหวัดยะลา<br>
ex<br>
body{<br>
    "responseType": "blob",<br>
    "body": ["RAY","YAL"]<br>
}<br>
