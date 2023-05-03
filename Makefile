all: generate_tex generate_pdf generate_html

generate_tex:
	pandoc --lua-filter div2latexenv.lua --lua-filter minted.lua --template main.tex test.md -o out.tex 

generate_pdf:
	xelatex -shell-escape out.tex

generate_html:
	pandoc test.md -s -o handout.html
