import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from . import file_selector
from . import text2md_processor
from . import md2chunk_processor

class MarkdownChunkApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Markdownチャンク作成システム")
        self.geometry("800x600")
        
        self.file_path = None
        self.original_text = ""
        self.processed_text = ""
        self.chunks = []
        
        # GUIウィジェットの生成
        self.create_widgets()

    def create_widgets(self):
        # ファイル選択ボタン
        self.select_button = tk.Button(self, text="ファイル選択", command=self.load_file)
        self.select_button.pack(pady=10)
        
        # プレビュー表示用テキストボックス（スクロール対応）
        self.preview = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=100, height=25)
        self.preview.pack(padx=10, pady=10)
        
        # チャンク化実行ボタン
        self.chunk_button = tk.Button(self, text="チャンク化実行", command=self.process_text)
        self.chunk_button.pack(pady=5)
        
        # 出力ボタン
        self.save_button = tk.Button(self, text="ファイルに保存", command=self.save_output)
        self.save_button.pack(pady=5)
    
    def load_file(self):
        """
        ファイル選択ダイアログを利用してファイルを読み込み、テキストをプレビューに表示
        """
        self.file_path = file_selector.select_file()
        if self.file_path:
            try:
                self.original_text = text2md_processor.read_file(self.file_path)
                self.preview.delete("1.0", tk.END)
                self.preview.insert(tk.END, self.original_text)
                messagebox.showinfo("成功", "ファイル読み込み完了")
            except Exception as e:
                messagebox.showerror("エラー", f"ファイル読み込みに失敗しました：{e}")
    
    def process_text(self):
        """
        読み込んだテキストの判別、変換およびチャンク化処理を実行
        """
        if not self.original_text:
            messagebox.showwarning("警告", "まずファイルを読み込んでください")
            return
        
        # テキストがマークダウン形式かどうかを判定し、テキストであればマークダウン化処理を施す
        if not text2md_processor.is_markdown(self.original_text):
            self.processed_text = text2md_processor.convert_to_markdown(self.original_text)
        else:
            self.processed_text = self.original_text
        
        chunks = md2chunk_processor.chunk_by_header(self.processed_text)
        
        # 固定サイズチャンク化のオプション（必要に応じ有効化可能）
        # chunks = md2chunk_processor.fixed_size_chunk(self.processed_text, chunk_size=500, overlap=50)
        
        self.chunks = chunks
        display_text = "\n\n" + ("―" * 40 + "\n\n").join(chunks)
        self.preview.delete("1.0", tk.END)
        self.preview.insert(tk.END, display_text)
        messagebox.showinfo("完了", f"チャンク化完了（チャンク数: {len(chunks)}）")
    
    def save_output(self):
        if not self.chunks:
            messagebox.showwarning("警告", "まずチャンク化を実行してください")
            return
        
        # 出力先ファイルの選択ダイアログを表示
        save_path = filedialog.asksaveasfilename(
            title="保存先を選択してください",
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if save_path:
            try:
                with open(save_path, "w", encoding="utf-8") as f:
                    for chunk in self.chunks:
                        f.write(chunk + "\n\n" + ("―" * 40) + "\n\n")
                messagebox.showinfo("成功", "ファイル保存完了")
            except Exception as e:
                messagebox.showerror("エラー", f"ファイル保存に失敗しました：{e}")

def run_app():
    app = MarkdownChunkApp()
    app.mainloop()
