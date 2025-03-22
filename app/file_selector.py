import tkinter as tk
from tkinter import filedialog

def select_file():
    """
    ファイル選択ダイアログを表示し、選択されたファイルのパスを返す
    """
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="ファイルを選択してください",
        filetypes=[("Text Files", "*.txt;*.md"), ("All Files", "*.*")]
    )
    return file_path