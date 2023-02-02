---
title: "API リクエストが監査ログストリーミングで利用可能に - Private Beta"
englishtitle: "API requests are available via audit log streaming – Private Beta"
date: "2023-02-01"
cardurl: "https://github.blog/changelog/2023-02-01-api-requests-are-available-via-audit-log-streaming-private-beta"
author: "Kevin Duck"
description: "GitHub Enterprise Cloud customers can now join a private beta which allows API request events to be streamed as part of their enterprise audit log."
coverimage: ""
---

<p>GitHub Enterprise Cloudの顧客は、APIリクエストイベントをエンタープライズ監査ログの一部としてストリーミングできるプライベートベータに参加できるようになりました。</p>
<p>このプライベートベータでは、企業のプライベートリポジトリに対するREST APIコールを、<a href="https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise">GitHubがサポートするストリーミングエンドポイントの</a>いずれかにストリーミングすることができます。この機能は今後、取得できるAPIイベントを拡大し、監査ログAPIを通じてこのデータを利用できるようにする予定です。</p>
<p>多くの GitHub ユーザーは GitHub の API を利用して GitHub の体験を拡張、カスタマイズしています。しかし、APIを利用することは、企業にとってセキュリティや運用上のユニークな課題を生み出す可能性があります。</p>
<p>ターゲット監査ログストリーミングAPIリクエストの導入により、Enterprise の Owner は以下のことが可能になります。</p>
<ul>
<li>プライベートリポジトリを対象としたAPIの使用状況をより良く理解、分析する</li>
<li>誤設定された可能性のあるアプリケーションや統合を特定し、診断する。</li>
<li>API レート制限の原因となっているプライベートリポジトリをターゲットとした API アクティビティのトラブルシューティング。</li>
<li>潜在的に悪意のある活動を特定するための API 固有の異常検出アルゴリズムの開発。</li>
</ul>
<p>プライベートベータへの参加を希望するEnterprise の Owner は、GitHubアカウントマネージャに連絡するか、<a href="https://github.com/enterprise/contact">弊社の営業</a>チームに連絡して、この機能を企業向けに有効化してもらう必要があります。有効化されると、監査ログストリームにAPIリクエストイベントが表示されるようになります。フィードバックは、<a href="https://github.com/community/community/discussions/45920">ベータ版フィードバックコミュニティのディスカッションポストで受け付けて</a>います。</p>


