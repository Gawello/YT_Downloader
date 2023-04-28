import sys
import customtkinter
import youtube_dl
from PyQt5.QtWidgets import QMessageBox


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{800}x{400}")

        # Configure Entry for video link
        self.link_text = customtkinter.CTkEntry(self, placeholder_text="Adres URL")
        self.link_text.grid(row=0, column=0, pady=12, padx=10)

        # Configure download button
        self.download_button = customtkinter.CTkButton(self, command=self.download)
        self.download_button.grid(row=0, column=1, pady=12, padx=10)

        # Configure progress bar
        self.progress_bar = customtkinter.CTkProgressBar(self)
        self.progress_bar.grid(row=1, column=0, columnspan=3, pady=12, padx=10)

        # Configure Label for download speed
        self.speed_label = customtkinter.CTkLabel(self, text="")
        self.speed_label.grid(row=2, column=0, pady=12, padx=10)

        # Configure close button
        self.close_button = customtkinter.CTkButton(self, text="Close", command=sys.exit)
        self.close_button.grid(row=4, column=2, pady=12, padx=10)

    def update_progress(self, d):
        # Update the progress bar value
        self.progress_bar.set(d['percent'])
        # Update the speed label with the current download speed
        self.speed_label.setText(f"Current speed: {d['speed']} b/s")

    def download(self):
        url = self.link_text.get()
        if not url:
            url = self.empty_url()
        self.ydl_opts = {'format': 'best[ext=mp4]/mp4'}
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            try:
                # Start download
                ydl.download([url])
                # Set the progress callback in the download options
                self.ydl_opts['progress_hooks'] = [self.update_progress]
            except:
                self.QMessageBox.warning('Error', 'Please enter a URL')
                return

    def empty_url(self):
        dialog = customtkinter.CTkInputDialog(text="Wprowadz adres URL", title="Wprowadź URL")
        return dialog.get_input()


app = App()
app.mainloop()
