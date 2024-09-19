# MilBook

![MillBook](images/sample_image.png)

MilBook is a Python-based automation tool designed to generate PDF handouts from a set of Markdown files. It allows users to input metadata like author, title, and date, and uses Pandoc and LaTeX for the final PDF generation.

## Features

- **GUI-based file selection:** Easily select source and output directories using `easygui`.
- **Metadata input:** Enter author, project title, and date information.
- **Markdown concatenation:** Concatenates multiple Markdown files from the source directory.
- **Pandoc & LaTeX integration:** Converts concatenated Markdown files into LaTeX and compiles them to a PDF.
- **Custom LaTeX filters:** Supports custom Lua filters for advanced LaTeX formatting.
- **Automated cleanup:** Removes temporary files after PDF generation.

## Requirements

To run MilBook, the following dependencies must be installed:

- **Python 3.x**
- **Pandoc** (for Markdown to LaTeX conversion)
- **XeLaTeX** (for compiling the LaTeX file into a PDF)
- **easygui** (for simple GUI dialogs)
- **configparser** (built-in Python module)
- **shutil** and **glob** (built-in Python modules)

## Installation

1. Install the required Python libraries:
    ```bash
    pip install easygui
    ```

2. Install **Pandoc**:
    - Download and install from [Pandoc's official website](https://pandoc.org/installing.html).

3. Install **XeLaTeX**:
    - If you're using a LaTeX distribution like TeX Live or MiKTeX, XeLaTeX should already be included.

4. **Templates and Lua Filters:**
    - The repository includes a LaTeX template (`lib/main.tex`) and Lua filters (`lib/minted.lua`, `lib/div2latexenv.lua`). These files are essential for the PDF generation process.
    - `main.tex`: Custom LaTeX template that includes options for formatting Markdown with Pandoc.
    - `minted.lua`: A Lua filter for enabling the use of the `minted` package for syntax highlighting.
    - `div2latexenv.lua`: A Lua filter that converts fenced div blocks in Markdown to LaTeX environments.

Make sure that the `lib` directory contains these template and filter files. You can modify the LaTeX template and Lua filters to fit your project's needs.


## Usage

1. Run the Python script:
    ```bash
    ./milbook.py
    ```

2. Use the GUI dialogs to:
   - Select the folder containing your Markdown files.
   - Select the output folder where the PDF will be saved.
   - Enter the name of the output file, the author, project title, and date.

3. The tool will:
   - Concatenate all `.md` files from the source folder.
   - Convert the concatenated Markdown into LaTeX using Pandoc.
   - Generate the final PDF using XeLaTeX.
   - Save the PDF to your specified output folder with the chosen filename.

### Configuration

MilBook stores the selected paths and metadata in a `config.ini` file. If this file exists, the tool will automatically use the stored values, bypassing the GUI selection process.

### Cleanup

After generating the PDF, MilBook cleans up intermediate files such as `out.tex`, `preout.md`, and other temporary LaTeX files generated during compilation.

### Example

1. Source Markdown files:
    - `src/sample.md`

2. Output: 
    - PDF will be generated at the chosen output folder, e.g., `out/handout.pdf`.

## TODO

    - Make better placements of tips and warnings
    - Create more callouts

## Reporting Issues

If you find a bug or have a feature request, please open an issue in the GitHub repository. Provide as much detail as possible, including steps to reproduce the issue.

Thank you for contributing to MilBook! Your help is greatly appreciated.


## License

MilBook is open-source and licensed under the MIT License.

