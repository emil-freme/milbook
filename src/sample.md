---
title: "Sample Document"  
author: "Emil Freme"  
date: "2024.9"
---

# Introduction

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris.

## Activities

::: {.activity data-latex=""}

1. Lorem ipsum dolor sit amet.  
2. Consectetur adipiscing elit.  
3. Integer nec odio.

:::

## Tips and Warnings 

A tip on the side of the page

::: {.tip data-latex=""}  
Use the `\newcommand` command to create new commands in LaTeX.  
:::

A warning on the side of the page

::: {.warning data-latex=""}  
Remember to always save your work before compiling the document.  
:::

## Comments

A comment box

::: {.commentbox data-latex=""}  
This is an additional comment about the section’s content.  
:::

## Code and Highlighting

By using `minted`, we can get beautiful code with syntax highlighting:

```python
def example_function():
    print("Hello, world!")
```

Here is an example of JavaScript code:

```javascript
function exampleFunction() {
    console.log("Hello, world!");
}
```

The codes are automatically formatted and include line numbering.

## Tables

Here is an example table using `booktabs` and `tabularx`:

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Item 1   | Lorem    | Ipsum    |
| Item 2   | Dolor    | Sit      |
| Item 3   | Amet     | Consectetur |

## Images

Here is an example of an image:

![Example Image](images/sample_image.png)

## Conclusion

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor.

---

### What This Sample Demonstrates:

1. **Activity (`activity`)**:
   - Encapsulates tasks and activities.

2. **Tip (`tip`)**:
   - Sidebar tip for helpful information.

3. **Warning (`warning`)**:
   - Sidebar warning for critical notes.

4. **Comment Box (`commentbox`)**:
   - Used to add supplementary comments or explanations.

5. **Code with Highlighting**:
   - Python and JavaScript code snippets using the `minted` package for syntax highlighting.

6. **Tables**:
   - A simple table created in Markdown, which will be translated into LaTeX format using `booktabs`.

7. **Images**:
   - Example of an image using the `graphicx` package.


