# gui.py
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from anonymizer import anonymize_file
import threading


def launch_gui():
    def browse_file():
        file_path.set(filedialog.askopenfilename())

    def start_anonymization():
        if not file_path.get():
            messagebox.showwarning("Warning", "Please select a file first.")
            return

        progress_bar.start()
        threading.Thread(target=run_anonymization).start()

    def run_anonymization():
        try:
            anonymize_file(file_path.get())
            messagebox.showinfo("Success", "Anonymization complete.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            progress_bar.stop()

    root = tk.Tk()
    root.title("Data Anonymizer GUI")
    root.geometry("400x200")

    file_path = tk.StringVar()

    tk.Label(root, text="Select a file to anonymize:").pack(pady=10)
    tk.Entry(root, textvariable=file_path, width=40).pack(pady=5)
    tk.Button(root, text="Browse", command=browse_file).pack(pady=5)
    tk.Button(root, text="Anonymize", command=start_anonymization).pack(pady=10)

    progress_bar = ttk.Progressbar(root, mode='indeterminate')
    progress_bar.pack(pady=5, fill='x', padx=20)

    root.mainloop()
