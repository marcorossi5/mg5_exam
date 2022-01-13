SHELL=/bin/bash
output = pDUNE_dn_strategies.pdf
paper = pDUNE_dn_strategies.tex

bibfile = ../blbl.bib

output = ex1_4.pdf

LC = pdflatex # -shell-escape
FPFlags = "-draftmode"

.PHONY: all clean clean_latex pdf

all: $(output)

pdf: $(output)


%.pdf : %.tex
	@$(LC) $(FPFLAGS) $< # > /dev/null

clean_latex:
	@echo "Removing all latex byproducts"
	@rm -f *.{600pk,aux,bak,bbl,bcf,blg,dvi,fdb_latexmk,fls,idx,ilg,ind,lof,log,lot,mf,nav,out,snm,synctex.gz,tdo,tfm,toc}

clean: clean_latex
	@echo "Removing latex pdf"
	@rm -f $(output)