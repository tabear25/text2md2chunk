import re

def read_file(file_path):
    # file_selector.pyで選択したファイルパスからテキストを読み込む
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# マークダウン形式になっているかの簡易判定
def is_markdown(text):
    return bool(re.search(r"^#{1,3}\s", text, flags=re.MULTILINE))

def convert_to_markdown(text):
    """
    テキストをマークダウン形式に変換する
    ・初行を見出しとみなして '# ' を付与する（必要に応じてルールの拡充が可能）
    ・リストやリンク等の変換は、ここでは簡易的に実装
    """
    lines = text.splitlines()
    if lines:
        # 最初の行を見出しとして変換
        lines[0] = "# " + lines[0].strip()
    
    converted_lines = []
    for line in lines:
        # 例：行頭にハイフンがあればリスト項目としてそのまま採用
        if re.match(r"^\s*-\s+", line):
            converted_lines.append(line)
        else:
            converted_lines.append(line)
    return "\n".join(converted_lines)
