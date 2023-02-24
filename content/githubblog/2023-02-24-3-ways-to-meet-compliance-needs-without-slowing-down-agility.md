---
title: "アジリティを低下させることなく、コンプライアンスのニーズに応える3つの方法"
subtitle: "安全性とコンプライアンスを維持しながら、開発者の生産性とコラボレーションを可能にする方法をご紹介します。ビジネスを停滞させることなく、コンプライアンスを維持します。セキュリティからCI/CDまで、ソフトウェアワークフローのあらゆるステップを自動化することで、開発者は最も重要な「構築」に集中することができます。"
englishsubtitle: "Learn how to enable developer productivity and collaboration while staying secure and compliant. Stay compliant without slowing down your business. From security to CI/CD, automate every step of your software workflow—so your developers can stay focused on what matters most: building."
englishtitle: "3 ways to meet compliance needs without slowing down agility"
date: "2023-02-24"
cardurl: "https://github.blog/2023-02-24-3-ways-to-meet-compliance-needs-without-slowing-down-agility/"
author: "Mark Paulsen"
description: " In the previous blog, Setting the foundations for compliance , we set the groundwork for developer-enabled compliance that will keep your teams happy, in the flow, secure, compliant, and auditable.  Today, we’ll walk through three practical ways that you can start meeting your compliance requirements without having to revolutionize or transform the culture in your company—all while enabling your developers to be more productive and happy.  1. Do the basics well and often  The first way to start meeting your compliance requirements is often overlooked because it’s so simple. No matter what industry you are in, whether it’s finance, automotive, government, or tech, there are some basic quick compliance wins that may be part of your existing developer workflows and culture.  Code review  A key part of writing clean code is code review. But having a repeatable and traceable code review process is also a foundational component of your compliance program. This ensures risks within software delivery are found and mitigated early—and are also auditable for future reviews.  Food for thought  Code is not limited to software! Think about infrastructure as code and policy as code. Access management is often an area that is considered in compliance reviews. Did you know that GitHub recently open sourced ‘Entitlements’ , the identity and access management solution that we use internally?  G"
coverimage: "https://github.blog/wp-content/uploads/2023/02/3-compliance-post.png?resize=1200%2C640"
category: "Engineering,Enterprise,Security,code scanning,compliance,Dependabot"
englishsummary: "ather compliance requirements   By following three practical steps, you can start meeting your compliance requirements without having to revolutionize or transform the culture in your company, while enabling developers to be more productive and happy."
summary: "コンプライアンス要件に対応 3つの実践的なステップを踏むことで、社内の文化を変革することなく、コンプライアンス要件を満たし、開発者の生産性と幸福度を向上させることが可能になります。"
---

<p>前回のブログ「<a href="https://github.blog/2023-01-26-setting-the-foundations-for-compliance/">コンプライアンスの基礎を固める</a>」では、開発者がコンプライアンスに対応できるようにするための基礎知識を紹介しました。</p>
<p>本日は、開発者の生産性と満足度を高めながら、企業文化を変革することなくコンプライアンス要件を満たすための 3 つの実践的な方法について説明します。</p>
<h1 id="1-do-the-basics-well-and-often">1.基本的なことをきちんと、頻繁に行う<a href="#1-do-the-basics-well-and-often" class="heading-link pl-2 text-italic text-bold" aria-label="1. Do the basics well and often"></a></h1>
<p>コンプライアンス要件に対応するための最初の方法は、非常に単純であるため、見過ごされがちです。金融、自動車、政府機関、ハイテクなど業種を問わず、開発者のワークフローや企業文化の一部として、コンプライアンスを迅速に達成するための基本的な方法があります。</p>
<h2 id="code-review">コードレビュー<a href="#code-review" class="heading-link pl-2 text-italic text-bold" aria-label="Code review"></a></h2>
<p><a href="https://scrumdictionary.com/term/clean-code/">クリーンなコードを</a>書くために重要なのは、コードレビューです。しかし、反復可能で追跡可能なコードレビュープロセスを持つことは、コンプライアンスプログラムの基礎となる要素でもあります。これにより、ソフトウェアのデリバリーにおけるリスクが早期に発見され、緩和されるとともに、将来のレビューのために監査可能であることが保証されます。</p>
<aside class="p-4 p-md-6 post-aside--large"><p class="h5-mktg gh-aside-title">考えるためのヒント</p><p>コードはソフトウェアに限定されるものではありません。インフラストラクチャはコードであり、ポリシーはコードであると考えてください。アクセス管理は、しばしばコンプライアンスレビューで検討される分野です。私たちが社内で使っているアイデンティティとアクセス管理のソリューションである<a href="https://github.blog/2022-06-09-introducing-entitlements-githubs-open-source-identity-and-access-management-solution/">「Entitlements」が、最近GitHubによってオープンソース化</a>されたことをご存知でしょうか。</p>
</aside>
<p>GitHubでは、何百万人もの開発者が毎日利用している<a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">プルリクエストが</a>既存のワークフローの一部となっているため、コードレビューが容易になっています。GitHubはまた、コンプライアンステスターや監査役がプルリクエストをレビューするのも簡単で、一元化された場所にある不変の監査ログにアクセスすることができます。</p>
<aside class="post-aside--small float-sm-right col-sm-5 col-md-6 col-lg-5 my-5 my-sm-2 ml-sm-4 ml-lg-6"><p class="h6-mktg gh-aside-title">ヒント!</p><p><a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule">ブランチ保護ルールを使って</a>、ブランチに対するプルリクエストを強制できることをご存知ですか？自動チェックを指定したり、このルールに管理者を含めるかどうかを指定したりすることもできます。</p>
</aside>
<h2 id="separation-of-duties">職務の分離<a href="#separation-of-duties" class="heading-link pl-2 text-italic text-bold" aria-label="Separation of duties"></a></h2>
<p>企業によっては、職務の分離とは、トランザクションやプロセスを手動で管理しすぎている<em>人の</em>ことだと定義されていることがあります。これは、最新の<a href="https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition">クラウドネイティブの</a>プラクティスを導入する際に、不安になる可能性があります。</p>
<p>ありがたいことに、職務分掌に対するより現代的なアプローチをサポートする業界からのガイダンスがあります。 <a href="https://www.pcidssguide.com/pci-dss-requirement-6/">PCI-DSS 要件ガイドでは</a>、<em>個人という</em>用語を使用せず、機能と<em>アカウントに</em>焦点を当てることで、よりクラウド ネイティブに適したアプローチを提供しています。</p>
<blockquote><p>「この要件の目的は、開発およびテスト機能を本番機能から分離することです。例えば、開発者は開発環境では昇格した特権を持つ管理者レベルのアカウントを使用し、本番環境にはユーザーレベルのアクセス権を持つ別のアカウントを持つことができます。"とあります。</p></blockquote>
<p>このアプローチは、クラウドネイティブの<a href="https://12factor.net/">12ファクターアプリケーションの</a>方法論とよく合致しています。<a href="https://learn.microsoft.com/en-us/dotnet/architecture/cloud-native/definition">Build, release, run factorの</a>説明では、「各リリースは、ビルド、リリース、実行の各段階において厳格な分離を実施する必要があります。各リリースには一意のIDが付与され、ロールバック機能をサポートする必要がある "とあります。チームは、機能の分離と一意のIDへのトレーサビリティがある限り、手動でコントロールしすぎる人を心配することなく、生産へのデリバリーを完全に自動化することができます。さらに、PCI-DSSのような業界のベストプラクティスや要件に沿ったものであることが保証されます。</p>
<p>職務の分離を可能にするためには、明確なアイデンティティとアクセス管理戦略を持つ必要があります。ありがたいことに、車輪の再発明をする必要はありません。GitHub Enterprise には、開発環境全体へのアクセスを管理するためのオプションがいくつか用意されています。</p>
<ul>
<li><a href="https://docs.github.com/en/enterprise-cloud@latest/admin/identity-and-access-management/using-saml-for-enterprise-iam/configuring-saml-single-sign-on-for-your-enterprise">企業向けのSAMLシングルサインオンを設定</a>することができます。これは追加チェックで、ユーザーの真正性を自社の ID プロバイダーに対して確認することができます (ただし、自社の GitHub アカウントはそのまま使用します)。</li>
<li>そして、<a href="https://docs.github.com/en/enterprise-cloud@latest/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group">チームのメンバーシップを</a>ID プロバイダーのグループと<a href="https://docs.github.com/en/enterprise-cloud@latest/organizations/organizing-members-into-teams/synchronizing-a-team-with-an-identity-provider-group">同期さ</a>せることができます。その結果、ID プロバイダでグループのメンバーシップを変更すると、GitHub のチーム・メンバーシップ (および関連するアクセス権) も更新されます。</li>
<li>あるいは、GitHub<a href="https://docs.github.com/en/enterprise-cloud@latest/admin/identity-and-access-management/using-enterprise-managed-users-for-iam/about-enterprise-managed-users">Enterprise Managed Users</a>(EMUs)を採用することもできます。これはGitHub Enterpriseの一種で、IDプロバイダを通じて一元管理されたアカウントでのみログインできる。ユーザーは個人アカウントでGitHubにログインする必要はなく、会社のリソースにアクセスするためにシングルサインオンを使用することができます。(これについては、EMUの探索とそれがもたらすメリットについて、<a href="https://github.blog/2022-12-20-emus-more-than-just-flightless-birds/">こちらのブログ</a>記事をご覧ください)。</li>
</ul>
<h2 id="ai-powered-compliance">AIを活用したコンプライアンス<a href="#ai-powered-compliance" class="heading-link pl-2 text-italic text-bold" aria-label="AI-powered compliance"></a></h2>
<p>前回の<a href="https://github.blog/2023-01-26-setting-the-foundations-for-compliance/">ブログでは</a>、AIを活用したコンプライアンスと、<a href="https://github.blog/2023-02-14-github-copilot-now-has-a-better-ai-model-and-new-capabilities/">セキュリティ</a>、製造業、銀行における既存の機会のいくつかを簡単に取り上げました。また、コンプライアンスの基本をさらに最適化する可能性のある機会がいくつか控えています。</p>
<p><a href="https://www.microsoft.com/en-us/worklab/kevin-scott-on-5-ways-generative-ai-will-transform-work-in-2023">生成的なAI</a>ツールを活用することで、ユニットテストを独自に作成し、宣言型DevOpsワークフローで職務分離が確実に実施されるようになる可能性は十分にあります。  生成的AIの非決定的な性質のため、実行するたびに異なる結果が出るかもしれませんし、ユニットテストにはまだ誰も思いつかないようなリスクシナリオが含まれるかもしれません。これによって、真のリスクベースコンプライアンスを驚くほど高めることができるのです。</p>
<p>デリバリーにおいてコンプライアンスによく取り組むことの大きなメリットの1つは、<a href="https://www.forbes.com/sites/forbestechcouncil/2022/03/17/how-to-build-trust-with-continuous-compliance/">信頼度の</a>向上です。しかし、信頼を定量化することは非常に難しく、特に<a href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-deep-learning/">ディープラーニングソリューションを</a>活用したいと考えている規制された業界内では困難です。これは、継続的なコンプライアンスを可能にするだけでなく、企業がビジネス価値を向上させる新しいテクノロジーを導入する際にも役立ちます。</p>
<h2 id="dependency-management">ディペンデンシー・マネジメント<a href="#dependency-management" class="heading-link pl-2 text-italic text-bold" aria-label="Dependency management"></a></h2>
<p>企業は、サプライチェーンにおいて、オープンソースソフトウェアへの依存度を高めています。その結果、依存関係管理のための最適化された、繰り返し可能で可聴な管理は、あらゆる業界のコンプライアンスプログラムの基礎になりつつあります。</p>
<aside class="p-4 p-md-6 post-aside--large"><p class="h5-mktg gh-aside-title">ご存じですか？</p><p>The Linux Foundation は、<a href="https://slsa.dev/">Supply chain Levels for Software Artifacts (SLSA)</a> を制定しました。これはオープンなセキュリティフレームワークで、ソフトウェアのサプライチェーン全体のセキュリティを向上させるための標準的なチェックのセットを提供するために使用されています。</p>
</aside>
<p>GitHubの観点から、Dependabotはあなたのサプライチェーンが安全であるという確信を提供することができます。Dependabotを設定すると、開発者はセキュリティ上の脅威が発見されるとすぐに警告を受け、通常のワークフローで対策を講じることができるようになります。</p>
<p>Dependabotを活用することで、既知の脆弱性を持つソフトウェアの依存関係をリポジトリが使用した場合、不変かつ監査可能なアラートを受け取ることができます。プルリクエストは、開発者またはセキュリティチームによって起動され、将来のレビューのために監査可能なアーティファクトの別のセットを与えることができます。</p>
<aside class="post-aside--small float-sm-right col-sm-5 col-md-6 col-lg-5 my-5 my-sm-2 ml-sm-4 ml-lg-6"><p class="h6-mktg gh-aside-title">ヒント!</p><p>Dependabotは、たとえ緊急のセキュリティ問題がない場合でも、依存関係を最新に保つのに役立ちます。</p>
</aside>
<h2 id="approvals">承認<a href="#approvals" class="heading-link pl-2 text-italic text-bold" aria-label="Approvals"></a></h2>
<p>ほとんどの組織には承認プロセスがありますが、時間がかかったり、プロセスの後半で発生したりすることがあります。Google は、DORA 2019 state of DevOps レポートの結果に基づき、<a href="https://cloud.google.com/architecture/devops/devops-process-streamlining-change-approval">ピアレビューが変更承認プロセスの合理化に</a>役立つと説明しています。</p>
<p>デリバリーパイプラインには、リリース前の要件のサインオフ、テスト結果、セキュリティレビュー、本番運用準備の確認など、承認が必要な管理ポイントが多数存在する可能性があります。</p>
<p>社内の体制や連携に応じて、プロセス全体のさまざまな段階でチームにサインオフを求めることができます。ビルドとテストの段階では、プルリクエストで手動承認を行うことで、必要なレビューを収集することができます。</p>
<aside class="post-aside--small float-sm-right col-sm-5 col-md-6 col-lg-5 my-5 my-sm-2 ml-sm-4 ml-lg-6"><p class="h6-mktg gh-aside-title">ヒント!</p><p><a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners">CODEOWNERS ファイルを使用して</a>、変更されたファイルに依存するプルリクエストにユーザーまたはチームを自動的に割り当てることができます。たとえば、特定のチームがdocsコンテンツを所有している場合、CODEOWNERSファイルでそれらに対してdocsフォルダを指定することができます。</p>
</aside>
<p>ビルドとテストが完了したら、コードをインフラストラクチャにリリースする時が来ました。デプロイメント・パターンと戦略について話すことは、この記事の範囲外です。しかし、デプロイメントプロセスの一部として、承認が必要になる場合があります。</p>
<p>これらの承認を得るために、<a href="https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment">デプロイメントに環境を</a>使用する必要があります。環境は、デプロイメント ターゲット（ステージング、テスト、本番など）を記述するために使用されます。環境を使うことで、GitHub Actions がデプロイを開始する前に<a href="https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#required-reviewers">手動で承認を</a>得ることができるようになります。</p>
<p>どちらの場合も、必要な承認回数を決める際にはトレードオフの関係にあることを忘れないようにしましょう。必要なレビューの数を多く設定しすぎると、手作業が必要になるため配信のペースに影響が出る可能性があります。可能であれば、チェックを自動化して手動によるオーバーヘッドを減らし、全体的な敏捷性を最適化することを検討してください。</p>
<aside class="post-aside--small float-sm-right col-sm-5 col-md-6 col-lg-5 my-5 my-sm-2 ml-sm-4 ml-lg-6"><p class="h6-mktg gh-aside-title">ヒント!</p><p>ユニットテストやファジングなどのチェックを自動化する場合は、ソース管理されていることに留意してください。これは、トレーサビリティにおいて大きな利点となり、エラーを起こしやすい手動チェックに頼るよりも、どの品質チェックが実行されたかを正確に把握することができるようになります。</p>
</aside>
<h1 id="2-have-a-common-understanding-of-concepts-and-terms">2.コンセプトと用語の共通理解<a href="#2-have-a-common-understanding-of-concepts-and-terms" class="heading-link pl-2 text-italic text-bold" aria-label="2. Have a common understanding of concepts and terms"></a></h1>
<p>これもまた、当たり前のことのように聞こえるので、見過ごされるかもしれません。しかし、開発者やDevOps、クラウドネイティブの実務者が日常的に使っている概念や用語で、コンプライアンステスターや監査人がまったく理解できないものは、おそらくたくさんあるはずです。</p>
<p>2015年のことですが、<em>The Phoenix Projectの</em>著者であるGene Kim氏と他の数名の著者が、<a href="https://cdn2.hubspot.net/hubfs/228391/Corporate/DevOps_Audit_Defense_Toolkit_v1.0.pdf?t=1453925000299">DevOps Audit Defense Toolkitを</a>作成しました。最初のブログで述べたように、この文書の目的は、"IT管理者と実務者が監査プロセスについて教育し、監査人に対して、ビジネスリスクを理解し、そのリスクを適切に軽減していることを証明できるようにする "ことでした。しかし、何から始めればいいのでしょうか？</p>
<p>以下に、GitHubに関連する管理目標に関する基本的な用語のチートシートと、コンプライアンス、規制、リスク、監査などの世界とのマッピングを示します。開発者とコンプライアンスや監査担当者の間で共通の理解を得るためのよいきっかけになるでしょう。</p>
<div class="content-table-wrap"><table>
<tr>
<td><strong>目的</strong>
   </td>
<td><strong>統制</strong>
   </td>
<td><strong>財務報告</strong>
   </td>
<td><strong>業界のフレームワーク</strong>
   </td>
</tr>
<tr>
<td>コードレビューコントロールは、セキュリティ要件に対応しているか、コードが理解可能で、保守可能で、適切にフォーマットされているかを確認します。
   </td>
<td>プルリクエストは、GitHub上のリポジトリでブランチにプッシュした変更を他の人に伝えることができます。プルリクエストがオープンされると、自分の変更がベースブランチにマージされる前に、共同作業者と変更の可能性について議論したりレビューしたり、フォローアップコミットを追加したりすることができます。
   </td>
<td>SOX: 変更管理</p>
<p>COSO:統制活動-アプリケーションの変更管理を実施する。
   </td>
<td>NIST Cyber:DE.CM-4 -悪意のあるコードが検出される。</p><p>

PCI-DSS：6.3.2。すべてのカスタムコードに脆弱性がないか、手動または自動でレビューする。</p>
<p>
SLSA: 二人によるレビューは、誤りを発見し、悪質な行為を抑止するための業界のベストプラクティスである。
   </td>
</tr>
<tr>
<td>パスワードとセキュリティトークンについて、コードリポジトリをスキャンするためのコントロールとプロセスを導入すること。  秘密が本番環境に到達しないように、防止策を実施する必要があります。
   </td>
<td>秘密スキャンは、GitHub リポジトリに存在するすべてのブランチの Git 履歴全体をスキャンし、秘密を探します。  GitHubプッシュ保護は、開発者がコードをプッシュする際に信頼性の高い秘密をチェックし、秘密が確認された場合はプッシュをブロックします。
   </td>
<td>SOX: ITセキュリティ</p>
<p>
COSO統制活動-セキュリティの向上
   </td>
<td>NIST Cyber:PR.DS-5：情報漏えいに対する保護が実施されている。</p>
<p>
PCI-DSS：6.5.3。セキュリティが不十分な暗号鍵の保管から保護する。
   </td>
</tr>
</table></div>
<p>これをまとめるために、<a href="https://resources.github.com/forrester/">GitHub Enterprise CloudとAdvanced Securityの経済</a>効果に関する最新のForresterレポートに、開発者とコンプライアンステスターや監査人の間で共通の理解が得られるという利点の素晴らしい例が示されています。  このレポートでは、開発者と監査人の両方に役立つ自動化された文書化プロセスの利点の1つを強調しています。</p>
<blockquote><p>"これらの新しい標準化された文書構造により、監査人はコンプライアンスに必要な文書を容易に見つけ、まとめることができるようになりました。このため、インタビューに応じた組織は、業界のコンプライアンスやセキュリティ監査に備える時間を節約することができました。"</p></blockquote>
<h1 id="3-helping-developers-understand-where-they-fit-into-the-three-lines-of-defense">3.開発者が 3 つの防衛ラインのどこに当てはまるかを理解できるようにする<a href="#3-helping-developers-understand-where-they-fit-into-the-three-lines-of-defense" class="heading-link pl-2 text-italic text-bold" aria-label="3. Helping developers understand where they fit into the three lines of defense"></a></h1>
<p><a href="https://www.isaca.org/resources/isaca-journal/issues/2018/volume-4/roles-of-three-lines-of-defense-for-information-security-and-governance">3つの </a>防衛ラインは、リスクマネジメントとガバナンスに使用されるモデルです。このモデルは、リスク対策に関わるチームの役割と責任を明確にするのに役立ちます。</p>
<p>エンドユーザーにソフトウェアを出荷し続けるエンジニアリングチームとエンジニアリングリードは、<em>第一の</em>防衛ラインであると考えましょう。このチームが、自分たちのソリューションの中にあるリスクを特定するための適切なレベルのスキルを持っていることを確認することは、非常に重要です。</p>
<p><em>第二の</em>防御ラインは、通常、組織レベルのフレームワーク、ポリシー、およびツールによって、大規模に達成されます。これは、第一の防衛線がリスク軽減のための手法をどれだけうまく導入しているか、組織全体で一貫してリスクを測定し、定義しているかを監視する役割を果たすものである。</p>
<p>内部監査は、<em>第三の</em>防衛ラインです。レッドチームとブルーチームが互いに補完し合うように、内部監査は3つの防衛ラインの最後のパズルピースと考えることができる。内部監査は、リスクマネジメントとガバナンスの有効性を評価し、経営幹部や外部の規制当局と連携して、実行されている統制の意識を高める。</p>
<p>例えてみましょう。ホッケーチームは、単にゴールを決めるだけでなく、自分たちに対するゴールを防ぐために構成されています。</p>
<ul>
<li><strong>フォワード</strong>：彼らはゴールを決めたり、ゴールをアシストしたりするために存在する。しかし、彼らはディフェンスの他のポジションと連携するよう求められることもあります。ディフェンスの第一線と考えましょう。彼らの仕事は、ビジネス価値を提供し、かつ安全なソリューションを作ることです。 </li>
<li><strong>ディフェンダー</strong>: 主な役割は、明らかにゴールを防ぐことです。しかし、現在の優先順位（オフェンスかディフェンスか）については、フォワードとパートナーを組みます。彼らは第二の防衛ラインのようなもので、リスクの監視を行い、エンジニアリングチームと協力します。  </li>
<li><strong>ゴールテンダー</strong>：最後の防衛ライン。内部監査に相当するものと考えることができる。  フォワードやディフェンダーとは独立した存在で、異なる責任、ツール、視点を持つ。  </li>
</ul>
<p>ホッケーのチームで、フォワードは非常に強いが、ディフェンスとゴールキーパーが弱いチームは、ほとんど成功しない。  また、ディフェンスが強くてもオフェンスが弱いチームも、成功することはほとんどない。成功するには、3つの側面がすべて調和していることが必要なのです。</p>
<p>これはビジネスでも同じです。もし、あなたのソリューションが顧客の要求を満たしていても、安全でなければ、あなたのビジネスは失敗に終わります。安全性が高くても、使い勝手が悪かったり、価値を提供できなかったりすれば、それは失敗に終わります。成功は、価値とリスク管理の適切なバランスを見つけることによって達成されます。</p>
<p>開発者は、自分たちのチームのためにゴールを決めること、つまり私たちの世界を動かすソフトウェアを作ることが目的であることを理解できます。  しかし、開発者はチームの防御能力をサポートし、ソフトウェアの安全性を確保する必要があります。彼らの成功は、より広いチームの成功に依存しており、新たな責任を負う必要はないのです。</p>
<h1 id="next-steps">次のステップ<a href="#next-steps" class="heading-link pl-2 text-italic text-bold" aria-label="Next steps"></a></h1>
<p>ここまで、開発フローにコンプライアンスを導入する方法をご紹介してきました。<a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule">ブランチ保護ルールや</a> <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests">プルリクエストから</a>、<a href="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners">CODEOWNERS</a>や<a href="https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#required-reviewers">環境承認まで</a>、GitHub にはコンプライアンスに自然と集中できるような機能がいくつもあります。</p>
<p>これは、問題解決のための一歩に過ぎません。コンプライアンスとDevOpsの実践者の間で共通言語を持つことは、実施された対策を示す上で非常に重要です。その共通言語があれば、誰もがコンプライアンスについて考えなければならないことは明らかであり、エンジニアリングチームは3つの防衛線の一部なのです。</p>
<p>このシリーズの次回は、開発者のワークフローでコンプライアンスを確保する方法について説明します。</p>
<p><em>安全性とコンプライアンスを保ちながら、開発者のスピードとコラボレーションを向上させる準備はできていますか？<a href="https://github.com/enterprise">GitHub Enterprise</a> がどのように役立つかをご覧ください。</em></p>


