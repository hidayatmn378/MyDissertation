# MyThesis

<!--Based on the Journal "Effect of Meteorological Parameters on Ocean Layer Variability in the Bay of Bengal"-->

----------------------------------------------------------------------
eksekusi file dengan cara
pdflatex -synctex=1 -interaction=nonstopmode --shell-escape thesis.tex
----------------------------------------------------------------------


----------------------------------------------------------------------
Cara install Package baru
sumber: https://tex.stackexchange.com/questions/1137/where-do-i-place-my-own-sty-or-cls-files-to-make-them-available-to-all-my-te
----------------------------------------------------------------------

#Tahap 1,
install package yang sudah di download dengan cara:
tex nama_file.ins
contoh: tex apacite.ins 

#Tahap 2,
copy folder hasil download package ke 
/usr/share/texlive/texmf-dist/tex/latex
gunakan syntax:
sudo cp -r nama_folder /usr/share/texlive/texmf-dist/tex/latex
contoh: sudo cp -r apacite /usr/share/texlive/texmf-dist/tex/latex

#Tahap 2.1 install new package, 
max@hostname ~: $ wget mirrors.ctan.org/macros/latex/contrib/subfloat.zip # download link for subfloat, if you don't trust this, you can download it manually
max@hostname ~: $ unzip subfloat.zip
max@hostname ~: $ cd subfloat
max@hostname ~/subfloat: $ latex subfloat.ins
max@hostname ~/subfloat: $ sudo mkdir /usr/share/texmf/tex/latex/subfloat
max@hostname ~/subfloat: $ sudo mkdir -p /usr/share/texmf/doc/subfloat
max@hostname ~/subfloat: $ sudo cp subfloat.sty /usr/share/texmf/tex/latex/subfloat/
max@hostname ~/subfloat: $ sudo cp subfloat.pdf /usr/share/texmf/doc/subfloat
max@hostname ~/subfloat: $ sudo texhash # update your LaTeX distribution

#Tahap 3,
run texhash 
buka terminal di /usr/share/texlive/texmf-dist/tex/latex dan ketik
sudo texhash
----------------------------------------------------------------------

----------------------------------------------------------------------
Hapus output
./clean
----------------------------------------------------------------------

----------------------------------------------------------------------
Cara agar hanya 1x masukkan username & password github
git config --global credential.helper cache
----------------------------------------------------------------------

----------------------------------------------------------------------
New branch
git checkout -b apacite

Pindah branch
git checkout apacite 
atau
git checkout main

Push branch
git push -u thesis apacite

----------------------------------------------------------------------
notes:
packages harus tetap di copy diluar supaya bibliografi tidak error


