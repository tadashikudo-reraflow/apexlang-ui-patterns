---
description: "Common principles for APEX screen design: Theme Roller, Template Options, CSS variables, placement rules, accessibility. Read before applying any specific pattern."
---

# Design Principles

## Priority Order (Upgrade-Safe)

1. **Theme Roller** — 色・フォント・レイアウト全体
2. **Template Options** — 個々のRegion/Item/Buttonの余白・強調
3. **CSS Variables** — `:root` やスコープ付きで上書き
4. **中央化した静的ファイル** — `#APP_FILES#` または `#WORKSPACE_FILES#`
5. **ページレベルのインラインCSS** — 最終手段（後で移行する）

## CSS Variables to Prefer

```css
:root {
  --ut-body-background-color: ...;
  --ut-component-text-default-color: ...;
  --ut-component-background-color: ...;
  --ut-component-border-color: ...;
  --a-button-background-color: ...;
  --a-button-text-color: ...;
  --ut-palette-primary: ...;
}
```

ハードコードした色より変数を優先する。変数名は、APEX 26.1 の Universal Theme の CSS で定義されているかを確かめる。

## UX Rules

- 1ページに主アクションは原則1つ（Hotボタン）
- 関連情報はRegion/Cardでグループ化
- レスポンシブ: Column CSS Classes を活用（`col-xs-12` など）
- アクセシビリティ: Theme Rollerのコントラストチェッカーを使う
- 静的IDをRegionに付与し、JSから安定して参照する

## Placement of CSS / JS

- Application User Interface → File URLs を最優先
- ページの File URLs は次点
- Inline は避ける

## APEXlang Collaboration

- 構文・検証は公式 `oracle/skills` の apexlang スキルに任せる
- このプロジェクトは「どのTemplate Optionを選ぶか」「どのCSS変数を変えるか」を指示する
- 生成後に見た目を調整するフローを推奨

## What to Avoid

- 購読テンプレートの直接編集
- ページごとの散在したCSS
- 脆弱なセレクタ（`#t_Region_body` など）
- 複数のHotボタン
- CSS変数を無視したハードコード
