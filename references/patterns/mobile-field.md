---
description: "Mobile field pattern. Vertical job list with a bottom drawer for one-handed result entry. Use for phone screens used on site, visits and inspections."
---

# スマホ現場型

対象：Oracle APEX 26.1 / Universal Theme 26.1（テーマスタイルは Iris を土台）
状態：2026-11-02 採用。見本は `examples/mobile-field/mock.html`。**一覧とパネルの基本は APEX 26.1.5 で動かして確かめました（9 章）。実際のスマホでは未確認です。**

---

## 1. 型の名前と用途

**型の名前：スマホ現場型**

- **一言で**：現場の人が片手でスマホを持ち、今日の作業を上から順に確かめ、終わったらその場で結果を入れるための型です。
- **向いている業務**：
  - 設備の点検や修理の訪問
  - 工事現場の日々の確認
  - 配送・回収の立ち寄り記録
  - 介護や営業の訪問記録
- **画面は2つだけ**です。
  1. **今日の作業の一覧**（縦に並ぶ。状態は色と文字でひと目で分かる）
  2. **結果を入れる下から出るパネル**（一覧の行か、下の「次の作業を記録」ボタンから開く）
- **向かない業務**：一度にたくさんの行を見比べる仕事や、PCで長い書類を入れる仕事。こうした仕事には台帳グリッドや原票と確認欄の横並びを使います。

## 2. 見た目の方向

- **屋外でも読める**：
  - 背景は明るい灰色、カードは白です。
  - 文字は濃い色にして、強いコントラストを優先します。
  - 飾りの影やグラデーションは使いません。
- **状態は色だけに頼らない**：完了・作業中・未着手・要再訪を、次の3つで示します。
  - 小さな札（色＋文字）
  - 行の左端の色の帯
  - 札の中の点
- **時刻を先に読ませる**：
  - 各行の一番上に時刻を置きます（Content Row の overline）。
  - その下に現場名を大きく、作業内容を小さく置きます。
- **親指の届く下半分に大事な操作を集める**：
  - 一覧の画面では、下に固定した「次の作業を記録」が主ボタンです。
  - パネルの中では、下に固定した「結果を登録」が主ボタンです。
- **主ボタンは1画面に1つ**：
  - 一覧の主ボタンは「次の作業を記録」だけです。
  - パネルの主ボタンは「結果を登録」だけです。
  - 絞り込み・写真の追加・閉じるは、どれも控えめなボタンにします。
- **押せる場所は 44×44px 以上**にします（見本の測り方と結果は 9 章）。
- **入力は「選ぶ」を先に**：結果は3択の大きなボタンにして、キーボードを開かなくても登録できるようにします。メモは任意です。

## 3. Theme Roller ／ Template Options ／ CSS変数

決める順番は **Theme Roller → Template Options → CSS変数 → 静的ファイルのCSS** です。購読しているテンプレートは直接書き換えません。

### 3-1. Theme Roller

- テーマスタイル：**Iris**（26.1 の新規アプリの既定）
- 主の色（Primary）：濃い青。白い文字とのコントラストを高めに取ります。
- Success・Warning・Danger の色：完了＝緑、作業中＝黄土、要再訪＝赤。屋外でも見分けやすい濃さにします。
- 文字：システムフォントのまま（Iris は Oracle Sans も選べますが、日本語の見え方は実機未確認）

### 3-2. Template Options（標準の設定だけで決める部分）

| 対象 | 設定 | 26.1 の CSS で確かめたクラス |
|---|---|---|
| 結果入力ページ（Modal Dialog、Dialog Template＝Drawer） | Position＝**Bottom** | `t-Drawer--pullOutBottom`（APEXlang 上は `js-dialog-class-t-Drawer--pullOutBottom`） |
| 同上 | Size＝**Medium**（Large は 375×812 で高さ約 731px になり、画面を覆った。9 章） | `t-Drawer--md` |
| 主ボタン（両画面） | Hot、Size＝**Large**、Width＝**Stretch**（Large だけでは高さ 40px。44px にする方法は 3-3） | `t-Button--hot`、`t-Button--large`、`t-Button--stretch`。`t-Button--xlarge` は SQLcl 26.3 の検証で Text ボタンの Template Option として無効だった |
| 主ボタンを入れる Buttons Container（一覧の画面） | 狭い画面で下に固定する設定 | `t-ButtonRegion--stickToBottom`（CSS では幅 639px 以下が対象。APEX 26.1.5 の 375px で下に固定されることを確認） |
| 結果の3択（Radio Group） | ピル型ボタンで表示 | `t-Form-fieldContainer--radioButtonGroup` |
| 今日の作業の一覧（Content Row） | 狭い画面で縦に積む | `t-ContentRow--stackMobile` |

Template Options の画面上の正確な表示名は実機未確認です。上の表は、26.1 の Core.min.css にあるクラス名から判断しています。

### 3-3. CSS変数（実在を確かめたものだけ）

すべて、26.1 の CSS ファイルで実在を確かめました（`static.oracle.com/cdn/apex/26.1.0/themes/theme_42/26.1/css/Core.min.css`）。
- 「宣言あり」は、CSS の中で値が決められている変数です。
- 「参照のみ」は、CSS が `var()` で読みにいくだけの差し込み口です。値を入れれば効くはずですが、効き方は未確認です（10 章）。

| 変数 | 用途 | 見本の値の目安 | 26.1 での確認 |
|---|---|---|---|
| `--ut-pillbutton-padding-y` | 3択ボタンの上下の余白 | 1rem | 宣言あり |
| `--ut-pillbutton-line-height` | 3択ボタンの行の高さ | 1.25rem | 宣言あり |
| `--ut-pillbutton-font-size` | 3択ボタンの文字 | 0.9375rem | 宣言あり |
| `--ut-cr-overline-font-size` | 一覧の時刻の大きさ | 1rem | 参照のみ |
| `--ut-cr-overline-font-weight` | 一覧の時刻の太さ | 700 | 参照のみ |
| `--ut-cr-title-font-size` | 一覧の現場名の大きさ | 1.0625rem | 宣言あり |
| `--ut-cr-desc-font-size` | 一覧の作業内容の大きさ | 0.875rem | 参照のみ |
| `--ut-dialog-pullout-max-block-size` | 下から出るパネルの高さの上限 | 88dvh（既定は 90dvh） | 参照のみ |
| `--ut-xs-field-input-font-size` | スマホ幅での入力欄の文字 | 1rem（iOS の自動拡大を避ける。効き方は実機未確認） | 宣言あり |
| `--ut-palette-success`／`--ut-palette-warning`／`--ut-palette-danger` | 状態の色（Theme Roller で決めた値をそのまま使う） | — | 宣言あり |
| `--ut-focus-outline-color` | キーボード操作時の枠の色 | 主の色 | 宣言あり |

- CSS の値から計算すると、3択ボタンの既定の高さは、余白 0.25rem×2＋行 1rem で約 24px です。上の3つの変数で約 52px に上げます（実機未確認）。
- Large は実測でも 40px でした。`--a-button-padding-y` を .875rem にすると 44px になります。

### 3-4. 静的ファイルのCSS（最後の手段。数行だけ）

- **行の左端の状態の色の帯**：Content Row の行に状態ごとのクラスを付けて、左の線を色分けします。クラスの付け方は 7 章の「未確認」を見てください。
- **パネルの上の角を丸くする（任意）**：26.1 の下から出る Drawer は、角が `border-radius:0!important` で固定されています。丸くするには `!important` を上書きする必要があるので、**やらないのが基本**です。見本では見た目の参考として丸くしています。

## 4. 既存8型との違い

| 既存の型 | スマホ現場型との違い |
|---|---|
| ミニマル | ミニマルはPCの広い画面で余白を楽しむ型です。スマホ現場型は狭い画面に必要なものだけ詰め、屋外で読める濃さを優先します。 |
| ダークネオン | ダークネオンは暗い背景で光る色を見せます。スマホ現場型は日差しの下で読むことを前提に、明るい背景を使います。 |
| 原票と確認欄の横並び | 横並びはPCで書類を見比べる型です。スマホ現場型は横に並べず、一覧→パネルの縦の流れだけにします。 |
| 3Dシーン | 3Dシーンは表現を見せる型です。スマホ現場型は回線が弱い現場でも軽く動くことを優先し、絵や動きは使いません。 |
| RPG風 | RPG風は楽しさで続けてもらう型です。スマホ現場型は数秒で入力を終えることだけを目標にします。 |
| 稟議ルート | 稟議ルートは承認の順番を見せる型です。スマホ現場型の結果は作業の記録で、承認の流れは持ちません。 |
| 台帳グリッド | 台帳グリッドはPCで多くの行と列を一度に見る型です。スマホ現場型は1人分の今日の作業（数件〜十数件）だけを縦に並べます。 |
| シフト盤 | シフト盤は人×日の表で予定を組む型です。スマホ現場型は組まれた予定を、現場で1件ずつ片付ける側の画面です。 |

**まとめ**：既存の8つの型は、どれもPCの画面を主な前提にしています。スマホ現場型は、片手・屋外・短い時間という条件で作る、初めての型になります。

## 5. 参考URL（今回開いて表示を確かめたもの。確認日 2026-11-02 JST）

1. Oracle 公式ブログ「Universal Theme Evolves with the New Iris Theme Style, Smarter Templates, and Modern UX Capabilities」（2026-07-20）
   https://blogs.oracle.com/apex/universal-theme-evolves-with-the-new-iris-theme-style-smarter-templates-and-modern-ux-capabilities
   - 26.1 で Drawer が上と下からも出せるようになったこと、その設定の場所。
2. Oracle APEX 26.1 Release Notes「New Features」（公式ドキュメント。更新日 不明）
   https://docs.oracle.com/en/database/oracle/apex/26.1/htmrn/new-features.html
   - 上下の Drawer、Inline Drawer の Footer、tabular numbers・flex の utility クラス、ボタンの「Show as Disabled」、「Show Success Message」動的アクションが 26.1 の機能であること。
3. Tomas Kucharzyk「Oracle APEX 26.1 Finally Gets Top and Bottom Drawers」（コミュニティのブログ。公開日 不明）
   https://kuchatom.hashnode.dev/oracle-apex-26-1-finally-gets-top-and-bottom-drawers
   - Template Options の Position で下を選べること、Size の選び方、Inline Drawer でも同じ設定ができること。
4. 日日是Oracle APEX「ドロワーを画面下から表示する - Codexを使って」（2026-06-17）
   http://apexugj.blogspot.com/2026/06/apex261-universal-theme-drawer-position.html
   - APEXlang では `js-dialog-class-t-Drawer--pullOutBottom` という値になること。
5. 合同会社playpark「モバイルシフト管理アプリ」（2026-02-24。自社製品の紹介記事）
   https://www.playpark.co.jp/blog/shift-bud-mobile-ux
   - 狭い画面では表を縮めずに縦の一覧へ切り替え、編集は下から出るパネルで親指だけで行う、という考え方。記事中の数字は会社の発表です。
6. Oracle APEX 26.1 Universal Theme の CSS
   https://static.oracle.com/cdn/apex/26.1.0/themes/theme_42/26.1/css/Core.min.css
   - 3 章のクラス名と変数の確認に使いました。

文章やコードは写していません。考え方と設定の場所だけを参考にしました。

## 6. 想定する弱点

- **下から引き下げて閉じる操作が確認できていない**：
  - 指で下に引いて閉じる動きは、26.1 の資料と CSS では見つかっていません（実機未確認）。この型では、閉じる手段を右上の「×」と Esc キーとして考えます。
  - 「×」は親指から遠い右上にあります。
- **電波が弱い現場**：APEX はページを開くたびにサーバーとやり取りします。電波のない場所での入力（オフライン）は、標準の部品ではできません。
- **件数が多い日**：
  - 1日 20 件を超えると縦に長くなり、「次の作業」を探しにくくなります。
  - そのため「未完了」の絞り込みを最初から選んだ状態にする案もあります。
- **写真**：Image Upload でカメラを起動できるか、写真の大きさをどう抑えるかは、端末ごとに違います（実機未確認）。
- **角を丸くしたい、という要望**：Drawer の角は `!important` で固定されているため、丸くすると更新のたびに見た目が崩れる心配があります。
- **手袋や濡れた手**：44px は最低ラインです。現場によっては 56px 以上が欲しくなります。

## 7. APEX 26.1 の標準部品でどこまで作れるか

印の意味：
- **標準**：設定だけでできる
- **CSS変数**：3-3 の変数の上書きが必要
- **CSS**：静的ファイルのCSSが必要
- **表示切替**：リージョンや項目の表示・非表示（動的アクションや条件）が必要
- **未確認**：実機で確かめていない

### 7-1. 今日の作業の縦一覧（一覧の画面）

| 部分 | 作り方 | 印 |
|---|---|---|
| 一覧の本体 | Content Row リージョン。上の小さい行（overline）＝時刻、タイトル＝現場名、説明＝作業内容、Badge＝状態 | 標準 |
| 行全体を押してパネルを開く | Content Row の全体リンク（APEXlang では `action` の `position: fullRowLink`）で、結果入力ページ（Drawer）へ移動 | 標準（APEX 26.1.5 で確認） |
| 狭い画面で縦に積む | Template Options の Stack Mobile | 標準 |
| 時刻を太く大きく | `--ut-cr-overline-font-size`、`--ut-cr-overline-font-weight` | CSS変数 |
| 状態の札の色（完了＝緑など） | Badge の value と state に列を割り当て、SQL で `success` などを返す | 標準（APEX 26.1.5 で確認） |
| 行の左端の色の帯 | 状態ごとのクラスを行に付けて、静的ファイルで左の線の色を決める | CSS（行にクラスを付ける方法は未確認） |
| 時刻の数字をそろえる | 26.1 の `u-tabular-nums` を付ける | 標準 |
| 上の進み具合（2/6 件と棒） | 件数は SQL で出せる。棒の見た目は Metric Card では出せないため、文字だけにするか、小さな CSS を足す | 文字だけなら標準／棒は CSS |
| 絞り込み（すべて・未完了・完了） | Radio Group をピル型で表示し、変わったら一覧を Refresh（Page Items to Submit） | 標準＋**表示切替**（一覧の再読み込み）。高さ 44px は CSS変数 |
| 下に固定した「次の作業を記録」 | Buttons Container を 639px 以下で下に固定する Template Option。ボタンは Hot＋Large＋Stretch | 標準（固定するときの動きは実機未確認） |
| 全部終わった日の「次の作業」 | ボタンの Server-side Condition と、26.1 の **Show as Disabled** で押せない形で残す | 標準＋**表示切替**（条件） |
| 0件の日の文言 | Content Row の「データがないとき」の文言 | 標準 |

### 7-2. 下から出る結果入力パネル（結果入力ページ）

| 部分 | 作り方 | 印 |
|---|---|---|
| 下から出るパネル | 別ページを Modal Dialog にし、Dialog Template＝Drawer、Position＝Bottom、Size＝Large | 標準 |
| パネルの高さの上限 | `--ut-dialog-pullout-max-block-size`（参照のみの差し込み口。既定 90dvh） | CSS変数（効き方は実機未確認） |
| 見出し（現場名・時刻）と「×」 | Drawer のタイトルにページ項目を差し込む。「×」は Drawer の標準の閉じるボタン | 標準（「×」が 44px 以上あるかは実機未確認） |
| 結果の3択（完了・一部完了・要再訪） | Radio Group をピル型で表示、Stretch Inputs で横いっぱい | 標準＋CSS変数（高さを 44px 以上に） |
| 「要再訪」のときだけ「再訪の理由」を出す | 動的アクションの Show／Hide（3択の値が「要再訪」のとき）。サーバー側でも必須チェックをする | **表示切替**＋標準 |
| 作業時間（開始・終了） | Date Picker の時刻だけの表示、または Text Field（type が time になるかは未確認） | 標準（時刻だけの入力の形は実機未確認） |
| 写真の追加 | Image Upload 項目（26.1 で貼り付けにも対応） | 標準（スマホでカメラを直接開けるかは実機未確認） |
| メモ | Textarea | 標準 |
| 下に固定した「結果を登録」 | Drawer の下の Footer（Dialog Footer の位置）に置いた Buttons Container。ボタンは Hot＋Large＋Stretch | 標準（スクロールしても下に残るかは実機未確認） |
| 登録後に閉じて一覧を更新 | ページ処理で保存して Close Dialog。一覧の画面の Dialog Closed 動的アクションで Content Row を Refresh し、26.1 の **Show Success Message** で「登録しました」を出す | 標準＋**表示切替**（一覧の再読み込み） |
| パネルの上の角丸 | `border-radius:0!important` の上書き | CSS（勧めない） |

### 7-3. まとめ

- **標準で作れる部分**：一覧、行全体のリンク、札の色、下から出るパネル、3択、メモ、一覧の下に固定した主ボタン、登録後の一覧の更新は、APEX 26.1.5 で動きました（9 章）。写真と、パネルの Footer の固定は試していません。実際のスマホでは、どれも未確認です。
- **CSS変数で直す部分**：3択ボタンの高さと主ボタンの高さ（44px 以上にするため）、時刻の文字の大きさと太さ、パネルの高さの上限。
- **静的ファイルのCSSが要る部分**：行の左端の色の帯と、9 章の幅と 44px の調整（アプリの静的ファイルに置く CSS）です。進み具合を棒で出す場合も必要です。角丸は勧めません。
- **表示切替が要る部分**：
  - 「要再訪」のときの理由欄（Show／Hide）
  - 絞り込みと登録後の一覧の再読み込み（Refresh）
  - 全部終わった日の主ボタン（条件＋Show as Disabled）

## 8. 見本について

- `examples/mobile-field/mock.html` は1ファイルで完結し、保存はしません。URL の最後に `#drawer` を付けると、パネルが開いた状態で始まります。
- 下のボタンは、まだ記録していない最初の作業を指します。要再訪や一部完了で記録した作業には戻りません。
- 見本はパネルの上の角を丸くしていますが、APEX では丸くしないのが基本です（3-4）。
- 見本の変数名（`--m-*`）は見本用で、APEX の変数ではありません。

## 9. 375px 幅と 44px の確認（見本のみ）

幅375px・高さ812px・タッチありのヘッドレス Chrome で、一覧、パネル、理由欄を出した状態を測りました。3つとも横スクロールは出ず、操作する部分は 44×44px 以上です。入力欄の上の見出し文字は押す場所ではないので数に入れていません。APEX で作った画面が同じ寸法になるかは**実機未確認**です。

### APEX 26.1.5 での確認（2026-11-03）

試作アプリを APEX 26.1.5 の環境（Oracle の ADB Free のコンテナ）に取り込み、幅375px・高さ812px・タッチありのヘッドレス Chromium で動かしました。実際のスマホではまだ試していません。

**動いたこと**

- `apex validate` と `apex import` が DB 接続ありで通る
- 横スクロールは出ない（scrollWidth 375）
- Content Row の全体リンクで行を押すと、下から出るパネルが開く（Bottom の Drawer。高さ約 731px で、画面の 90% が上限）
- Badge の色と文字を列の値で変えられる（`plugin-badge` の value と state）
- 下のボタンは画面の下に固定される。押すと、記録していない最初の作業を開く
- 要再訪で理由が空の時は検証で止まる。保存するとパネルが閉じ、一覧の札が変わる

**最初の確認で見つかり、直したこと**

| 直す前 | 直した方法 | 直した後 |
|---|---|---|
| 主ボタンが高さ 40px で右に寄る | `--a-button-padding-y` を .875rem にし、`t-ButtonRegion-wrap` を block に変える | 343×44px |
| 3択が幅 53px で折り返す | `--ut-pillbutton-*` で高さを上げ、ラジオの親を幅いっぱいの flex にする（各項目の 33.3% はテーマの規則） | 114×52px |
| 検証エラーの通知が3択に重なる | 2つの検証を `displayLocation: inlineWithField` にし、`error` に項目を結びつける。必須の検証は `valueRequired` をやめて自前で書く | 入力欄のすぐ下に出て、重ならない |
| 通知の見出しと必須の文言が英語 | 上と同じ。`primaryLanguage: ja` も設定 | この2つの検証では英語が出ない |
| パネルが画面いっぱいに広がる | `t-Drawer--lg` を `t-Drawer--md` に変える | 高さ 480px。パネル内にスクロールなし |
| 「一部完了」を選ぶと札が「作業中」になる | `doing` で `saved='Y'` の行は「一部完了」と出す | 札が選んだ言葉と揃う |
| ヘッダーの2つのメニューと「×」が小さい | `min-block-size` と `min-inline-size` を 44px にする | 一覧もパネルも 44px 未満の操作部品なし |

CSS は `shared-components/static-files/css/mobile-field.css` にまとめ、ページ 1 と 2 の `css` で読みます。

**分かった注意点**

- 通知は `position: fixed` で、パネルの中では上の入力に重なります。理由欄や3択の検証は `inlineWithField` にします。
- 検証以外の通知（サーバーのエラーなど）は、今も通知の形で出ます。ADB Free の `primaryLanguage: ja` だけでは APEX 既定の文言は日本語になりませんでした。
- apex スキルの `compiler-truth audit` は5件で通りません（2026-11-03）。`plugin-badge` の `label` と `state` を Region の項目として読み、`plsqlFunctionBody` の中の `return` も項目として読んでいます。SQLcl 26.3 の `apex validate` は通り、取り込んだ画面でも札が動くので、アプリの誤りではなく監査の読み違いと判断しました。残る2件は、スキルの `component-attributes.json` が 26.1.0 のままで、SQLcl 26.3 の記録と合わないという指摘です。

**まだ試していないこと**：作業時間、写真、絞り込み、進み具合、行の左端の色の帯、理由欄の出し分け（試作に入れていません）。

## 10. 未確認の一覧

- 下から引いて閉じる操作の有無
- Template Options の画面上の正確な表示名（Position、Size、下に固定する設定など。クラス名は 26.1 の CSS で確認済み）
- Drawer の Footer に置いたボタンが、パネル内をスクロールしても下に残るか
- Content Row の行に状態ごとのクラスを付けられるか
- 「参照のみ」の変数（`--ut-cr-overline-font-size`、`--ut-cr-overline-font-weight`、`--ut-cr-desc-font-size`、`--ut-dialog-pullout-max-block-size`）を上書きしたときの効き方
- `--ut-xs-field-input-font-size` で iOS の自動拡大を避けられるか
- 作業時間の「時刻だけ」の入力の形（Date Picker の設定、または Text Field）
- Image Upload でスマホのカメラを直接開けるか、写真の大きさをどう抑えるか
- Iris で Oracle Sans を選んだときの日本語の見え方
- APEX 26.1.5 のヘッドレス Chromium で測った 375px／44px の結果が、実際のスマホでも同じになるか
