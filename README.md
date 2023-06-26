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
    pip install -r requirements.txt
    python setup.py develop
   ```

