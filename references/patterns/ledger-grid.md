---
description: "Dense ledger pattern. Compact grid, metric cards and a detail drawer. Use for order, inventory and billing list-detail screens."
---

# 台帳グリッド型

対象：Oracle APEX 26.1 / Universal Theme 26.1（テーマスタイルは Iris を土台）
状態：2026-11-02 採用。見本は `examples/ledger-grid/mock.html`。**APEX の実機では動かして確かめていません（実機未確認）。**

---

## 1. 型の名前と用途

- **型の名前**：台帳グリッド型
- **どの業務か**：受注・案件・在庫・請求などの「一覧と詳細」業務（例：受注台帳）
- **どの画面か**：受注の一覧（1画面に40行前後が見える高密度の表）＋ 右から出る詳細の引き出し（Drawer）
- **この画面の主アクション（1つ）**：「受注を登録」
  - 詳細の引き出しは別ページ（Drawer のダイアログページ）なので、そちらの主アクションは「保存」1つです。
- **受注につながる理由**：Excel の台帳から移りたい会社が多く、「Excel と同じくらい一覧で見えて、Excel より安全」という見せ方が商談で効くからです。26.1 では Interactive Grid に表計算ソフトからの貼り付けが加わり、移行の話がしやすくなりました。

## 2. 見た目の方向

- **情報の密度を優先**。行の高さを詰め、横線だけで区切ります（縦線と縞模様はなし）。
- 数字は**桁がそろう数字**で右寄せ。金額の列だけ少し濃い文字にします。
- 差し色は**紺（こん）**1色。選んでいる行の左に紺の線を出します。状態のバッジだけは、意味を伝えるために成功・警告などの状態色を使います。
- 表の上に、小さな**数字カード（Metric Card、26.1 の新部品）を4枚**。カードを押すとその条件で絞り込みます（「今月の受注」「出荷待ち」「入金待ち」「要対応」）。
- 状態は「色＋記号＋文字」のバッジで示します（例：● 出荷待ち、✓ 完了、! 要対応）。
- 詳細は画面を移らず、右からの引き出しで開きます。一覧の位置を失いません。

## 3. 設定（優先順：Theme Roller → Template Options → CSS変数 → 静的ファイル）

### 3-1. Theme Roller

Iris を元に「Save As」で新しいスタイルを作ります。

| 決めること | 値の例 | 対応するCSS変数（26.1のCSSで実在を確認） |
|---|---|---|
| 主色 | 紺 `#1F4E79` | `--ut-palette-primary` |
| 主色の上の文字色 | 白 | `--ut-palette-primary-contrast` |
| 画面の背景 | 薄い灰 `#F6F7F9` | `--ut-body-background-color` |
| 部品の角の丸み | 2px | `--ut-component-border-radius` |
| 部品の影 | なし（線だけ） | `--ut-component-box-shadow` |
| 区切り線の色 | `rgba(0,0,0,.08)` | `--ut-component-inner-border-color` |
| 成功色（完了） | 緑 `#2E6B3A` | `--ut-palette-success` |

- **Theme Roller 画面の項目名と、上の変数との対応は未確認**です。

### 3-2. Template Options

| 場所 | テンプレート | Template Options |
|---|---|---|
| ページ | Standard（一覧）／Drawer（詳細ページ） | 詳細ページは Page Mode：Modal Dialog、Dialog Template：Drawer。大きさは中（26.1 の CSS に `t-Drawer--md` があることを確認。**表示名は未確認**） |
| 数字カード | Metric Card（26.1 の新しいテーマコンポーネント） | 行の選択（Row Selection）を有効にして絞り込みに使う。**選べる項目の細目は未確認** |
| 数字カードの並べ方 | Flexbox Container（26.1 新規） | Flex Item Sizing：Fill Space（高さと幅をそろえる） |
| 一覧 | Interactive Grid（Standard リージョン） | リージョン：Remove Body Padding、Header は Hidden（ページ見出しと重複させない） |
| 状態のバッジ | IG 列の HTML 式で Badge のテンプレート部品を呼ぶ（26.1 でクライアント側のテンプレート部品が IG 列でも使えるようになった） | Badge の見た目は「subtle」系（26.1 の CSS に `t-Badge--subtle` を確認） |
| 数字の列 | IG 列の CSS Classes に `u-tabular-nums` | 26.1 で追加されたユーティリティクラス。CSS 内で `font-variant-numeric:tabular-nums` を確認 |
| 登録ボタン | Text ボタン | **Hot**（このページで Hot はこれ1つ） |
| 詳細ページの保存ボタン | Text ボタン | **Hot**（詳細ページで Hot はこれ1つ） |

- 表示名は過去版の UT 参照ページで確かめたもので、**26.1 での表示名は未確認**です（クラス `t-Region--noPadding` `t-Region--removeHeader` `t-Button--hot` は 26.1 の CSS で確認済み）。

### 3-3. CSS変数（Theme Roller で足りない所だけ）

置き場所：Theme Roller の Custom CSS。IG リージョンに自作クラス `lg-dense`、数字カードを並べる Flexbox Container に自作クラス `lg-metrics` を付けて、それぞれの中だけに効かせます。

```css
.lg-dense {
  --a-gv-cell-height: 28px;
  --a-gv-header-cell-height: 30px;
  --a-gv-cell-padding-y: 4px;
  --a-gv-cell-padding-x: 8px;
  --a-gv-font-size: 13px;
  --a-gv-header-background-color: var(--ut-component-toolbar-background-color);
  --a-gv-cell-border-color: var(--ut-component-inner-border-color);
  --a-gv-row-hover-background-color: var(--ut-component-highlight-background-color);
}

.lg-metrics {
  --ut-metric-card-background-color: var(--ut-component-background-color);
}
```

使った変数はすべて 26.1 の CSS（Core / Vita / Iris）の中で定義されていることを確認しました：
`--ut-palette-primary` `--ut-palette-primary-contrast` `--ut-palette-success` `--ut-body-background-color` `--ut-component-border-radius` `--ut-component-box-shadow` `--ut-component-inner-border-color` `--ut-component-toolbar-background-color` `--ut-component-highlight-background-color` `--ut-component-background-color` `--ut-metric-card-background-color` `--a-gv-cell-height` `--a-gv-header-cell-height` `--a-gv-cell-padding-y` `--a-gv-cell-padding-x` `--a-gv-font-size` `--a-gv-header-background-color` `--a-gv-cell-border-color` `--a-gv-row-hover-background-color`

- `--a-gv-*` は Interactive Grid の中で使われている変数（Oracle の変数一覧では「App UI から来た変数」と説明）。**IG の行の高さを変えたとき、仮想スクロールや固定列の高さ計算がずれないかは実機未確認**です。

### 3-4. 静的ファイル

- 使いません（選択行の左の紺の線も、IG の選択行の既定の見た目で足りるか実機で見てから判断。足りなければ数行の CSS を Theme Roller の Custom CSS に足す）。

## 4. 既存の型との違い

| 既存の型 | 違い |
|---|---|
| ミニマル | 余白を減らし、1画面の情報量を最大にする逆の方向 |
| ダークネオン | 明るい背景で長時間見ても疲れにくい事務向け |
| 原票と確認欄の横並び | 1件を見比べる型ではなく、多くの件数を並べて探す型 |
| 3Dシーン | 立体表現なし |
| RPG風 | 遊びの要素なし。Excel 台帳からの移行を意識 |
| 稟議ルート | 1件の承認の流れではなく、多くの件数を一覧で探して直す |
| シフト盤 | 人×日付の面ではなく、1行1件の台帳 |
| スマホ現場型 | スマホで数件を縦に並べる型ではなく、PCで数十行を一度に見る |

## 5. 参考にしたもの（今回ページを開いて確認）

確認日：2026-11-02。文章やコードは写していません。

- Oracle APEX 26.1 新機能一覧（IG の貼り付け、IG 列のテンプレート部品、IR 列の CSS Classes、ユーティリティクラス）
  https://docs.oracle.com/en/database/oracle/apex/26.1/htmrn/new-features.html
- Oracle ブログ：Metric Card、Flexbox Container、Drawer
  https://blogs.oracle.com/apex/universal-theme-evolves-with-the-new-iris-theme-style-smarter-templates-and-modern-ux-capabilities
- Theme Roller の使い方
  https://docs.oracle.com/en/database/oracle/apex/26.1/htmdb/using-theme-roller.html
- UT 参照アプリ：CSS変数
  https://oracleapex.com/ords/r/apex_pm/ut/css-variables
- UT 参照アプリ：Standard Reports
  https://oracleapex.com/ords/r/apex_pm/ut/standard-reports
- 24.2 の変数一覧（接頭辞 --a は App UI 由来という説明）
  https://static.oracle.com/cdn/apex/24.2.0/themes/theme_42/24.2/docs/Core.html
- 26.1 の CSS 本体（変数の実在確認）
  https://static.oracle.com/cdn/apex/26.1.0/themes/theme_42/26.1/css/Core.min.css
- IBM Carbon デザインシステム：データ表（行の高さの段階、ツールバーと行の高さをそろえる考え方を参考）
  https://carbondesignsystem.com/components/data-table/usage/

## 6. 想定する弱点

- 行を詰めるとタッチ操作（タブレット）では押しにくい。タブレット向けには `lg-dense` を外す切り替えが要る。
- 文字が小さいと年配の利用者には読みにくい。13px を下限にする。
- 数字カードを押して絞り込む動きは、IG の保存済みレポートの絞り込みと二重になり、利用者が混乱するおそれ。
- IG の変数を上書きすると、テーマ更新で変数名が変わったときに効かなくなる（変数は Oracle の変数一覧に載っているが、将来の保証はない）。
- 行の高さの変更と IG の内部計算の相性は実機未確認。

## 未確認の項目（この案）

- Theme Roller 画面の項目名と、CSS変数との対応
- Template Options の 26.1 での表示名（Drawer の大きさ・Region の項目）
- Metric Card の設定項目の細目（ブログの説明以上のこと）
- `--a-gv-cell-height` などを変えたときの IG の表示（実機未確認）
- IG 列の HTML 式で Badge を呼ぶ書き方の動作（新機能一覧に記載、実機未確認）
- IG の選択行の既定の見た目で、紺の線の代わりになるか
- IG の縦線を消す設定（`--a-gv-cell-border-color` だけで足りるか）
