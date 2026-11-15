# Prompt sent to Claude (Sonnet 5.5, Medium effort):

I want to create a syntax coloring theme in Visual Studio Code for editing PEG grammars specifications.

Here are the specific tokens that should be coloured:

* "<-" which stands for the definition of a grammar rule
* "/" which stands for an alternative syntax for a grammar rule
* "(" and ")" which stand for the grouping of entities (e.g. names rules)
* "[", "]" and "-" which help describing authorized chars in specified strings
* "+", "?" and "*" which stand for one-or-more, one-or-zero and zero-or-more repetitions of the preceeding entity
* "'" which encloses single characters

The color for these specific tokens should be the same and they should be displayed bold.

Furthermore "##" will be used for comments (running until the end of the line). Comments should then be displayed italic and with a color different from the specific tokens listed above.

The rest of the text should be displayed white if background is dark and black if background is light.

Finally, it would be fine to be able to highlight any selected part of text and provide a way to:

* go to the related rule definition if any;
* walk up or down through the occurences of the selected text if any.


1. Propose a configuration file that allows for this, adapted to dark and light themes;
2. Explain how to use it (install, etc.) with Visual Studio Code.



# Claude answer:

I'll build this as a small VS Code extension: a TextMate grammar for the tokens, two color themes (dark and light), and a tiny provider script for go-to-definition and occurrence highlighting.

I built this as a small VS Code extension, `peg-grammar.zip`, with the PEG highlighting, a dark and a light theme, and the navigation features. I checked that the JSON files parse and that `extension.js` passes a syntax check, but I haven't loaded it in VS Code itself.

## 1. What's in it

```
peg-grammar/
├── package.json                    # declares the language, grammar, themes, defaults
├── language-configuration.json     # "##" comments, brackets, quotes, word pattern
├── extension.js                    # go to definition, references, highlights, outline
├── syntaxes/peg.tmLanguage.json    # tokenizer (which characters get which scope)
├── themes/peg-dark-color-theme.json
├── themes/peg-light-color-theme.json
└── example.peg                     # sample file to test with
```

**Coloring**
- **Operators and delimiters:** `<-`, `/`, `( )`, `[ ]`, `-` (only inside `[...]`), `+ ? *` and the `'` quotes all get the same scope family, `keyword.operator.peg.*`. Each theme colors that family with one color, in bold. The text inside quotes and character classes is left uncolored.
- **Comments:** `## ...` to end of line is italic, in a color different from the operators.
- **Everything else:** white in PEG Dark and black in PEG Light.

| | Operators (bold) | Comments (italic) | Other text |
|---|---|---|---|
| PEG Dark | `#FFB454` orange | `#6FBF73` green | `#FFFFFF` |
| PEG Light | `#B8470A` dark orange | `#2E7D32` dark green | `#000000` |

**Navigation**
- **F12 or Ctrl+Click** on a rule name jumps to its `Name <- ...` definition.
- **Shift+F12** lists all references to the rule.
- **Ctrl+Shift+O** shows an outline of all rules.
- **Occurrence highlighting:** put the cursor on a rule name and every occurrence is highlighted. **F7** goes to the next occurrence and **Shift+F7** to the previous one.
- **Arbitrary selected text** is highlighted natively by VS Code (`editor.selectionHighlight`). To step through those matches, use **Ctrl+F3** and **Shift+Ctrl+F3** (Cmd+F3 on macOS). **Ctrl+D** adds the next match to the selection.

The extension ignores comments, quoted strings and character classes when it looks for rule names. A rule name inside `'...'` or `[...]` is therefore not treated as a reference.

## 2. Installing it

**Quickest, with no tooling:**
1. Unzip `peg-grammar.zip`.
2. Copy the `peg-grammar` folder to your VS Code extensions folder:
   - Linux/macOS: `~/.vscode/extensions/`
   - Windows: `%USERPROFILE%\.vscode\extensions\`
3. Restart VS Code, or run **Developer: Reload Window**.

**Or package it as a `.vsix`:**
```
cd peg-grammar
npx @vscode/vsce package      # may ask you to add a repository field or LICENSE
code --install-extension peg-grammar-0.1.0.vsix
```

**To try it without installing:** open the `peg-grammar` folder in VS Code and press **F5**. A second window (Extension Development Host) opens with the extension loaded.

**Using it:**
1. Open a file ending in `.peg`, such as `example.peg`. The language shows as "PEG" in the bottom-right status bar.
2. Pick a theme with **Ctrl+K Ctrl+T** (Cmd+K Cmd+T on macOS): choose **PEG Dark** or **PEG Light**.

**If you want to keep your current theme:** you can apply the same colors to any theme from `settings.json`, with separate blocks for dark and light:
```json
"editor.tokenColorCustomizations": {
  "[*Dark*]": { "textMateRules": [
    { "scope": "keyword.operator.peg", "settings": { "foreground": "#FFB454", "fontStyle": "bold" } },
    { "scope": "comment.line.number-sign.peg", "settings": { "foreground": "#6FBF73", "fontStyle": "italic" } }
  ]},
  "[*Light*]": { "textMateRules": [
    { "scope": "keyword.operator.peg", "settings": { "foreground": "#B8470A", "fontStyle": "bold" } },
    { "scope": "comment.line.number-sign.peg", "settings": { "foreground": "#2E7D32", "fontStyle": "italic" } }
  ]}
}
```
This only changes the operator and comment colors. The plain text then takes whatever color your theme uses, so it won't necessarily be pure white or black. The two supplied themes are the ones that set that.

## Limitations
- **Rule names:** they are matched as `[A-Za-z_][A-Za-z0-9_]*`. A name containing a hyphen, such as `my-rule`, would be split at the hyphen. Tell me if your grammars use hyphens and I'll adjust the pattern.
- **Single file:** navigation works within the current file only, not across files.
- **Quotes:** only single-quoted strings are tokenized, as you specified. `"..."` strings are not colored.
- **File extension:** files must end in `.peg`. Add other extensions in `package.json` under `contributes.languages[0].extensions`.