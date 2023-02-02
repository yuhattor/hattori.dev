---
title: "GitHubの可用性レポート: 2023年1月"
subtitle: "1月に、Package と Pagesのパフォーマンスが低下するインシデントと、Git ユーザーに影響を与えるインシデントの2つが発生しました"
englishsubtitle: "In January, we experienced two incidents, one that resulted in degraded performance for Packages and Pages and another that impacted Git users."
englishtitle: "GitHub Availability Report: January 2023"
date: "2023-02-01"
cardurl: "https://github.blog/2023-02-01-github-availability-report-january-2023/"
author: "Jakub Oleksy"
description: "In January, we experienced two incidents. One that resulted in degraded performance for GitHub Packages and GitHub Pages, and another that impacted git users."
coverimage: "https://github.blog/wp-content/uploads/2022/04/Engineering-Enterprise@2x-1.png?resize=1600%2C850"
category: "Engineering,Enterprise,GitHub Availability Report"
---

<p>1月、私たちは2つのインシデントを経験しました。ひとつはGitHub PackagesとGitHub Pagesのパフォーマンスが低下するもので、もうひとつはgitユーザーに影響を与えるものでした。</p>
<p><strong>1月30日 21:48 UTC (35分継続)</strong></p>
<p>弊社のサービスモニターがGitHub PackagesとGitHub Pagesのパフォーマンス低下を検出しました。コンテナレジストリへのリクエストのほとんどが失敗し、一部のGitHub Pagesのビルドにも影響がありました。この現象はバックエンドの変更が原因であると判断し、その変更を元に戻すことで緩和されました。</p>
<p>この事象は最近発生したものであるため、現在その要因を調査中であり、来月のレポートでより詳細なアップデートを提供する予定です。</p>
<p><strong>1月30日 18:35 UTC (7時間継続)</strong></p>
<p>私たちは、アップストリームからの最新バージョンで、本番用Gitバイナリをアップグレードしました。この更新には、アーカイブを生成する際に<code>gzip</code>の内部実装を使用するように変更することが含まれていました。その結果、GitHub が提供する "Download Source" リンクの内容に微妙な変更が生じ、チェックサムの不一致が発生しました。コンテンツは変更されていません。</p>
<p>多くのコミュニティへの影響を認識した後、圧縮の変更をロールバックして以前の動作に戻しました。</p>
<p>上記と同様に、この事故の要因についても調査中であり、来月のレポートでより詳細な情報を提供する予定です。</p>
<hr />
<p><a href="https://www.githubstatus.com/">状況の</a>変化については、当社の<a href="https://www.githubstatus.com/">ステータスページで</a>リアルタイムに更新していますので、ぜひご覧ください。私たちが取り組んでいることについてもっと知りたい方は、<a href="https://github.blog/category/engineering/">GitHub Engineering Blogを</a>ご覧ください。</p>


