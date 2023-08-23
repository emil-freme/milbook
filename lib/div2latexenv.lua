-- based on https://tex.stackexchange.com/questions/525924/with-pandoc-how-to-apply-a-style-to-a-fenced-div-block
function Div(el)
    if el.attributes["data-latex"] == "" then
        table.insert(
            el.content, 1, 
            pandoc.RawBlock("latex", string.format("\\begin{%s}", el.classes[1]))
            )

        table.insert(
            el.content, 
            pandoc.RawBlock("latex", string.format("\\end{%s}", el.classes[1]))
            )
    end
    return el
end
