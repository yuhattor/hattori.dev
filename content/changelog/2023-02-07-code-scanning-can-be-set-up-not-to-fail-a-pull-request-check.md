---
title: "コードスキャンは、プルリクエストチェックを失敗しないように設定することができます"
englishtitle: "Code scanning can be set up not to fail a pull request check"
date: "2023-02-07"
cardurl: "https://github.blog/changelog/2023-02-07-code-scanning-can-be-set-up-not-to-fail-a-pull-request-check"
author: "Kevin Duck"
description: " Code scanning can now be set up to never cause a pull request check failure.  By default, any code scanning alerts with a security-severity of critical or high will cause a pull request check failure.  You can specify which security-severity level for code scanning results should cause the code scanning check to fail, including None , by going to the Code security and Analysis tab in the repository settings.  This has shipped to GitHub.com and will be available in GitHub Enterprise Server 3.9. Learn more about severity levels for security alerts and Code scanning results check failures on pull requests.  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/54394529/217245862-9c98e4c9-1c55-4fa5-a907-5b80300ffbe6.png?ssl=1"
englishsummary: "  Code scanning can be configured to not cause pull request check failures, and this feature is available on GitHub.com and GitHub Enterprise Server 3.9."
summary: "コードスキャンは、プルリクエストのチェックに失敗しないように設定することができ、この機能は GitHub.comと GitHub Enterprise Server 3.9で利用可能です。"
---

<p>コードスキャンがプルリクエストチェックの失敗の原因にならないように設定できるようになりました。</p>
<p>デフォルトでは、<code>security-severity</code>が「<code>Critical</code>または「<code>High</code>」のコードスキャン警告は、プルリクエストチェックの失敗の原因となります。<br />
リポジトリ設定の<strong>コードセキュリティと分析</strong>タブで、コードスキャン結果の<code>セキュリティ-重大度</code>レベルを指定して、コードスキャンチェックを失敗させることができます（<code>None</code>を含む）。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/54394529/217245862-9c98e4c9-1c55-4fa5-a907-5b80300ffbe6.png?ssl=1" alt="Screenshot code-scanning-settings" data-recalc-dims="1"></p>
<p>これはGitHub.comに出荷され、GitHub Enterprise Server 3.9で利用可能になる予定です。<a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/triaging-code-scanning-alerts-in-pull-requests#code-scanning-results-check-failures">プルリクエストの</a> <a href="https://github.blog/changelog/2021-07-19-codeql-code-scanning-new-severity-levels-for-security-alerts/">セキュリティアラートと</a> <a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/triaging-code-scanning-alerts-in-pull-requests#code-scanning-results-check-failures">コードスキャン結果のチェック失敗</a>の<a href="https://github.blog/changelog/2021-07-19-codeql-code-scanning-new-severity-levels-for-security-alerts/">深刻度</a>レベルについてはこちらをご覧ください。</p>


