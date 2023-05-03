all: generate_tex generate_pdf

generate_tex:
	pandoc --lua-filter div2latexenv.lua --lua-filter minted.lua --template main.tex test.md -o out.tex 

generate_pdf:
	pdflatex -shell-escape out.tex 
