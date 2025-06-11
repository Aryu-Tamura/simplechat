import json
import os
import urllib.request # 標準ライブラリurllib.requestをインポートします

# 環境変数からColabのAPI URLを取得します（この後、CDKから設定します）
API_URL = os.environ.get("API_URL")

def handler(event, context):
    # API Gatewayから渡されたリクエストボディを読み込みます
    body = json.loads(event["body"])
    # ユーザーが入力したメッセージを取得します
    message = body["message"]

    # 宿題の要件を満たすシンプルな実装として、受け取ったメッセージをそのままプロンプトとします
    prompt = message

    try:
        # あなたのColab APIに送信するデータを作成します
        data = {
            "prompt": prompt
        }
        # データをJSON形式のバイト列に変換します
        post_data = json.dumps(data).encode('utf-8')

        # HTTPリクエストのヘッダーを設定します
        headers = {
            "Content-Type": "application/json"
        }
        # リクエストオブジェクトを組み立てます
        req = urllib.request.Request(API_URL, post_data, headers)

        # 組み立てたリクエストをAPIに送信し、レスポンスを受け取ります
        with urllib.request.urlopen(req) as res:
            # レスポンスボディを読み込み、JSONとして解釈します
            response_body = json.loads(res.read().decode('utf-8'))
            # APIからの応答テキスト（"response"キーの値）を取得します
            response_text = response_body.get("response", "APIから正常な応答がありませんでした。")

    except Exception as e:
        # API呼び出し中に何らかのエラーが発生した場合の処理
        print(f"Error calling external API: {e}")
        response_text = "APIの呼び出し中にエラーが発生しました。"

    # フロントエンド（チャット画面）に返すレスポンスを作成します
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"message": response_text}),
    }