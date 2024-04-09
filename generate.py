import configparser
import easygui
import glob
import os
import shutil
import subprocess

# Concatenate MDs
print("Concating MDs")

config = configparser.ConfigParser()

if not config.read("config.ini"):
    src_path = easygui.diropenbox("Selecione uma pasta com os fontes",
                                  "Milbook", "src")
    out_path = easygui.diropenbox("Selecione uma pasta destino",
                                  "Milbook", "out")
    out_name = easygui.enterbox("Nome do arquivo de saida", "Milbook",
                                "handout", True)

    config["Default"] = {"src_path": src_path, 
                         "out_path": out_path, 
                         "out_name": out_name
                         }
    with open("config.ini", "w") as configfile:
        config.write(configfile)
else:
    src_path = config["Default"]["src_path"]
    out_path = config["Default"]["out_path"]
    out_name = config["Default"]["out_name"]





          

with open("preout.md", "wb") as preout:

    for file in os.listdir(src_path):
        with open(f"{src_path}/{file}", "rb") as temp:
            print(f"--{file}")
            shutil.copyfileobj(temp, preout)


print("Generating Tex File")
subprocess.run(["pandoc", 
                "--lua-filter", "lib/div2latexenv.lua",
		        "--lua-filter", "lib/minted.lua",
		        "--template", "lib/main.tex",
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




