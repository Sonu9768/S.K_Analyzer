import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from modules import password_checker, port_scanner, traffic_monitor
from modules import encrypted_notes, vulnerability_scanner, mac_changer
from modules import shodan_tool, process_monitor

class SKAnalyzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("S.K_Analyzer - Cybersecurity Toolkit")
        self.root.geometry("1000x750")
        self.root.configure(bg="#0f0f0f")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=10)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Load and display hacker image from icon folder
        try:
            hacker_img = Image.open("icon/hacker.png")
            hacker_img = hacker_img.resize((120, 120), Image.Resampling.LANCZOS)
            self.tk_hacker = ImageTk.PhotoImage(hacker_img)
            img_label = tk.Label(root, image=self.tk_hacker, bg="#0f0f0f")
            img_label.grid(row=0, column=0, pady=(20, 0))
        except Exception as e:
            messagebox.showerror("Image Load Error", f"Could not load icon/hacker.png:\n{e}")

        # Stylish title
        title_label = tk.Label(
            root, text="S.K_Analyzer", font=("Courier New", 50, "bold"),
            fg="#00FF00", bg="#0f0f0f"
        )
        title_label.grid(row=1, column=0, pady=(0, 0))

        # Buttons in two columns
        btn_frame = tk.Frame(root, bg="#0f0f0f")
        btn_frame.grid(row=2, column=0, padx=50, pady=10, sticky="nsew")

        for i in range(2):
            btn_frame.grid_columnconfigure(i, weight=1)

        buttons = [
            ("Password Checker", password_checker.run),
            ("Port Scanner", port_scanner.run),
            ("Traffic Monitor", traffic_monitor.run),
            ("Encrypted Notes", encrypted_notes.run),
            ("Vulnerability Scanner", vulnerability_scanner.run),
            ("MAC Changer", mac_changer.run),
            ("Shodan Tool", shodan_tool.run),
            ("Process Monitor", process_monitor.run),
        ]

        for idx, (text, command) in enumerate(buttons):
            row = idx // 2
            col = idx % 2
            b = tk.Button(
                btn_frame, text=text, command=command,
                bg="#1e1e1e", fg="#00FF00", activebackground="#2a2a2a",
                activeforeground="#00ff88", font=("Consolas", 12),
                relief="flat", width=35
            )
            b.grid(row=row, column=col, pady=8, padx=10, ipady=6, sticky="ew")

        # Footer
        footer = tk.Label(
            root, text="Developed by S.K", bg="#0f0f0f",
            fg="#666666", font=("Consolas", 10)
        )
        footer.grid(row=3, column=0, pady=(0, 10), sticky="s")

if __name__ == "__main__":
    root = tk.Tk()
    app = SKAnalyzerApp(root)
    root.mainloop()
