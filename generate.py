#!/usr/bin/env python3
import configparser
import easygui
import glob
import os
import shutil
import subprocess

config = configparser.ConfigParser()

if not config.read("config.ini", encoding="utf-8"):
    src_path = easygui.diropenbox("Selecione uma pasta com os fontes",
                                  "Milbook", "src")
    out_path = easygui.diropenbox("Selecione uma pasta destino",
                                  "Milbook", "out")
    out_name = easygui.enterbox("Nome do arquivo de saida", "Milbook",
                                "handout", True)

    author = easygui.enterbox("Nome do Autor", "Milbook")
    title = easygui.enterbox("Titulo do Projeto", "Milbook")
    date = easygui.enterbox("Data", "Milbook")

    config["Default"] = {"src_path": src_path, 
                         "out_path": out_path, 
                         "out_name": out_name
                         }
    config["Metadata"] = {"author": author, 
                          "title": title,
                          "date": date
                          }

    with open("config.ini", "w", encoding="utf-8") as configfile:
        config.write(configfile)
else:
    src_path = config["Default"]["src_path"]
    out_path = config["Default"]["out_path"]
    out_name = config["Default"]["out_name"]
    author = config["Metadata"]["author"]
    title = config["Metadata"]["title"]
    date = config["Metadata"]["date"]
# Concatenate MDs
print("Concating MDs")

with open("preout.md", "wb") as preout:

    for file in sorted(glob.glob(os.path.join(src_path, "*.md"))):
        if file == "preout.md":
            continue
        with open(f"{file}", "rb") as temp:
            print(f"--{file}")
            shutil.copyfileobj(temp, preout)
            preout.write(b"\n\n")

src_path_latexed = src_path.replace("\\", "/")

print("Generating Tex File")
subprocess.run(["pandoc", 
                "--lua-filter", "lib/div2latexenv.lua",
		        "--lua-filter", "lib/minted.lua",
		        # "--lua-filter", "lib/blackboardEnv.lua",
		        "--template", "lib/main.tex",
                "--variable", f"graphicspath={src_path_latexed}",
                "--metadata", f"author={author}",
                "--metadata", f"title={title}",
                "--metadata", f"date={date}",
                "--top-level-division", "chapter",
		        "preout.md", "-o", "out.tex"])

print("Generating PDF")
subprocess.run(["xelatex", "-shell-escape", "out.tex"])
#Run two time to get references right
subprocess.run(["xelatex", "-shell-escape", "out.tex"])


shutil.copy("out.pdf", f"{out_path}/{out_name}.pdf")

print("Cleanup")
cleanup_files = glob.glob("out.*")
for cf in cleanup_files:
    os.remove(cf)

os.remove("preout.md")




