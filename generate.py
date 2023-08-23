import subprocess
import os
import shutil
import glob

# Concatenate MDs
print("Concating MDs")

with open("preout.md", "wb") as preout:
    for file in os.listdir("src"):
        with open(f"src/{file}", "rb") as temp:
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


print("Cleanup")
os.replace("out.pdf", "out/handout.pdf")

cleanup_files = glob.glob("out.*")
for cf in cleanup_files:
    os.remove(cf)

os.remove("preout.md")




