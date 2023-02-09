---
title: "Gradle、Maven、Scala、Millレポジトリでの依存関係サブミッションに関する提案"
englishtitle: "Dependency submission suggestions on Gradle, Maven, Scala and Mill repositories"
date: "2023-02-08"
cardurl: "https://github.blog/changelog/2023-02-08-dependency-submission-suggestions-on-gradle-maven-scala-and-mill-repositories"
author: "Kevin Duck"
description: " Dependency graph automatically supports many ecosystems , but some additional ecosystems require configuration to submit dependencies with the dependency submission API . The community maintains several GitHub Actions that make this easier.  Users with write access to Gradle, Maven, Scala, and Mill repositories now see messaging on their dependency graph that directs them to an action that will scan and submit dependencies for their ecosystem. Users with access to Dependabot alerts will also see messaging on their repository's Dependabot alerts tab.  Prompts will display if a repository includes any of the following files: pom.xml , build.gradle , build.gradle.kts , build.sbt , or build.sc .  The dependency graph team is working to have native support for these types of ecosystems with more news to come later this year.  Learn more about the dependency graph  Explore dependency submission actions in GitHub Marketplace  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/3474250/215532424-81457e15-5aa0-4bbf-bf51-d20f5bf6b7a3.png?ssl=1"
englishsummary: "  The dependency graph team is working to have native support for various ecosystems, with additional ecosystems requiring configuration to submit dependencies with the dependency submission API and GitHub Actions to make this easier, and more news to come later this year."
---

<p>Dependency Graphは<a href="https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph#supported-package-ecosystems">多くのエコシステムを</a>自動的にサポートしますが、いくつかの追加エコシステムでは、<a href="https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api">依存関係提出APIで</a>依存関係を提出するための設定が必要です。コミュニティは、これを容易にするためにいくつかのGitHub Actionsを維持しています。</p>
<p>Gradle、Maven、Scala、および Mill のリポジトリに書き込み権限を持つユーザは、依存性グラフに、そのエコシステムの依存性をスキャンして送信するアクションに誘導するメッセージが表示されるようになりました。Dependabotアラートへのアクセス権を持つユーザーは、リポジトリのDependabotアラートタブにメッセージも表示されるようになりました。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/3474250/215532424-81457e15-5aa0-4bbf-bf51-d20f5bf6b7a3.png?ssl=1" alt="img" data-recalc-dims="1"></p>
<p>リポジトリに<code>pom.xml</code>,<code>build.gradle</code>,<code>build.gradle.kts</code>,<code>build.sbt</code>,<code>build.scの</code>いずれかのファイルが含まれている場合、プロンプトが表示されます。</p>
<p>Dependency Graph チームは、これらのエコシステムのネイティブサポートに取り組んでおり、今年後半にさらなるニュースをお届けする予定です。</p>
<ul>
<li><a href="https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph">Dependency Graph についてもっと知る</a></li>
<li><a href="https://github.com/marketplace?query=dependency+submission+">GitHub Marketplace の Dependency Submission アクションを見る</a></li>
</ul>


