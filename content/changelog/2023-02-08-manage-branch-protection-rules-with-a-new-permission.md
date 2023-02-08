---
title: "新しい権限でブランチプロテクションルールを管理"
englishtitle: "Manage branch protection rules with a new permission"
date: "2023-02-08"
cardurl: "https://github.blog/changelog/2023-02-08-manage-branch-protection-rules-with-a-new-permission"
author: "Kevin Duck"
description: " You can now create a custom role to manage branch protections without having to grant the Admin role. Previously, to manage branch protections you had to be an Admin which provides additional permissions that may not be needed. For tighter control of Admin permissions, you can now craft a custom role that has the Edit repository rules permission, allowing just the right amount of access.  This permission grants the ability to create , edit , and delete both branch protection rules and protected tags .  For more information, visit Managing custom repository roles for an organization in the GitHub documentation.  We appreciate feedback on this in GitHub's public feedback discussions .  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/7575792/215608072-49f28961-f372-445b-8575-dded7ab7df2a.png?ssl=1"
englishsummary: "  You can now create a custom role to manage branch protections with just the right amount of access, and feedback on this is welcome in GitHub's public feedback discussions."
summary: "  ブランチの保護を管理するために、適切なアクセス権を持つカスタムロールを作成できるようになりました。これに関するフィードバックは、GitHub のパブリックフィードバックディスカッションで受け付けています。"
---

<p>ブランチプロテクションを管理するための<a href="https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization#repository">カスタムロールを作成</a>する際に、Admin ロールを付与する必要がなくなりました。以前は、ブランチプロテクションを管理するにはAdminである必要があり、必要でない可能性のある追加のパーミッションが提供されていました。管理者権限をより厳密に制御するために、<strong>リポジトリルールの編集</strong>権限を持つカスタムロールを作成し、適切な量のアクセスを許可することができるようになりました。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/7575792/215608072-49f28961-f372-445b-8575-dded7ab7df2a.png?ssl=1" alt="Image of Custom roles that shows the new Edit Repository Rules permission" data-recalc-dims="1"></p>
<p>このパーミッションは、次の両方の<em>作成</em>、<em>編集</em>、および<em>削除を</em>行う能力を付与します。 <strong><a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule">ブランチ保護ルール</a></strong>と <strong><a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/configuring-tag-protection-rules">保護タグ</a></strong>.</p>
<p>詳しくは、GitHub のドキュメントにある<a href="https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization">Managing custom repository roles for an organization</a>をご覧ください。</p>
<p>この件に関するフィードバックは、GitHub の<a href="https://github.com/orgs/community/discussions/categories/repositories">公開フィードバックディスカッションで</a>お願いします。</p>


