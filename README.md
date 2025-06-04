# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR  meminta bantuan dalam mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

Permasalahan bisnis yang dihadapi adalah perusahaan Jaya-Jaya Maju memiliki attrition rate yang tergolong tinggi sekitar lebih dari 10%. Hal ini menunjukkan bahwasanya banyak dari karyawan yang lebih memilih untuk berhenti bekerja atau resign dari perusahaan tersebut. Yang dapat mengakibatkan penurunan produktivitas serta kualitas kerja dari perusahaan tersebut.

### Cakupan Proyek

- melakukan data preprocessing.
- membuat model machine learning untuk melakukan prediksi attrition.
- menganalisis faktor yang menyebabkan attrition.
- membuat business dashboard untuk membantu HR memonitor faktor tersebut.

### Persiapan

Sumber data: [Dataset Jaya-Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

- Setup environment:

```
python -m venv .venv
.\.venv\Scripts\activate
```

- Install Requirements:
```
pip install -r requirements.txt
```

- Jalankan Stremalit
```
streamlit run prediction.py
```


## Business Dashboard

Business dashboard pada proyek ini dibuat dengan menggunakan Public Tableau. Pada dashboard ini ditampilkan total karyawan, jumlah karyawan yang resign, karyawan aktif, attrition rate, rata-rata usia karyawan serta rata-rata pendapatan dari karyawan itu. Grafik pie chart juga digunakan untuk melihat distribusi karyawan yang resign dengan beberapa fitur seperti jenis kelamin, perjalanan bisnis, status pernikahan, dan lembur. 

Selain itu grafik batang digunakan dalam melihat distribusi dari pegawai yang resign dengan beberapa fitur seperti Job Role, Education Field, Education, Monthly income, serta job involvement. dan juga menggunakan line chart untuk melihat distribusi dari pegawai yang resign dengan fitur seperti years at company dan years since last promotion.

Link Dashboard: [HR Dashboard](https://public.tableau.com/views/HR-Analytics_17477137452960/AttritionDashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Link Streamlit: [HR Prediction](https://hr-attrition-dashboard.streamlit.app/)


## Conclusion

Perusahaan Jaya Jaya Maju memiliki attrition rate mencapai 16.92%. hal ini menunjukkan banyak karyawan yang memilih untuk resign dari perusahaan tersebut.  Ada beberapa faktor yang ditemukan berdasarkan berdasarkan hasil analisis data yang diberikan.
- kebanyakan karyawan yang keluar adalah karyawan dengan jenis kelamin pria dan karyawan yang masih single.
- kebanyakan karyawan yang keluar berasal dari departemen RnD, serta job role sebagai sales executive.
- banyak karyawan yang keluar dikarenakan gaji di bawah rata-rata dari total keseluruhan karyawan, yaitu dibawah $5000. serta tingkat kenaikan gaji karyawan yang rendah membuat karyawan cenderung untuk resign.
- karyawan banyak yang keluar pada rentang usia 25-35 tahun.
- kebanyakan karyawan yang melakukan lembur memiliki kecenderungan untuk keluar dibandingkan dengan yang tidak.


### Rekomendasi Action Items (Optional)

Guna menyelesaikan permasalahan perusahaan tersebut, ada beberapa rekomendari action items yang dapat diterapkan:
1. Meningkatkan gaji serta persentase kenaikan gaji. Dengan gaji yang sesuai karyawan akan lebih merasa di hargai dan dapat membuatnya bertahan di perusahaan tersebut.
2. Melakukan evaluasi terhadap departemen, jobrole, dan yang lain yang memiliki attrition tinggi. dengan melakukan hal tersebut, perusahaan dapat meningkatkan tingkat kepuasan pegawai dalam departemen serta role yang dipegangnya.
3. Mengevaluasi beban kerja pegawai. Dengan melakukan hal tersebut dapat mengurangi beban kerja pegawai yang terlalu banyak, sehingga mereka tidak perlu sering dalam melakukan lembur.
4. Dapat melakukan kebijakan sistem pegawai kontrak dengan jangka waktu tertentu, dikarenakan kebanyakan pegawai yang resign berada di rentang usia 25-35 tahun, serta memberikan pelatihan pegawai mendapatkan ruang untuk terus berkembang di perusahaan tersebut.
