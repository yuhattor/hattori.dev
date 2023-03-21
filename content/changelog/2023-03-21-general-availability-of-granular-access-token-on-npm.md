---
title: "npmでのグラニュラーアクセストークンの一般的な利用可能性"
englishtitle: "General availability of granular access token on npm"
date: "2023-03-21"
cardurl: "https://github.blog/changelog/2023-03-21-general-availability-of-granular-access-token-on-npm"
author: "Kevin Duck"
description: " Today we are making the granular access token feature on npm generally available.  Granular access token, allows you to:  Restrict token access to specific packages and/or scopes  Grant tokens access to specific organizations for org and user management  Set a token expiration date  Limit token access based on IP address ranges  Select between read and/or write access for the token  We recommend using granular access tokens with least privileges for automating your publishing and org management activities. You can allow your package to be published without 2FA using granular access tokens from your trusted CI/CD systems. Additionally, you can also configure your package to require 2FA when publishing from a local machine to defend against account hijacking.  Read more about creating a granular access token here .  "
coverimage: ""
englishsummary: "  NPM's new granular access token feature allows users to restrict token access to specific packages and scopes, grant tokens access to organizations, set a token expiration date, limit token access based on IP address ranges, and select between read and"
summary: "  NPMの新機能であるGranular Access Tokenは、トークンのアクセスを特定のパッケージやスコープに制限したり、トークンのアクセスを組織に付与したり、トークンの有効期限を設定したり、IPアドレス範囲に基づくトークンへのアクセスを制限したり、読み取りと書き込みを選択したりすることができます。"
---

<p>本日、npmの<a href="https://docs.npmjs.com/about-access-tokens#about-granular-access-tokens">granular access token</a>機能を一般公開しました。</p>
<p>Granular access tokenは、以下のことを可能にします。</p>
<ul>
<li>特定のパッケージやスコープにトークンへのアクセスを制限する。</li>
<li>組織やユーザー管理のために、特定の組織にトークンのアクセス権を付与する。</li>
<li>トークンの有効期限を設定する</li>
<li>IPアドレス範囲に基づくトークンのアクセス制限</li>
<li>トークンの読み出しと書き込みのどちらかを選択する</li>
</ul>
<p>公開と組織管理の自動化には、最小限の権限を持つ粒状のアクセストークンを使用することをお勧めします。信頼できるCI/CDシステムからのきめ細かいアクセストークンを使って、2FAなしでパッケージを公開できるようにすることができます。さらに、アカウントの乗っ取りを防ぐために、ローカルマシンから公開するときに<a href="https://docs.npmjs.com/requiring-2fa-for-package-publishing-and-settings-modification">2FAを要求するようにパッケージを構成</a>することもできます。</p>
<p>グラニュラーアクセストークンの作成について、詳しくは<a href="https://docs.npmjs.com/creating-and-viewing-access-tokens#creating-granular-access-tokens-on-the-website">こちらを</a>ご覧ください。</p>


