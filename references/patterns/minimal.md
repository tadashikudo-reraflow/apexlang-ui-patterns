---
description: "Minimal whitespace business UI pattern. White + soft green, generous spacing. Use for Todo, simple lists, login-matched screens."
---

# Minimal Pattern

## When to Use

- 余白を活かした業務画面
- Todo、一覧、ログイン画面のトーンを揃えたいとき
- 強い装飾を避け、可読性を優先したいとき

## Visual Direction

- 背景: 白〜ごく薄いグレー
- アクセント: ソフトな緑
- 区切り: 控えめなボーダーまたは余白のみ
- モバイルでは縦積みに再配置

## Implementation Guidance

1. Theme Roller で Primary を緑系に、背景を明るくする
2. Region に Template Option で余白を増やす（padding 多め）
3. 必要なら以下のCSS変数を中央ファイルで上書き:

```css
:root {
  --ut-body-background-color: #ffffff;
  --ut-component-border-color: #e8f5e9;
  --ut-palette-primary: #4caf50;
}
.minimal-region {
  padding: 1.5rem 2rem;
}
```

4. 主アクションは1つのHotボタン
5. レスポンシブ: `col-xs-12` でモバイル時に全幅

## APEXlang Notes

- 標準の Region / Item を使い、Template Options で調整
- 公式スキルの page-layout-templates や region-components をベースにする
- 独自HTMLは最小限に

## Inspiration

Qiita記事「余白を生かしたミニマルUI」
