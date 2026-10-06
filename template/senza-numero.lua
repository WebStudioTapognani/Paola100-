-- Titoli speciali che pandoc 3.1 non sa passare a Typst.
-- {.unnumbered}: Premessa e Allegati restano senza numero; nell'indice entrano
--   solo i titoli di primo livello, non i loro paragrafi.
-- {.parte}: "# Il metodo {.parte}" diventa "Parte II. Il metodo", con pagina
--   d'apertura propria; i capitoli continuano la numerazione.
local ROMANI = { "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X" }
local parti = 0

local function in_typst(inlines)
  local testo = pandoc.write(pandoc.Pandoc({ pandoc.Plain(inlines) }), "typst")
  return (testo:gsub("%s+$", ""))
end

function Header(el)
  if el.level == 1 and el.classes:includes("parte") then
    parti = parti + 1
    local prefisso = "Parte " .. ROMANI[parti] .. ". "
    if FORMAT:match("typst") then
      return pandoc.RawBlock(
        "typst",
        string.format("#heading(level: 1, numbering: none)[%s%s] <parte>", prefisso, in_typst(el.content))
      )
    end
    el.content:insert(1, pandoc.Str(prefisso))
    el.classes:insert("unnumbered")
    return el
  end

  if not FORMAT:match("typst") or not el.classes:includes("unnumbered") then
    return nil
  end
  return pandoc.RawBlock(
    "typst",
    string.format(
      "#heading(level: %d, numbering: none, outlined: %s)[%s]",
      el.level,
      el.level == 1 and "true" or "false",
      in_typst(el.content)
    )
  )
end
