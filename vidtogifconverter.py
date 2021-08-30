import tkinter.filedialog
from moviepy.editor import VideoFileClip

file = tkinter.filedialog.askopenfilename(title="Select File")

# The name of the gif
name = file.split("/")
name = name[-1].split(".")
name = name[0]

# Create the gif
clip = VideoFileClip(file)
clip.write_gif(f"{name}.gif", fps=24)

print("Task Completed!")
