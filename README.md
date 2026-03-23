<div align="center">

<!-- 🖼️ ANIMATED HEADER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0e27,25:0d1b4b,50:1a2f6e,75:1e3a8a,100:2563eb&height=220&section=header&text=🖼️%20Image%20Resizer%20App&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=Simple%20%7C%20Fast%20%7C%20High-Quality%20Image%20Resizing%20in%20Your%20Browser&descAlignY=58&descSize=16&animation=fadeIn" />

<br/>

<!-- TYPING ANIMATION -->
[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=60A5FA&center=true&vCenter=true&width=700&lines=🖼️+Upload+%7C+Resize+%7C+Download+—+That+Simple!;⚡+Powered+by+Pillow+%7C+LANCZOS+Algorithm;📐+Custom+Width+%26+Height+Controls;💾+One-Click+PNG+Download;✅+No+Installation+Needed+—+Runs+in+Browser!)](https://git.io/typing-svg)

<br/>

<!-- BADGES -->
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-Image%20Processing-1e3a8a?style=for-the-badge&logo=python&logoColor=white)

<br/>

![Status](https://img.shields.io/badge/Status-Active-6BCB77?style=flat-square)
![Formats](https://img.shields.io/badge/Supports-.jpg%20%7C%20.jpeg%20%7C%20.png-60A5FA?style=flat-square)
![Algorithm](https://img.shields.io/badge/Algorithm-LANCZOS-1e3a8a?style=flat-square)
![No Install](https://img.shields.io/badge/No%20Installation-Runs%20in%20Browser-2563eb?style=flat-square)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Zameer%20Shaikh-0077B5?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/zameer-shaikh-1a9482345)

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## 🖼️ What is Image Resizer App?

> A **clean and minimal Streamlit web app** that lets you upload, resize, and download images instantly — right in your browser. No heavy software, no installation, no hassle. Just upload and resize in seconds! ✨

```python
# Three steps. That's it.
step_1 = "📤 Upload your image"
step_2 = "📐 Set your desired width & height"
step_3 = "💾 Download the resized image"
# ✅ Done — no installation needed!
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## ✨ Features At a Glance

<div align="center">

| ✅ Feature | 📝 Description |
|:---|:---|
| 📤 **Image Upload** | Supports `.jpg`, `.jpeg`, and `.png` formats |
| 👁️ **Instant Preview** | Uploaded image displayed immediately for preview |
| 📐 **Custom Dimensions** | Set desired width & height via sidebar controls |
| 🔢 **Smart Defaults** | Dimension inputs default to the original image size |
| ✂️ **High-Quality Resize** | Uses Pillow's `Image.LANCZOS` algorithm for crisp results |
| 🔍 **Side-by-Side View** | Original & resized image shown together for comparison |
| 💾 **One-Click Download** | Download resized image as `.png` with a single click |
| ✅ **Zero Installation** | Runs fully in the browser — no software needed |

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🔧 How It Works

### 📤 Step 1 — Upload an Image

```
📁  Supported Formats:  .jpg  |  .jpeg  |  .png
👁️  Uploaded image is displayed instantly as a preview
```

---

### ⚙️ Step 2 — Set Resize Dimensions

```
📐  Enter desired Width  →  via sidebar control
📐  Enter desired Height →  via sidebar control
🔢  Defaults to original image dimensions automatically
```

---

### ✂️ Step 3 — Image Resizing

```python
# Under the hood
from PIL import Image

resized = image.resize((new_width, new_height), Image.LANCZOS)
# LANCZOS → best quality downsampling algorithm 🎯
```

> 💡 **Why LANCZOS?** It's the gold standard for high-quality image resizing — minimizes pixelation and preserves sharpness even at smaller sizes.

---

### 💾 Step 4 — Download

```
📦  Resized image prepared in .png format
🖱️  One-click Download button → saves to your device instantly
✅  No watermarks. No compression loss. Clean output.
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Pillow-Image%20Library-1e3a8a?style=for-the-badge&logo=python&logoColor=white" />
</p>

<div align="center">

| 🧩 Component | 🛠️ Tool |
|:---|:---|
| 🖥️ **UI / Frontend** | Streamlit |
| 🖼️ **Image Processing** | Pillow (PIL) |
| 📐 **Resize Algorithm** | `Image.LANCZOS` |
| 💾 **Output Format** | PNG |

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🚀 How to Run

```bash
# 1️⃣ Clone the repository
git clone https://github.com/Zameer17/Image-Resizer-App.git
cd Image-Resizer-App

# 2️⃣ Install dependencies
pip install streamlit pillow

# 3️⃣ Run the app
streamlit run app.py
```

> ✅ App opens in your browser at `http://localhost:8501`

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 📁 Project Structure

```
Image-Resizer-App/
│
├── 📄 app.py             # Main Streamlit app
├── 📄 requirements.txt   # Dependencies
└── 📄 README.md          # You are here!
```

---

## 🔮 Future Improvements

```
🎨  Support for more formats — .webp, .bmp, .gif
📏  Aspect ratio lock toggle
🔄  Batch image resizing
☁️  Deploy on Streamlit Cloud
📱  Mobile-friendly responsive UI
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

---

## 🌐 Connect with Me

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Zameer%20Shaikh-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zameer-shaikh-1a9482345)
[![GitHub](https://img.shields.io/badge/GitHub-Zameer17-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Zameer17)

<br/>

> *"Simplicity is the ultimate sophistication."* — Leonardo da Vinci 🎨

<br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:2563eb,25:1e3a8a,50:0d1b4b,75:0a0e27,100:0a0e27&height=120&section=footer&animation=fadeIn" />

</div>
