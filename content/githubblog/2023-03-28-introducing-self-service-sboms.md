---
title: "セルフサービス型SBOMの導入"
subtitle: "開発者とコンプライアンスチームは、クラウドリポジトリのための新しいSBOM生成ツールを手に入れることができます。"
englishsubtitle: "Developers and compliance teams get a new SBOM generation tool for cloud repositories."
englishtitle: "Introducing self-service SBOMs"
date: "2023-03-28"
cardurl: "https://github.blog/2023-03-28-introducing-self-service-sboms/"
author: "Eric Tooley"
description: " Following the precedent set by Executive Order 14028 , security and compliance teams increasingly request software bills of materials (SBOMs) to identify the open source components of their software projects, assess their vulnerability to emerging threats, and verify alignment with license policies. So, we asked ourselves, how do we make SBOMs easier to generate and share?  Today, we’re happy to announce a new Export SBOM function that allows anyone with read access to a GitHub cloud repository to generate an NTIA -compliant SBOM with a single click. The resulting JSON file saves project dependencies and metadata, like versions and licenses in the industry standard SPDX format, which can then be used with security and compliance workflows and tools, or reviewed in Microsoft Excel (use a JSON-to-CSV converter for compatibility with Google Sheets).  While this new self-service capability makes it easy to generate SBOMs on-demand, developers can also make SBOM generation a regular step of their development workflow. First, if you already have an SBOM for your project, you can upload it to the dependency graph to receive Dependabot alerts on any dependencies with known vulnerabilities. Next, use GitHub’s SBOM gh CLI extension to programmatically generate SBOMs from your repository’s dependency graph, or use a third-party GitHub Action to generate SBOMs at build time. A REST API fo"
coverimage: "https://github.blog/wp-content/uploads/2022/01/Security-Open-Source-Product.png?resize=1200%2C630"
category: "Open Source,Security,compliance,dependency graph,SBOM,supply chain security"
englishsummary: "  GitHub has released a new Export SBOM function that allows users to generate NTIA-compliant SBOMs with a single click, as well as programmatically generate SBOMs and use third-party GitHub Actions to generate SB"
summary: "  GitHubは、ワンクリックでNTIA準拠のSBOMを生成できる新しいExport SBOM機能をリリースし、プログラムによるSBOM生成やサードパーティのGitHub Actionsを使用してSBOMを生成できるようにしました。"
---

<p><a href="https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity">大統領令14028</a>号の先例にならって、セキュリティとコンプライアンスのチームは、ソフトウェアプロジェクトのオープンソースコンポーネントを特定し、新たな脅威に対する脆弱性を評価し、ライセンスポリシーとの整合性を確認するために、ソフトウェア部品表（SBOM）を要求することが増えています。そこで私たちは、どうすればSBOMを簡単に作成し、共有できるようになるのか、と考えました。</p>
<p>GitHubのクラウドリポジトリにアクセスできる人なら誰でも、ワンクリックで<a href="https://ntia.gov/page/software-bill-materials">NTIA準拠の</a>SBOMを生成できるようになりました。生成されたJSONファイルは、プロジェクトの依存関係や、バージョンやライセンスなどのメタデータを業界標準のSPDX形式で保存し、セキュリティやコンプライアンスのワークフローやツールで使用したり、Microsoft Excelで確認することができます（Google Sheetsとの互換性のためにJSONからCSVへの変換器を使用します）。</p>
<p>この新しいセルフサービス機能により、SBOMをオンデマンドで簡単に生成できるようになりましたが、開発者はSBOM生成を開発ワークフローの通常のステップにすることも可能です。まず、プロジェクトのSBOMがすでにある場合は、<a href="https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api">それを依存関係グラフにアップロード</a>して、既知の脆弱性を持つ依存関係に関するDependabotアラートを受け取ることができます。次に、<a href="https://github.com/advanced-security/gh-sbom">GitHubのSBOM gh CLI拡張を</a>使用して、リポジトリの依存関係グラフからプログラムでSBOMを生成するか、<a href="https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api#generating-and-submitting-a-software-bill-of-materials-sbom">サードパーティのGitHub Actionを</a>使用してビルド時にSBOMを生成します。依存関係グラフからSBOMを生成するためのREST APIは近日公開予定です。</p>
<p>GitHubのサプライチェーンセキュリティソリューションの一環として、セルフサービスSBOMはGitHub上のすべてのクラウドリポジトリで無料です。</p>
<h2 id="whats-changing">何が変わるの？<a href="#whats-changing" class="heading-link pl-2 text-italic text-bold" aria-label="What’s changing?"></a></h2>
<p>SBOM を生成するには、リポジトリの依存関係グラフにある新しい<strong>Export SBOM</strong>ボタンをクリックするだけです：</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/sbom1.png?w=1024&#038;resize=1024%2C664" alt="Screenshot of dependency graph" width="1024" height="664" class="aligncenter size-large wp-image-70955 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/sbom1.png?w=1600 1600w, https://github.blog/wp-content/uploads/2023/03/sbom1.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/sbom1.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/sbom1.png?w=1024&#038;resize=1024%2C664 1024w, https://github.blog/wp-content/uploads/2023/03/sbom1.png?w=1536 1536w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<p>これにより、SPDX 形式の機械読み取り可能な JSON ファイルが作成されます。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/sbom2.png?w=1024&#038;resize=1024%2C737" alt="Screenshot of JSON file contents" width="1024" height="737" class="aligncenter size-large wp-image-70956 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/sbom2.png?w=1600 1600w, https://github.blog/wp-content/uploads/2023/03/sbom2.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/sbom2.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/sbom2.png?w=1024&#038;resize=1024%2C737 1024w, https://github.blog/wp-content/uploads/2023/03/sbom2.png?w=1536 1536w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<hr>
<h3 id="learn-more-about-sboms">SBOMについてもっと知る<a href="#learn-more-about-sboms" class="heading-link pl-2 text-italic text-bold" aria-label="Learn more about SBOMs"></a></h3>
<ul>
<li><a href="https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository">SBOMドキュメンテーション</a></li>
<li><a href="https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/using-the-dependency-submission-api">依存関係提出API</a></li>
<li><a href="https://github.com/advanced-security/gh-sbom">GitHub SBOMコマンドラインインターフェース（CLI）拡張機能</a></li>
<li><a href="https://github.com/microsoft/sbom-tool">Microsoft SBOMツール</a></li>
</ul>


