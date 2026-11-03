---
description: "Shift board pattern. Person-by-date board with labelled chips and staffing warnings. Use for weekly or monthly roster screens."
---

# シフト盤型

対象：Oracle APEX 26.1 / Universal Theme 26.1（テーマスタイルは Iris を土台）
状態：2026-11-02 採用。見本は `examples/shift-board/mock.html`。**APEX の実機では動かして確かめていません（実機未確認）。**

---

## 1. 型の名前と用途

- **型の名前**：シフト盤型
- **どの業務か**：店舗・介護施設・コールセンター・工場などの「勤務表（シフト表）」作り
- **どの画面か**：管理者が1週間（または1か月）の勤務表を組む画面。縦に人、横に日付。
- **この画面の主アクション（1つ）**：「この週の勤務表を確定」（1か月表示では「この月の勤務表を確定」）
- **受注につながる理由**：勤務表を Excel で作っている現場は多く、「人が足りない日が自動で赤くなる」「連勤や夜勤明けの無理が警告される」は、現場の管理者に一目で価値が伝わるからです。

## 2. 見た目の方向

- **ホワイトボードにマグネットを貼る**イメージ。明るい灰色の盤面に、丸みのある小さな札（早・日・遅・夜・休）を並べます。
- 札は**色＋1文字＋模様**の3つで見分けます。夜勤は濃い色、休みは白地に点線枠など、色が分からなくても区別できるようにします（WCAG 1.4.1 の考え方）。
- 一番下の行に**「必要人数との差」**。足りない日は「▲−1」のように記号と数字で示し、赤系の地にします。
- 左端に名前と週の合計時間（固定列）。右側の列に「選んだ札の編集」と「警告の一覧」（6連勤、夜勤明けの日勤、週40時間超え）。
- 札の並ぶ盤面が主役なので、ヘッダーや枠は控えめにします。

## 3. 設定（優先順：Theme Roller → Template Options → CSS変数 → 静的ファイル）

### 3-1. Theme Roller

Iris を元に「Save As」で新しいスタイルを作ります。

| 決めること | 値の例 | 対応するCSS変数（26.1のCSSで実在を確認） |
|---|---|---|
| 主色 | 青緑 `#0F6E6E` | `--ut-palette-primary` |
| 主色の上の文字色 | 白 | `--ut-palette-primary-contrast` |
| 盤面（画面の背景） | 明るい灰 `#EEF0EF` | `--ut-body-background-color` |
| 部品の角の丸み | 8px | `--ut-component-border-radius` |
| 危険色（人数不足） | `#A4262C` | `--ut-palette-danger` |
| 警告色（連勤など） | `#8A5A00` | `--ut-palette-warning` |
| 右側の列の幅 | 320px | `--ut-body-actions-width` |

- 札の色は UT の色番号（`--u-color-1` 〜 `--u-color-45`、各 `-contrast` 付き）から選び、Theme Roller 側で色を変えられるようにします（色番号の変数は UT 参照アプリの CSS変数ページと 26.1 の CSS で確認）。
- **Theme Roller 画面の項目名と、上の変数との対応、どの色番号を Theme Roller で変えられるかは未確認**です。

### 3-2. Template Options

| 場所 | テンプレート | Template Options |
|---|---|---|
| ページ | Right Side Column | 右側の列に編集欄と警告。右側の列は折りたためる（UT 参照アプリの説明による。26.1 の実機では未確認） |
| 盤面 | Interactive Grid（SQL の PIVOT で「人×日付」の形にする） | リージョン：Remove Body Padding、Header は Hidden |
| 左端の固定列 | IG の列の固定（Freeze） | 名前と週の合計時間の列を固定する。**設定名と動作は未確認** |
| 札 | IG 列の HTML 式からテンプレート部品を呼ぶ（26.1 で IG 列でもクライアント側のテンプレート部品が使えるようになった） | 札の色は `u-color-N` クラスで付ける（26.1 の CSS に `u-color-29` などを確認） |
| まとめての入力 | IG の貼り付け（26.1 新機能：範囲の切り取り・貼り付け、表計算ソフトからのドラッグ） | 設定方法の細目は**未確認** |
| 人数の差の行 | IG の集計行、または別の Classic Report を盤面の下にそろえて置く | 26.1 の CSS に `--a-gv-grandtotal-background-color` があることを確認。**集計行での表示方法は未確認** |
| 警告の一覧 | Classic Report ＋ Media List テンプレート | 種類ごとに Alert 風のアイコン |
| 確定ボタン | Text ボタン（右側の列の上） | **Hot**（このページで Hot はこれ1つ） |
| 編集欄 | Standard リージョン | Item Spacing：Slim |

- 表示名は過去版の UT 参照ページで確かめたもので、**26.1 での表示名は未確認**です（クラス `t-Region--noPadding` `t-Region--removeHeader` `t-Form--slimPadding` `t-Button--hot` `t-MediaList` は 26.1 の CSS で確認済み）。

### 3-3. CSS変数（Theme Roller で足りない所だけ）

置き場所：Theme Roller の Custom CSS。IG リージョンに自作クラス `sb-board` を付けて、その中だけに効かせます。

```css
.sb-board {
  --a-gv-cell-height: 40px;
  --a-gv-cell-padding-x: 4px;
  --a-gv-cell-border-color: transparent;
  --a-gv-background-color: var(--ut-body-background-color);
  --a-gv-header-background-color: var(--ut-body-background-color);
  --a-gv-grandtotal-background-color: var(--ut-component-background-color);
  --a-gv-row-hover-background-color: var(--ut-component-highlight-background-color);
  --ut-badge-border-radius: 6px;
}
```

使った変数はすべて 26.1 の CSS（Core / Vita / Iris）の中で定義されていることを確認しました：
`--ut-palette-primary` `--ut-palette-primary-contrast` `--ut-palette-danger` `--ut-palette-warning` `--ut-body-background-color` `--ut-component-border-radius` `--ut-body-actions-width` `--u-color-1` `--u-color-45` `--ut-component-background-color` `--ut-component-highlight-background-color` `--ut-badge-border-radius` `--a-gv-cell-height` `--a-gv-cell-padding-x` `--a-gv-cell-border-color` `--a-gv-background-color` `--a-gv-header-background-color` `--a-gv-grandtotal-background-color` `--a-gv-row-hover-background-color`

### 3-4. 静的ファイル（最後の手段）

- 札の模様（夜勤の斜線、休みの点線枠）は変数では作れないため、アプリの静的ファイル `shift-board.css`（30行ほど）に入れます。
- 中身は自作クラス `.sb-chip`、`.sb-chip--night` などだけ。UT のクラスは上書きしません。購読しているテンプレートも編集しません。

## 4. 既存の型との違い

| 既存の型 | 違い |
|---|---|
| ミニマル | 色を「意味の記号」として積極的に使う |
| ダークネオン | 明るい盤面。札は落ち着いた中間色 |
| 原票と確認欄の横並び | 1件の見比べではなく、人×日付の面で全体のバランスを見る |
| 3Dシーン | 平面。ホワイトボードの比喩だけ借りる |
| RPG風 | ゲーム要素なし。ただし札を置いていく手ざわりは、遊び心を少しだけ残す |
| 台帳グリッド | 1行1件の表ではなく、人×日付の面で人数の過不足を見る |
| 稟議ルート | 1件の流れではなく、週や月の全体を一度に組む |
| スマホ現場型 | 組まれた予定を現場で片付ける側ではなく、管理者が予定を組む側 |

## 5. 参考にしたもの（今回ページを開いて確認）

確認日：2026-11-02。文章やコードは写していません。

- Oracle APEX 26.1 新機能一覧（IG の切り取り・貼り付け、IG 列のテンプレート部品、Drawer の上下）
  https://docs.oracle.com/en/database/oracle/apex/26.1/htmrn/new-features.html
- Oracle ブログ：Iris、Flexbox Container、Drawer
  https://blogs.oracle.com/apex/universal-theme-evolves-with-the-new-iris-theme-style-smarter-templates-and-modern-ux-capabilities
- Theme Roller の使い方
  https://docs.oracle.com/en/database/oracle/apex/26.1/htmdb/using-theme-roller.html
- UT 参照アプリ：CSS変数（`--u-color-N` の一覧）
  https://oracleapex.com/ords/r/apex_pm/ut/css-variables
- UT 参照アプリ：ページテンプレート（Right Side Column）
  https://oracleapex.com/ords/r/apex_pm/ut/pages
- 26.1 の CSS 本体（変数の実在確認）
  https://static.oracle.com/cdn/apex/26.1.0/themes/theme_42/26.1/css/Core.min.css
- W3C：色だけで情報を伝えない（WCAG 1.4.1。色と模様を併用する考え方）
  https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html

## 6. 想定する弱点

- 1か月表示（31列）だと横に長く、ノートPCでは横スクロールが必要。
- IG を PIVOT で「人×日付」にすると、日付の列が週ごとに変わるため、列の定義を動的にする工夫が要る（実装の手間が大きい。実機未確認）。
- 札のドラッグ＆ドロップは IG の標準にはない。26.1 の貼り付けで代わりにするが、「マグネットを動かす」感覚には届かない。
- 夜勤・連勤のルールは業種や会社で違うため、警告の条件は毎回作り直しになる。
- 静的ファイルを1つ持つので、テーマ更新時に見た目の確認が必要。

## 未確認の項目（この案）

- Theme Roller 画面の項目名と、CSS変数との対応、`--u-color-N` のうち Theme Roller で変えられる範囲
- Template Options の 26.1 での表示名
- IG の貼り付け機能の設定方法の細目
- IG の集計行に `--a-gv-grandtotal-background-color` が効くか
- `--a-gv-cell-height` を 40px にしたときの IG の表示（実機未確認）
- PIVOT で日付の列を週ごとに変える作り方
- 26.1 で右側の列（Right Side Column）を折りたためるか
- 左端の列の固定の設定名と動作
