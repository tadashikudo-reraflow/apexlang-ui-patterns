---
description: "3D scene pattern using Three.js / WebGL inside APEX. Use for city exploration, stadium, or other real-time 3D visuals."
---

# 3D Scene Pattern

## When to Use

- ブラウザ上でリアルタイム3Dを描画したいとき
- 街並み、球場、パズル盤面などの演出

## Implementation Guidance

1. HTML Region（または Static Content + HTML）を用意
2. Three.js は版を固定して Static Application Files に置き、File URLs で読み込む
   - 外部CDNは顧客環境のCSPや閉域構成で止まることがあるので、既定にしない
   - 新しい版はES Modules配布が前提なので、読み込み方は採用する版の公式手順に合わせる
3. コンテナ要素を用意し、JSでシーンを初期化
4. データは PL/SQL で生成し、ページアイテムまたは Ajax で渡す
5. APEXの認証・セッションはそのまま利用する

## Skeleton

```html
<div id="scene-container" style="width:100%;height:600px;"></div>
```

```js
// 中央の静的ファイルに置く（Inlineにしない）
// three.js scene, camera, renderer
// load data from APEX items or apex.server.process
```

## Notes

- 重い処理は requestAnimationFrame で
- ページ離脱時に dispose する
- パフォーマンスとアクセシビリティに注意

## Inspiration

Qiita記事「夜景を巡る3Dの街並み」「3Dと連動する画面演出」
