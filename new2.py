#buat data Descriptive_Statistics (1).csv

import pandas as pd

# Baca file CSV
file_path = "Descriptive_Statistics (1).csv"  # Ganti dengan path file Anda
df_stats = pd.read_csv(file_path)

# Konversi DataFrame ke tabel HTML dengan scrollable feature
table_html = df_stats.to_html(classes="table table-striped", index=False)

# Buat konten HTML
html_content = f"""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visualisasi Statistik Deskriptif</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            text-align: center;
        }}
        h1 {{
            color: #007bff;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
            text-align: left;
        }}
        .scrollable-table {{
            overflow-x: auto;
            white-space: nowrap;
            margin: 20px auto;
            max-width: 100%;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }}
        table {{
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
    </style>
</head>
<body>

    <h1>Statistik Deskriptif</h1>
    <div class="container">
        <h2>Dataset Overview</h2>
        <div class="scrollable-table">
            {table_html}
        </div>
    </div>

</body>
</html>
"""

# Simpan konten HTML ke file
output_file_path = "descriptive_statistics_scrollable.html"
with open(output_file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"File HTML berhasil dibuat: {output_file_path}")

