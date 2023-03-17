---
title: "シークレットスキャニングの変更で、通知のオプトイン方法が変わる"
englishtitle: "Secret scanning changes to how you opt in to notifications"
date: "2023-03-17"
cardurl: "https://github.blog/changelog/2023-03-17-secret-scanning-changes-to-how-you-opt-in-to-notifications"
author: "Kevin Duck"
description: " We announced two weeks ago that we are changing how you receive notifications for secret scanning alerts. From today, those changes are in effect.  What action should I take?  If you are a repository administrator, organization owner, security manager, or user with read access to secret scanning alerts:  Watch your repositories of interest by choosing "All activity" or "Security alerts." This helps you choose what events GitHub will notify you about.  In your user notification settings , you must choose "Email" in the "Watching" section. This tells GitHub how to notify you. Secret scanning only supports email notifications at this time.  If you're a commit author:  As long as you are not ignoring the repository in your watch settings, commit authors always receive notifications for new secrets that are leaked. This means you receive a notification for any secret committed after an initial historical scan has run on the repository.  Learn more  Read our documentation on configuring secret scanning alerts  Read our blog post on how you can secure your public repositories, for free  "
coverimage: ""
englishsummary: ""
summary: ""
---

<p><a href="https://github.blog/changelog/2023-03-03-secret-scanning-changes-coming-to-how-you-opt-in-to-alert-notifications/">2週間前に</a>、シークレットスキャン警告の通知の受け取り方を変更することを<a href="https://github.blog/changelog/2023-03-03-secret-scanning-changes-coming-to-how-you-opt-in-to-alert-notifications/">お知らせ</a>しました。本日より、これらの変更が適用されます。</p>
<h3 id="what-action-should-i-take" id="what-action-should-i-take" >どのような対処をすればよいですか？<a href="#what-action-should-i-take" class="heading-link pl-2 text-italic text-bold" aria-label="What action should I take?"></a></h3>
<h4 id="if-you-are-a-repository-administrator-organization-owner-security-manager-or-user-with-read-access-to-secret-scanning-alerts" id="if-you-are-a-repository-administrator-organization-owner-security-manager-or-user-with-read-access-to-secret-scanning-alerts" >リポジトリ管理者、組織所有者、セキュリティ管理者、またはシークレットスキャンアラートの読み取り権限を持つユーザーである場合。<a href="#if-you-are-a-repository-administrator-organization-owner-security-manager-or-user-with-read-access-to-secret-scanning-alerts" class="heading-link pl-2 text-italic text-bold" aria-label="If you are a repository administrator, organization owner, security manager, or user with read access to secret scanning alerts:"></a></h4>
<ul>
<li>すべてのアクティビティ&quot; または &quot;セキュリティアラート&quot; を選択して、関心のあるリポジトリを監視してください。</li>
<li><a href="https://github.com/settings/notifications">ユーザー通知</a>設定では、&quot;Watching&quot; セクションで &quot;Email&quot; を選択する必要があります。これはGitHubに<em>どのように</em>通知するかを伝えるものです。シークレットスキャンは、現時点ではメールでの<em>通知にのみ</em>対応しています。</li>
</ul>
<h4 id="if-youre-a-commit-author" id="if-youre-a-commit-author" >あなたがコミット作成者である場合<a href="#if-youre-a-commit-author" class="heading-link pl-2 text-italic text-bold" aria-label="If you&#039;re a commit author:"></a></h4>
<p>ウォッチ設定でリポジトリを無視していない限り、コミット作成者は常に新しいシークレットが流出したときの通知を受け取ります。つまり、リポジトリで最初の履歴スキャンが実行された後にコミットされた秘密については、通知を受け取ることができます。</p>
<h3 id="learn-more" id="learn-more" >もっと詳しく<a href="#learn-more" class="heading-link pl-2 text-italic text-bold" aria-label="Learn more"></a></h3>
<ul>
<li><a href="https://docs.github.com/en/code-security/secret-scanning/managing-alerts-from-secret-scanning#configuring-notifications-for-secret-scanning-alerts">シークレットスキャンアラートの設定に関するドキュメントをお読みください。</a></li>
<li><a href="https://github.blog/2023-02-28-secret-scanning-alerts-are-now-available-and-free-for-all-public-repositories/">公開リポジトリの安全性を確保する方法について、当社のブログ記事をお読みください（無料）。</a></li>
</ul>


