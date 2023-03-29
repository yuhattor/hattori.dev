---
title: "Gitのブランチプロテクトを回避するための情報メッセージ"
englishtitle: "Info messages for bypassing branch protections in Git"
date: "2023-03-29"
cardurl: "https://github.blog/changelog/2023-03-29-info-messages-for-bypassing-branch-protections-in-git"
author: "Kevin Duck"
description: " We now show bypassed branch protection rules in response to Git pushes. These are information messages and are not designed to block workflows.  Historically there was no indication after a Git push that branch rules had been bypassed.  Repo admins, actors with the bypass branch protections permissions , and actors in bypass lists on branch protections will now see a list of rules that were bypassed.  We appreciate your feedback in GitHub's public feedback discussions  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/7575792/228326077-f6cc9a18-1819-4faf-b006-4c0adcae4553.png?w=600&ssl=1"
englishsummary: "  Git pushes now display a list of rules that were bypassed, providing feedback to repo admins, actors with the bypass branch protections permissions, and actors in bypass lists on branch protections."
summary: "  Git のプッシュで、バイパスされたルールのリストが表示されるようになり、レポ管理者、ブランチプロテクトのバイパス権限を持つアクター、ブランチプロテクトのバイパスリストのアクターにフィードバックされるようになりました。"
---

<p>Gitのプッシュに対応して、<a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule">ブランチ保護ルールが</a>バイパスされたことを表示するようになりました。これは<code>情報</code>メッセージであり、ワークフローをブロックするためのものではありません。</p>
<p>これまでは、Gitプッシュの後にブランチルールがバイパスされたことを示すことはありませんでした。</p>
<p>レポ管理者、<a href="https://docs.github.com/en/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization#repository">ブランチプロテクトのバイパス権限を</a>持つアクター、ブランチプロテクトのバイパスリストに含まれるアクターには、バイパスされたルールのリストが表示されるようになりました。</p>
<p align="left">
<img decoding="async" alt="Screenshot of Git command line interface showing list of rules" src="https://i0.wp.com/user-images.githubusercontent.com/7575792/228326077-f6cc9a18-1819-4faf-b006-4c0adcae4553.png?w=600&#038;ssl=1" data-recalc-dims="1">
</p>
<p>GitHubの<a href="https://github.com/orgs/community/discussions/categories/repositories">パブリックフィードバックディスカッションでの</a>ご意見をお待ちしております。</p>


