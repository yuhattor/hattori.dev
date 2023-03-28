---
title: "コードスキャンにより、リポジトリ上で有効化されたツールの健全性を確認できる"
englishtitle: "Code scanning shows the health of tools enabled on a repository"
date: "2023-03-28"
cardurl: "https://github.blog/changelog/2023-03-28-code-scanning-shows-the-health-of-tools-enabled-on-a-repository"
author: "Kevin Duck"
description: " The new code scanning tool status page allows users to view the status of CodeQL and other code scanning tools.  The page shows all the tools that are enabled on the repository and provides information about their setup types, configurations, and any relevant failures or warnings. If a tool is not working as expected, this is a good place to start troubleshooting the issue.  You can visit the new tool status page by using the button at the top of the repository's Code Scanning page .  Statuses for the tool  The page indicates three possible statuses for the tool: all configurations are working, some need attention, and some are not working.  Code scanning needs to have received at least one analysis for the default branch to provide a tool status. Only the status of the default branch is reported.  The page shows the latest state of all analysis configurations for the tool. For instance, if you created two separate workflows to scan two distinct parts of the repository independently, the page displays the most recent state of the tool by combining the statuses of both.  The page structure  For each tool, the page provides actionable information about misconfigurations and errors, the number of scanned files per language, the setup types and configurations, the list of rules the tool checks against, and detailed CSV reports.  Error messages  To help you with debugging, the tool"
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/54394529/227717362-fd61b7c9-fcb8-4325-a9ff-d13e5049365d.png?w=600&ssl=1"
englishsummary: " status page includes a list of error messages with details about what went wrong and how to fix it.  The new code scanning tool status page allows users to view the status of CodeQL and other code scanning tools, providing actionable information about mis"
summary: "ステータスページには、エラーメッセージのリストと、何が間違っていたのか、どのように修正するのかについての詳細が含まれています。  新しいコードスキャンツールのステータスページでは、CodeQLやその他のコードスキャンツールのステータスを表示することができ、誤操作に関する実用的な情報を提供します。"
---

<p>新しいコード スキャン ツールのステータス ページでは、CodeQL およびその他のコード スキャン ツールのステータスを確認できます。<br />
 このページでは、リポジトリ上で有効になっているすべてのツールが表示され、セットアップ タイプ、構成、および関連する障害や警告に関する情報を提供します。ツールが期待通りに動作しない場合、問題のトラブルシューティングを開始するのに適した場所です。<br />
<br /><a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/managing-code-scanning-alerts-for-your-repository#viewing-the-alerts-for-a-repository">リポジトリのコード スキャン ページの</a>上部にあるボタンを使用すると、新しいツール ステータス ページにアクセスできます。</p>
<p align="center">
<img decoding="async" alt="code-scanning-tool-status-page-access" src="https://i0.wp.com/user-images.githubusercontent.com/54394529/227717362-fd61b7c9-fcb8-4325-a9ff-d13e5049365d.png?w=600&#038;ssl=1" data-recalc-dims="1">
</p>
<h3 id="statuses-for-the-tool" id="statuses-for-the-tool" >ツールのステータス<a href="#statuses-for-the-tool" class="heading-link pl-2 text-italic text-bold" aria-label="Statuses for the tool"></a></h3>
<p>このページでは、ツールの3つのステータスが表示されます。すべてのコンフィギュレーションが機能している、いくつかのコンフィギュレーションは注意が必要、いくつかは機能していない。<br />
<br />コードスキャンがツールのステータスを提供するには、デフォルトブランチの分析を少なくとも1つ受信する必要があります。<br />
<br />このページには、ツールのすべての解析設定の最新状態が表示されます。たとえば、リポジトリの 2 つの異なる部分を独立してスキャンするために 2 つの別々のワークフローを作成した場合、このページでは、両方のステータスを組み合わせてツールの最新の状態を表示します。</p>
<h3 id="the-page-structure" id="the-page-structure" >ページの構造<a href="#the-page-structure" class="heading-link pl-2 text-italic text-bold" aria-label="The page structure"></a></h3>
<p>各ツールについて、設定ミスやエラー、言語ごとのスキャンファイル数、設定タイプや設定内容、ツールがチェックするルールのリスト、詳細なCSVレポートなど、実用的な情報を提供します。</p>
<p align="center">
<img decoding="async" alt="code-scanning-tool-status-page-detailed" src="https://i0.wp.com/user-images.githubusercontent.com/54394529/228172209-1ac9438c-a98e-4094-ab74-f58e594fb9a5.png?w=600&#038;ssl=1" data-recalc-dims="1">
</p>
<h4 id="error-messages" id="error-messages" >エラーメッセージ<a href="#error-messages" class="heading-link pl-2 text-italic text-bold" aria-label="Error messages"></a></h4>
<p>デバッグを支援するために、ツール ステータス ページには、ツールのセットアップと解析の実行中に複数のコード スキャン システム コンポーネントから収集したエラー メッセージが表示されます。これには、CodeQL、コード スキャン ワークフロー、SARIF アップロード制限、内部コード スキャン システムからのエラーが含まれます。<br />
<br />サードパーティのコード スキャン ツールは、まだツール関連のエラーをこのページに配信することができません。将来的には、これらのツールは SARIF のアップロードを通じてコード スキャンにエラー メッセージを送信できるようになる予定です。</p>
<h4 id="scanned-files" id="scanned-files" >スキャンされたファイル<a href="#scanned-files" class="heading-link pl-2 text-italic text-bold" aria-label="Scanned files"></a></h4>
<p>スキャンされたファイル」セクションでは、<a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-the-tool-status-page#how-codeql-defines-scanned-files">リポジトリ内のファイル数と比較して、言語ごとに分析されたファイルの</a>数が表示されます<a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-the-tool-status-page#how-codeql-defines-scanned-files">。</a><br />
<br />このセクションでは、コードスキャンツールがリポジトリ上で正しく動作しているかどうかを判断するのに役立ち、リポジトリに存在するがサポートされていない言語やツールによって分析されていない言語は無視して、ツールがサポートし分析している言語に関する情報のみを表示します。<br />
<br />このセクションでは、サードパーティ製のコードスキャンツールはまだ表示しません。将来的には、サードパーティツールは、SARIFアップロードを通じてコードスキャンにエラーメッセージを提出できるようになる予定です。</p>
<h3 id="delivery-dates" id="delivery-dates" >納期について<a href="#delivery-dates" class="heading-link pl-2 text-italic text-bold" aria-label="Delivery dates"></a></h3>
<p>これはGitHub.comに出荷され、GitHub Enterprise Server 3.9で利用可能になる予定です。</p>
<p><a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning">コードスキャンと</a> <a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-the-tool-status-page">ツールのステータスページについて</a>詳しくはこちら<br />
<br /><a href="https://github.com/features/security">GitHub Advanced Securityについて</a>詳しくはこちら。</p>


