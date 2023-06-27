# Image_super_resolution-Image_processing

## Dependencies and Installation
- Python >= 3.7 (Recommend to use Anaconda)
- PyTorch >= 1.7
- cudatoolkit >= 11
- streamlit >= 1.22

Installation

1) Clone
   ```bash
    git clone https://github.com/nebokekuma/Image_super_resolution-Image_processing.git
    cd Real-ESRGAN
    ```

2) Install dependent packages
   ```bash
    # We use BasicSR for both training and inference
    pip install basicsr
    # facexlib and gfpgan are for face enhancement
    pip install facexlib
    pip install gfpgan
   ```

## Quick Inference
 
 Python Script 

```console
Usage: python inference_realesrgan.py -n RealESRGAN_x4plus -i infile -o outfile [options]...

A common command: python inference_realesrgan.py -n RealESRGAN_x4plus -i infile --outscale 3.5 --face_enhance

  -h                   show this help
  -i --input           Input image or folder. Default: inputs
  -o --output          Output folder. Default: results
  -n --model_name      Model name. Default: RealESRGAN_x4plus
  -s, --outscale       The final upsampling scale of the image. Default: 4
  --suffix             Suffix of the restored image. Default: out
  -t, --tile           Tile size, 0 for no tile during testing. Default: 0
  --face_enhance       Whether to use GFPGAN to enhance face. Default: False
  --fp32               Use fp32 precision during inference. Default: fp16 (half precision).
  --ext                Image extension. Options: auto | jpg | png, auto means using the same extension as inputs. Default: auto
```

Inference

 ```bash
    python inference_realesrgan.py -n RealESRGAN_x4plus -i inputs --face_enhance
 ```

Results are in the `results` folder

## GUI 

1) To run the Gui use the following command

   ```bash
    cd Real-ESRGAN
    Streamlit run gui_main.py
   ```



## Note

1) In the case of cuda memory out of bound error message, try to decrease the size of the input image or crop the image as necessary.
2) It is better to use only a single input image to avoid any errors. Use the clear Button after every use to clear the images in the input folder provided in the GUI after every use. In the case of implementation via terminal manually empty out the input folder.
3) Create a inputs folder and a results folder inside the Real-ESRGAN directory if it doesn't consist either of the folders or create one automatically

