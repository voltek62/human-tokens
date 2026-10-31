#!/usr/bin/env python3
"""Assemble index.html (page complète) à partir de src/head.html et src/page.html.
Usage : python3 build.py [chemin-de-sortie-sans-squelette]
Le second fichier, optionnel, est la version head + corps sans <html>/<head>/<body>,
pour un hébergeur qui ajoute son propre squelette."""
import sys, pathlib
root = pathlib.Path(__file__).parent
head = (root / "src/head.html").read_text(encoding="utf-8")
page = (root / "src/page.html").read_text(encoding="utf-8")
full = ('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        '<style>[hidden]{display:none!important}body{margin:0}</style>\n' + head + '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
(root / "index.html").write_text(full, encoding="utf-8")
print("index.html :", len(full), "octets")
if len(sys.argv) > 1:
    pathlib.Path(sys.argv[1]).write_text(head + "\n" + page, encoding="utf-8")
    print("fragment :", sys.argv[1])
