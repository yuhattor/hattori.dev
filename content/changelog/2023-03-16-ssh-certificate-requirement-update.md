---
title: "SSH Certificateの要件更新"
englishtitle: "SSH Certificate requirement update"
date: "2023-03-16"
cardurl: "https://github.blog/changelog/2023-03-16-ssh-certificate-requirement-update"
author: "Kevin Duck"
description: " The "Require SSH certificates" policy now allows GitHub apps to call Git APIs using a user-to-server token, bringing them up to parity with OAuth app support.  The SSH certificate requirement mandates that users in your organization call Git APIs using an SSH certificate issued by your organization, in place of their own SSH key or a PAT.  To support automation, it has an exception in place for OAuth apps and GitHub app server-to-server tokens, which allows applications you've approved to call Git APIs for your organization.  With this change, we are extending that exception to GitHub app user-to-server tokens, for when a user has signed into a GitHub app that's installed in your organization.  This change also applies when the enterprise-level setting requires SSH certificates across all organizations in the enterprise.  To learn more, see "Managing your organization's SSH certificate authorities" or "Managing SSH certificate authorities for your enterprise" .  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/1666363/225112716-0e0c0c73-ce3b-4b49-a1fe-46fdb9395a39.png?ssl=1"
englishsummary: ""
summary: ""
---

<p>SSH証明書を要求する」ポリシーで、GitHubアプリがユーザーからサーバーへのトークンを使ってGit APIを呼び出せるようになり、OAuthアプリのサポートと同等になった。</p>
<p>SSH証明書の要件は、組織内のユーザーが自分のSSHキーやPATの代わりに、組織が発行したSSH証明書を使用してGit APIを呼び出すことを義務付けています。<br />
自動化をサポートするために、OAuthアプリとGitHubアプリのサーバー間トークンについては例外を設けており、承認したアプリケーションが組織のGit APIを呼び出すことができるようになっています。<br />
今回の変更で、この例外を GitHub アプリのユーザーからサーバーへのトークンにも拡張します。これは、ユーザーが組織内にインストールされている GitHub アプリにサインインした場合のためです。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/1666363/225112716-0e0c0c73-ce3b-4b49-a1fe-46fdb9395a39.png?ssl=1" alt="Screenshot of the SSH Certificate requirement checkbox" data-recalc-dims="1"></p>
<p>この変更は、エンタープライズレベルの設定で、エンタープライズ内のすべての組織でSSH証明書を必要とする場合にも適用されます。</p>
<p>詳細については、<a href="https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-git-access-to-your-organizations-repositories/managing-your-organizations-ssh-certificate-authorities#adding-an-ssh-certificate-authority">「組織のSSH認証局の管理」</a>または<a href="https://docs.github.com/en/enterprise-cloud@latest/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-security-settings-in-your-enterprise#managing-ssh-certificate-authorities-for-your-enterprise">「企業のSSH認証局の管理</a>」を参照してください。</p>


