---
name: apexlang-ui-patterns
description: "Oracle APEX / APEXlang screen design patterns. Use when creating or customizing APEX pages for specific visual styles (minimal, dark-neon, RPG, 3D, review layout, approval route, dense ledger, shift board, mobile field). Complements official oracle/skills apexlang."
type: workflow
lifecycle: active
---

# APEXlang UI Patterns — Screen Design Catalog

Oracle APEX画面の「見た目・UX」を意図的にコントロールするためのスキル。  
公式のAPEXlang生成・検証スキルを補完する。

対象: APEX 26.1（26.2は未検証）。

## When to Use

- ユーザーが特定のデザイン方向性を指定したとき（ミニマル、ダーク、ネオン、RPG、3Dなど）
- 標準の表・フォーム以外の表現を求められたとき
- アップグレード耐性のあるカスタム方法を優先したいとき
- 公式skillsで生成したアプリの見た目を調整したいとき

## Core Workflow

1. **意図を確認**
   - ビジネス系かエンタメ系か
   - 主タスクは何か（1ページに主アクションは原則1つ）
   - レスポンシブの要件

2. **デザイン型を選択**
   下の呼び出しテーブルを参照し、該当する `references/patterns/*.md` を読む。

3. **共通原則を適用**
   `references/principles.md` を参照。Theme Roller → Template Options → CSS変数 → 中央静的ファイルの順を優先。

4. **APEXlang / 公式スキルと連携**
   - 構文の正しさは公式 `oracle/skills` (apexlang) に任せる
   - このスキルは「どの設定・どのCSS変数・どのレイアウトにするか」を指示する

5. **レビュー**
   - コントラスト、レスポンシブ、主アクションの明確さ、アップグレード耐性を確認

## Design Pattern Routing Table

| ユーザーの言葉・要件 | 読むファイル |
|----------------------|--------------|
| ミニマル / 余白 / 白緑 / Todo / シンプル業務 | `references/patterns/minimal.md` |
| ダーク / ネオン / ダッシュボード / 在庫 / グラフ多め | `references/patterns/dark-neon.md` |
| レビュー / 確認欄 / 文書 / 原票 / 横並び | `references/patterns/review-layout.md` |
| 3D / 街並み / Three.js / WebGL / 演出 | `references/patterns/3d-scene.md` |
| RPG / マップ / チャット / ゲーム風 / 青いウィンドウ | `references/patterns/rpg-style.md` |
| 稟議 / 承認 / 申請 / 承認ルート / 経費 / 購買 | `references/patterns/ringi-route.md` |
| 台帳 / 受注 / 一覧と詳細 / 高密度の表 / Excel移行 | `references/patterns/ledger-grid.md` |
| 勤務表 / シフト / 人×日付 / 人数不足 | `references/patterns/shift-board.md` |
| スマホ / 現場 / 訪問 / 点検 / 片手入力 | `references/patterns/mobile-field.md` |
| 共通原則・CSS変数・配置ルールが必要なとき | `references/principles.md` |

該当する型がない場合は `principles.md` を基に、Universal Themeの範囲で提案する。

## 他スキルとの分担

- 構文・生成・検証・配置: 公式 `oracle/skills` の apexlang
- 製品ごとのDesign Contractから資産を作る: `apex-visual-adapter`
- SPA風の画面遷移と全体のUX: `apex-spa-ux-orchestrator`
- このスキル: 見た目の型の選択と、型ごとの設定の指針

## Key Principles (Summary)

- Template Options と Theme Roller を最優先
- CSSは中央化した静的ファイルに置き、CSS変数を上書きする
- 購読テンプレートは直接編集しない
- 主アクションは1つのHotボタン
- 公式APEXlang skillsと併用する

詳細は `references/principles.md`。

## References

- Official: https://github.com/oracle/skills (apex/apexlang)
- Inspiration: Qiita - APEXlangでVibe Coding：画面デザイン集
