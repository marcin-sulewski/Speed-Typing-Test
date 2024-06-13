import tkinter as tk
from tkinter import ttk
import random
import time

class TypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Speed Typing Test")
        self.root.geometry("720x480")
        self.root.config(bg="#113C4A")
        root.resizable(0,0)
        
        self.texts = [
            "WSB Merito w Warszawie jest miejscem intensywnej nauki.",
            "Studenci WSB Merito w Warszawie mają dostęp do nowoczesnych technologii edukacyjnych.",
            "Wykładowcy WSB Merito w Warszawie są doświadczonymi specjalistami w swoich dziedzinach.",
            "Studenci WSB Merito w Warszawie mają możliwość uczestniczenia w praktykach zawodowych.",
            "WSB Merito w Warszawie oferuje bogaty kalendarz wydarzeń i konferencji.",
            "Biblioteka WSB Merito w Warszawie gromadzi szeroki zasób literatury naukowej.",
            "Studenci WSB Merito w Warszawie mogą rozwijać swoje zainteresowania poprzez liczne koła naukowe.",
            "WSB Merito w Warszawie stawia na praktyczne umiejętności w edukacji.",
            "Uczelnia WSB Merito w Warszawie współpracuje z lokalnymi i międzynarodowymi firmami.",
            "Studenci WSB Merito w Warszawie mają dostęp do platformy e-learningowej."  
        ]
        
        self.current_text = random.choice(self.texts)
        self.start_time = None
        self.end_time = None
        
        self.title_label = tk.Label(root, text="Speed Typing Test", font=("Helvetica", 24, "bold"), bg="#113C4A", fg="#FDFDFD")
        self.title_label.pack(pady=10)
        
        self.text_frame = tk.Frame(root, bg="#113C4A")
        self.text_frame.pack(pady=10)
        
        self.text_label = tk.Label(self.text_frame, text=self.current_text, font=("Helvetica", 14), wraplength=500, justify="center", bg="#113C4A", fg="#FDFDFD")
        self.text_label.pack(pady=20)
        
        self.entry = ttk.Entry(root, width=50, font=("Helvetica", 12),)
        self.entry.pack(pady=20)
        self.entry.bind("<KeyRelease>", self.check_input)
        self.entry.config(state='disabled')
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#113C4A")
        self.result_label.pack(pady=10)
        
        self.stats_frame = tk.Frame(root, bg="#113C4A")
        self.stats_frame.pack(pady=10)

        self.wpm_label = tk.Label(self.stats_frame, text="WPM: 0", font=("Helvetica", 14), bg="#113C4A", fg="#FDFDFD")
        self.wpm_label.pack(side=tk.LEFT, padx=10)

        self.timer_label = tk.Label(self.stats_frame, fg="#FDFDFD", text="Time: 0.0s", font=("Helvetica", 14), bg="#113C4A")
        self.timer_label.pack(side=tk.LEFT, padx=10)

        self.restart_button = ttk.Button(root, text="Restart", command=self.restart)
        self.restart_button.pack(padx=20, pady=20)
        
        self.start_button = ttk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=30, pady=20)
        
        self.stop_button = ttk.Button(root, text="Stop", command=self.stopbutton)
        self.stop_button.pack(side=tk.RIGHT, padx=30, pady=20)
        
 
        
    def start(self):
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.entry.focus_set()
        self.start_time = time.time()
        self.update_timer()
    
    def stopbutton(self):
        if self.start_time and not self.end_time:
            self.end_time = time.time()      

    def stop(self):
        if self.start_time and not self.end_time:
            self.end_time = time.time()      
            self.calculate_results()

    def check_input(self, event):
        typed_text = self.entry.get()
        
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            words_per_minute = (len(typed_text.split()) / elapsed_time) * 60
            self.wpm_label.config(text=f"WPM: {words_per_minute:.2f}")
            self.timer_label.config(text=f"Time: {elapsed_time:.2f}s")
        
        if typed_text == self.current_text:
            self.stop()
    
    def calculate_results(self):
        time_taken = self.end_time - self.start_time
        words_per_minute = (len(self.current_text.split()) / time_taken) * 60
        accuracy = sum(1 for a, b in zip(self.entry.get(), self.current_text) if a == b) / len(self.current_text) * 100
        
        self.result_label.config(text=f"Completed! Time: {time_taken:.2f} seconds | WPM: {words_per_minute:.2f} | Accuracy: {accuracy:.2f}%", fg="#FDFDFD")
        self.entry.config(state='disabled')
    
    def restart(self):
        self.current_text = random.choice(self.texts)
        self.text_label.config(text=self.current_text)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.wpm_label.config(text="WPM: 0")
        self.timer_label.config(text="Time: 0.0s")
        self.start_time = None
        self.end_time = None
        self.entry.config(state='disabled')
        
    def update_timer(self):
        if self.start_time and not self.end_time:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=f"Time: {elapsed_time:.2f}s")
            self.root.after(100, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTest(root)
    root.mainloop()
