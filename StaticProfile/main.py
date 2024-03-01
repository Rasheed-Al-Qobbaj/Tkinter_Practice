from PIL import Image, ImageTk, ImageDraw  # Python Imaging Library for image processing
import tkinter as tk  # Python's standard GUI (Graphical User Interface) package


# Main application class
class MainApplication(tk.Tk):

    # Constructor
    def __init__(self):
        super().__init__()

        # Initialize text for name
        self.label = None

        # Initialize text for bio
        self.text = None

        # Initialize labels and photo
        self.github_label = None
        self.photo = None

        # Set window title and size
        self.title("StaticProfile")
        self.geometry("750x600")

        # Set window background color
        self.configure(bg='#2D2D2D')

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Create name label
        self.label = tk.Label(self, text="Rasheed Alqobbaj", font=("Helvetica", 24), fg="white", bg='#2D2D2D')
        self.label.pack(pady=10)

        # Open and resize profile photo
        image = Image.open("Profile.png")
        image = image.resize((250, 250))

        # Create a circular mask
        mask = Image.new('L', image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)

        # Create a new RGBA image with a transparent background
        result = Image.new('RGBA', image.size, (0, 0, 0, 0))

        # Paste the original image onto the result image using the mask
        result.paste(image, mask=mask)
        self.photo = ImageTk.PhotoImage(result)

        # Create photo label
        self.label = tk.Label(self, image=self.photo, bg='#2D2D2D')
        self.label.pack(pady=10)

        # Create bio text
        bio_text = ("I'm a Computer Science student with a deep passion for technology "
                    "and a strong commitment to community development.\n\n"
                    "I believe in making a positive impact through innovation. "
                    "My portfolio showcases my journey in the tech world while highlighting "
                    "my technical skills and contributions to the community.")

        # Create bio text widget
        self.text = tk.Text(self, font=("Helvetica", 12), fg="white", bg='#2D2D2D', bd=0, padx=10,
                            wrap=tk.WORD, height=6)
        self.text.insert(tk.END, bio_text)
        self.text.config(state=tk.DISABLED)
        self.text.pack(pady=10)

        # Create a title label
        title_label = tk.Label(self, text="Things I Love", font=("Helvetica", 24, 'bold'), fg="white", bg='#2D2D2D')
        title_label.pack(pady=10)

        # Create a list of things you love
        things_i_love = ["• Myself", "• Coding", "• Python", "• AI"]

        # Create a Listbox widget
        self.listbox = tk.Listbox(self, font=("Helvetica", 12), fg="white", bg='#2D2D2D', bd=0, highlightthickness=0)

        # Insert each item from the list into the Listbox
        for item in things_i_love:
            self.listbox.insert(tk.END, item)

        # Pack the Listbox to make it visible
        self.listbox.pack()

        # Create email label
        self.label = tk.Label(self, text="Email: rasheedsrq@gmail.com", font=("Helvetica", 12), fg="white",
                              bg='#2D2D2D')
        self.label.pack(pady=10)

        # Create GitHub link label
        self.github_label = tk.Label(self, text="Github: Rasheed-Al-Qobbaj", font=("Helvetica", 12), fg="blue",
                                     cursor="hand2",
                                     bg='#2D2D2D')
        self.github_label.pack(pady=10)

        # Bind events for Github link label
        self.github_label.bind("<Enter>", self.on_enter)
        self.github_label.bind("<Leave>", self.on_leave)
        self.github_label.bind("<Button-1>", self.open_github)

    # Event handler for mouse entering Github link label
    def on_enter(self, event):
        self.github_label['foreground'] = 'red'

    # Event handler for mouse leaving Github link label
    def on_leave(self, event):
        self.github_label['foreground'] = 'blue'

    # Event handler for clicking Github link label
    def open_github(self, event):
        import webbrowser
        webbrowser.open("https://github.com/Rasheed-Al-Qobbaj")


# Main function
if __name__ == "__main__":
    # Create and run application
    app = MainApplication()
    app.mainloop()
