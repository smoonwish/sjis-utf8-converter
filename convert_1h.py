import urllib.request

# 気象庁の公開ページ
# https://www.data.jma.go.jp/stats/data/mdrr/docs/csv_dl_format_prenh.html
# 1時間降水量CSV
data_url = "https://www.data.jma.go.jp/stats/data/mdrr/pre_rct/alltable/pre1h00_rct.csv"

try:
    # 1. 気象庁からデータを取得
    req = urllib.request.Request(data_url)
    with urllib.request.urlopen(req) as response:
        # Shift_JIS(CP932)でデコード
        content = response.read().decode('cp932', errors='ignore')
    
    # 2. UTF-8に変換して保存
    with open("jma_latest_utf8.csv", "w", encoding="utf-8-sig") as f:
        f.write(content)
        
    print("変換成功: jma_latest_utf8.csv を作成しました。")

except Exception as e:
    print(f"エラーが発生しました: {e}")
