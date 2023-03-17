---
title: "コードスキャンにより、プルリクエストでより正確で適切なアラートが表示されます。"
englishtitle: "Code scanning shows more accurate and relevant alerts on pull requests"
date: "2023-03-17"
cardurl: "https://github.blog/changelog/2023-03-17-code-scanning-shows-more-accurate-and-relevant-alerts-on-pull-requests"
author: "Kevin Duck"
description: " Code scanning is now using a new way of analysing and displaying alerts on pull requests. The change ensures code scanning only shows accurate and relevant alerts for the pull request.  Previously, code scanning presented all alerts unique to the pull request branch, even if they were unrelated to the code changes the pull request introduced. Now, the tool reports only alerts inside the lines of code that the pull request has changed, which makes it easier to fix these contextualised alerts in a timely manner.  The complete list of code scanning alerts on the pull request branch can be seen on the Security tab of the repository.  In addition, code scanning will no longer show fixed alerts on pull requests. Instead, you can check whether an alert has been fixed by your pull request on the Security tab of the repository by using search filters: pr:111 tool:CodeQL . If you fix an alert in the initial commit in the pull request, it will not be present on the PR branch.  This has shipped to GitHub.com and will be available in GitHub Enterprise Server 3.10.  Learn more about viewing an alert on your pull request.  Learn more about GitHub Advanced Security.  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/54394529/225644070-2049fa0b-ffe0-48df-8b91-4cb05353484b.png?w=600&ssl=1"
englishsummary: "  Code scanning now only displays relevant alerts on pull requests, making it easier to fix contextualised alerts quickly, and fixed alerts can be seen on the Security tab of the repository."
summary: "  コードスキャンでは、プルリクエストに関連するアラートのみが表示されるようになり、文脈に沿ったアラートを迅速に修正することが容易になりました。修正されたアラートは、リポジトリのセキュリティタブで確認することができます。"
---

<p>コードスキャンは、プルリクエストのアラートを分析し表示する新しい方法を使用するようになりました。この変更により、コードスキャンはプルリクエストに正確で関連性のあるアラートのみを表示するようになりました。</p>
<p>以前は、コードスキャンは、プルリクエストが導入したコード変更とは無関係であっても、プルリクエストブランチに固有のすべてのアラートを表示していました。現在、このツールは、プルリクエストが変更したコード行の内側のアラートのみを報告し、これらの文脈に沿ったアラートをタイムリーに修正することが容易になりました。</p>
<p align="center">
<img decoding="async" alt="code scanning on the slide-out enablement panel on the security coverage page" src="https://i0.wp.com/user-images.githubusercontent.com/54394529/225644070-2049fa0b-ffe0-48df-8b91-4cb05353484b.png?w=600&#038;ssl=1" data-recalc-dims="1">
</p>
<p>プルリクエストブランチのコードスキャンアラートの完全なリストは、<a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository">リポジトリの<strong>セキュリティ</strong>タブで</a>確認することができます。</p>
<p align="center">
<img decoding="async" alt="code scanning on the slide-out enablement panel on the security coverage page" src="https://i0.wp.com/user-images.githubusercontent.com/54394529/224053247-756aac24-6cae-4b22-8840-955d27676aab.png?w=600&#038;ssl=1" data-recalc-dims="1">
</p>
<p>また、コードスキャンでは、プルリクエストで修正されたアラートが表示されなくなります。代わりに、検索フィルター：<code>pr:111 tool:CodeQL</code> を使用して、リポジトリの Security タブで、プルリクエストによってアラートが修正されたかどうかを確認できます。プルリクエストの最初のコミットでアラートを修正した場合、PRブランチには存在しません。</p>
<p>これはGitHub.comに出荷され、GitHub Enterprise Server 3.10で利用可能になる予定です。</p>
<p><a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/triaging-code-scanning-alerts-in-pull-requests#viewing-an-alert-on-your-pull-request">プルリクエストでアラートを表示する方法について、詳しくはこちらをご覧ください。</a><br />
<br /><a href="https://github.com/features/security">GitHub Advanced Securityの詳細についてはこちらをご覧ください。</a></p>


