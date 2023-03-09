---
title: "マルチリポジトリのバリアント解析（ベータ版）を使用して、CodeQLクエリをスケールアップして実行します。"
englishtitle: "Use multi-repository variant analysis (beta) to run CodeQL queries at scale"
date: "2023-03-09"
cardurl: "https://github.blog/changelog/2023-03-09-use-multi-repository-variant-analysis-beta-to-run-codeql-queries-at-scale"
author: "Kevin Duck"
description: " Today we have released multi-repository variant analysis for CodeQL in public beta to help the OSS security community power up their research with CodeQL.  CodeQL is the static code analysis engine that powers GitHub code scanning . Out of the box, CodeQL is able to find many different types of security vulnerability and flag them up in pull requests.  But one of CodeQL’s superpowers is its versatility and customizability: you can use it to find virtually any pattern in source code. As such, it’s a great tool for finding new types of vulnerabilities – once you’ve identified an interesting pattern, model it as a CodeQL query, and then run it against your repository to find all occurrences of that pattern! But most vulnerabilities are relevant to many codebases. Wouldn’t it be amazing if you could easily run your query against many repos at the same time? Well, now you can with multi-repository variant analysis — which we’ve just shipped in public beta!  This new feature will allow security researchers to run CodeQL analyses against large numbers of repos, straight from the CodeQL extension for VS Code , making it possible to identify new types of security vulnerabilities in the most popular open-source codebases.  Checkout the CodeQL for VS Code documentation to get learn how to get started with multi-repository variant analysis. We'd also love to hear your feedback on this Git"
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/42464962/221604905-24e95054-a01e-4060-a9df-81bbe0be75aa.png?ssl=1"
englishsummary: "HUb issue  CodeQL's new multi-repository variant analysis feature allows security researchers to easily identify new types of security vulnerabilities in the most popular open-source codebases."
summary: "HUb issue CodeQLの新しいマルチリポジトリバリアント解析機能により、セキュリティ研究者は、最も人気のあるオープンソースのコードベースにおける新しいタイプのセキュリティ脆弱性を容易に特定することができます。"
---

<p>本日、OSSセキュリティコミュニティがCodeQLを使った研究をパワーアップさせるために、CodeQLのマルチリポジトリバリアント解析をパブリックベータでリリースしました。</p>
<p><a href="https://codeql.github.com/">CodeQLは</a>、<a href="https://github.com/features/security">GitHubのコードスキャンを</a>強化する静的コード解析エンジンです。CodeQLはすぐに、さまざまな種類のセキュリティ脆弱性を見つけ、プルリクエストでフラグを立てることができます。</p>
<p>しかし、CodeQLの超能力の1つは、その汎用性とカスタマイズ性であり、ソースコード内のほぼすべてのパターンを見つけるために使用することができます。興味深いパターンを特定したら、それをCodeQLクエリとしてモデル化し、リポジトリに対して実行すると、そのパターンのすべての出現箇所を見つけることができます！そのため、新しいタイプの脆弱性を見つけるのに最適なツールです。しかし、ほとんどの脆弱性は、多くのコードベースに関連しています。もし、多くのリポジトリに対して同時にクエリを簡単に実行できるとしたら、それは素晴らしいことだと思いませんか？今回、パブリック・ベータ版をリリースしたマルチ・リポジトリ・バリアント分析で、それが可能になりました。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/42464962/221604905-24e95054-a01e-4060-a9df-81bbe0be75aa.png?ssl=1" alt="Screenshot 2023-02-22 at 16 39 39" data-recalc-dims="1"></p>
<p>この新機能により、セキュリティ研究者は、<a href="https://codeql.github.com/docs/codeql-for-visual-studio-code/">VS Code用のCodeQL拡張</a>機能から直接、多数のリポジトリに対してCodeQL分析を実行できるようになり、最も人気のあるオープンソースコードベースの新しいタイプのセキュリティ脆弱性を特定することができるようになりました。</p>
<p><a href="https://codeql.github.com/docs/codeql-for-visual-studio-code/running-codeql-queries-at-scale-with-mrva">CodeQL for VS Code のドキュメントを</a>チェックして、マルチリポジトリのバリアント解析を始める方法を学んでください。また、この<a href="https://gh.io/mrva-public-beta-discussion">GitHubコミュニティでのディスカッションで</a>、皆様のご意見をお聞かせください。</p>


