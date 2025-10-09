# ポートフォリオの企画

## ゴール
awsリソース, python, flask:　これらを組み合わせて、下記の要件が満たせることを検証する。

### 機能要件

- Publicに公開できるAPIエンドを構築する。
- APIエンドポイントにCURD操作ができるメソッドを用意する。

### 詳細な要件
- プラットフォームはAWS Serverless環境とする。VPCは不要
- デプロイは、`sam_cli`を使う。
- 独自ドメイン名を利用する。`api.ysklab.work`

## 今回やらないこと
- 詳細なログ出し、ログ保存などの運用面に関する実装
- 実装したメソッドへのunittest
- セキュリティに関する詳細な実装
    - APIGatewayへのWAF適用
    - Lambdaに割り当てるIAMポリシーの最小権限

# 構成図

![構成図](./images/ysk-port-01.png)


# データモデルとサンプルデータ

# 操作方法

## 実装するメソッド
- movie_is_exists
- item_add
- item_get
- item_delete

## movie_is_exists 

```bash
curl -X GET https://target.domain.com/api 
-data '{}' 
```

## item_add

## item_get

## item_delete

# テスト

pythonコードを書いてunittestは実施しないが、デプロイ後に
Postmanから上記`curl`によるエンドテストは実施

# 参考資料

# 今後の展望
