---
title: "GitHub Actions - デフォルトのGITHUB_TOKENの権限を読み取り専用に更新する"
englishtitle: "GitHub Actions – Updating the default GITHUB_TOKEN permissions to read-only"
date: "2023-02-02"
cardurl: "https://github.blog/changelog/2023-02-02-github-actions-updating-the-default-github_token-permissions-to-read-only"
author: "Kevin Duck"
description: "Previously, GitHub Actions gets a GITHUB_TOKEN with both read/write permissions by default whenever Actions is enabled on a repository."
coverimage: ""
---

<p>これまでGitHub Actionsは、リポジトリ上でActionsを有効にすると、デフォルトで読み取り/書き込みの両方のパーミッションを持つGITHUB_TOKENを取得していました<br />
これはデフォルトでは寛容すぎるため、セキュリティを向上させるために、今後はデフォルトを<strong>読み取り専用トークンに</strong>変更します。必要であれば、読み取り/書き込みに変更することができます。</p>
<p>この変更は、既存の企業、組織、リポジトリに影響を与えることはありません。以下は、今後のデフォルトの設定方法です。</p>
<ol>
<li><a href="https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#configuring-the-default-github_token-permissions">企業</a>: 新しいエンタープライズには、読み取り専用のトークンが設定されます。</li>
<li><a href="https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-the-default-github_token-permissions">エンタープライズが所有する組織</a>: 新しい組織は、親企業からパーミッションを継承します。 </li>
<li><a href="https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-the-default-github_token-permissions">エンタープライズによって所有されていない組織</a>: 新しい組織は、読み取り専用のトークンを持つことになります。</li>
<li>組織が所有する<a href="https://docs.github.com/en/enterprise-cloud@latest/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions">リポジトリ</a>: 新しいリポジトリは、親組織のパーミッションを継承します。</li>
<li><a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#configuring-the-default-github_token-permissions">個人</a>アカウントが所有するリポジトリ: 新しいリポジトリは読み取り専用トークンになります。</li>
</ol>


