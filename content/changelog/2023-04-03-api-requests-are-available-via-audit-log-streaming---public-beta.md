---
title: "APIリクエストは監査ログストリーミングで利用可能 - パブリックベータ版"
englishtitle: "API requests are available via audit log streaming – Public Beta"
date: "2023-04-03"
cardurl: "https://github.blog/changelog/2023-04-03-api-requests-are-available-via-audit-log-streaming-public-beta"
author: "Kevin Duck"
description: " GitHub Enterprise Cloud customers can now join a public beta for streaming API request events as part of their enterprise audit log.  As part of this beta, REST API calls against enterprise's private and internal repositories can be streamed to one of GitHub's supported streaming endpoints .  Note: hashed_token and token_id have been redacted for security reasons.  Many GitHub users leverage GitHub's APIs to extend and customize their GitHub experience. However, use of APIs can create unique security and operational challenges for Enterprises. With the introduction of targeted audit log streaming API requests, enterprise owners are now able to:  Better understand and analyze API usage targeting their private and internal repositories;  Identify and diagnose potentially misconfigured applications or integrations;  Identify the authentication tokens being used by specific applications or integrations;  Troubleshoot API contributing to API rate limiting;  Leverage API activity when performing forensic investigations; and  Develop API specific anomaly detection algorithms to identify potentially malicious API activity.  Enterprise owners interested in the public beta can follow the instructions in our docs for enabling audit log streaming of API requests. Once enabled, you should begin seeing API request events in your audit log stream. Feedback can be provided at our beta feedbac"
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/95828167/229549675-7d472b3b-c636-47c2-8372-4adcde52d1f9.png?w=693&ssl=1"
englishsummary: "  GitHub Enterprise Cloud customers can now join a public beta to stream API request events as part of their enterprise audit log to better understand, analyze, and identify potentially misconfigured applications or integrations."
summary: "  GitHub Enterprise Cloudのお客様は、パブリックベータに参加することで、APIリクエストイベントを企業監査ログの一部としてストリームし、潜在的に誤った設定のアプリケーションや統合をより良く理解、分析、特定することができます。"
---

<p>GitHub Enterprise Cloudをご利用のお客様は、エンタープライズ監査ログの一部としてAPIリクエストイベントをストリーミングするパブリックベータに参加できるようになりました。</p>
<p>このベータ版の一部として、企業のプライベートおよび内部リポジトリに対するREST APIコールは、<a href="https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise">GitHubがサポートするストリーミングエンドポイントの</a>1つにストリーミングできます。<br />
<img decoding="async" alt="image (4)" src="https://i0.wp.com/user-images.githubusercontent.com/95828167/229549675-7d472b3b-c636-47c2-8372-4adcde52d1f9.png?w=693&#038;ssl=1" data-recalc-dims="1"></p>
<p><sub>注：セキュリティ上の理由から、<code>hashed_token</code>と <code>token_id</code>は再表示されています。 </sub></p>
<p>多くのGitHubユーザーは、GitHubのAPIを活用してGitHubの体験を拡張したりカスタマイズしています。しかし、APIを利用することで、企業にとってセキュリティや運用上のユニークな課題が生じることがあります。APIリクエストを対象とした監査ログストリーミングの導入により、企業経営者は以下のことが可能になりました：</p>
<ul>
<li>プライベートおよび内部リポジトリを対象としたAPI利用をよりよく理解し、分析する；</li>
<li>誤設定された可能性のあるアプリケーションや統合を特定し、診断する；</li>
<li>特定のアプリケーションや統合で使用されている認証トークンを特定する；</li>
<li>APIレート制限に寄与しているAPIのトラブルシューティング；</li>
<li>フォレンジック調査の際にAPIアクティビティを活用する。</li>
<li>潜在的に悪意のあるAPIアクティビティを識別するためのAPI固有の異常検出アルゴリズムを開発する。</li>
</ul>
<p>パブリックベータに関心のある企業オーナーは、<a href="https://docs.github.com/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#enabling-audit-log-streaming-of-api-requests">APIリクエストの監査ログストリーミングを有効に</a>するために、私たちのドキュメントの指示に従うことができます。有効化すると、監査ログストリームにAPIリクエストイベントが表示されるようになるはずです。フィードバックは、<a href="https://github.com/community/community/discussions/45920">ベータ版のフィードバック・コミュニティのディスカッション・ポストで</a>提供することができます。</p>


