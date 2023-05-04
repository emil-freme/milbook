infile = test.md
outfile = handout
all: generate_tex generate_pdf rename_pdf generate_html

generate_tex:
	pandoc --lua-filter div2latexenv.lua \
		--lua-filter minted.lua \
		--template main.tex \
		$(infile) -o out.tex 

generate_pdf:
	xelatex -shell-escape out.tex

rename_pdf:
	mv out.pdf $(outfile).pdf

generate_html:
	pandoc $(infile) -s -o $(outfile).html
