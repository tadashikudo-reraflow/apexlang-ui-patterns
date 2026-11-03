---
description: "RPG-style UI pattern. Blue windows, map + info panels, chat dialogs. Use for game-like map and conversation screens."
---

# RPG Style Pattern

## When to Use

- 地図をフィールドのように見せたいとき
- チャットやメニューをゲーム風ウィンドウにしたいとき

## Visual Direction

- 青いグラデーションのウィンドウ
- 白い枠線
- 地図 + 情報パネルの組み合わせ
- 必要に応じて MapLibre GL JS

## Implementation Guidance

1. 複数の Region または HTML でパネルを構成
2. 地図は Map Region または MapLibre を HTML Region 内で使用
3. CSSで青いグラデーションと枠を再現
4. チャットは Static Content + Dynamic Action で更新

## Notes

- 公式の Map コンポーネントと組み合わせ可能
- 過度なカスタムCSSは避け、変数を活用

## Inspiration

Qiita記事「RPG風のマップUI」「RPG風のチャットUI」
