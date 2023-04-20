import streamlit as st
from inference_realesrgan import main as inference_main
import streamlit as st
from realesrgan import RealESRGANer
from PIL import Image
import os
from io import BytesIO
from zipfile import ZipFile
from streamlit_image_comparison import image_comparison
import time
# import shutil


def streamlit_main():
    

    progress_text = "Operation in progress. Please wait."
    
    # Streamlit configuration
    # Set up the Streamlit app
    
    st.set_page_config(page_title='Super Resolution')
    hide_menu_style = """
        <style>
        @MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.title("Super Resolution")
    # # Rest of dependancies
    buf = BytesIO()  # Setting up BytesIO to download results

    # Taking input image from the user
    image_file = st.file_uploader(
        "Upload Image", type=['png', 'jpeg', 'jpg', 'webp'])
    save_image(image_file)
    if image_file:
      model_name = st.selectbox(
        "Model",
        [   
            "Face super resolution model",
            "Text super resolution model"
        ],
        index=0
        )
  
      denoise_strength = st.slider("Denoise strength", 0.0, 1.0, 0.5, 0.25)
      outscale = st.slider("Output scale", 2.0, 4.0, 4.0, 0.5 )
    #   tile_size = st.slider("Tile size", 0, 512, 0, 32)
    #   tile_pad = st.slider("Tile padding", 0, 32, 10, 2)
    #   pre_pad = st.slider("Pre padding size", 0, 32, 0, 2)
      face_enhance = st.checkbox("Face enhancement")
      if face_enhance:
         face_enhance = '--face_enhance'
      half = st.radio('Half Precision', options=("off", 'On'), index=0)
      if half == 'On':
        half = ''
      else:
        half = '--fp32'
      alpha_upsampler = st.selectbox(
            "Alpha upsampler", ["realesrgan", "bicubic"]
        )
    #   ext = st.selectbox("Image extension", ["auto", "jpg", "png"])


    # Runnning the model and upscalling user input
    if (st.button('Enhance')):
        filesinputlist = []
         # os.chdir('Real-ESRGAN/')
        for filename in os.listdir('inputs/'):
            temp = filename.split(".")
            if f'{temp[0].lower()}_out.png'not in os.listdir('results/'):
            # if os.path.isfile(f"{Temp[0].lower()}_out.png") not in os.listdir('results/'):
                 os.system(
                    "python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs/{0} -o results -dn {1} --outscale {2} {3} {4} --alpha_upsampler {5} ".format(filename, denoise_strength,outscale, half, face_enhance, alpha_upsampler))
                 my_bar = st.progress(0, text=progress_text)

                 for percent_complete in range(100):
                    time.sleep(1)
                    if  os.path.isfile(f'results{temp[0].lower()}_out.png'):
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    else: 
                       my_bar.progress(100,text= "complete")
                       break
                        
            else:
                 # skip file it already exists in output (unless specfied not to)
                continue
        

        for filename in os.listdir('results/'):
            if '_out.' in filename.lower():
                target = filename
                filesinputlist.append(filename)
                if '.jpg' in target.lower():
                   format = 'JPEG'
                elif '.jpeg' in target.lower():
                   format = 'JPEG'
                elif '.png' in target.lower():
                   format = 'PNG'
                else:
                   format = 'webp'
        
        
                 # First file in list
        
        res = load_image(f'results/{filesinputlist[0]}')
        st.image(res, width=None)
        res.save(buf, format=format)
        byte_img = buf.getvalue()
        # with ZipFile(f'Output {filesinputlist[0]}.zip', 'w') as zipObj2:
        #     for i in os.listdir("results/"):
        #         zipObj2.write(f"results/{i}")

        
        
        with open(f'results/{filesinputlist[0]}', "rb") as fp:
            btn = st.download_button(
               label="Download Image",
               data=fp,
               mime="image/png"
               )
    if(st.button('clear')):
       clear()

    
    
    if(st.button("Compare")):
           st.markdown("LR to HR Image Comparison")
           image_comparison(
            img1=image_file,
            img2= res,
            label1="Before",
            label2="After",
            )
           
     
    

   

    

@st.cache_data
def load_image(image_file):
    img = Image.open(image_file)
    return img


# Saving uploaded image in input folder for processing
def save_image(image_file):
  if image_file is not None:
    filename = image_file.name
    img = load_image(image_file)
    st.image(image=img, width=None)
    with open(os.path.join('inputs/', filename), "wb") as f:
      f.write(image_file.getbuffer())
      st.success("Succesfully uploaded file for processing".format(filename))

def clear():
   for filname in os.listdir("results/"):
      os.remove(f'results/{filname}')
   for input_folder_filename in os.listdir("inputs/"):
      os.remove(f'inputs/{input_folder_filename}')


  
    # if (st.download_button(label='Download Upscaled Image', data=zipObj2)):
    #   st.success('Image Saved!')








# # Get the input image
# uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# if uploaded_file is not None:
#     # Display the input image
#     st.image(uploaded_file, caption="Original Image")

#     # Choose the model
#     model_name = st.selectbox(
#         "Select the model to use",
#         [
#             "RealESRGAN_x4plus",
#             "RealESRNet_x4plus",
#             "RealESRGAN_x4plus_anime_6B",
#             "RealESRGAN_x2plus",
#             "realesr-animevideov3",
#             "realesr-general-x4v3"
#         ]
#     )



















# def upscale_image(image_file, model_name):
#     # Load the image
#     img = cv2.imread(image_file.name)

#     # Upscale the image
#     real_esrganer = RealESRGANer(
#         scale=4,
#         model_path=None,
#         model_name=model_name,
#         tile=0,
#         tile_pad=10,
#         pre_pad=0,
#         half=False,
#         alpha_upsampler="bicubic",
#         face_enhance=False
#     )
#     img_upscaled = real_esrganer.enhance(img)

#     return img_upscaled





    # Upscale the image
    # with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    #     temp_file.write(uploaded_file.read())
    # img_upscaled = upscale_image(temp_file, model_name)

    # Display the upscaled image
    # st.image(img_upscaled, caption="Upscaled Image")


if __name__ == "__main__":
    streamlit_main()