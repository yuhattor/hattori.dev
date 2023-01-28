---
title: プルリクエストの差し戻し用API
englishtitle: API for reverting a pull request
date: 2023-01-27
cardurl: https://github.blog/changelog/2023-01-27-api-for-reverting-a-pull-request
author: Kevin Duck
description: "A GraphQL mutation is now available for reverting a merged pull request: revertPullRequest"
coverimage: ""
---

<p>マージされたプルリクエストを元に戻すための GraphQL 変換 ```[revertPullRequest](https://docs.github.com/graphql/reference/mutations#revertpullrequest)``` が利用できるようになりました。 <a href="https://docs.github.com/graphql/reference/mutations#revertpullrequest"><strong><code>revertPullRequest</code></strong></a>.</p>
<p>ウェブ上のプルリクエストページの revert アクションと同様に、この API を呼び出すと、マージされたプルリクエストで行われた変更を取り消す新しいプルリクエストが作成されます。</p>
<p>プルリクエストの<a href="https://docs.github.com/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/reverting-a-pull-request">取り消しについて</a>詳しくはこちら。</p>
