---
title: "カスタムリポジトリのロールAPI GAとブレークチェンジ"
englishtitle: "Custom repository roles API GA and breaking change"
date: "2023-03-07"
cardurl: "https://github.blog/changelog/2023-03-07-custom-repository-roles-api-ga-and-breaking-change"
author: "Kevin Duck"
description: " The Custom Repository Roles REST API has moved to general availability, with a breaking change to the path used.  Previously, the API was found at /orgs/{org}/custom_roles – it has been moved to /orgs/{org}/custom-repository-roles . With organization-level custom roles in progress, we found that the custom_roles path was wasn't specific enough and could generate confusion.  The deprecated beta API will be removed from api.github.com in 6 months, on September 7th, 2023.  On GitHub Enterprise Server, the API will be available at its new path in version 3.9. The previous API to list roles was added in GHES 3.4, and will be removed with the next API version .  To learn more about custom repository roles, see "About custom repository roles" and "Custom repository roles REST API" .  "
coverimage: ""
englishsummary: ""
summary: ""
---

<p><a href="https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles?apiVersion=2022-11-28">カスタムリポジトリロールの</a>REST APIが一般公開され、使用されるパスが変更されました。<br />
以前は、APIは<code>/orgs/{org}/custom_rolesに</code>ありましたが、<code>/orgs/{org}/custom-repository-rolesに</code>移動されました。<a href="https://github.com/github/roadmap/issues/586">組織レベルのカスタムロールが</a>進行中で、<code>custom_rolesの</code>パスが十分に具体的でなく、混乱を引き起こす可能性があることがわかりました。<br />
非推奨のベータ版APIは、6ヶ月後の2023年9月7日に<code>api.github.comから</code>削除される予定です。<br />
GitHub Enterprise Serverでは、APIはバージョン3.9でその新しいパスで利用できるようになる予定です。以前の<a href="https://docs.github.com/en/enterprise-server@3.4/rest/orgs/custom-roles">ロールを一覧表示</a>するAPIはGHES 3.4で追加されましたが、次の<a href="https://docs.github.com/en/rest/overview/api-versions?apiVersion=2022-11-28">APIバージョンで</a>削除される予定です。</p>
<p>カスタムリポジトリロールの詳細については、<a href="https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-repository-roles">「カスタムリポジトリロールについて」</a>、<a href="https://docs.github.com/en/enterprise-cloud@latest/rest/orgs/custom-roles#create-a-custom-repository-role&amp;apiVersion=2022-11-28">「カスタムリポジトリロールREST API</a>」をご覧ください。</p>


