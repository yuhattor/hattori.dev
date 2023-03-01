---
title: "すべての公開リポジトリでシークレットスキャンアラートが無料で利用可能になりました！"
subtitle: "シークレットスキャンアラートが、すべての公開リポジトリで一般に利用できるようになりました。管理者はワンクリックでアラート体験をオンにできるようになりました。"
englishsubtitle: "Secret scanning alerts are now generally available for all public repositories. Admins can now turn on the alert experience with one click."
englishtitle: "Secret scanning alerts are now available (and free) for all public repositories"
date: "2023-02-28"
cardurl: "https://github.blog/2023-02-28-secret-scanning-alerts-are-now-available-and-free-for-all-public-repositories/"
author: "Zain Malik"
description: " In December, we announced the public beta for free secret scanning alerts across public repositories . Since its release, 70 thousand public repositories have turned on secret scanning alerts, helping users like you to triage thousands of leaked secrets.  As of today, GitHub secret scanning’s alert experience is generally available and free for all public repositories. You can enable secret scanning alerts across all the repositories you own to notify you of leaked secrets across your full repository history including code, issues, description, and comments.  GitHub secret scanning works with 100+ service providers in the GitHub Partner Program. In addition to alerting users, we will continue to notify our partners when one of their secrets is leaked. But with secret scanning alerts enabled, you’ll now also receive alerts for secrets where it’s not possible to notify a partner–for example, if self-hosted keys are exposed–along with a full audit log of actions taken on the alert.  This empowers you with full visibility into your risk at scale. One example of this in practice is @rajbos , DevOps Consultant and Trainer, who enabled secret scanning on approximately 14 thousand repositories and discovered over one thousand secrets. Rob remarked, “My research proves the point to why everyone should have secret scanning enabled. I have researched 14 thousand public GitHub Action repo"
coverimage: "https://github.blog/wp-content/uploads/2022/01/Security-Open-Source-Product.png?resize=1200%2C630"
category: "Open Source,Security,Secret Scanning"
englishsummary: ""
summary: "GitHubのシークレットスキャンは現在、すべての公開リポジトリを対象に無料で提供されており、ユーザーが数千件の流出シークレットを発見し、トリアージするのに役立っています。"
---

<p>12月、私たちは<a href="https://github.blog/2022-12-15-leaked-a-secret-check-your-github-alerts-for-free/">公開リポジトリ全体で無料の秘密スキャンアラートを提供するパブリックベータを</a>発表しました。リリース以来、7万ものパブリックリポジトリがシークレットスキャンアラートを有効にし、あなたのようなユーザーが何千もの流出した秘密をトリアージするのに役立っています。</p>
<p><strong>本日より、GitHubのシークレットスキャンのアラート機能は、すべてのパブリックリポジトリで無料でご利用いただけるようになりました。所有するすべてのリポジトリでシークレットスキャンのアラートを有効にすると、コード、課題、説明、コメントなどリポジトリの全履歴にわたって流出した秘密を通知することができます。</strong></p>
<p>GitHubの秘密スキャンは、GitHubパートナープログラムに参加している100社以上のサービスプロバイダーと連携しています。ユーザーへのアラートに加え、パートナーの秘密が流出した際にも引き続き通知します。しかし、シークレットスキャンアラートを有効にすると、パートナーに通知することができないシークレット（例えば、セルフホスティングのキーが公開された場合）についても、アラートに対するアクションの完全な監査ログと一緒にアラートを受け取ることができるようになりました。</p>
<p><strong>これにより、大規模なリスクを完全に可視化することができます。</strong>DevOpsコンサルタント兼トレーナーの<a href="https://github.com/rajbos">@rajbosは</a>、約14,000のリポジトリで秘密スキャンを有効にし、1,000以上の秘密を発見しました。Rob は次のように述べています。「私の調査は、誰もが秘密スキャンを有効にすべき理由を証明しています。私は14,000の公開GitHub Actionリポジトリを調査し、その中から1,000以上の秘密を発見しました！" と述べています。</p>
<p>"GitHub Advanced Securityの使い方について多くの人にトレーニングしているにもかかわらず、私はこれを通じて自分のリポジトリに秘密を発見してしまいました。"</p>
<p class="purple-text text-gradient-purple-coral mt-6 mb-6">複数年の経験があるにもかかわらず、自分自身にも起こることです。それくらい、間違ってシークレットを入れてしまうことは簡単なことなのです。</p>
<p>"シークレットスキャンを有効にすると、シークレットが通知され、パートナーはすでにそれを自動的に取り消すことができるので、コードの世界をもう少し安全にすることができます。"Robの体験談は、彼の<a href="https://devopsjournal.io/blog/2023/01/22/Making-the-case-for-secret-scanning">ブログ記事で</a>お読みください。</p>
<h2 id="get-started-in-one-click">ワンクリックで開始<a href="#get-started-in-one-click" class="heading-link pl-2 text-italic text-bold" aria-label="Get started in one click"></a></h2>
<p>公開リポジトリの所有者または管理者であれば、誰でも秘密スキャンアラートを有効にすることができます。企業管理者と組織の所有者は、複数のリポジトリに対して一括してアラートを有効にすることもできます。これを行うには、「設定」タブに移動し、「セキュリティ」の「コードセキュリティと分析」をクリックします。Secret scanning」を見つけて、「Enable」をクリックします。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/Feb-15-2023-13-16-37.gif" alt="Gif demonstrating how to enable secret scanning on the &quot;Settings&quot; menu under the section labeled &quot;Security.&quot;"></p>
<p>リポジトリに対してシークレットスキャンの警告を有効にする方法については、<a href="https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning">ドキュメントで</a>詳しく説明しています。</p>
<h3 id="become-a-github-secret-scanning-partner">GitHub のシークレットスキャンパートナーになる<a href="#become-a-github-secret-scanning-partner" class="heading-link pl-2 text-italic text-bold" aria-label="Become a GitHub secret scanning partner"></a></h3>
<p>もしあなたがサービスプロバイダーで、共有ユーザーを秘密の漏洩から守ることに興味があるなら、秘密<a href="https://docs.github.com/en/developers/overview/secret-scanning-partner-program">スキャンパートナープログラムに</a>参加することをおすすめします。現在、200以上のパターンと100以上の<a href="https://docs.github.com/en/code-security/secret-scanning/secret-scanning-patterns#supported-secrets-for-partner-patterns">パートナーを </a>サポートしています。まずは、<a href="mailto:secret-scanning@github.com">secret-scanning@github.com</a> までメールをお送りください。</p>


