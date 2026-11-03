# CODESTYLE

- 文書は日本語。識別子・ファイル名・frontmatter の description は英語。
- パターンのファイル名は小文字ケバブケース。frontmatter に `description` を持つ。
- CSS変数は、APEX 26.1 の Universal Theme で定義されているものだけを使う。`scripts/check_repo.py` に `--ut-vars` で変数の一覧を渡すと確かめられる。
- Pythonは標準ライブラリのみ。エラーは1行で理由を出し、exit 1 にする。
