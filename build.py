#!/usr/bin/env python3
"""Generate index.html from site.json and template.html."""
import io
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def card(item):
    parts = ['<li><a href="%s">' % esc(item["url"])]
    parts.append('<span class="head">')
    parts.append('<span class="icon">%s</span>' % item["icon"])
    parts.append('<span class="name">%s' % esc(item["name"]))
    parts.append('<span class="path">%s</span>' % esc(item["path"]))
    parts.append('</span></span>')
    if item.get("desc"):
        parts.append('<span class="desc">%s</span>' % esc(item["desc"]))
    parts.append('</a></li>')
    return "        " + "".join(parts)


def chip(item):
    title = ' title="%s"' % esc(item["title"]) if item.get("title") else ""
    return '        <li><a href="%s"%s>%s</a></li>' % (
        esc(item["url"]), title, esc(item["name"]))


def section(sec):
    render = card if sec["style"] == "cards" else chip
    cls = "apps" if sec["style"] == "cards" else "chips"
    lines = ["    <section>",
             "      <h2>%s</h2>" % esc(sec["title"]),
             '      <ul class="%s">' % cls]
    lines += [render(i) for i in sec["items"]]
    lines += ["      </ul>", "    </section>"]
    return "\n".join(lines)


def main():
    site = json.load(io.open(os.path.join(BASE, "site.json"), encoding="utf-8"))
    tpl = io.open(os.path.join(BASE, "template.html"), encoding="utf-8").read()
    body = "\n\n".join(section(s) for s in site["sections"])
    out = tpl.replace("{{SECTIONS}}", body)
    io.open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(out)
    n = sum(len(s["items"]) for s in site["sections"])
    print("index.html: %d sections, %d items" % (len(site["sections"]), n))


if __name__ == "__main__":
    main()
