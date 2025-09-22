import tkinter as tk
from tkinter import scrolledtext, Entry
import shlex


class Ext4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ext4 Shell")
        self.root.geometry("600x400")

        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled')
        self.output_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=5, pady=5)

        tk.Label(input_frame, text="(ext4)$").pack(side=tk.LEFT)
        self.input_entry = Entry(input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        self.input_entry.bind('<Return>', self.execute_command)
        self.input_entry.focus_set()

        self.append_output("ext4 Shell started. Type 'exit' to quit.\n")

    def append_output(self, text):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, text)
        self.output_area.see(tk.END)
        self.output_area.config(state='disabled')

    def execute_command(self, event):
        line = self.input_entry.get()
        self.input_entry.delete(0, tk.END)

        self.append_output(f"(ext4)$ {line}\n")

        if line == "exit":
            self.root.quit()
            return

        args = shlex.split(line)
        if args == []:
            return

        if args[0] == "ls":
            self.append_output(f"{' '.join(args)}\n")
        elif args[0] == "cd":
            self.append_output(f"{' '.join(args)}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = Ext4GUI(root)
    root.mainloop()