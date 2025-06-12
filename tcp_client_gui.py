import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox
from chatroom import ClientTCP
import threading
import socket

class GUIClientTCP(ClientTCP):
    def __init__(self, client_name, server_port):
        super().__init__(client_name, server_port)
        self.root = tk.Tk()
        self.root.title(f"TCP Chatroom - {client_name}")
        self.root.geometry("400x500")

        self.chat_area = scrolledtext.ScrolledText(self.root, state='disabled', wrap=tk.WORD)
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Configure tags for sent and received messages
        self.chat_area.tag_configure('sent', foreground='blue', justify='right')
        self.chat_area.tag_configure('received', foreground='black', justify='left')

        self.entry_field = tk.Entry(self.root)
        self.entry_field.pack(padx=10, pady=(0, 10), fill=tk.X)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=(0, 10))

        self.root.protocol("WM_DELETE_WINDOW", self.exit_chat)

    def receive_gui(self):
        while not self.exit_receive.is_set():
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message == 'server-shutdown':
                    self.append_message("Server is shutting down...", 'received')
                    self.exit_chat()
                    break
                # Check if the message is from self
                if message.startswith(f"{self.client_name}:"):
                    self.append_message(message, 'sent')
                else:
                    self.append_message(message, 'received')
            except socket.error:
                break

    def append_message(self, message, tag):
        self.chat_area.configure(state='normal')
        self.chat_area.insert(tk.END, message + '\n', tag)
        self.chat_area.configure(state='disabled')
        self.chat_area.see(tk.END)

    def send_message(self):
        message = self.entry_field.get()
        if message:
            if message == 'exit':
                self.exit_chat()
                return
            self.send(message)
            self.entry_field.delete(0, tk.END)

    def exit_chat(self):
        try:
            self.send('exit')
        except:
            pass
        self.exit_run.clear()
        self.exit_receive.set()
        self.client_socket.close()
        self.root.destroy()

    def run(self):
        if self.connect_server():
            self.exit_run.set()
            threading.Thread(target=self.receive_gui, daemon=True).start()
            self.root.mainloop()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', type=str, required=True)
    args = parser.parse_args()
    client = GUIClientTCP(args.name, 12345)
    client.run()