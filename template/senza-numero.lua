-- pandoc 3.1 non passa a Typst la classe .unnumbered dei titoli:
-- li riscriviamo come #heading(numbering: none) così Premessa e Allegati restano senza numero.
-- Nell'indice entrano solo i titoli di primo livello, non i loro paragrafi.
function Header(el)
  if not FORMAT:match("typst") or not el.classes:includes("unnumbered") then
    return nil
  end
  local testo = pandoc.write(pandoc.Pandoc({ pandoc.Plain(el.content) }), "typst")
  testo = testo:gsub("%s+$", "")
  return pandoc.RawBlock(
    "typst",
    string.format(
      "#heading(level: %d, numbering: none, outlined: %s)[%s]",
      el.level,
      el.level == 1 and "true" or "false",
      testo
    )
  )
end
