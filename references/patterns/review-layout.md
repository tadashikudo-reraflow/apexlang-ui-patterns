---
description: "Review layout pattern. Large original document area next to confirmation fields. Use for document review and approval screens."
---

# Review Layout Pattern

## When to Use

- 原票・文書を大きく見せ、横に確認欄を置く画面
- 入力内容と原本を見比べながら作業するとき

## Visual Direction

- 原票側: 広めの領域、落ち着いた背景
- 確認側: フォーム項目を整理して配置
- 全体はソフトな色調で集中を妨げない

## Implementation Guidance

1. 2カラムレイアウト（例: 8/4 または 7/5）
2. 左側: Static Content または Display Only で原本を大きく
3. 右側: Form Region で確認項目
4. 主アクション（承認・確認）は下部または固定位置のHotボタン
5. 背景は白〜生成り系

## APEXlang Notes

- Region の Column CSS Classes で横並びを制御
- 公式の form と static content 系テンプレートを組み合わせる

## Inspiration

Qiita記事「文書と確認欄を並べるレビューUI」
