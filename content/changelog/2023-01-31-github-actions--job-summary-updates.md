---
title: "GitHubのアクション。ジョブサマリーの更新"
englishtitle: "GitHub Actions: Job summary updates"
date: "2023-01-31"
cardurl: "https://github.blog/changelog/2023-01-31-github-actions-job-summary-updates"
author: "Kevin Duck"
description: "We are making chnages to job summaries and logs in GitHub Actions that will impact customers using self-hosted runners. Over the next six months, customers using self-hosted runners will need to ensure machines have appropriate network access to communicate with the GitHub hosts below so that job summaries and logs emitted from Actions workflows can work as expected."
coverimage: ""
---

<p>GitHub Actionsのジョブサマリーとログに変更があり、セルフホストランナーをご利用のお客様に影響があります。今後6ヶ月間、セルフホストランナーをご利用のお客様は、Actions ワークフローから出力されるジョブサマリーやログが期待通りに動作するよう、マシンが以下の GitHub ホストと通信できる適切なネットワークアクセスを持っていることを確認する必要があります。</p>
<ul>
<li><code>アクション-結果-レシーバー-production.githubapp.com</code></li>
<li><code>productionresultssa*.blob.core.windows.net</code></li>
</ul>
<p>2023年7月31日以降、セルフホストランナーを使用していて、前述のホストを許可するようにネットワークアクセス設定を更新していない場合、ジョブサマリーやログが正しく表示されない可能性があります。</p>
<p>詳しくは以下をご覧ください。<br />
<a href="https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#communication-between-self-hosted-runners-and-github">セルフホストランナーとGitHubの通信について</a>」をご覧ください。</p>
<p>ご質問は、<a href="https://github.com/orgs/community/discussions/categories/actions-and-packages">GitHub Actions コミュニティ</a>をご覧ください。</p>
<p>Actions の今後の予定については、<a href="https://github.com/orgs/github/projects/4247/views/1?filterQuery=actions">公開されているロードマップを</a>ご覧ください。</p>


