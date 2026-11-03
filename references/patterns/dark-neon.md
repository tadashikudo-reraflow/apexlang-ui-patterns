---
description: "Dark neon dashboard pattern. Dark background with bright charts. Use for high-density dashboards and inventory-style screens."
---

# Dark Neon Pattern

## When to Use

- 情報量の多いダッシュボード
- 複数のチャート（棒・円・折れ線）を並べたいとき
- 暗い背景に明るいデータを強調したいとき

## Visual Direction

- 背景: 暗い紺〜黒
- チャート・アクセント: ネオン系（シアン、マゼンタなど）
- 階層を明確にし、データが浮かび上がるようにする

## Implementation Guidance

1. Theme Roller で Dark 系の Theme Style をベースにする
2. チャートRegionを複数配置し、系列色をコントラスト高く
3. CSS変数例:

```css
:root {
  --ut-body-background-color: #0a0a12;
  --ut-component-text-default-color: #e0e0ff;
  --ut-component-background-color: #12121c;
}
.neon-accent {
  border-color: #00ffcc;
  box-shadow: 0 0 12px #00ffcc33;
}
```

4. アニメーションは控えめに（パフォーマンス）

## APEXlang Notes

- Chart Region を中心に構成
- 公式の chart テンプレートをベースに、Theme Style で色を調整

## Inspiration

Qiita記事「ダークネオンのダッシュボード」
