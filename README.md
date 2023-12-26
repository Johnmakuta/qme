# qme
An easy to use QR generator because I'm sick of ads. 

# Installation 
## Conda Installation
Currently I use Anaconda for nearly all of my package management in Python so miniconda is a minimum need to be installed if you'd like to use my specfile. 

For Windows:
```bash
onda create --name qme_env --file win_64_conda_spec_file.txt
```

For Mac
```bash
onda create --name qme_env --file osx_64_conda_spec_file.txt
```

I will attempt to make more specfiles as time goes on but I only have an old x64 macbook and a Windows PC to develop on normally so...

# Manual Installation
The follwing packages are needed:
- tkinter
- qrcode
- segno

```bash
conda create --name qme_env
conda activate qme_env
conda install -c anaconda tk
conda install -c conda-forge qrcode
conda install -c conda-forge segno
```

# Running
All you gotta do is run python
```bash
python qr_app.py
```