.pyimport streamlit as st
from PIL import  Image
import io

def resize_image (image, width, height):
    #using LANCZOS for high quality resizing
    return image.resize((width, height), Image.LANCZOS)

def main():
    st.title("Image Resizer App")
    st.write("This app allows you to upload an image and resize it to a specified Width and Height")

    #Uploading an image file
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "png",  "jpeg",])

    if  uploaded_file is not None:
        # Displaying the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        #Resizing options
        st.sidebar.header("Resize Options")
        width = st.sidebar.number_input("Width", min_value=1, value=image.width)
        height = st.sidebar.number_input("Height",  min_value=1, value=image.height)

        #Resized Image
        resized_image = resize_image(image, width, height)

        #Showing Resized Image
        st.subheader("Resized Image")
        st.image(resized_image, caption='Resized Image', use_column_width=True)

        #Saving resized image to bytesIO object
        buffered  = io.BytesIO()
        resized_image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        #Download Button
        st.download_button(
            label="Download Resized Image",
            data = img_bytes,
            file_name="resized_image.png",
            mime="image/png",
        )

if  __name__ == "__main__":
    main()
