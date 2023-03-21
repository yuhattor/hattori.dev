---
title: "CodeQLによるコードスキャン初期設定において、「セキュリティ拡張」クエリスイートを使用できるようになりました。"
englishtitle: "You can now use the “security extended” query suite in code scanning default setup with CodeQL"
date: "2023-03-21"
cardurl: "https://github.blog/changelog/2023-03-21-you-can-now-use-the-security-extended-query-suite-in-code-scanning-default-setup-with-codeql"
author: "Kevin Duck"
description: " You can now enable the "security extended" query suite for repositories using code scanning default setup with CodeQL. This query suite can be selected during set up, or changed at any time by viewing and editing the CodeQL configuration.  Code scanning's default query suites have been carefully designed to ensure that they look for the security issues most relevant to developers, whilst also minimizing the occurrence of false positive results. However, if you and you developers are interested in seeing a wider range of alerts you can enable the security extended query suite. This suite includes the same queries as in the default query suite, plus:  extra queries with slightly lower severity and precision.  extra experimental queries.  If you enable the security extended suite you may see more CodeQL alerts in your repository and on pull requests. For more information, see "About code scanning alerts" .  Read more about code scanning default setup .  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/19343236/225629975-c328c7b2-12e3-4940-a248-03cab8f7b725.png?ssl=1"
englishsummary: ""
summary: ""
---

<p>CodeQL でコードスキャンのデフォルト設定を使用しているリポジトリに対して、「セキュリティ拡張」クエリスイートを有効にすることができるようになりました。このクエリスイートは、セットアップ時に選択することも、CodeQLの設定を表示および編集することでいつでも変更することができます。</p>
<p>Code Scanのデフォルトのクエリスイートは、開発者に最も関係のあるセキュリティ問題を確実に検索し、同時に誤検出の発生を最小限に抑えるように慎重に設計されています。しかし、もしあなたやあなたの開発者が、より幅広いアラートを見たい場合は、セキュリティ拡張クエリスイートを有効にすることができます。このクエリ・スイートには、デフォルトのクエリ・スイートと同じクエリに加え、以下のクエリが含まれています。</p>
<ul>
<li>重大度と精度が若干低い追加クエリ。</li>
<li>実験的な追加クエリ。</li>
</ul>
<p>セキュリティ拡張スイートを有効にすると、リポジトリやプルリクエストでより多くの CodeQL アラートが表示されることがあります。詳細については、<a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning-alerts#enabling-experimental-alerts">「コードスキャンアラートについて</a>」を参照してください。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/19343236/225629975-c328c7b2-12e3-4940-a248-03cab8f7b725.png?ssl=1" alt="Code scanning default setup query suites" data-recalc-dims="1"></p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/19343236/225630244-ffb1192f-f49c-463d-8644-0587450d961d.png?ssl=1" alt="Code scanning default setup view configuration" data-recalc-dims="1"></p>
<p><a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning-for-a-repository#configuring-code-scanning-automatically">コードスキャニングのデフォルト設定について</a>もっと読む。</p>


