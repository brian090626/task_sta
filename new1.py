#buat file datasta.csv nomor 1

import pandas as pd

# Baca file CSV
file_path = "datasta.csv"  # Ganti dengan path file CSV Anda
df = pd.read_csv(file_path)

# Konversi DataFrame ke tabel HTML
table_html = df.to_html(classes="table table-striped", index=False)

# Gabungkan dengan file HTML
html_content = f"""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualisasi Data Suara</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; text-align: center; }}
        h1 {{ color: #007bff; }}
        .container {{ max-width: 800px; margin: auto; text-align: left; }}
        img {{ width: 100%; max-width: 700px; border-radius: 5px; margin-bottom: 20px; }}
        table {{
            margin: auto;
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #f4f4f4;
        }}
        .scrollable-table {{
            overflow-x: auto;
            white-space: nowrap;
        }}
    </style>
</head>
<body>

    <h1>Analisis dan Visualisasi Data Suara</h1>
    
    <div class="container">
        <h2>1. Time Series Line Plot</h2>
        <p>Visualisasi ini menunjukkan bagaimana amplitudo berubah terhadap waktu untuk tiga sinyal suara.</p>
        <img src="line_plot.png" alt="Time Series Line Plot">
        
        <h2>2. Histogram (Distribusi Amplitudo)</h2>
        <p>Menampilkan distribusi nilai amplitudo dalam dataset suara.</p>
        <img src="histogram.png" alt="Histogram">

        <h2>3. Box Plot (Sebaran Fitur)</h2>
        <p>Menunjukkan distribusi nilai amplitudo dengan median, quartiles, dan outliers.</p>
        <img src="boxplot.png" alt="Box Plot">

        <h2>4. Spectrogram (Analisis Frekuensi)</h2>
        <p>Memvisualisasikan bagaimana energi tersebar dalam frekuensi suara seiring waktu.</p>
        <img src="spectrogram.png" alt="Spectrogram">

        <h2>5. Scatter Plot (Korelasi Fitur)</h2>
        <p>Menunjukkan hubungan antara dua sinyal suara dalam dataset.</p>
        <img src="scatter_plot.png" alt="Scatter Plot">
        
        <h2>6. Dataset CSV</h2>
        <p>Berikut adalah data dari file CSV:</p>
        <div class="scrollable-table">
            {table_html}
        </div>
    </div>

</body>
</html>
"""

# Simpan file HTML
output_file_path = "index_with_scrollable_csv.html"  # Ganti nama sesuai kebutuhan
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"File HTML berhasil dibuat: {output_file_path}")
