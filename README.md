# clask.compile-error.net

Nostr 関連の自作アプリ・リレー・bot のインデックスページ。

## 構成

| ファイル | 役割 |
|---|---|
| `site.json` | 掲載項目のデータ（セクション・アイコン・名前・パス・URL・説明） |
| `template.html` | ページの外枠と CSS。`{{SECTIONS}}` が一覧に置換される |
| `build.py` | `site.json` + `template.html` → `index.html` を生成 |
| `index.html` | 生成物。公開されるのはこれ |

## 項目を追加・変更する

1. `site.json` を編集する
2. `python3 build.py` で `index.html` を生成する
3. 内容を確認して公開する

`index.html` は生成物なので直接編集しない。

### セクションの形式

`style` が `cards` のセクションは1項目あたり次のキーを持つ。`desc` は省略可。

```json
{ "icon": "📊", "name": "Emoji Ranking", "path": "clask.compile-error.net/emoji-ranking",
  "url": "emoji-ranking/", "desc": "リアクション (kind 7) を集計して…" }
```

`style` が `chips` のセクション（More on GitHub）は `name` と `url`、任意で `title`。
