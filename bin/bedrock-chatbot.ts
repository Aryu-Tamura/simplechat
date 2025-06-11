import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { BedrockChatbotStack } from '../lib/bedrock-chatbot-stack';

const app = new cdk.App();
new BedrockChatbotStack(app, 'BedrockChatbotStack', {
  // ★★★ このapiUrlの行を追加し、URLをあなたのものに書き換えます ★★★
  //     （必ず /generate を末尾につけてください）
  apiUrl: "  https://9cb9-35-234-31-4.ngrok-free.app",

  // modelIdは今回利用しないので、そのままでも、行ごと削除してもOKです
  // modelId: 'us.amazon.nova-lite-v1:0',

  // 環境設定（この部分は変更しません）
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION || 'us-east-1'
  }
});

// タグ設定（この部分は変更しません）
cdk.Tags.of(app).add('Project', 'BedrockChatbot');
cdk.Tags.of(app).add('Environment', 'Dev');
