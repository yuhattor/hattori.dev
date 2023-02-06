---
title: "流れに身を任せながらOWASPの脆弱性を緩和する方法"
subtitle: "GitHub Advanced Security が OWASP Top 10 脆弱性のいくつかにどのように対処できるかを見てみましょう。"
englishsubtitle: "Explore how GitHub Advanced Security can help address several of the OWASP Top 10 vulnerabilities"
englishtitle: "How to mitigate OWASP vulnerabilities while staying in the flow"
date: "2023-02-06"
cardurl: "https://github.blog/2023-02-06-how-to-mitigate-owasp-vulnerabilities-while-staying-in-the-flow/"
author: "Mark Paulsen"
description: " The pace and scale of security vulnerabilities is increasing. This is in spite of the fact that teams have been trying to keep their code secure for years. So, why are vulnerabilities still such a problem? When teams use security tools and strategies that don’t optimize the developer experience, development is slowed down. This creates frustration, undermines customer usability, and hampers business success. Businesses that use such tools and strategies end up de-prioritizing security, and instead focus on shipping software quickly.  Here at GitHub, we want to help you mitigate vulnerabilities while boosting developer productivity. Fortunately, the Open Web Application Security Project (OWASP) can help. OWASP provides a Top 10 list of vulnerabilities that gives developers and organizations the context they need to address security and compliance risks within their applications. Today, we’ll examine several of OWASP’s vulnerabilities and developer-optimized strategies for keeping your software safe while maintaining and even increasing developer productivity.  Security at the expense of usability comes at the expense of Security.  - Avi Douglen, OWASP Board of Directors  1. The ideal application security environment  First of all, your development team needs an environment that fosters success. And the most important part of this is embedding security into the developer workflo"
coverimage: "https://github.blog/wp-content/uploads/2022/11/owasp.png?resize=1200%2C656"
category: "Security,DevSecOps,supply chain security"
englishsummary: ""
summary: ""
---

<p>セキュリティ脆弱性の発生ペースと規模が拡大しています。これは、チームが何年も前からコードの安全性を保とうとしてきたにもかかわらず、です。では、なぜ脆弱性がこれほどまでに問題なのでしょうか？チームが、開発者の体験を最適化しないセキュリティツールや戦略を使用すると、開発が遅くなります。これはフラストレーションを生み、顧客の使い勝手を悪くし、ビジネスの成功を妨げることになります。このようなツールや戦略を使用する企業は、結局、セキュリティの優先順位を下げ、ソフトウェアを早く出荷することに注力しています。</p>
<p>GitHubでは、開発者の生産性を高めながら、脆弱性を緩和するお手伝いをしたいと考えています。幸いなことに、Open Web Application Security Project (OWASP)がその手助けをしてくれる。OWASPは脆弱性の<a href="https://owasp.org/www-project-top-ten/#:~:text=The%20OWASP%20Top%2010%20is,step%20towards%20more%20secure%20coding">トップ10リストを</a>提供しており、開発者や組織がアプリケーションのセキュリティやコンプライアンスリスクに対処するために必要な情報を提供しています。本日は、OWASP の脆弱性のいくつかと、開発者の生産性を維持し、さらに向上させながらソフトウェアを安全に保つための、開発者に最適な戦略について検討します。</p>
<figure class="gh-full-blockquote mx-0 pl-6 mt-6 mt-md-7 mb-7 mb-md-8"><blockquote><p>ユーザビリティを犠牲にしたセキュリティは、セキュリティを犠牲にすることになるのです。</p></blockquote><figcaption class="text-mono color-fg-muted f5-mktg mt-3">- Avi Douglen、OWASP 理事会</figcaption></figure>
<h2 id="1-the-ideal-application-security-environment">1.理想的なアプリケーションセキュリティ環境<a href="#1-the-ideal-application-security-environment" class="heading-link pl-2 text-italic text-bold" aria-label="1. The ideal application security environment"></a></h2>
<p>まず第一に、開発チームには、成功を促進する環境が必要です。そして、その最も重要な部分は、開発者のワークフローにセキュリティを埋め込むことです。一般的に、セキュリティリスクを特定するために、サードパーティの異種ツールを使用します。しかし、これらのツールは遅く、ノイズが多く、生産性を低下させる可能性があります。しかし、セキュリティを開発者のフローに組み込むと、コードを迅速かつ容易に保護することができます。<a href="https://resources.github.com/appsec/#ghasebook">GitHub Advanced Security ebookで</a>説明したように、その他の理想的な環境の構成要素は以下のとおりです。</p>
<ul>
<li>コード、秘密、サプライチェーンにまたがるセキュリティ態勢の可視化。</li>
<li>軽量で文脈に応じたコミュニケーション・チャネルにより、容易なコラボレーションを可能にする。</li>
<li>ビジネスニーズに合わせた拡張性</li>
</ul>
<p>ビジネスの成熟度によっては、これらの機能を一度に実装することは不可能かもしれません。しかし、ビジネスの成熟度や継続的な改善に伴い、この理想的な環境を育成することで、脆弱性から保護し、安全なソフトウェアをより早く出荷できるようになります。</p>
<h2 id="2-owasp-vulnerabilities-risk-mitigation-and-prevention">2.OWASP 脆弱性のリスク軽減と予防<a href="#2-owasp-vulnerabilities-risk-mitigation-and-prevention" class="heading-link pl-2 text-italic text-bold" aria-label="2. OWASP vulnerabilities risk mitigation and prevention"></a></h2>
<p>理想的な状態を説明したところで、いくつかの OWASP 脆弱性と、それを軽減するためのテクニックを見ていきましょう。</p>
<h3 id="a02-cryptographic-failures"><a href="https://owasp.org/Top10/A02_2021-Cryptographic_Failures/">A02-Cryptographic Failures（暗号の失敗</a><a href="#a02-cryptographic-failures" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;a href=&quot;https://owasp.org/Top10/A02_2021-Cryptographic_Failures/&quot;&gt;A02-Cryptographic Failures&lt;/a&gt;"></a></h3>
<p>開発者は、自分のソフトウェアを意図的にセキュリティの脅威にさらすことはありません。しかし、API キー、平文パスワード、セキュリティ・トークン、その他の機密データがコード内に残り、暗号の脆弱性につなが ることがあります。</p>
<p>理想的には、秘密が企業、組織、またはリポジトリに到達することはありません。しかし、それらはしばしば発生し、緩和される必要があります。幸いなことに、GitHub Advanced Securityが役に立ちます。</p>
<p>GitHub の<a href="https://docs.github.com/en/code-security/secret-scanning/about-secret-scanning">秘密スキャン</a>機能は、<a href="https://docs.github.com/en/enterprise-cloud@latest/code-security/secret-scanning/protecting-pushes-with-secret-scanning">プッシュ保護</a>機能を実装することで、コードをスキャンして公開されている秘密を探すだけでなく、プッシュで信頼度の高い秘密 (誤検出率の低い秘密) をチェックすることもできるようになります。検出された秘密はすべてリストアップされるので、それを見直して削除することができます。削除しないことが決定された場合、監査証跡が作成されます。</p>
<h3 id="a03-injection"><a href="https://owasp.org/Top10/A03_2021-Injection/">A03-インジェクション</a><a href="#a03-injection" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;a href=&quot;https://owasp.org/Top10/A03_2021-Injection/&quot;&gt;A03-Injection&lt;/a&gt;"></a></h3>
<p>クロスサイトスクリプティング、パスインジェクション、SQLインジェクション、NoSQLインジェクションは、長年アプリケーションを悩ませ、OWASPトップ10に入り続けている脆弱性のいくつかです。</p>
<p>これらの脆弱性に対処する戦略の1つは、一貫した効果的な<a href="https://github.com/features/code-review">セキュリティコードレビューを</a>実施することです。コードがきれいになり、技術的負債やコード臭がなくなるだけでなく、より安全になるのです。これらの脆弱性をレビューすることは、既存のGitHubプルリクエストのワークフローの一部とすることができます。</p>
<p><a href="https://github.blog/2022-02-17-code-scanning-finds-vulnerabilities-using-machine-learning/">コードスキャンは</a>、機械学習の力を活用してインジェクションの脆弱性を発見し、開発者やセキュリティ専門家へのリスク伝達を支援することも可能です。<a href="https://codeql.github.com/">CodeQL</a>はコードスキャンを強化し、セキュリティ脆弱性がないかデータをスキャンします。</p>
<h3 id="a04-insecure-design"><a href="https://owasp.org/Top10/A04_2021-Insecure_Design/">A04-安全でない設計</a><a href="#a04-insecure-design" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;a href=&quot;https://owasp.org/Top10/A04_2021-Insecure_Design/&quot;&gt;A04-Insecure Design&lt;/a&gt;"></a></h3>
<p><a href="https://github.blog/2020-09-02-how-we-threat-model/">脅威のモデル化</a>戦略を導入することで、開発者、セキュリティ専門家、さらにはリスク管理チーム間のコラボレーションを促進することができます。これにより、コードが一行も書かれる前に、アーキテクチャとデザインパターンが可能な限り安全であることを確認することができます。</p>
<h3 id="a06-vulnerable-and-outdated-components"><a href="https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/">A06-Vulnerable and Outdated Components（脆弱で古いコンポーネント</a><a href="#a06-vulnerable-and-outdated-components" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;a href=&quot;https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/&quot;&gt;A06-Vulnerable and Outdated Components&lt;/a&gt;"></a></h3>
<p>オープンソースコンポーネントの採用が急速に進む中、ソフトウェアの構成を理解し、脆弱性のあるコンポーネントを更新できるようにすることが、これまで以上に重要になっています。</p>
<p>脆弱なコンポーネントや古いコンポーネントのリスクを管理するための最善の戦略の1つは、セキュリティ脅威が発見されたらすぐに開発者に警告し、通常のワークフローやツールの中で対策を講じることができるようにすることです。</p>
<p><a href="https://github.blog/2022-05-25-how-we-use-dependabot-to-secure-github/">Dependabotを</a>活用することで、既知の脆弱性を持つソフトウェアの依存関係をリポジトリが使用する際にアラートを受け取ることができます。セキュリティチームから<a href="https://docs.github.com/en/code-security/dependabot/working-with-dependabot/managing-pull-requests-for-dependency-updates">プルリクエストを起こすことも</a>でき、セキュリティと開発者がコミュニケーションをとるためのシンプルで効果的な方法となります。</p>
<p>これらのツールの最も良いところは、GitHub の中で行われることです。そのため、生産性の低下や過度なコンテキストの切り替えを心配する必要はありません。</p>
<h2 id="developer-empowering-application-security">開発者の力を引き出すアプリケーション・セキュリティ<a href="#developer-empowering-application-security" class="heading-link pl-2 text-italic text-bold" aria-label="Developer-empowering application security"></a></h2>
<p>これらの戦略を実施することで、開発者組み込みの、コラボレーション可能でスケーラブルなアプリケーション・セキュリティ環境を構築し、サプライチェーン全体のリスク軽減を実現することができます。同時に、開発者の生産性に悪影響を与えないようにすることができます。</p>
<div class="post-content-cta"><p>当社は、2月15日から16日まで開催されるOWASP 2023 Global AppSec Dublinのイベントに参加し、ブース#DA2に出展します。このトピックをより深く掘り下げ、これらの戦略に関するあらゆる疑問にお答えするため、<a href="https://resources.github.com/owasp-dublin-2023/?utm_source=github&#038;utm_medium=blog&#038;utm_campaign=2023q3-evt-emea-OWASPDublin2023_Security_blog">当社のエキスパートとの時間を予約して</a>ください。</p>
<p>ハンズオンの経験を積みたいですか？<a href="https://skills.github.com/">GitHub Skillsで</a>、その詳細と、その他の実践的な学習方法をご覧ください。</p>
</div>


