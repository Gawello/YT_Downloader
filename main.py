import sys
import youtube_dl
import pdb
import os
from PyQt5 import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QComboBox, QFileDialog, QMessageBox,
                             QProgressBar, QProgressDialog)


# https://www.youtube.com/watch?v=FfWtIaDtfYk
# Create application class
class Application(QWidget):
    def __init__(self):
        super().__init__()
        # Define the ydl_opts dictionary as an instance variable
        self.ydl_opts = {}
        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle("YT downloader by Gawello")

        # Create a label
        label = QLabel("Enter the URL: ", self)
        label.move(20, 20)

        # Create a text field
        self.text_field = QLineEdit(self)
        self.text_field.move(20, 50)

        # Create a drop-down list for video quality
        self.quality_list = QComboBox(self)
        self.quality_list.addItem("Low")
        self.quality_list.addItem("Medium")
        self.quality_list.addItem("High")
        self.quality_list.move(20, 80)

        # Create a button to change the save location
        self.location_button = QPushButton('Change Save Location', self)
        self.location_button.move(20, 110)
        self.location_button.clicked.connect(self.change_location)

        # Create a button to download the video
        self.download_button = QPushButton('Download', self)
        self.download_button.move(180, 80)
        self.download_button.clicked.connect(self.download_video)

        # Create a progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(20, 140, 360, 20)

        # Create a label to display the download speed
        self.speed_label = QLabel("", self)
        self.speed_label.move(20, 120)

        # Set the window size
        self.setGeometry(300, 300, 400, 180)

    def update_progress(self, d):
        # Update the progress bar value
        self.progress_bar.setValue(d['percent'])
        # Update the speed label with the current download speed
        self.speed_label.setText(f"Current speed: {d['speed']} bytes/second")

    def change_location(self):
        # Open a file dialog to choose the save location
        save_location, _ = QFileDialog.getSaveFileName(self, 'Save File', 'C:/', '*.mp4')
        # Save the chosen save location
        self.save_location = save_location

    def download_video(self):
        pdb.set_trace()
        # Get the URL of the video from the text field
        url = self.text_field.text()

        # Check if the URL is empty
        if not url:
            # Display an error message in a popup
            QMessageBox.warning(self, 'Error', 'Please enter a URL')
            return

        # Get the selected video quality from the drop-down list
        quality = self.quality_list.currentText()

        # Set the download options based on the selected quality
        if quality == "Low":
            self.ydl_opts = {'format': 'worstvideo[ext=mp4]+worstaudio[ext=m4a]/mp4'}
        elif quality == "Medium":
            self.ydl_opts = {'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4'}
        elif quality == "High":
            self.ydl_opts = {'format': 'best[ext=mp4]/mp4'}

        # Print the self.ydl_opts dictionary
        print(self.ydl_opts)

        # Set the default save location to the folder containing the code
        default_save_location = os.path.dirname(os.path.abspath(__file__))
        save_location = 'C:/my_downloads'

        # If the user has chosen a save location, use it instead of the default location
        if hasattr(self, 'save_location'):
            save_location = self.save_location

        # Set the outtmpl option to the chosen save location
        self.ydl_opts['outtmpl'] = r"C:\Users\my_downloads.mp4"

        # Set the progress callback in the download options
        self.ydl_opts['progress_hooks'] = [self.update_progress]

        # Set the progress callback in the download options
        self.ydl_opts['progress_hooks'] = [self.update_progress]

        # Start the download
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            ydl.download([url])


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
