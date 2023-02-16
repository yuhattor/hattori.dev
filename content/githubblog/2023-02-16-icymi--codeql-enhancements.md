---
title: "ICYMI：CodeQLの機能強化"
subtitle: "CodeQLのユーザーエクスペリエンスの向上と、新しい言語のスキャン、新しいタイプのCWEの検出、アプリケーションのより深い分析を可能にする機能強化について説明します。"
englishsubtitle: "Learn about CodeQL's improved user experience and enhancements that let you scan new languages, detect new types of CWEs, and perform deeper analyses of your applications."
englishtitle: "ICYMI: CodeQL enhancements"
date: "2023-02-16"
cardurl: "https://github.blog/2023-02-16-icymi-codeql-enhancements/"
author: "Walker Chabbott"
description: " Over the last year, GitHub has brought a number of enhancements to CodeQL , the semantic analysis engine that powers code scanning. You can now scan new languages, detect new types of CWEs, perform deeper analyses of your applications, and enjoy improvements to the user experience. Let’s check out some of these major enhancements to CodeQL and learn how you can take advantage of them in your environment.  Test new ecosystems  Have you tried scanning your Ruby codebases? We announced the general availability of Ruby support for CodeQL at GitHub Universe 2022. We’ve made a number of improvements since our beta, including doubling the number of default queries, providing coverage for all Ruby-related OWASP categories out-of-the-box, and optimizing performance to deliver tests in less than five minutes for 90% of beta users. To date, users scanning their Ruby codebases have fixed over 4,000 alerts, and on an average day we run almost 5,000 Ruby analyses.  Ruby has been a vital part of our SDLC for many years, as it allows us to build flexible applications to meet our evolving needs. The ability to scan Ruby codebases and identify and remediate vulnerabilities all within GitHub means that our developers are able to secure their code without disrupting their workflow.  - Matt McQuillan / Director of Engineering Services / Hashicorp  You can also test your mobile applications with th"
coverimage: "https://github.blog/wp-content/uploads/2022/08/Security-Product@2x.png?resize=1600%2C850"
category: "Security,code scanning,CodeQL,SAST"
englishsummary: "  GitHub has made a number of enhancements to CodeQL, including support for scanning Ruby codebases and the ability to scan mobile applications, to help developers secure their code without disrupting their workflow."
summary: "  GitHubは、Rubyコードベースのスキャンやモバイルアプリケーションのスキャン機能など、CodeQLに多くの機能強化を行い、開発者がワークフローを中断することなくコードを保護できるよう支援します。"
---

<p>昨年、GitHubはコードスキャンを支えるセマンティック解析エンジンである<a href="https://codeql.github.com/docs/codeql-overview/">CodeQLに</a>多くの機能拡張を行いました。新しい言語のスキャン、新しいタイプのCWEの検出、アプリケーションのより深い分析、そしてユーザーエクスペリエンスの向上が可能になりました。CodeQLの主な強化点を確認し、お客様の環境でどのように活用できるかを学びましょう。</p>
<h2 id="test-new-ecosystems">新しいエコシステムのテスト<a href="#test-new-ecosystems" class="heading-link pl-2 text-italic text-bold" aria-label="Test new ecosystems"></a></h2>
<p>Rubyのコードベースのスキャンを試したことはありますか？私たちは、GitHub Universe 2022でCodeQLの<a href="https://github.blog/changelog/2022-11-09-codeql-code-scanning-launches-ruby-analysis-support-in-ga/">Rubyサポートの一般提供を</a>発表しました。デフォルトクエリの数を2倍にし、Ruby関連のOWASPカテゴリすべてをすぐにカバーできるようにし、パフォーマンスを最適化して90%のベータユーザーが5分以内にテストを提供できるようにするなど、ベータ版から多くの改良を加えています。現在までに、Ruby コードベースをスキャンしたユーザは 4,000 件以上の警告を修正し、平均して 1 日に約 5,000 件の Ruby 分析が実行されています。</p>
<figure class="gh-full-blockquote mx-0 pl-6 mt-6 mt-md-7 mb-7 mb-md-8"><blockquote><p>Ruby は、進化するニーズに合わせて柔軟なアプリケーションを構築できるため、長年にわたって当社の SDLC に不可欠な要素となっています。Rubyのコードベースをスキャンし、脆弱性の特定と修正をすべてGitHub上で行うことができるため、当社の開発者はワークフローを中断することなくコードの安全性を確保することができます。</p></blockquote><figcaption class="text-mono color-fg-muted f5-mktg mt-3">- Matt McQuillan / エンジニアリング・サービス・ディレクター / Hashicorp</figcaption></figure>
<p>CodeQLの<a href="https://github.blog/changelog/2022-11-28-codeql-code-scanning-launches-kotlin-analysis-support-beta/">Kotlinサポートのベータ</a>版で、モバイルアプリケーションのテストも可能ですCodeQL は現在、Kotlin および Java と Kotlin の混合プロジェクトにネイティブで対応しています。Kotlinのサポートは、私たちの既存のJavaサポートの延長であり、モバイルとサーバーサイドの両方のアプリケーションのために、Java用の既存のCodeQLクエリのすべての利点を利用することができます。</p>
<p>Kotlinは、モバイルアプリケーションセキュリティへの最初の投資であり、Swiftのベータサポートは今年後半に登場する予定です。</p>
<p>新しい言語に対するテストだけを利用できるわけではありません。現在の言語サポートにも、以下のような改良を加えています。</p>
<ul>
<li>Java 19のフルサポート</li>
<li>Go 1.19のフルサポート </li>
<li>C#11のビルドサポート </li>
<li>Python 3.11のフルサポート</li>
</ul>
<p>これにより、毎日使用する言語の多くをスキャンし、アプリケーションを安全に出荷できるようになりました。</p>
<h2 id="perform-deeper-analysis-of-your-code">コードのより詳細な分析<a href="#perform-deeper-analysis-of-your-code" class="heading-link pl-2 text-italic text-bold" aria-label="Perform deeper analysis of your code"></a></h2>
<p>コードスキャンでは、CodeQLクエリを使用してセキュリティ脆弱性を検出します。クエリーの使用は複雑に聞こえるかもしれませんが、GitHubの研究者やコミュニティのセキュリティ研究者によって書かれ、キュレーションされた、最も重要な脆弱性から一般的な脆弱性までをカバーする、すぐに使えるクエリーを提供することで簡単に行えるようにしました。また、開発者が特定のバグや過去に問題を起こした可能性のある脆弱性をチェックするために、カスタムクエリを作成することも可能です。</p>
<p>CodeQLの分析機能を簡単に利用できるように、新しいクエリを多数追加しました。CodeQLは現在、昨年より27％増の318のデフォルトセキュリティクエリを同梱しており、オプションの拡張クエリパックで最大432まで有効にすることができます。</p>
<p>Depandabotアラートと合わせて、これらのクエリは、該当するOWASPの全カテゴリ、SANS CWE Top 25の100%、WASCの該当カテゴリの100%をカバーしています。これは、セキュリティチームがCodeQLが最も重要な脆弱性を検出していると確信できるだけでなく、開発者がプルリクエストの中ですぐに確認できることを意味します。</p>
<div class="image-frame image-frame-full border rounded-2 overflow-hidden d-flex flex-row flex-justify-center" style="background: #EAEEF2"><br />
<img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/codescannin1.png?w=1024&#038;resize=1024%2C716" alt="Screenshot of the GitHub code scanning bot displaying potential problems. Underneath the highlighted code, two people have a conversation about how to remediate them." width="1024" height="716" class="aligncenter size-large wp-image-70172 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/codescannin1.png?w=1262 1262w, https://github.blog/wp-content/uploads/2023/02/codescannin1.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/codescannin1.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/codescannin1.png?w=1024&#038;resize=1024%2C716 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /><br /></div>
<p>CWEベースのカバレッジの全リストは、<a href="https://codeql.github.com/codeql-query-help/codeql-cwe-coverage/">CodeQLのCWEカバレッジページを</a>ご覧ください。また、<a href="https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/">サポートされている言語とフレームワークのページでは</a>、ライブラリやフレームワークのすべてのアップデートと、各言語のクエリの変更履歴へのリンクを確認することができます。</p>
<h2 id="seamlessly-use-codeql">CodeQLのシームレスな使用<a href="#seamlessly-use-codeql" class="heading-link pl-2 text-italic text-bold" aria-label="Seamlessly use CodeQL"></a></h2>
<p>最後に、CodeQL の使用感について、いくつかの改善を行いました。コードスキャンに<a href="https://github.blog/changelog/2022-11-01-code-scanning-now-supports-using-codeql-packs-on-github-com-and-ghes/">CodeQLパックのサポートを</a>追加し、GitHub.comとGitHub EnterpriseでCodeQLパックを活用できるようになりました。また、<a href="https://github.blog/changelog/2022-08-31-code-scanning-customize-your-codeql-analysis-using-query-filters/">クエリフィルタを使用してCodeQL分析をカスタマイズ</a>する機能を開始しました。これにより、コードベースに関連しない可能性のある特定のチェックを柔軟にフィルタリングし、どのセキュリティチェックが最も関連性が高いかについて、より正確な結果を確認することができます。<a href="https://github.blog/changelog/2023-02-07-codeql-code-scanning-is-now-16-faster/">CodeQLは</a>、クラス最高の精度と低い偽陽性率を損なうことなく、<a href="https://github.blog/changelog/2023-02-07-codeql-code-scanning-is-now-16-faster/">分析の実行速度を16%</a>向上させました。</p>
<p>セキュリティ研究者のために、<a href="https://github.blog/changelog/2022-09-21-codeql-for-vs-code-download-codeql-databases-from-github-com/">私</a>たちは最も人気のあるオープンソースプロジェクトの<a href="https://github.blog/changelog/2022-09-21-codeql-for-vs-code-download-codeql-databases-from-github-com/">CodeQLデータベースを作成し、保存して</a>います。これらのデータベースは、VS Code の CodeQL 拡張機能を通じて簡単に入手でき、セキュリティ調査を行いながら CodeQL カスタムクエリの作成と実行を効率化することができます。</p>
<p>また、GitHubコミュニティもCodeQLの成功の重要な要因となっており、ユーザーはリソースや知識を共有し、プラットフォームの開発に貢献しています。例えば、今年、コードベースのセキュリティリスクを分析するための新しいクエリを追加する際に、GitHub コミュニティが役に立ちました。</p>
<p>これらの新機能や統合により、開発者は最初から安全なコードを構築することが容易になり、セキュリティ研究者は問題になる前に脆弱性を発見することができるようになりました。</p>
<h3 id="get-started-with-codeql">CodeQLを始める<a href="#get-started-with-codeql" class="heading-link pl-2 text-italic text-bold" aria-label="Get started with CodeQL"></a></h3>
<p>CodeQLとコードスキャンをリポジトリで始めたい場合は、新しい<a href="https://github.blog/2023-01-09-default-setup-a-new-way-to-enable-github-code-scanning/">デフォルトのセットアップオプション</a>で簡単に有効にすることができます。いつものように、CodeQLはオープンソースリポジトリで無料で使用することができます。プライベートリポジトリでCodeQLを活用したい場合は、GitHub EnterpriseサブスクリプションにGitHub Advanced Securityを追加することが可能です。詳しくは<a href="https://github.com/enterprise/contact?ref_page=/security&#038;ref_cta=Contact%20Sales&#038;ref_loc=security%20platform%20page">営業にお問い合わせ</a>ください。</p>
<p>私たちは常に製品を改善する方法を探していますので、<a href="https://github.com/github/codeql/blob/main/CONTRIBUTING.md">このレポに </a>コメントを書き込んで、あなたやコミュニティのためにCodeQLを改善する手助けをしてください。</p>


