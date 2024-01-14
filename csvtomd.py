import pandas as pd


def csv_to_markdown_table(csv_file_path, md_file_path):
    # 讀取 CSV 檔案
    df = pd.read_csv(csv_file_path)

    # 將 DataFrame 轉換為 Markdown 表格
    markdown_str = "| " + " | ".join(df.columns) + " |\n"
    markdown_str += "|-" + "-|-".join(["-" * len(col) for col in df.columns]) + "-|\n"

    for _, row in df.iterrows():
        row_str = "| " + " | ".join(row.astype(str)) + " |\n"
        markdown_str += row_str

    # 寫入 Markdown 檔案
    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(markdown_str)


# 指定你的 CSV 檔案路徑和輸出的 Markdown 檔案路徑
csv_file_path = "data\dataset.csv"
md_file_path = "dataset.md"

# 轉換並寫入 Markdown 檔案
csv_to_markdown_table(csv_file_path, md_file_path)
