---
description: "Approval route pattern. Paper background, one vermilion accent, stamp-like route. Use for expense, purchase and contract approval screens."
---

# 稟議ルート型

対象：Oracle APEX 26.1 / Universal Theme 26.1（テーマスタイルは Iris を土台）
状態：2026-11-02 採用。見本は `examples/ringi-route/mock.html`。**APEX の実機では動かして確かめていません（実機未確認）。**

---

## 1. 型の名前と用途

- **型の名前**：稟議ルート型
- **どの業務か**：経費・購買・契約などの「申請承認」業務
- **どの画面か**：承認する人が使う「承認待ちの一覧 ＋ 申請の中身 ＋ 承認ルート」の画面（1ページ）
- **この画面でやること（主アクションは1つ）**：「承認する」
  - 差し戻し・保留は脇役のボタンとして残しますが、目立つ色のボタンは「承認する」だけにします。
- **受注につながる理由**：どの会社にも承認の流れがあり、「今だれの所で止まっているか」が一目で分かる画面は説明しやすく、デモで伝わりやすいからです。

## 2. 見た目の方向

- 白い紙のような背景に、**朱色（しゅいろ）を1色だけ**差し色として使います。朱色は「承認済みの判子」と「承認する」ボタンにだけ使います。期限切れと期限が近い印に使う危険色・警告色は、差し色ではなく状態を示す色として、アイコンと文字を必ず添えます。
- 画面の中心に**承認ルートを横一列**で置きます。
  - 済んだ人：朱色の丸い判子風の印（名前と日付入り）
  - 今の人：点線の丸（「あなたの番」）
  - これからの人：灰色の丸
- 金額や日付は**桁がそろう数字**（等幅の数字）で右寄せにします。
- 左に承認待ちの一覧（期限が近い順）。期限切れは「色＋アイコン＋文字」の3つで示します（色だけに頼らない）。
- 下に、差し戻しや質問のやりとりを吹き出しで並べます。

## 3. 設定（優先順：Theme Roller → Template Options → CSS変数 → 静的ファイル）

### 3-1. Theme Roller（いちばん先にここで決める）

テーマスタイル **Iris** を元に「名前を付けて保存（Save As）」で新しいスタイルを作り、色を変えます。既定のスタイルは上書きできない仕様です（Oracle の Theme Roller 文書に記載）。

| 決めること | 値の例 | 対応するCSS変数（26.1のCSSで実在を確認） |
|---|---|---|
| 主色（ボタン・印） | 朱色 `#B7342B` | `--ut-palette-primary` |
| 主色の上の文字色 | 白 `#FFFFFF` | `--ut-palette-primary-contrast` |
| 画面の背景 | 生成り `#FAF8F5` | `--ut-body-background-color` |
| 部品の角の丸み | 4px | `--ut-component-border-radius` |
| 部品の影 | 小さい影 | `--ut-component-box-shadow`（値に `--ut-shadow-sm` を使う） |
| 危険色（期限切れ） | 濃い赤 `#A4262C` | `--ut-palette-danger` |
| 警告色（期限が近い） | 黄土色 `#8A5A00` | `--ut-palette-warning` |

- Iris で「Custom」の pillar（自分で色を選ぶ方式）が使えることは Oracle のブログで確認しました。ただし、**Theme Roller 画面上の項目名（ラベル）と、上の表のどの項目がどの変数に結び付くかは未確認**です。
- フォントは「システム標準」を選びます（Iris で Oracle Sans と切り替えられるとブログに記載。日本語はシステム標準のほうが安全と判断）。

### 3-2. Template Options（宣言的な設定）

| 場所 | テンプレート | Template Options |
|---|---|---|
| ページ | Left Side Column | 左に承認待ち一覧を置く |
| 承認待ち一覧 | Classic Report ＋ レポートテンプレート「Media List」 | リージョン側：Remove Body Padding、Body Height は Auto |
| 申請の要点 | Standard リージョン | Accent は付けない（朱色を判子とボタンだけに使うため）／Item Spacing：Slim |
| 承認ルート | List ＋ リストテンプレート「Wizard Progress」 | 26.1 の CSS に `t-WizardSteps` クラスがあることを確認。**表示名・選べる項目は未確認** |
| 明細表 | Classic Report（Standard） | Stretch Report、Row Highlighting、境界線は Horizontal Only |
| やりとり | Comments（テンプレートコンポーネント） | Style：Chat（吹き出し）。26.1 で追加された Alignment を「自分＝outbound／相手＝inbound」 |
| 経過 | Classic Report ＋ Timeline | Style：Compact |
| 承認ボタン | Text ボタン | **Hot**（このページで Hot はこれ1つだけ） |
| 差し戻し・保留 | Text ボタン | 通常（Hot にしない）。保留は 26.1 の「Type：Menu」ボタンの中に入れる |

- 表示名は過去版の UT 参照ページ（Collapsible Region、Timeline、Standard Reports など）で確かめたもので、**26.1 での表示名は未確認**です。対応するクラス（`t-Form--slimPadding`、`t-Report--stretch`、`t-Report--rowHighlight`、`t-Report--horizontalBorders`、`t-Timeline--compact`、`t-Comments--chat`、`t-Button--hot`）が 26.1 の Core.min.css にあることは確認済みです。
- 承認の中身は APEX の「承認タスク（Unified Task List／Task Details）」に載せる前提です。26.1 で「別の人に情報提供を頼める」機能が増えたことを新機能一覧で確認しました。

### 3-3. CSS変数（Theme Roller で足りない所だけ）

置き場所：Theme Roller の Custom CSS（スタイルと一緒に保存される）。テンプレート本体は触りません。

```css
/* 承認ルートだけに効かせる（クラス名は自作。.rr- で始める） */
.rr-page {
  --ut-region-header-background-color: var(--ut-body-background-color);
  --ut-report-cell-hover-background-color: var(--ut-component-highlight-background-color);
  --ut-badge-border-radius: 2px;
  --ut-comment-chat-border-radius: 6px;
  --ut-timeline-avatar-size: 24px;
}
```

使った変数はすべて 26.1 の CSS（Core / Vita / Iris）の中で定義されていることを確認しました：
`--ut-palette-primary` `--ut-palette-primary-contrast` `--ut-palette-danger` `--ut-palette-warning` `--ut-body-background-color` `--ut-component-border-radius` `--ut-component-box-shadow` `--ut-shadow-sm` `--ut-region-header-background-color` `--ut-report-cell-hover-background-color` `--ut-component-highlight-background-color` `--ut-badge-border-radius` `--ut-comment-chat-border-radius` `--ut-timeline-avatar-size`

### 3-4. 静的ファイル（最後の手段）

- 判子風の丸印（二重線の円、文字の縦書き風配置）だけは変数では作れないため、アプリの静的ファイル `ringi-route.css`（20行ほど）に入れます。
- 中身は自作クラス `.rr-stamp` だけ。UT のクラスを上書きしません。

## 4. 既存の型との違い

| 既存の型 | 違い |
|---|---|
| ミニマル | 余白より「流れ（ルート）」が主役。差し色の朱色に意味（承認済み）を持たせる |
| ダークネオン | 明るい紙の背景。光る表現は使わない |
| 原票と確認欄の横並び | 原票の画像と入力欄を見比べる型ではなく、「誰の番か」と「決めること1つ」に絞る型 |
| 3Dシーン | 立体表現なし。標準部品と小さな静的 CSS で組める |
| RPG風 | ゲームらしさなし。日本の稟議の判子という実務の比喩を使う |
| 台帳グリッド | 多くの件数を探す表ではなく、1件の「誰の番か」を見せる |
| シフト盤 | 予定を組む面ではなく、決まった順番を1人ずつ進める流れ |
| スマホ現場型 | 現場で作業結果を入れる型ではなく、机で中身を読んで判断する型 |

## 5. 参考にしたもの（今回ページを開いて確認）

確認日：2026-11-02。文章やコードは写していません。

- Oracle APEX 26.1 新機能一覧（UT の強化、承認タスクの強化、ボタンの Type：Menu）
  https://docs.oracle.com/en/database/oracle/apex/26.1/htmrn/new-features.html
- Oracle ブログ：Iris スタイル、Comments の inbound/outbound、Drawer 上下
  https://blogs.oracle.com/apex/universal-theme-evolves-with-the-new-iris-theme-style-smarter-templates-and-modern-ux-capabilities
- Theme Roller の使い方（Save As、Custom CSS、Iris と Vita の互換）
  https://docs.oracle.com/en/database/oracle/apex/26.1/htmdb/using-theme-roller.html
- UT 参照アプリ：CSS変数
  https://oracleapex.com/ords/r/apex_pm/ut/css-variables
- UT 参照アプリ：Timeline（列名と使い方）
  https://oracleapex.com/ords/r/apex_pm/ut/timeline-reports
- UT 参照アプリ：Comments Report
  https://oracleapex.com/ords/r/apex_pm/ut/comments-report
- UT 参照アプリ：ページテンプレート（Left Side Column など）
  https://oracleapex.com/ords/r/apex_pm/ut/pages
- 26.1 の CSS 本体（変数の実在確認に使用）
  https://static.oracle.com/cdn/apex/26.1.0/themes/theme_42/26.1/css/Core.min.css
  https://static.oracle.com/cdn/apex/26.1.0/themes/theme_42/26.1/css/Iris.min.css
- W3C：色だけで情報を伝えない（WCAG 1.4.1）
  https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html

## 6. 想定する弱点

- 承認ルートが6人を超えると横一列に収まらず、スマホでは縦に折り返す必要がある（折り返しの見え方は実機未確認）。
- 判子風の印は日本向け。海外の取引先には意味が伝わりにくい。
- 朱色が `--ut-palette-danger`（赤）と近く、「承認済み」と「エラー」を取り違えるおそれ。危険色はより暗い赤にし、必ずアイコンと文字を添える。
- 「Wizard Progress」リストを承認ルートに流用するのは本来の用途と違う。テーマ更新で見た目が変わる可能性がある（実機未確認）。
- 静的ファイルを1つ持つので、テーマ更新時に見た目の確認が必要。

## 未確認の項目（この案）

- Theme Roller 画面の項目名と、CSS変数との対応
- Template Options の 26.1 での表示名（クラスの存在は確認済み）
- 「Wizard Progress」リストテンプレートの 26.1 での選択肢
- Comments の Alignment を列の値で切り替える動作（ブログに記載あり、実機未確認）
- 画面全体の見え方・スマホ表示（実機未確認）
- 承認タスクの Unified Task List／Task Details を、一覧と申請の中身とルートを並べた1ページの形にできるか
