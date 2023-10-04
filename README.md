# Intelligent Search FHTW

Search with natural language expressions in a set of provided documents (from UAS Technikum Vienna).

Based on the iX Article [Maschinen auf Text abrichten](https://www.heise.de/select/ix/2023/13/2307514452409693169), Resources to the article: [ix.de/zy3m](ix.de/zy3m), [GitHub](https://github.com/ix-magazin/Maschinen_auf_Text_abrichten/)


## 1. Install

ATTENTION: use Python3.10 - not never dur to restrictions in one of the libraries

* Nvidia-Drivers for your GPU
* Evaluate the CUDA version with the following command: ```nvidia-smi``` (should be above 11)
* Setup python virtual environment (venv)
```shell
py -3.10 -m pip install virtualenv
py -3.10 -m virtualenv .venv
.venv\Scripts\activate
```

* Install required libraries (alternativly install them manually, see 1.1)  
  ```pip install -r requirements.txt```

### 1.1 Manual installation of used libraries

* Upgrade PIP: ```pip install --upgrade pip```
* Install Hystack  
```bash
pip install farm-haystack[colab,ocr,preprocessing,file-conversion,pdf]
```

* Install PyTorch with CUDA extensions:  
Fetch PIP install command from PyTorch Website: https://pytorch.org/get-started/locally/
On 4.8.2023 for my RTX2080 it was:
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

* Install PDFMiner:
On windows the PDF-converter included in Haystack does not work well, so this is done by myself with PDFMiner
```
pip install pdfminer
pip install pdfminer.six
```

## 2. Run

* Activate the virtual environment  
```./.venv/Scripts/activate```

1. Download the dataset files: ```./01_download-????-files.cmd```

2. Add dataset files to the document store
  This will convert all documents (pdf, word, etc.) to plain text and add this to a haystack document store.
  Then the store will be indiced generating a DPR (Dense Passage Retrieval)

  The following models will be used:
  * query_embedding_model="deepset/gbert-base-germandpr-question_encoder",
  * passage_embedding_model="deepset/gbert-base-germandpr-ctx_encoder",
  
  ATTENTION: DPR on texts with to the model unknown words, won't work too well. In that case different specific models have to be used or the plain-old word-search can be used as workaround.

  ```
  ./add_documents.py
  ```

## Further Resources

* [Haysack Toutorial: Process your documents](https://haystack.deepset.ai/tutorials/08_preprocessing)