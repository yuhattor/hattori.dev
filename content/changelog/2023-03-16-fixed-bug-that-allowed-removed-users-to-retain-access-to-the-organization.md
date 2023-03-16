---
title: "削除されたユーザーが組織へのアクセス権を保持できる不具合を修正しました。"
englishtitle: "Fixed bug that allowed removed users to retain access to the organization"
date: "2023-03-16"
cardurl: "https://github.blog/changelog/2023-03-16-fixed-bug-that-allowed-removed-users-to-retain-access-to-the-organization"
author: "Kevin Duck"
description: " GitHub Security was notified about an issue where users still had access to organizations after being removed. Our Security team investigated potential instances and determined there were occasional instances where users’ permissions were not fully removed when teams were deleted or they were part of a team when they were removed from the organization. While we investigated the root causes, which stemmed from background job and permissions issues, a manual fix has been implemented since October 20, 2022. We have addressed the underlying issues and the need for the previously implemented manual fix. We have also cleaned up any users that were not removed when they should have been. There is no further action that is required by any organization.  "
coverimage: ""
englishsummary: "  GitHub Security investigated potential instances of users not being fully removed from organizations when teams were deleted or they were part of a team when they were removed, and implemented a manual fix and addressed the underlying issues to ensure that no further action is"
summary: "  GitHub Securityは、チームが削除されたときにユーザーが組織から完全に削除されない、または削除されたときにチームに属していた、という潜在的な事例を調査し、手動による修正を実施し、根本的な問題に対処して、これ以上のアクションがないようにしました。"
---

<p>GitHub Securityは、ユーザーが削除された後も組織へのアクセス権が残っている問題について通知されました。セキュリティチームが潜在的な事例を調査した結果、チームが削除された際にユーザーのパーミッションが完全に削除されていなかったり、組織から削除された際にチームの一員であったりする事例が時折あることが判明しました。バックグラウンドジョブとパーミッションの問題に起因する根本的な原因を調査する一方で、2022年10月20日以降、手動による修正が実施されています。私たちは、根本的な問題と、以前に実施された手動修正の必要性に対処しました。また、削除すべき時に削除されなかったユーザーをクリーンアップしました。どの組織でも、これ以上必要なアクションはありません。</p>


