py -3.10 -m pip install virtualenv
py -3.10 -m virtualenv .venv
.venv\Scripts\activate

pip install --upgrade pip
pip install farm-haystack[colab,ocr,preprocessing,file-conversion,pdf]

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install pdfminer pdfminer.six