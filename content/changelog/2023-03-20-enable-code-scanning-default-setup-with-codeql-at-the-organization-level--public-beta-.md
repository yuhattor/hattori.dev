---
title: "組織レベルでCodeQLによるコードスキャンのデフォルト設定を有効にする（パブリックベータ版）"
englishtitle: "Enable code scanning default setup with CodeQL at the organization level (public beta)"
date: "2023-03-20"
cardurl: "https://github.blog/changelog/2023-03-20-enable-code-scanning-default-setup-with-codeql-at-the-organization-level-public-beta"
author: "Kevin Duck"
description: " Enabling CodeQL analysis with code scanning default setup for eligible repositories in your organization is now as easy as a single click from the organization's settings page or a single API call .  You can use code scanning default setup to enable CodeQL analysis for pull requests and pushes on eligible repositories without committing any workflow files. Currently, this feature is only available for repositories that use GitHub Actions and it supports analysis of JavaScript/TypeScript, Python and Ruby. We plan to add support for additional languages soon.  To help you identify which repositories are eligible for the "enable all" feature, two new security coverage filters have been added:  code-scanning-default-setup : returns a list of enabled, eligible or not eligible repositories  advanced-security : returns a list of repositories with GitHub Advanced Security enabled or not enabled  This feature has been released as a public beta on GitHub.com and will also be available as a public beta on GitHub Enterprise Server 3.9.  Learn more about configuring code scanning at scale using CodeQL and the "Enable or disable a security feature for an organization" REST API  Learn more about GitHub Advanced Security  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/2262535/226442176-989f6151-3f9c-46f1-a2e0-07e31d96985c.png?w=600&ssl=1"
englishsummary: ""
summary: ""
---

<p>組織内の対象となるリポジトリに対して、コードスキャンをデフォルト設定したCodeQLの解析を有効にすることは、組織の設定ページから1回クリックするか、<a href="https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs?apiVersion=2022-11-28#enable-or-disable-a-security-feature-for-an-organization">1回のAPIコールで</a>簡単にできるようになりました。<br />
</p>
<p align="center">
<img decoding="async" alt="Code scanning enable all default setup button on the organization's 'Settings' page" src="https://i0.wp.com/user-images.githubusercontent.com/2262535/226442176-989f6151-3f9c-46f1-a2e0-07e31d96985c.png?w=600&#038;ssl=1" data-recalc-dims="1">
</p>
<p>
コードスキャンのデフォルト設定を利用することで、ワークフローファイルをコミットすることなく、対象リポジトリのプルリクエストとプッシュに対してCodeQLによる解析を有効にすることができます。現在、この機能は GitHub Actions を使用しているリポジトリでのみ利用可能で、JavaScript/TypeScript、Python、Ruby の解析に対応しています。近日中に追加言語のサポートを追加する予定です。</p>
<p>どのリポジトリが「enable all」機能の対象となるかを特定するために、2つの新しいセキュリティカバレッジフィルタが追加されました。</p>
<ul>
<li><code>code-scanning-default-setup</code>: 有効、対象、対象外のリポジトリのリストを返します。</li>
<li><code>advanced-security</code>: GitHub Advanced Securityが有効または無効なリポジトリの一覧を返す。</li>
</ul>
<p>この機能はGitHub.comでパブリックベータとしてリリースされており、GitHub Enterprise Server 3.9でもパブリックベータとして提供される予定です。</p>
<p><a href="https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning-at-scale">CodeQLと</a> <a href="https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/orgs?apiVersion=2022-11-28#enable-or-disable-a-security-feature-for-an-organization">「組織のセキュリティ機能を有効または無効にする」REST APIを</a>使用した<a href="https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning-at-scale">スケールでのコードスキャン設定の詳細については</a>こちら<br />
<br /><a href="https://github.com/features/security">GitHub Advanced Securityの詳細については</a>こちら</p>


