# APEXlang UI Patterns

Oracle APEX / APEXlang 向けの、画面デザインの型をまとめたスキルです。AI のコーディングエージェントに読み込ませて使います。

A design-pattern skill for Oracle APEX / APEXlang screens, meant to be loaded by AI coding agents. The documents are written in Japanese.

> 非公式のプロジェクトです。Oracle とは関係がありません。詳しくは [NOTICE](NOTICE) を見てください。

## 何ができるか

このスキルを読み込むと、AI が次のことを安定して行えるようになります。

- 「ミニマル」「ダークネオン」「稟議ルート」「スマホ現場」などの言葉から、合うデザインの型を選ぶ
- Universal Theme の CSS 変数と Template Options を優先した、アップグレードに強い直し方をとる
- 公式のスキルで作ったアプリに、あとからデザインの意図を当てる

## 公式のスキルとの関係

| 領域 | 担当 |
|------|------|
| APEXlang の構文、生成、検証、デプロイ | 公式の [oracle/skills](https://github.com/oracle/skills)（apex/apexlang） |
| 画面の見た目と UX の型、デザインの意図 | このスキル |

両方を一緒に使うことを勧めます。

## 対象

APEX 26.1 です。26.2 は確かめていません。実機で確かめていない点は、各型の文書に「未確認」として書いてあります。

## デザインの型

| 型 | 向いている画面 | ファイル |
|----|------|----------|
| ミニマル | 余白を大きくとる業務画面、Todo | `references/patterns/minimal.md` |
| ダークネオン | ダッシュボード、在庫、グラフの多い画面 | `references/patterns/dark-neon.md` |
| レビュー | 原票と確認欄を横に並べる画面 | `references/patterns/review-layout.md` |
| 3D | Three.js などの演出を置く画面 | `references/patterns/3d-scene.md` |
| RPG | マップやチャットのあるゲーム風の画面 | `references/patterns/rpg-style.md` |
| 稟議ルート | 申請と承認の流れを見せる画面 | `references/patterns/ringi-route.md` |
| 台帳グリッド | 一覧と詳細、密度の高い表 | `references/patterns/ledger-grid.md` |
| シフト盤 | 人×日付の勤務表、人数不足の表示 | `references/patterns/shift-board.md` |
| スマホ現場 | 訪問・点検など、片手で入れる画面 | `references/patterns/mobile-field.md` |

どの型にも共通する考え方は `references/principles.md` にあります。型ごとの見本の HTML は `examples/` にあります。

## 使い方

1. このリポを、使っているエージェントのスキルの置き場にコピーします
2. エージェントは `SKILL.md` の表を見て、要件に合う型の文書を読みます

## 検査

```bash
python3 scripts/check_repo.py
```

呼び出しの表、frontmatter、見本のパス、評価の JSON を確かめます。CSS 変数名も確かめたい時は、APEX 26.1 の Universal Theme の CSS から抜き出した変数名の一覧（1行に1つ）を `--ut-vars` で渡します。

## ライセンス

- コード（`scripts/`、`examples/` の HTML・CSS・JavaScript）: MIT
- 文書（上に含まれないもの）: CC BY 4.0

詳しくは [LICENSE](LICENSE) を見てください。
