---
title: "GitHub Actions：setup-go アクションがデフォルトでキャッシュを有効にするようになりました。"
englishtitle: "GitHub Actions: The setup-go Action now enables caching by default"
date: "2023-03-24"
cardurl: "https://github.blog/changelog/2023-03-24-github-actions-the-setup-go-action-now-enables-caching-by-default"
author: "Kevin Duck"
description: " Enabling caching by default has demonstrated improved workflow performance, and can reduce build times by 20-40% for repositories with dependencies greater than 100 MB! This change has been made to the latest setup-go Action(V4) . Developers no longer have to specify the cache: true parameter in their YAML file to obtain the benefits of caching. For more information on building, testing, and caching dependencies with Go, check out the docs here !  "
coverimage: ""
englishsummary: "  Enabling caching by default in the latest setup-go Action(V4) has been shown to reduce build times by 20-40% for repositories with dependencies greater than 100 MB."
summary: "  最新のsetup-go Action(V4)では、デフォルトでキャッシュを有効にすることで、依存関係が100MBを超えるリポジトリでビルド時間を20～40%短縮することが示されています。"
---

<p>デフォルトでキャッシュを有効にすることで、ワークフローのパフォーマンスが向上し、依存関係が100MBを超えるリポジトリでは、ビルド時間を20～40%短縮できることが実証されました！この変更は、最新のsetup-go Action<a href="https://github.com/marketplace/actions/setup-go-environment">(V4)</a>で行われました。開発者は、キャッシュの利点を得るために、YAMLファイルで<code>cache: true</code>パラメータを指定する必要がなくなりました。Goによる依存関係の構築、テスト、キャッシュの詳細については、<a href="https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-go#caching-dependencies">こちらの</a>ドキュメントを参照してください！</p>


