import tempfile
import os

temp_dir = tempfile.gettempdir()
test_file = os.path.join(temp_dir, "manim_test_output.txt")

with open(test_file, "w") as f:
    f.write("Hello from Manim/Python!")

print(f"File created at: {test_file}")