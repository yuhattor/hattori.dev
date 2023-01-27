---
title: コンプライアンスの基盤整備
subtitle: 開発者対応型コンプライアンスへの基礎固めを実施
englishsubtitle: Laying the groundwork for developer-enabled compliance.
englishtitle: Setting the foundations for compliance
date: 2023-01-26
cardurl: https://github.blog/2023-01-26-setting-the-foundations-for-compliance/
author: Mark Paulsen
description: While compliance is foundational to delivering software around the world, there may be instances where developers get frustrated with policy enforcement slowing down their workflow.
coverimage: https://github.blog/wp-content/uploads/2023/01/This-Grid-1200x640-10.png?resize=1200%2C640
category: Enterprise,compliance
---

<p>コンプライアンスは世界中にソフトウェアを届けるための基礎ですが、ポリシーの強制によってワークフローが遅くなることに開発者が不満を感じる場合もあるかもしれません。</p>
<p>セキュリティ、データ、プライバシーの要件や規制が異なる地域や企業間で世界中のソフトウェアを実行できるようにするのがコンプライアンスなので、私たちGitHubはビジネスのニーズと開発者の幸福のバランスをとることに精通しています。<a href="https://github.blog/2023-01-25-100-million-developers-and-counting/">1億人の開発</a>者とFortune 100の90%がGitHub上でソフトウェアを構築しているのですから。</p>
<p>ここでは、開発者が最高の仕事をするためのツールを提供し、かつビジネスのコンプライアンスニーズを満たす方法について深く掘り下げていきましょう。</p>
<h2 id="compliance-defined">コンプライアンスの定義<a href="#compliance-defined" class="heading-link pl-2 text-italic text-bold" aria-label="Compliance, defined"></a></h2>
<p>コンプライアンスを辞書で厳密に<a href="https://www.merriam-webster.com/dictionary/compliance">定義</a>すると、「願望、要求、提案、方式に従うこと」「強制に従うこと」「公式の要件を満たすこと」に焦点が当てられます。  この定義から、柔軟性、開放性、コラボレーションを重視する開発コミュニティで、コンプライアンスがあまり議論されない理由がわかります。</p>
<p>より開発者やクラウドネイティブに優しい定義は、<a href="https://martinfowler.com/articles/devops-compliance.html">Office of Compliance</a>(OoC) の記述に見ることができます。OoC は、コンプライアンスを "達成すべき望ましい結果一式と、本番環境に配備する前にシステムを検証する必要のあるプロセス" とみなしています。  理想的な状態とその状態に到達するためのプロセスを定義することは、公式の要件に従うよう強制されるよりもずっと良いように聞こえます。</p>
<h2 id="setting-the-groundwork-for-compliance">コンプライアンスのための基礎固め<a href="#setting-the-groundwork-for-compliance" class="heading-link pl-2 text-italic text-bold" aria-label="Setting the groundwork for compliance"></a></h2>
<p>コンプライアンスというと敷居が高いように思われるかもしれませんが、成功するためにまず理解しておくべき、非常に実践的な考え方があります。</p>
<h3 id="understanding-your-population">母集団を把握する<a href="#understanding-your-population" class="heading-link pl-2 text-italic text-bold" aria-label="Understanding your population"></a></h3>
<p>これは当たり前のことですが、コードがどこにあり、開発者が誰であるかを知らなければ、ソフトウェア開発のコンプライアンスニーズに対応できないことを明記しておきます。</p>
<p>コードがGitHubのようなプラットフォームで一元管理されている場合、この最初のコンセプトはカバーされているはずです。  もしコードを一元管理できるプラットフォームがない場合は、まず使用しているすべてのツールを見つけ、そのツールにアクセスできるすべての開発者のリストを取得する必要があります。  ご想像の通り、これは時間のかかる作業であり、母集団が完全である保証はありません。</p>
<h3 id="understanding-access">アクセスの把握<a href="#understanding-access" class="heading-link pl-2 text-italic text-bold" aria-label="Understanding access"></a></h3>
<p>母集団を理解したら、次に誰が何にアクセスできるかを理解する必要があります。  コードは、おそらく組織内で最も重要な情報の一部であり、開発者が安全に利用できるようにする必要があります。 <a href="https://www.microsoft.com/en-us/security/business/security-101/what-is-information-security-infosec">CIAの三原則は</a>、コードの安全性を確保し、必要な人だけがアクセスできるようにするための仕組みを提供します。</p>
<ul>
<li><strong>機密性</strong>：組織は、許可されたユーザーのみが情報にアクセスできるようにするための対策を制定する必要があります。</li>
<li><strong>完全性</strong>：正確で信頼できるデータが重要であり、権限のないユーザーがアクセス、変更、またはその他の方法で干渉することを許可しない。</li>
<li><strong>可用性</strong>：許可されたユーザーが必要な時に、信頼できる一貫したデータへのアクセスを保証すること。</li>
</ul>
<p>GitHubは、個人や企業がコードへのアクセスをコントロールできるようにするために、すべての<a href="https://docs.github.com/en/repositories">リポジトリや</a>その他のリソースに<a href="https://docs.github.com/en/get-started/learning-about-github/access-permissions-on-github">アクセス権限を</a>設定し、各ユーザーが業務に必要なものだけにアクセスできるようにしています（最小権限の原則とも呼ばれる）。エンタープライズアカウントという概念は、GitHubのコアに組み込まれています。これにより、アクセスを総合的に管理し、既存のプロバイダーと統合してチームを同期させ、管理を容易にし、ガードレールを設定してエンジニアリングチームの安全な基盤を確保することができるようになります。</p>
<p>世界中の開発者のうち<a href="https://github.blog/2023-01-25-100-million-developers-and-counting/">1億</a>人がGitHubを利用しているため、個人と企業のすべての開発者が必要なときにいつでも利用できるようにします。コミュニティへのコミットメントとして、<a href="https://www.githubstatus.com/">GitHubの可用性</a>レポートを毎月公開し、必要なときにコードが利用可能であることを確認しています。</p>
<p>GitHub Enterprise のような中央のツールを使うことで、必要な管理のオーバーヘッドを減らすことができます。もし、現在のツール環境が複雑になりすぎていて、何か助けが必要な場合は、最近のブログポスト「<a href="https://github.blog/2022-10-26-3-strategies-for-consolidating-your-toolkit-and-boosting-productivity/">ツールキットを統合するための3つのヒント</a>」をご覧ください。</p>
<h3 id="user-attestation">ユーザー認証<a href="#user-attestation" class="heading-link pl-2 text-italic text-bold" aria-label="User attestation"></a></h3>
<p>この段階では、コードがどこにあるか、ユーザーの人口、CIAの3要素に対処していることを確認するための管理方法を理解しています。次に、ユーザーが持つアクセス権を定期的に証明するプロセスを導入する必要があります。従業員が別の役割に移ったり、会社を辞めたりした場合、そのアクセスを確実に取り消すためのプロセスを導入する必要があります。</p>
<p>今後のブログでは、<a href="https://github.com/features/actions">GitHub Actions</a> による自動化と、<a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">プルリクエストによる</a>開発者のワークフローを活用して、ユーザーの認証に関連するコンプライアンスを最適化する方法について説明します。</p>
<h3 id="continuous-compliance">継続的なコンプライアンス<a href="#continuous-compliance" class="heading-link pl-2 text-italic text-bold" aria-label="Continuous Compliance"></a></h3>
<p><a href="https://resources.github.com/ci-cd/">継続的インテグレーション（CI）/継続的デリバリー（CD</a>）という言葉は誰もが知っていると思いますが、何かを継続的に行うというコンセプトは、コンプライアンスにも適用できます。CI/CDの大きなメリットの1つは<a href="https://resources.github.com/ci-cd/#ci-cd-benefits">スピード</a>です。コンプライアンステストや監査が、DevOpsのCI/CDパイプラインのように高速でシームレスに行われる世界を想像してみてください。</p>
<p>継続的なコンプライアンスは一晩で魔法のように現れるわけではありませんが、コンプライアンスの基礎となる部分を理解し、その下準備を始めていれば、コンプライアンスのテストと監査をより速くするいくつかの大きな利点が得られます。</p>
<h5 id="1-no-surprises">1.不意打ちを食らわない。<a href="#1-no-surprises" class="heading-link pl-2 text-italic text-bold" aria-label="1. No surprises."></a></h5>
<p>コンプライアンス・テストや監査が始まるときに起こりうる最悪のシナリオの1つは、驚かされたり、準備不足になったりすることです。テスト担当者や監査担当者が新しい成果物を要求してきたからと言って、新しい成果物を作成する必要はありません。</p>
<h5 id="2-common-understanding">2.共通の理解<a href="#2-common-understanding" class="heading-link pl-2 text-italic text-bold" aria-label="2. Common understanding."></a></h5>
<p><a href="https://cdn2.hubspot.net/hubfs/228391/Corporate/DevOps_Audit_Defense_Toolkit_v1.0.pdf?t=1453925000299">DevOps監査防御ツールキットの</a>主な目標は、コミュニケーションを改善し、共通の理解を生み出し、"IT管理者と実務者を監査プロセスについて教育し、監査人に対して、ビジネスリスクを理解し、そのリスクを適切に軽減していることを証明できるようにする "ことでした。ITと監査人のコミュニケーションと情報共有が改善されれば、監査がより効率的になり、Forresterによれば、<a href="https://resources.github.com/forrester/">大幅なコスト削減</a>が可能になります。</p>
<h5 id="3-built-into-developer-workflows">3.開発者のワークフローに組み込まれる。<a href="#3-built-into-developer-workflows" class="heading-link pl-2 text-italic text-bold" aria-label="3. Built into developer workflows."></a></h5>
<p>ソフトウェアデリバリーライフサイクルの基礎からコンプライアンスが設計されている場合、開発者は日々のフローの一部として、必要なコントロールを満たし、成果物を収集することになります。</p>
<h3 id="ai-enabled-compliance">AIで実現するコンプライアンス<a href="#ai-enabled-compliance" class="heading-link pl-2 text-italic text-bold" aria-label="AI-Enabled compliance"></a></h3>
<p>GitHubでは、すでに機械学習を活用して、セキュリティやコンプライアンスに重要な<a href="https://github.blog/2022-02-17-leveraging-machine-learning-find-security-vulnerabilities/">セキュリティ脆弱</a>性を発見するための支援を行っています。製造業では、<a href="https://www.businesswire.com/news/home/20221215005002/en/DarwinAI-brings-AI-powered-Visual-Quality-Inspection-to-market-and-announces-a-funding-round-led-by-BDC-Capital-to-accelerate-growth"> 監査や工程検査の</a>支援にAIが採用され始めています。また、ガートナーは、<a href="https://www.gartner.com/en/newsroom/press-releases/2022-05-24-gartner-identifies-three-technology-trends-gaining-tr">銀行が </a>詐欺の検出やリスクのモデリングに近々活用する技術として、ジェネレーティブAIを挙げています。</p>
<p>AIや機械学習を継続的なコンプライアンスに活用することのメリットと可能性は、非常に魅力的です。今後のブログでは、その先にあるものを詳しく見ていきたいと思います。</p>
<h2 id="next-steps">次のステップ<a href="#next-steps" class="heading-link pl-2 text-italic text-bold" aria-label="Next steps"></a></h2>
<p>このようなコンプライアンスの基礎的な側面がよく理解できたら、これらのコンセプトを実装するための次のステップについて考え始めることができます。これが難しいところです。次回の記事では、開発者を満足させながらコンプライアンスの必要性を満たす、いくつかの実用的な方法を紹介します。</p>
<div class="post-content-cta"><p>安全性とコンプライアンスを保ちつつ、開発者の作業効率を上げるにはどうしたらいいでしょうか?<a href="https://github.com/enterprise">GitHub Enterprise</a> がどのように役立つかを見てみましょう。</p>
</div>


