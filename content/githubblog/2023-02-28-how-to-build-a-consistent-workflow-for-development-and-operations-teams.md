---
title: "開発チームと運用チームの一貫したワークフローを構築する方法"
subtitle: "GitHubとHashiCorpの連携により、企業は一貫したワークフローとアクションで、より速く、より安全に開発し、顧客に出荷することができるようになります。"
englishsubtitle: "Explore how using GitHub and HashiCorp together enables enterprises to develop and ship to their customers faster and more secure with consistent workflows and actions."
englishtitle: "How to build a consistent workflow for development and operations teams"
date: "2023-02-28"
cardurl: "https://github.blog/2023-02-28-how-to-build-a-consistent-workflow-for-development-and-operations-teams/"
author: "Mark Paulsen"
description: " In GitHub’s recent 2022 State of the Octoverse report , HashiCorp Configuration Language (HCL) was the fastest growing programming language on GitHub. HashiCorp is a leading provider of Infrastructure as Code (IaC) automation for cloud computing. HCL is HashiCorp’s configuration language used with tools like Terraform and Vault to deliver IaC capabilities in a human-readable configuration file across multi-cloud and on-premises environments.  HCL’s growth shows the importance of bringing together the worlds of infrastructure, operations, and developers. This was always the goal of DevOps. But in reality, these worlds remain siloed for many enterprises.  In this post we’ll look at the business and cultural influences that bring development and operations together, as well as security, governance, and networking teams. Then, we’ll explore how GitHub and HashiCorp can enable consistent workflows and guardrails throughout the entire CI/CD pipeline.  The traditional world of operations (Ops)  Armon Dadgar, co-founder of HashiCorp, uses the analogy of a tree to explain the traditional world of Ops. The trunk includes all of the shared and consistent services you need in an enterprise to get stuff done. Think of things like security requirements, Active Directory, and networking configurations. A branch represents the different lines of business within an enterprise, providing servic"
coverimage: "https://github.blog/wp-content/uploads/2022/12/1200x640-1.png?resize=1200%2C640"
category: "Engineering,Enterprise,Product,DevOps,GitOps,HCL,Infrastructure as Code"
englishsummary: "ers to those lines of business.  HashiCorp Configuration Language (HCL)'s growth shows the importance of bringing together the worlds of infrastructure, operations, and developers, which is the goal of DevOps, but many enterprises still remain sil"
summary: ""
---

<p>GitHubが最近発表した「<a href="https://octoverse.github.com/">2022 State of the Octoverse」レポートにおいて</a>、HashiCorp Configuration Language（HCL）がGitHubで<a href="https://octoverse.github.com/2022/top-programming-languages">最も成長したプログラミング言語と</a>なりました。HashiCorpは、クラウドコンピューティングのためのInfrastructure as Code (IaC) 自動化のリーディングプロバイダーです。HCLは、<a href="https://www.terraform.io/">Terraformや</a> <a href="https://www.vaultproject.io/">Vaultなどの</a>ツールと共に使用されるHashiCorpの設定言語で、マルチクラウドやオンプレミス環境において、人間が読みやすい設定ファイルでIaC機能を提供することができます。</p>
<p>HCLの成長は、インフラ、運用、開発者の世界を一つにすることの重要性を示しています。これは常にDevOpsの目標でした。しかし、現実には、多くの企業でこれらの世界がサイロ化したままになっています。</p>
<p>この記事では、開発チームと運用チーム、そしてセキュリティ、ガバナンス、ネットワーク・チームを結びつけるビジネスと文化の影響について見ていきます。そして、GitHubとHashiCorpがCI/CDパイプライン全体を通して一貫したワークフローとガードレールをどのように実現できるかを探ります。</p>
<h2 id="the-traditional-world-of-operations-ops">従来の運用（Ops）の世界<a href="#the-traditional-world-of-operations-ops" class="heading-link pl-2 text-italic text-bold" aria-label="The traditional world of operations (Ops)"></a></h2>
<p>HashiCorpの共同創業者であるArmon Dadgar氏は、従来のOpsの世界を「<a href="https://www.youtube.com/watch?v=1Fca7S5BP1k%E2%80%A6%E2%80%A6%E2%80%A6">木」に例えて</a>説明しています。トランクには、物事を成し遂げるために企業で必要な、共有され一貫性のあるサービスがすべて含まれています。セキュリティ要件、Active Directory、ネットワーク構成などを考えてみてください。ブランチは、企業内のさまざまなビジネスラインを表し、社内または社外にサービスや製品を提供します。葉は、ソフトウェアやサービスが展開されるさまざまな環境と技術を表します。クラウド、オンプレミス、コンテナ環境などです。</p>
<p>多くの企業では、これらの異なるビジネス領域間のコミュニケーション・チャネルやプロセスが煩雑で、コストがかかる場合があります。インフラやアーキテクチャに大きな変更があった場合、通常、複数のチケットが複数のチームに提出され、企業内のさまざまな部署でレビューと承認が行われます。組織を保護するために、変更諮問委員会が一般的に使用されます。通常、文書化が完了しない限り、変更を進めることはできません。一般的に、将来の監査に必要な一連のガバナンスログと監査可能な成果物が存在します。</p>
<p>もし、チームが最適化された自動化されたワークフローを持ち、それを使って納期を早め、安全なガードレールのセットで仕事を終わらせることができるようになったら、企業にとってより有益ではないでしょうか？これは、時間とコストの大幅な節約につながり、ビジネス価値の向上につながる可能性があります。</p>
<p><a href="https://github.blog/2022-12-20-increase-developer-productivity-save-time-on-developer-onboarding-and-drive-roi-in-2023/">最近のForresterのレポートでは</a>、GitHubを使うことで3年間で433%のROIを達成したという結果が出ています。もちろん、時間の節約や効率の向上は言うまでもなく、一貫性と作業の合理化によってもたらされるその他の質的なメリットもあります。</p>
<p>あなたの製品やサービスは、遅々として進まない、手作業でエラーが起こりやすいプロセスではなく、セキュリティとガバナンスが組み込まれた最適化された経路でデプロイされることになるでしょう。これこそ、<a href="https://resources.github.com/devops/">DevOps</a>、<a href="https://opengitops.dev/">GitOps</a>、<a href="https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition">Cloud Nativeの</a>夢ではないでしょうか？</p>
<h2 id="introducing-iac">IaCの導入<a href="#introducing-iac" class="heading-link pl-2 text-italic text-bold" aria-label="Introducing IaC"></a></h2>
<p>別の例えを使いましょう。IaCは、ソフトウェアやサービスをホストするリソース（サーバー、データベース、ネットワークコンポーネント、PaaSサービスなど）の設計図だと考えてください。</p>
<p>病院と学校を設計する場合、両シナリオで同じ全体的な設計図を使用することはないでしょう。なぜなら、両シナリオはまったく異なる目的を持ち、要件も大きく異なるからです。しかし、2つの設計にまたがって再利用できる構成要素や基礎があるはずです。</p>
<p>HCLのようなIaCソリューションでは、ソフトウェア開発でメソッド、モジュール、パッケージライブラリを再利用するのと同様に、これらのビルディングブロックを定義して再利用することができます。IaCであるため、アプリケーションでコラボレーションやデプロイを行う際に使用するのと同じ推奨プラクティスをインフラに採用することができます。</p>
<p>結局のところ、<a href="https://resources.github.com/devops/#devops-benefits">DevOpsの方法論を</a>採用するチームは、生産性、クラウド対応のスケーラビリティ、コラボレーション、およびセキュリティが向上することが分かっているのです。</p>
<h2 id="a-better-way-to-deliver">より良いデリバリー方法<a href="#a-better-way-to-deliver" class="heading-link pl-2 text-italic text-bold" aria-label="A better way to deliver"></a></h2>
<p>このような背景から、インフラストラクチャをコード化することで得られる具体的なメリットと、それが従来の運用文化の変革にどのように役立つかを探ってみましょう。</p>
<h3 id="storing-code-in-repositories">リポジトリにコードを保存する<a href="#storing-code-in-repositories" class="heading-link pl-2 text-italic text-bold" aria-label="Storing code in repositories"></a></h3>
<p>まずは、最も低いところにある果実から始めましょう。IaCであれば、GitHubなどのソースコード・リポジトリにインフラストラクチャやアーキテクチャ・パターンを保存することができます。これにより、完全なバージョン履歴を持つ単一のソース・オブ・トゥルースを手に入れることができる。これにより、必要に応じて変更をロールバックしたり、履歴から特定のバージョンの真実をデプロイしたりすることが容易にできるようになります。</p>
<p>企業内のチームは、Git リポジトリ内の個別の<a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches">ブランチで</a>コラボレーションを行うことができます。ブランチを使うことで、チームや個人は「自分のスペース」で生産的になり、「本番」の真実のソース（通常はメインブランチ）から離れて、他のチームの進行中の作業に悪影響を与えることを心配する必要がなくなります。</p>
<p>前節で述べた再利用可能なビルディングブロックであるTerraformモジュールも、Gitリポジトリに保存されバージョン管理されています。そこからTerraform Cloudのプライベートレジストリにインポートすることで、全チームが簡単にモジュールを発見できるようになります。GitHubで新しいリリースバージョンのタグが付けられると、レジストリにも自動的に更新されます。</p>
<h3 id="collaborate-early-and-often">早期かつ頻繁にコラボレーションする<a href="#collaborate-early-and-often" class="heading-link pl-2 text-italic text-bold" aria-label="Collaborate early and often"></a></h3>
<p>上で説明したように、チームは現在の状態に影響を与えないように、別々のブランチで変更を加えることができます。しかし、その変更を本番環境のコードベースに反映させたい場合はどうすればいいのでしょうか。もしあなたが Git に慣れていないのなら、<a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">プルリクエストという</a>言葉を聞いたことがないかもしれません。その名のとおり、あるブランチから別のブランチに変更を「引き込む」ことができます。</p>
<p>GitHub のプルリクエストは、チーム内の他のユーザーとコラボレーションするためのすばらしい方法です。ピアレビューを受けることで、フィードバックを自分の作業に反映させることができます。プルリクエストのプロセスは、チーム全体のコラボレーションを促進するために意図的に非常にソーシャルになっています。</p>
<p>GitHub では、ブランチ保護ルールを設定してメインブランチへの直接の変更を不可とすることもできます。そうすれば、すべてのユーザーがコードを実運用に移すにはプルリクエストを経由しなければならなくなります。ブランチ保護ルールには、最低限必要なレビュアーの人数を指定することもできます。</p>
<blockquote><p>
 <strong>ヒント:</strong>GitHub の<a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners">CODEOWNERS ファイルという</a>特殊なファイルを使えば、編集中のファイルに基づいてプルリクエストにレビュアーを自動的に追加することができます。例えば、すべてのHCLファイルは、コアインフラストラクチャチームによるレビューが必要かもしれません。あるいは、勘定系システムのIaC設定には、コンプライアンスチームによるレビューが必要かもしれません。
</p></blockquote>
<p>通常、特定の周期で行われる変更諮問委員会とは異なり、プルリクエストはコードを本番環境に導入するためのプロセスの自然な一部となります。また、意思決定や議論の質も向上します。外部システムで推奨される「イエス/ノー」の決定ではなく、プルリクエストで直接コンテキストと推奨を確認することができます。</p>
<p>プロビジョニングプロセスではコラボレーションも重要です。GitHubとTerraform Cloudの統合により、これらのプロセスを複数のチーム間でスケールさせることができます。Terraform Cloud は Terraform の状態を安全に保存し、GitHub リポジトリと直接統合することで、プルリクエストとマージのライフサイクルをターンキーで体験できるようなワークフロー機能を提供します。</p>
<h3 id="bringing-automated-quality-reviews-into-the-process">自動化された品質レビューをプロセスに取り入れる<a href="#bringing-automated-quality-reviews-into-the-process" class="heading-link pl-2 text-italic text-bold" aria-label="Bringing automated quality reviews into the process"></a></h3>
<p>前節の続きですが、プルリクエストでは、提案された変更の品質を自動的にチェックすることもできます。ソフトウェアでは、アプリケーションが正しくコンパイルされているか、ユニットテストは合格しているか、セキュリティの脆弱性はないかなどをチェックするのが一般的です。</p>
<p>IaCの観点からは、同様の自動チェックを我々のプロセスに取り入れることができます。Git<a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks">Hub のステータスチェックを</a>使えば、特定の条件を満たしているかどうかを明確に把握することができます。</p>
<p>GitHub Actions は、GitHub のプルリクエストでこうした自動チェックを実行するためによく使われるものです。IaCの品質を判断するために、以下のようなチェックを入れることができます。</p>
<ul>
<li>コードが構文的に正しいかどうかを検証する（例えば<a href="https://developer.hashicorp.com/terraform/cli/commands/validate">Terraform validate</a>）。</li>
<li>コードが特定の標準に従っていることを確認するためのLinting（例えば、<a href="https://github.com/terraform-linters/tflint">TFLintや</a> <a href="https://developer.hashicorp.com/terraform/cli/commands/fmt">Terraform format</a>）。</li>
<li>静的コード解析により、「設計時」にインフラストラクチャの設定ミスを特定します (たとえば、<a href="https://github.com/aquasecurity/tfsec">tfsec</a>や<a href="https://github.com/tenable/terrascan">terrascan</a> など)。</li>
<li>関連するユニットテストまたは統合テスト（<a href="https://terratest.gruntwork.io/">Terratest</a> などのツールを使用）。</li>
<li>インフラストラクチャを「スモークテスト」環境にデプロイし、インフラストラクチャの構成が（既知のパラメータセットと共に）望ましい状態にデプロイされることを検証します。</li>
</ul>
<p>Terraform on GitHubを使い始めるのは簡単です。Terraformのバージョンは<a href="https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software">LinuxベースのGitHubでホストされたランナーにインストール</a>されていますし、HashiCorpには<a href="https://github.com/marketplace/actions/hashicorp-setup-terraform">公式のGitHub Actionがあり、</a>指定したTerraformバージョンを使ってランナーに<a href="https://github.com/marketplace/actions/hashicorp-setup-terraform">Terraformをセットアップして</a>くれます。</p>
<h3 id="compliance-as-an-automated-check">自動チェックとしてのコンプライアンス<a href="#compliance-as-an-automated-check" class="heading-link pl-2 text-italic text-bold" aria-label="Compliance as an automated check"></a></h3>
<p>先日、デリバリーパイプラインにコンプライアンス、セキュリティ、監査を組み込むことと、このアプローチの利点について<a href="https://github.blog/2023-01-26-setting-the-foundations-for-compliance/">ブログを</a>書きました。既存の開発パイプラインやワークフローに IaC を追加すると、以前は手動だったコンプライアンステストや成果物を、HCL の設定ファイルに直接コードとして記述することができるようになります。</p>
<p>IaCの自然な拡張として、<a href="https://docs.hashicorp.com/sentinel/concepts/policy-as-code">コードとしてのポリシーは</a>、セキュリティとコンプライアンスチームが組織の要求の定義を一元化することを可能にします。Terraform CloudはHashiCorp SentinelとOpen Policy Agent (OPA)のフレームワークをサポートしており、GitHubリポジトリからポリシーセットを自動的に取り込み、すべてのプロビジョニング実行に一貫して適用することができます。これにより、設定ミスが本番環境に出る前に、ポリシーが適用されるようになります。</p>
<p>最近の別の<a href="https://github.blog/2023-02-24-3-ways-to-meet-compliance-needs-without-slowing-down-agility/">ブログで</a>言及された追加ボーナスは、AIを搭載したコンプライアンスソリューションを活用して、配信をさらに最適化する能力です。AIが、開発およびインフラのデリバリー・パイプライン全体にわたって、手作業なしでコンプライアンスに焦点を当てたユニットテストを生成する未来を想像してみてください。</p>
<h3 id="security-in-the-background">バックグラウンドでのセキュリティ<a href="#security-in-the-background" class="heading-link pl-2 text-italic text-bold" aria-label="Security in the background"></a></h3>
<p>依存関係を最新の状態に保つための便利なツール、Dependabotをご存じかもしれません。しかし、Dependabot が<a href="https://github.blog/changelog/2021-06-10-dependabot-now-supports-terraform-1-0/">Terraform をサポートして</a>いることをご存知でしょうか？つまり、<a href="https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates#supported-repositories-and-ecosystems">Terraformのプロバイダやモジュールのバージョンを最新に保つために、Dependabotを</a>利用することができるのです。</p>
<h2 id="checks-complete-time-to-deploy">チェック完了、デプロイの時間<a href="#checks-complete-time-to-deploy" class="heading-link pl-2 text-italic text-bold" aria-label="Checks complete, time to deploy"></a></h2>
<p>チェックが完了したら、次は新しいインフラ構成をデプロイする番です！ブランチやデプロイ戦略は、この先も続きます。ブランチやデプロイの戦略については、この記事の範囲外なので、別の議論に譲りましょう。</p>
<p>しかし、GitHub Actions はデプロイの面でも役に立ちます。先ほど説明したように、GitHub上でTerraformを使い始めるのは簡単です。Terraformのバージョンは<a href="https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners#preinstalled-software">LinuxベースのGitHubでホストされているランナーにインストール</a>されていますし、HashiCorpには<a href="https://github.com/marketplace/actions/hashicorp-setup-terraform">公式のGitHub Actionがあり、</a>指定したTerraformのバージョンを使ってランナー上に<a href="https://github.com/marketplace/actions/hashicorp-setup-terraform">Terraformをセットアップして</a>くれます。</p>
<p>しかし、これをさらに進化させることができるのですTerraformでは、変更を本番環境に反映させる前に、<code>terraform</code> <code>planという</code>コマンドを使って変更の影響を把握するのが一般的です。</p>
<h3 id="reviewing-environment-changes-in-a-pull-request">プルリクエストで環境の変更を確認する<a href="#reviewing-environment-changes-in-a-pull-request" class="heading-link pl-2 text-italic text-bold" aria-label="Reviewing environment changes in a pull request"></a></h3>
<p>HashiCorp は、<a href="https://developer.hashicorp.com/terraform/tutorials/automation/github-actions">GitHub Actions を使って Terraform を自動化</a>する例を示しています。この例では、GitHub Actionsを使ってTerraform Cloudによるリリースをオーケストレーションしています。この例では、<code>terraform plan</code>コマンドの出力をプルリクエストにコピーして承認します（これも、選択した開発フローに依存します）。</p>
<h3 id="reviewing-environment-changes-using-github-actions-environments">GitHub Actions の環境を使った環境変更のレビュー<a href="#reviewing-environment-changes-using-github-actions-environments" class="heading-link pl-2 text-italic text-bold" aria-label="Reviewing environment changes using GitHub Actions environments"></a></h3>
<p><a href="https://www.hashicorp.com/blog/automate-infrastructure-provisioning-workflows-with-the-github-action-for-terraform">HashiCorpの</a>例をもとに、もうひとつの例を考えてみましょう。GitHub Actions には、environment (<a href="https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment">環境</a>) という概念が組み込まれています。この環境は、目標とするデプロイ先への論理的なマッピングだと考えてください。保護ルールを環境と関連づけることで、デプロイ前に承認が得られるようになります。</p>
<p>では、GitHub Action のワークフローを作りましょう。2 つの環境 (計画用とデプロイ用の 2 つ) を用意します。</p>

```
name: 'Review and Deploy to EnvironmentA'
on: [push]

jobs:
  review:
    name: 'Terraform Plan'
    environment: environment_a_plan
    runs-on: ubuntu-latest

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v2

      - name: 'Terraform Setup'
        uses: hashicorp/setup-terraform@v2
        with:
          cli_config_credentials_token: ${{ secrets.TF_API_TOKEN }}

      - name: 'Terraform Init'
        run: terraform init


      - name: 'Terraform Format'
        run: terraform fmt -check

      - name: 'Terraform Plan'
        run: terraform plan -input=false

  deploy:
    name: 'Terraform'
    environment: environment_a_deploy
    runs-on: ubuntu-latest
    needs: [review]

    steps:
      - name: 'Checkout'
        uses: actions/checkout@v2

      - name: 'Terraform Setup'
        uses: hashicorp/setup-terraform@v2
        with:
          cli_config_credentials_token: ${{ secrets.TF_API_TOKEN }}

      - name: 'Terraform Init'
        run: terraform init

      - name: 'Terraform Plan'
        run: terraform apply -auto-approve -input=false
```

<p>ワークフローを実行する前に、<a href="https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#deleting-an-environment">GitHubのリポジトリに環境を作成</a>し、保護ルールを<code>environment_a_deployに</code>関連付けることができます。つまり、本番デプロイの前にレビューが必要です。</p>
<h2 id="learn-more">もっと詳しく<a href="#learn-more" class="heading-link pl-2 text-italic text-bold" aria-label="Learn more"></a></h2>
<p><a href="https://www.hashicorp.com/resources/a-practitioner-s-guide-to-using-hashicorp-terraform-cloud-with-github">HashiCorpのTerraform CloudをGitHubで使うための実践的なガイド</a>で、始めるにあたっての一般的な推奨事項を確認してください。また、GitHubがどのように<a href="https://www.hashicorp.com/case-studies/github">Terraformを利用してミッションクリティカルな機能をより早く、より低コストで</a>提供しているかをご覧ください。</p>
<aside class="p-4 p-md-6 post-aside--large"><p class="h5-mktg gh-aside-title">3月9日にHashiCorpとGitHubによるWebセミナーを開催します。</p><p>GitHub上のHashiCorp Cloud Platform (HCP)を使って、HashiCorpがどのようにCI/CDパイプラインのセキュリティと高速化を実現するか、より深く掘り下げます。GitHubをトリガーとした実際のリリースパイプラインの詳細なデモを共有しながら、CI/CDガバナンスのベストプラクティスと、エンドツーエンドプロセスにセキュリティを構築し、大規模なエンタープライズアプリケーション管理およびデリバリーのガバナンスと品質要件を確実に満たす方法に関する苦労話について検討します。<a href="https://resources.github.com/devops/ci-cd-with-github-actions/"><strong>登録はこちらから</a></strong>. <a href="https://resources.github.com/devops/ci-cd-with-github-actions/"><img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/webinar.png?w=1024&#038;resize=1024%2C538" alt="" width="1024" height="538" class="aligncenter size-large wp-image-70356 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/webinar.png?w=1280 1280w, https://github.blog/wp-content/uploads/2023/02/webinar.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/webinar.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/webinar.png?w=1024&#038;resize=1024%2C538 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></a></p>
</aside>


