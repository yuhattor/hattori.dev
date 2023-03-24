---
title: "RSA SSHホストキーを更新しました"
subtitle: "3月24日05:00UTC頃、GitHub.comのGit操作の安全性を確保するために使用しているRSA SSHホスト鍵を、慎重を期して交換しました。"
englishsubtitle: "At approximately 05:00 UTC on March 24, out of an abundance of caution, we replaced our RSA SSH host key used to secure Git operations for GitHub.com."
englishtitle: "We updated our RSA SSH host key"
date: "2023-03-24"
cardurl: "https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/"
author: "Mike Hanley"
description: " At approximately 05:00 UTC on March 24, out of an abundance of caution, we replaced our RSA SSH host key used to secure Git operations for GitHub.com. We did this to protect our users from any chance of an adversary impersonating GitHub or eavesdropping on their Git operations over SSH. This key does not grant access to GitHub’s infrastructure or customer data. This change only impacts Git operations over SSH using RSA. Web traffic to GitHub.com and HTTPS Git operations are not affected.  Only GitHub.com’s RSA SSH key was replaced. No change is required for ECDSA or Ed25519 users. Our keys are documented here .  What happened and what actions have we taken?  This week, we discovered that GitHub.com’s RSA SSH private key was briefly exposed in a public GitHub repository. We immediately acted to contain the exposure and began investigating to understand the root cause and impact. We have now completed the key replacement, and users will see the change propagate over the next thirty minutes. Some users may have noticed that the new key was briefly present beginning around 02:30 UTC during preparations for this change.  Please note that this issue was not the result of a compromise of any GitHub systems or customer information. Instead, the exposure was the result of what we believe to be an inadvertent publishing of private information. We have no reason to believe that the expos"
coverimage: "https://github.blog/wp-content/uploads/2021/12/github-security_orange-banner.png?resize=1200%2C630"
category: "Security"
englishsummary: "ured key was used maliciously.  GitHub.com replaced its RSA SSH host key out of an abundance of caution after discovering it was briefly exposed in a public repository, and users should expect the change to propagate over the next thirty minutes"
summary: "の鍵が悪意を持って使用されていたことが判明しました。  GitHub.comは、RSA SSHホスト鍵が公開リポジトリで一時的に公開されていたことを発見した後、慎重を期して交換しました。"
---

<p>3月24日午前5時（UTC）頃、GitHub.comのGit操作を保護するために使用しているRSA SSHホスト鍵を交換しました。これは、GitHubになりすましたり、SSH経由でGitの操作を盗聴したりする可能性からユーザーを守るために行ったものです。この鍵は、GitHubのインフラや顧客データへのアクセスを許可するものではありません。この変更は、RSAを使用したSSH経由のGit操作にのみ影響します。GitHub.comへのウェブトラフィックやHTTPSでのGit操作には影響はありません。</p>
<p>GitHub.comのRSA SSH鍵のみが交換されました。ECDSAやEd25519のユーザーには変更の必要はありません。私たちの鍵は<a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints">ここに</a>文書化されています。</p>
<h3 id="what-happened-and-what-actions-have-we-taken">何が起こり、私たちはどのような行動をとったのか？<a href="#what-happened-and-what-actions-have-we-taken" class="heading-link pl-2 text-italic text-bold" aria-label="What happened and what actions have we taken?"></a></h3>
<p>今週、GitHub.comのRSA SSH秘密鍵がGitHubの公開リポジトリで短期間公開されたことが判明しました。私たちは直ちにこの暴露を食い止めるために行動し、根本的な原因と影響を理解するために調査を開始しました。現在、鍵の交換を完了し、今後30分ほどでユーザーには変更が反映される予定です。一部のユーザーは、この変更の準備中に、UTC2:30頃から新しいキーが一時的に存在していることに気づいたかもしれません。</p>
<p>この問題は、GitHubのシステムや顧客情報が侵害された結果ではないことに注意してください。この問題は、GitHubのシステムや顧客情報が侵害されたのではなく、個人情報を不用意に公開した結果であると考えられます。公開された鍵が悪用されたと考える理由はなく、慎重を期してこの措置をとりました。</p>
<h3 id="what-you-can-do">お客様ができること<a href="#what-you-can-do" class="heading-link pl-2 text-italic text-bold" aria-label="What you can do"></a></h3>
<p>ECDSAまたはEd25519の鍵を使用している場合は、何の変化もなく、何もする必要はありません。</p>
<p>SSHでGitHub.comに接続した際に以下のメッセージが表示された場合は、この先をお読みください。</p>
<pre><code>@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
警告：リモートホストの識別が変更されました！@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
誰かが何か悪さをしている可能性があります！
誰かが今まさにあなたのことを盗聴している可能性があります（中間者攻撃）！
また、ホストの鍵が変更されたばかりである可能性もあります。
リモートホストから送信されたRSA鍵のフィンガープリントは以下の通りです。
SHA256:uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s。
システム管理者にお問い合わせください。
このメッセージを消すには、~/.ssh/known_hostsに正しいホストキーを追加してください。
github.comのホスト鍵が変更され、厳密なチェックを要求しています。
ホストキーの検証に失敗しました。
</code></pre>
<p>上記のメッセージが表示された場合は、以下のコマンドを実行して、古い鍵を削除する必要があります：</p>
<pre><code>$ ssh-keygen -R github.com
</code></pre>
<p>または、手動で<code>~/.ssh/known_hosts</code>ファイルを更新して、古いエントリーを削除します。</p>
<p>次に、以下の行を手動で追加して、新しいRSA SSH公開鍵のエントリーを<code>~/.ssh/known_hosts</code>ファイルに追加してください：</p>
<pre><code>github．com ssh-ラーザAAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk=
</code></pre>
<p>または、ターミナルで以下を実行して、<code>~/.ssh/known_hosts</code> にある GitHub.com の RSA SSH 鍵を自動的に更新します：</p>
<pre><code>$ ssh-keygen -R github.com
$ curl -L https://api.github.com/meta | jq -r '.ssh_keys | .[]'.| sed -e 's/^/github.com /' &gt;&gt; ~/.ssh/known_hosts
</code></pre>
<p>以下のフィンガープリントが表示されることを確認することで、ホストが私たちの新しいRSA SSH鍵を介して接続していることを確認することができます：</p>
<pre><code>SHA256:uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s
</code></pre>
<p>GitHub Actionsのユーザーで、a<code>ctions/checkoutを</code> <code>ssh-key</code>オプションで使用している場合、ワークフローの実行に失敗することがあります。私たちは、@v2、@v3、@mainを含むすべてのサポートされたタグの<code>actions/checkout</code>アクションを更新しています。アクションをコミットSHAに固定し、<code>ssh-key</code>オプションを使用する場合、ワークフローを更新する必要があります。このプロセスについては、<a href="https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#reusing-third-party-workflows">Actionsセキュリティハードニングの公式ドキュメントで</a>詳しく説明しています。</p>
<p>さらに詳しい情報は、<a href="https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints">GitHubのSSH公開鍵フィンガープリントに関する公式</a>ドキュメントをご覧ください。</p>


