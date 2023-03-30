---
title: "SAMLIdentity GraphQL オブジェクトが `read` スコープをサポートするようになった。"
englishtitle: "SAMLIdentity GraphQL object now supports `read` scope"
date: "2023-03-30"
cardurl: "https://github.blog/changelog/2023-03-30-samlidentity-graphql-object-now-supports-read-scope"
author: "Kevin Duck"
description: " GitHub Enterprise Cloud administrators may need to review external identity information via the GraphQL API. Historically, this has required a token with the admin:org or admin:enterprise scope. We've taken a "least privilege" mindset in reviewing this flow and have now made this information available via the read:enterprise and read:org scopes for enterprise owner and organization owner actors.  For more information, see the GraphQL API documentation for Enterprise and Organization SAMLIdentity objects.  "
coverimage: ""
englishsummary: ""
summary: ""
---

<p>GitHub Enterprise Cloud の管理者は、GraphQL API を介して外部の ID 情報を確認する必要がある場合があります。これまでは、<code>admin:org</code>または<code>admin:enterprise</code>スコープでトークンが必要でした。私たちはこのフローを見直す際に「最小限の特権」という考え方を採用し、現在では企業オーナーおよび組織オーナーのアクター向けに<code>read:enterprise</code>および<code>read:org</code>スコープを使用してこの情報を利用できるようにしました。</p>
<p>詳細については、<a href="https://docs.github.com/en/graphql/reference/objects#enterpriseidentityprovider">Enterprise</a>および<a href="https://docs.github.com/en/graphql/reference/objects#organizationidentityprovider">Organization</a> <code>SAMLIdentity</code>オブジェクトに関する GraphQL API ドキュメントを参照してください。</p>


