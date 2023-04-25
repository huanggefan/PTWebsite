const katex_config = {
    delimiters:
        [
            {left: "$$", right: "$$", display: true},
            {left: "$", right: "$", display: false}
        ]
}

hljs.highlightAll()

renderMathInElement(document.body, katex_config)
