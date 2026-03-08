"""
===========================================
        CAESAR CIPHER PROJECT
===========================================
Prodigy Infotech Cyber Security Internship Task

This program performs:
1. Encryption using Caesar Cipher
2. Decryption using Caesar Cipher
3. Brute Force Attack
4. Frequency Analysis
5. File Encryption/Decryption

Author: Your Name
Language: Python 3
GUI: Tkinter
===========================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, scrolledtext
from collections import Counter
import os


class CaesarCipherGUI:
    """Caesar Cipher GUI Application with encryption, decryption, and analysis tools."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher - Cyber Security Tool")
        self.root.geometry("900x700")
        self.root.resizable(False, False)
        
        # Configure style
        self.root.configure(bg='#f0f0f0')
        
        # Create GUI components
        self.create_widgets()
    
    def create_widgets(self):
        """Create all GUI components."""
        # Header Frame
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="Caesar Cipher Encryption Tool", 
            font=("Arial", 20, "bold"),
            bg='#2c3e50',
            fg='white'
        )
        title_label.pack(pady=15)
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg='#f0f0f0')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Input controls
        left_panel = tk.Frame(content_frame, bg='#f0f0f0')
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        # Input section
        input_label = tk.Label(left_panel, text="Input Message:", font=("Arial", 10, "bold"), bg='#f0f0f0')
        input_label.pack(anchor='w')
        
        self.input_text = scrolledtext.ScrolledText(left_panel, height=5, width=40, wrap=tk.WORD)
        self.input_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Shift value section
        shift_frame = tk.Frame(left_panel, bg='#f0f0f0')
        shift_frame.pack(fill=tk.X, pady=5)
        
        shift_label = tk.Label(shift_frame, text="Shift Value (1-25):", font=("Arial", 10), bg='#f0f0f0')
        shift_label.pack(side=tk.LEFT, padx=5)
        
        self.shift_var = tk.StringVar(value="3")
        shift_spinbox = tk.Spinbox(shift_frame, from_=1, to=25, textvariable=self.shift_var, width=10)
        shift_spinbox.pack(side=tk.LEFT, padx=5)
        
        # Buttons section
        button_frame = tk.Frame(left_panel, bg='#f0f0f0')
        button_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            button_frame, 
            text="Encrypt", 
            command=self.encrypt, 
            bg='#27ae60', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=12
        ).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(
            button_frame, 
            text="Decrypt", 
            command=self.decrypt, 
            bg='#3498db', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=12
        ).pack(side=tk.LEFT, padx=5, pady=5)
        
        # File operations section
        file_frame = tk.Frame(left_panel, bg='#f0f0f0')
        file_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            file_frame, 
            text="Encrypt File", 
            command=self.encrypt_file, 
            bg='#e74c3c', 
            fg='white',
            font=("Arial", 9),
            width=15
        ).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(
            file_frame, 
            text="Decrypt File", 
            command=self.decrypt_file, 
            bg='#e67e22', 
            fg='white',
            font=("Arial", 9),
            width=15
        ).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Analysis buttons
        analysis_frame = tk.Frame(left_panel, bg='#f0f0f0')
        analysis_frame.pack(fill=tk.X, pady=10)
        
        tk.Button(
            analysis_frame, 
            text="Brute Force", 
            command=self.brute_force, 
            bg='#9b59b6', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=12
        ).pack(side=tk.LEFT, padx=5, pady=5)
        
        tk.Button(
            analysis_frame, 
            text="Frequency Analysis", 
            command=self.frequency_analysis, 
            bg='#1abc9c', 
            fg='white',
            font=("Arial", 10, "bold"),
            width=18
        ).pack(side=tk.LEFT, padx=5, pady=5)
        
        # Right panel - Output
        right_panel = tk.Frame(content_frame, bg='#f0f0f0')
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        output_label = tk.Label(right_panel, text="Output:", font=("Arial", 10, "bold"), bg='#f0f0f0')
        output_label.pack(anchor='w')
        
        self.output_text = scrolledtext.ScrolledText(right_panel, height=20, width=40, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Clear button
        clear_frame = tk.Frame(right_panel, bg='#f0f0f0')
        clear_frame.pack(fill=tk.X, pady=5)
        
        tk.Button(
            clear_frame, 
            text="Clear Output", 
            command=self.clear_output, 
            bg='#95a5a6', 
            fg='white',
            font=("Arial", 9)
        ).pack(side=tk.LEFT, padx=5)
    
    def encrypt_text(self, message, shift):
        """Encrypt text using Caesar Cipher."""
        encrypted_message = ""
        
        for char in message:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                encrypted_message += encrypted_char
            else:
                encrypted_message += char
        
        return encrypted_message
    
    def decrypt_text(self, message, shift):
        """Decrypt text using Caesar Cipher."""
        return self.encrypt_text(message, -shift)
    
    def encrypt(self):
        """Handle encryption button click."""
        try:
            message = self.input_text.get("1.0", tk.END).strip()
            shift = int(self.shift_var.get())
            
            if not message:
                messagebox.showwarning("Warning", "Please enter a message to encrypt!")
                return
            
            if not 1 <= shift <= 25:
                messagebox.showerror("Error", "Shift value must be between 1 and 25!")
                return
            
            encrypted = self.encrypt_text(message, shift)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Original Message:\n{message}\n\n")
            self.output_text.insert(tk.END, f"Shift Value: {shift}\n\n")
            self.output_text.insert(tk.END, f"Encrypted Message:\n{encrypted}")
        
        except ValueError:
            messagebox.showerror("Error", "Shift value must be a valid integer!")
    
    def decrypt(self):
        """Handle decryption button click."""
        try:
            message = self.input_text.get("1.0", tk.END).strip()
            shift = int(self.shift_var.get())
            
            if not message:
                messagebox.showwarning("Warning", "Please enter a message to decrypt!")
                return
            
            if not 1 <= shift <= 25:
                messagebox.showerror("Error", "Shift value must be between 1 and 25!")
                return
            
            decrypted = self.decrypt_text(message, shift)
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Encrypted Message:\n{message}\n\n")
            self.output_text.insert(tk.END, f"Shift Value: {shift}\n\n")
            self.output_text.insert(tk.END, f"Decrypted Message:\n{decrypted}")
        
        except ValueError:
            messagebox.showerror("Error", "Shift value must be a valid integer!")
    
    def brute_force(self):
        """Perform brute force attack on encrypted message."""
        message = self.input_text.get("1.0", tk.END).strip()
        
        if not message:
            messagebox.showwarning("Warning", "Please enter an encrypted message!")
            return
        
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Brute Force Attack Results:\n")
        self.output_text.insert(tk.END, "=" * 40 + "\n\n")
        
        for shift in range(1, 26):
            decrypted = self.decrypt_text(message, shift)
            self.output_text.insert(tk.END, f"Shift {shift:2d}: {decrypted}\n")
    
    def frequency_analysis(self):
        """Perform frequency analysis on the input text."""
        message = self.input_text.get("1.0", tk.END).strip()
        
        if not message:
            messagebox.showwarning("Warning", "Please enter a message for analysis!")
            return
        
        # Count letter frequencies
        letters_only = ''.join(c.upper() for c in message if c.isalpha())
        freq = Counter(letters_only)
        
        # Sort by frequency
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Frequency Analysis:\n")
        self.output_text.insert(tk.END, "=" * 40 + "\n\n")
        self.output_text.insert(tk.END, f"Total Characters: {len(letters_only)}\n\n")
        self.output_text.insert(tk.END, "Letter  | Count | Percentage\n")
        self.output_text.insert(tk.END, "-" * 40 + "\n")
        
        for letter, count in sorted_freq:
            percentage = (count / len(letters_only)) * 100
            self.output_text.insert(tk.END, f"{letter}      | {count:5d} | {percentage:6.2f}%\n")
    
    def encrypt_file(self):
        """Encrypt a file."""
        file_path = filedialog.askopenfilename(title="Select file to encrypt")
        
        if not file_path:
            return
        
        try:
            shift = int(self.shift_var.get())
            
            if not 1 <= shift <= 25:
                messagebox.showerror("Error", "Shift value must be between 1 and 25!")
                return
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            encrypted_content = self.encrypt_text(content, shift)
            
            output_file = file_path.rsplit('.', 1)[0] + '_encrypted.txt'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(encrypted_content)
            
            messagebox.showinfo("Success", f"File encrypted successfully!\nSaved as: {os.path.basename(output_file)}")
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"File Encryption Complete\n\n")
            self.output_text.insert(tk.END, f"Original File: {os.path.basename(file_path)}\n")
            self.output_text.insert(tk.END, f"Encrypted File: {os.path.basename(output_file)}\n")
            self.output_text.insert(tk.END, f"Shift Value: {shift}\n")
        
        except ValueError:
            messagebox.showerror("Error", "Shift value must be a valid integer!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def decrypt_file(self):
        """Decrypt a file."""
        file_path = filedialog.askopenfilename(title="Select file to decrypt")
        
        if not file_path:
            return
        
        try:
            shift = int(self.shift_var.get())
            
            if not 1 <= shift <= 25:
                messagebox.showerror("Error", "Shift value must be between 1 and 25!")
                return
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            decrypted_content = self.decrypt_text(content, shift)
            
            output_file = file_path.rsplit('.', 1)[0] + '_decrypted.txt'
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(decrypted_content)
            
            messagebox.showinfo("Success", f"File decrypted successfully!\nSaved as: {os.path.basename(output_file)}")
            
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"File Decryption Complete\n\n")
            self.output_text.insert(tk.END, f"Encrypted File: {os.path.basename(file_path)}\n")
            self.output_text.insert(tk.END, f"Decrypted File: {os.path.basename(output_file)}\n")
            self.output_text.insert(tk.END, f"Shift Value: {shift}\n")
        
        except ValueError:
            messagebox.showerror("Error", "Shift value must be a valid integer!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def clear_output(self):
        """Clear the output text area."""
        self.output_text.delete("1.0", tk.END)


def main():
    """Main function to run the application."""
    root = tk.Tk()
    app = CaesarCipherGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()