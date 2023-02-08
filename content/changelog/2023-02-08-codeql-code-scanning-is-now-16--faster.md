---
title: "CodeQL のコードスキャンが 16% 高速化"
englishtitle: "CodeQL code scanning is now 16% faster"
date: "2023-02-08"
cardurl: "https://github.blog/changelog/2023-02-07-codeql-code-scanning-is-now-16-faster"
author: "Kevin Duck"
description: " CodeQL is the engine that powers GitHub code scanning, used by more than 100,000 repositories to catch security vulnerabilities before they cause issues in deployments.  CodeQL is fully integrated into the Pull Request workflow , so it has to be as fast as possible to keep developers unblocked.  We're constantly working on performance improvements, from incremental optimizations to fundamental research , all with the goal of speeding up the nearly 150,000 checks we run every single day, without compromising our best-in-class precision and low false-positive rate.  With the recent release of CodeQL version 2.12, we looked back at the performance gains compared to version 2.11 (September 2022) to see how far we've come. We compared the analysis time for the same 55,000 repositories on GitHub.com and found an average improvement of 15.7% across all supported languages:  Users on GitHub.com automatically run the latest CodeQL version. Customers on GitHub Enterprise Server can update by following the sync processes explained here .  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/8023543/217301314-3922e02b-27f0-492b-be30-85221dfd5877.png?ssl=1"
englishsummary: "  CodeQL is an engine used by more than 100,000 repositories to catch security vulnerabilities before they cause issues in deployments, and has seen an average improvement of 15.7% in analysis time since September 2022."
summary: "CodeQLは、10万以上のリポジトリで利用され、セキュリティ脆弱性がデプロイメントに問題を引き起こす前にキャッチするためのエンジンで、2022年9月から平均15.7%の解析時間の改善が見られています。"
---

<p>CodeQL は GitHub のコードスキャンを支えるエンジンであり、10万以上のリポジトリで使用され、デプロイメントにおいて問題を引き起こす前にセキュリティ脆弱性を捕らえることができます。</p>
<p>CodeQLは<a href="https://github.blog/changelog/2022-06-02-users-can-view-and-comment-on-code-scanning-alerts-on-the-conversation-tab-in-a-pull-request/">Pull Requestのワークフローに</a>完全に統合されているため、開発者がブロックされないようにするためには、可能な限り高速である必要があります。</p>
<p>私たちは、クラス最高の精度と低い偽陽性率を損なうことなく、毎日実行される約15万件のチェックを高速化することを目標に、段階的な最適化から<a href="https://githubnext.com/projects/incremental-codeql/">基礎研究まで</a>、常にパフォーマンスの改善に取り組んでいます。</p>
<p>先日リリースされたCodeQLバージョン2.12では、バージョン2.11（2022年9月）と比較して、どの程度パフォーマンスが向上したかを振り返ってみました。GitHub.comにある同じ55,000のリポジトリの解析時間を比較したところ、対応するすべての言語で平均15.7%の向上が見られました。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/8023543/217301314-3922e02b-27f0-492b-be30-85221dfd5877.png?ssl=1" alt="codeql performance 2 11 2 12 improvement" data-recalc-dims="1"></p>
<p>GitHub.comのユーザーは、自動的に最新のCodeQLバージョンを実行します。GitHub Enterprise Serverをご利用のお客様は、<a href="https://docs.github.com/en/enterprise-server@3.7/admin/code-security/managing-github-advanced-security-for-your-enterprise/configuring-code-scanning-for-your-appliance#configuring-github-connect-to-sync-github-actions">こちらで説明</a>されている同期プロセスに従ってアップデートすることができます。</p>


