# Image-Resizer-App
Simple and easy to use Image Resizer Application

## 🔧 How the Image Resizer App Works

1. 📤 **Upload an Image**

   * The user selects an image file (`.jpg`, `.jpeg`, or `.png`) using the file uploader.
   * The uploaded image is displayed immediately for preview.

2. ⚙️ **Set Resize Dimensions**

   * The user enters the **desired width and height** using the sidebar controls.
   * By default, these values match the original image size, but they can be changed easily.

3. ✂️ **Image Resizing**

   * The app uses the **Pillow** library to resize the image with the `Image.LANCZOS` algorithm for **high-quality results**.
   * The resized image is shown below the original for comparison.

4. 💾 **Download the Resized Image**

   * The resized image is prepared in `.png` format.
   * A **download button** allows the user to save the resized image locally with one click.

---

✅ **No installation or heavy software needed** — resize your images instantly right in your browser!
