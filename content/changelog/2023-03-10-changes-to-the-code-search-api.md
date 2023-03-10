---
title: "コード検索APIの変更点"
englishtitle: "Changes to the code search API"
date: "2023-03-10"
cardurl: "https://github.blog/changelog/2023-03-10-changes-to-the-code-search-api"
author: "Kevin Duck"
description: " We are preparing to bring powerful new code search capabilities to GitHub. As part of that effort, on April 10, 2023, we will make several changes to the code search API :  Code search rate limits will be separated from the rate limits for other search types. The separate code search category will have a rate limit of 10 requests per minute.  We are deprecating support for sorting code search results. Once these changes take effect, all code search results will be sorted by best match.  All code search API endpoints will require authentication . This change only affects repository scoped queries, because all other query types already require authentication.  To prepare for these changes, make sure your code handles rate limiting . And if you’re using code search to track changes or find security vulnerabilities in your codebase, consider using webhooks or GitHub Advanced Security .  These changes will take effect in 30 days, on April 10, 2023.  "
coverimage: ""
englishsummary: "  GitHub is introducing powerful new code search capabilities on April 10, 2023, which will include separate rate limits for code search, no support for sorting code search results, and all code search API endpoints requiring authentication."
summary: "  GitHubは、2023年4月10日に、コード検索のレート制限を別に設ける、コード検索結果のソートをサポートしない、すべてのコード検索APIエンドポイントに認証を必要とする、強力な新しいコード検索機能を導入します。"
---

<p>私たちは、GitHubに<a href="https://github.com/features/code-search">強力な新しいコード検索</a>機能を導入する準備を進めています。その一環として、2023年4月10日にコード<a href="https://docs.github.com/en/rest/search?apiVersion=2022-11-28#search-code">検索APIに</a>いくつかの変更を加える予定です。</p>
<ul>
<li>コード検索のレートリミットは、他の検索タイプのレートリミットと分離されます。コード検索のレートリミットは、他の検索タイプのレートリミットから分離され、コード検索カテゴリは1分間に10リクエストのレートリミットを持つことになります。</li>
<li>コード検索結果の並べ替えのサポートは廃止されます。これらの変更が有効になると、すべてのコード検索結果はベストマッチでソートされるようになります。</li>
<li>すべてのコード検索APIエンドポイントに<a href="https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api?apiVersion=2022-11-28#authenticating">認証が必要に</a>なります。他のすべてのクエリタイプはすでに認証を必要とするため、この変更はリポジトリスコープのクエリにのみ影響します。</li>
</ul>
<p>これらの変更に備えるために、あなたのコードが<a href="https://docs.github.com/en/rest/search?apiVersion=2022-11-28#rate-limit">レート制限を処理する</a>ことを確認してください。また、コードベースの変更を追跡したり、セキュリティの脆弱性を見つけるためにコード検索を使用している場合は、<a href="https://docs.github.com/en/rest/webhooks?apiVersion=2022-11-28#repository-webhooks">Webhooks</a>または<a href="https://docs.github.com/en/rest/webhooks?apiVersion=2022-11-28#repository-webhooks">GitHub Advanced Security</a> の使用を検討してください。</p>
<p>これらの変更は、30日後の2023年4月10日に発効します。</p>


