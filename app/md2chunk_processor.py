import re

def chunk_by_header(text):
    pattern = re.compile(r"(^#{1,3}\s.*$)", re.MULTILINE)
    splits = pattern.split(text)
    
    chunks = []
    current_chunk = ""
    for part in splits:
        if re.match(r"^#{1,3}\s", part):
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = part + "\n"
        else:
            current_chunk += part + "\n"
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

# チャンクサイズとオーバーラップを指定して、固定サイズのチャンクに分割する
def fixed_size_chunk(text, chunk_size=250, overlap=30):
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0:
            start = 0
    return chunks
