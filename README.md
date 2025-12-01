# Manim Math Animations for High School Classrooms

![Project Review](thumbnail/IMG_0531.jpg)
<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#quick-start-for-teachers">Quick Start for Teachers</a> •
  <a href="#why-visual-animations">Why These Animations?</a> •
  <a href="#contributing">Contributing</a>
</p>

> **Concise • Engaging • Mathematically Accurate**

A growing collection of **Manim-powered animations** specifically designed for high school mathematics. In an era where student attention spans are shrinking, these short (usually 15–90 second) animations deliver key concepts quickly and memorably, leaving more class time for discussion, practice, and deeper exploration.

While visual tools are not a replacement for rigorous proof and problem-solving, they serve as powerful **cognitive hooks** that help students grasp ideas instantly and build lasting intuition.

## Current Topics (more added weekly)
- Linear Functions & Slope
- Quadratic Functions & Parabola Properties
- Exponential vs. Linear Growth
- Trigonometric Functions on the Unit Circle
- Systems of Equations (Graphical Solution)
- Pythagorean Theorem Proofs
- Geometric Transformations
- ...and many more coming!

## Why These Animations Work in High School

- **Under 2 minutes** → perfect for bell-ringers, recap, or mid-lesson clarification  
- **Zero fluff** → every frame serves the mathematical idea  
- **Clean voice-over ready** → add your own narration or use silently  
- Fully **open-source & customizable** → adapt to your curriculum, language, or pacing  

https://github.com/user/YourRepoName/assets/123456789/abcdef12-3456-7890-abcd-ef1234567890

## Quick Start for Teachers (5 minutes)

You don’t need to be a programmer! Here’s exactly what to do:

### 1. Install Manim (one-time only)

**MacOS**
```bash
brew install pyenv ffmpeg
pyenv install 3.11
pyenv global 3.11
pip install manim! 

```


**Windows (10 or 11)**
```bash
1. **Install Python 3.11** (if you don’t already have it)  
   → Download from https://www.python.org/downloads/release/python-31110/  
   → Choose **Windows installer (64-bit)**  
   → ⚡ **IMPORTANT**: check the box “Add Python 3.11 to PATH” before clicking Install

2. **Install FFmpeg** (needed for video export) – easiest method:  
   → Download the latest build from https://www.gyan.dev/ffmpeg/builds/  
   → Click “ffmpeg-release-essentials.zip”  
   → Extract the zip → copy the entire `bin` folder (inside the extracted folder) to `C:\ffmpeg\bin`  
   → Add it to PATH:  
      - Press `Win + X` → System → Advanced system settings → Environment Variables  
      - Under “System variables” find `Path` → Edit → New → add `C:\ffmpeg\bin` → OK all windows

3. **Install Manim**  
   Open **Command Prompt** or **PowerShell** (doesn’t need admin) and run:
   ```bash
   pip install manim