function Math(elem)
  if elem.mathtype == 'DisplayMath' then
    local math_content = elem.text
    local latex = string.format('\\begin{blackboard} \n %s \n \\end{blackboard}', math_content)
    return pandoc.Math('DisplayMath', latex)
  end
  return elem
end
