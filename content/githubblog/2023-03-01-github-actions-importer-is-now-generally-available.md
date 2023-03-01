---
title: "GitHub Actions Importerの一般提供を開始しました。"
subtitle: "この度、GitHub Actions Importerの一般提供を開始しました。GitHub Actions Importerは、Azure DevOps、CircleCI、GitLab、Jenkins、Travis CIからGitHub Actionsへの移行を計画、予測、自動化することができます。本製品はGitHubの公式CLIの拡張機能であり、本日よりGitHubユーザーであれば誰でも無料で利用することができます。マイグレーション [...]..."
englishsubtitle: "We’re excited to announce the general availability of GitHub Actions Importer. GitHub Actions Importer helps you plan, forecast, and automate migrations from Azure DevOps, CircleCI, GitLab, Jenkins, and Travis CI to GitHub Actions. This product is an extension of the official GitHub CLI and is available for free to any GitHub user starting today. Migrating […]"
englishtitle: "GitHub Actions Importer is now generally available"
date: "2023-03-01"
cardurl: "https://github.blog/2023-03-01-github-actions-importer-is-now-generally-available/"
author: "Dawit Gebregziabher"
description: " We’re excited to announce the general availability of GitHub Actions Importer. GitHub Actions Importer helps you plan, forecast, and automate migrations from Azure DevOps, CircleCI, GitLab, Jenkins, and Travis CI to GitHub Actions. This product is an extension of the official GitHub CLI and is available for free to any GitHub user starting today.  Migrating to a new CI/CD tool is often a manual and time-intensive endeavor. This is more pronounced for users that have a large and sophisticated CI/CD infrastructure—for instance, some of our largest customers have more than 15 thousand pipelines to migrate. Additionally, manual migrations introduce the potential for regressions in newly created pipelines. GitHub Actions Importer is designed to help plan and automate a large portion of the migration to provide teams with the speed and confidence to continue delivering software efficiently.  Why GitHub Actions?  GitHub Actions provides access to powerful, native CI/CD capabilities right next to your code hosted in GitHub. GitHub Actions is simple to enable and painless to maintain within your current GitHub workflow as there’s no longer a need to install, integrate, and maintain a third-party tool. GitHub Actions, along with other GitHub Enterprise offerings, improves developer productivity by 22% and reduces time spent managing tools and code infrastructure by 75%. Additionally, th"
coverimage: "https://github.blog/wp-content/uploads/2023/03/image-11.png?resize=1600%2C850"
category: "Enterprise,Product,GitHub Actions"
englishsummary: "  GitHub Actions Importer is designed to help plan and automate migrations from Azure DevOps, CircleCI, GitLab, Jenkins, and Travis CI to GitHub Actions, providing teams with the speed and confidence to continue delivering software efficiently."
summary: "  GitHub Actions Importerは、Azure DevOps、CircleCI、GitLab、Jenkins、Travis CIからGitHub Actionsへの移行を計画・自動化し、チームにスピードと自信を与え、効率的にソフトウェアを配信し続けることを支援するために設計されています。"
---

<p>この度、GitHub Actions Importerの一般提供を開始しました。GitHub Actions Importerは、Azure DevOps、CircleCI、GitLab、Jenkins、Travis CIからGitHub Actionsへの移行を計画、予測、自動化することができます。本製品は<a href="https://cli.github.com/">GitHubの</a>公式<a href="https://cli.github.com/">CLIの</a>拡張機能であり、本日よりGitHubユーザーであれば誰でも無料で利用することができます。</p>
<p>新しいCI/CDツールへの移行は、多くの場合、手作業で時間のかかる作業となります。これは、大規模で洗練されたCI/CDインフラを持つユーザーにとってより顕著です。例えば、私たちの最大の顧客の中には、移行するパイプラインが1万5千以上あるところもあります。さらに、手作業による移行は、新しく作成されたパイプラインにリグレッションが発生する可能性があります。GitHub Actions Importerは、マイグレーションの大部分を計画し自動化することで、チームが効率的にソフトウェアを提供し続けるためのスピードと自信を提供するために設計されています。</p>
<h3 id="why-github-actions">なぜGitHub Actionsなのか？<a href="#why-github-actions" class="heading-link pl-2 text-italic text-bold" aria-label="Why GitHub Actions?"></a></h3>
<p>GitHub Actionsは、GitHubでホストされているコードのすぐそばで、パワフルでネイティブなCI/CD機能を利用することができます。GitHub Actionsは、サードパーティツールをインストール、統合、維持する必要がないため、現在のGitHubワークフローの中で簡単に利用することができ、維持にも手間がかかりません。GitHub Actionsは、他のGitHub Enterprise製品と共に、<a href="https://resources.github.com/forrester/?utm_source=&#038;utm_medium=&#038;utm_campaign=2020q3-site-ww-ForresterReport&#038;utm_content=Blog">開発者の生産性を22%向上さ</a>せ、ツールやコードインフラの管理に費やす時間を75%削減することができます。さらに、信頼できる検証済みのパートナーやOSSコミュニティが提供する何千ものビルド済みアクションにより、GitHubのインターフェースを離れずにソフトウェアを提供することがこれまで以上に簡単にできるようになりました。</p>
<h2 id="how-it-works">仕組み<a href="#how-it-works" class="heading-link pl-2 text-italic text-bold" aria-label="How it works"></a></h2>
<p>GitHub Actions Importer は、移行プロセスを簡素化するために段階的なアプローチを使用しています。</p>
<ol>
<li><strong>計画。</strong>このフェーズでは、既存のCI/CDの使用状況を分析し、移行のためのロードマップを構築します。</p>
</li>
<li>
<p><strong>テスト。</strong>移行したワークフローが既存のパイプラインと同じように機能することを検証するために、ドライランの移行を実施します。GitHub Actions Importer はこのステップで無制限の繰り返しをサポートし、カスタム動作が新しい GitHub Actions ワークフローに正確にカプセル化されることを確認します。</p>
</li>
<li>
<p><strong>移行。</strong>この最後のフェーズでは、GitHub Actions Importer が有効なワークフローを生成し、それを GitHub リポジトリに追加するためのプルリクエストを発行します。移行を完了させるには、これらのワークフローをレビューし、自動的に移行されなかった構造を移行する必要があります。</p>
</li>
</ol>
<h2 id="getting-started">はじめに<a href="#getting-started" class="heading-link pl-2 text-italic text-bold" aria-label="Getting started"></a></h2>
<p>GitHub Actions Importer を今すぐ使い始めるには、GitHub の<a href="https://gh.io/actions-importer-documentation">ドキュメントを</a>ご覧ください。</p>
<hr>
<div class="mod-vh position-relative" style="height: 0; padding-bottom: calc((9 / 16)*100%);">
			<iframe loading="lazy" class="position-absolute top-0 left-0 width-full height-full" src="https://www.youtube.com/embed/WqiGP6h4fa0?version=3&#038;rel=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;fs=1&#038;hl=en-US&#038;autohide=2&#038;wmode=transparent" title="YouTube video player" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0"></iframe>
		</div>
<hr>
<h2 id="looking-ahead">今後の展望<a href="#looking-ahead" class="heading-link pl-2 text-italic text-bold" aria-label="Looking ahead"></a></h2>
<p>今後数ヶ月の間に、GitHub Actions Importer の強化や更新を続け、追加の CI/CD ツールをサポートする予定です。GitHub Actions Importerの今後の展開については、GitHubの<a href="https://github.com/orgs/github/projects/4247">ロードマップを</a>ご覧ください。いつも通り、皆様からのご意見をお待ちしております。フィードバックは<a href="https://gh.io/actions-importer-feedback">こちらで受け付けて</a>います。</p>


