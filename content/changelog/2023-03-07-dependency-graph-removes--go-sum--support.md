---
title: "依存関係グラフから `go.sum` のサポートが削除された。"
englishtitle: "Dependency graph removes `go.sum` support"
date: "2023-03-07"
cardurl: "https://github.blog/changelog/2023-03-07-dependency-graph-removes-go-sum-support"
author: "Kevin Duck"
description: " Dependency graph no longer ingests go.sum files for Go repositories, and Dependabot no longer alerts on vulnerabilities for dependencies found in go.sum files. Dependencies previously ingested from go.sum files have been removed from the dependency graph for all repositories on github.com.  go.sum files are not lock files but a log of all packages downloaded by Go when building a project. They may include multiple versions of a dependency, which may result in false positive Dependabot alerts for a vulnerable version that isn't actually used in the project.  Dependency graph continues to support go.mod files, the recommended format for Go projects. Use Go 1.17 or higher to ensure your go.mod file is a comprehensive view of all direct and transitive dependencies.  Learn more about the dependency graph  "
coverimage: ""
englishsummary: "  Dependabot will no longer alert on vulnerabilities for dependencies found in go.sum files, and Dependency graph will now only support go.mod files; users should upgrade to Go 1.17 or higher to ensure their go.mod"
summary: "  Dependabot は、go.sum ファイルで見つかった依存関係の脆弱性について警告しなくなり、Dependency graph は go.mod ファイルのみをサポートするようになりました。"
---

<p>依存関係グラフでは、Go リポジトリの<code>go.sum</code>ファイルが取り込まれなくなり、Dependabot は<code>go.sum</code>ファイルで見つかった依存関係の脆弱性について警告しなくなった。<code>go.sum</code>ファイルから取り込まれた依存関係は、github.comのすべてのリポジトリの依存関係グラフから削除されました。</p>
<p><code>go.sum</code>ファイルはロックファイルではなく、プロジェクトのビルド時に Go によってダウンロードされたすべてのパッケージのログです。これらのファイルには依存関係の複数のバージョンが含まれていることがあり、プロジェクトで実際に使用されていない脆弱なバージョンのDependabotアラートが誤検出されることがあります。</p>
<p>Dependency graph は、Go プロジェクトの推奨フォーマットである<code>go.mod</code>ファイルを引き続きサポートします。Go 1.17 以降を使用して、<code>go.mod</code>ファイルがすべての直接および推移的依存関係の包括的なビューであることを確認してください。</p>
<p><a href="https://docs.github.com/en/code-security/supply-chain-security/understanding-your-software-supply-chain/about-the-dependency-graph">依存性グラフの詳細はこちら</a></p>


