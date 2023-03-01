---
title: "GitHubの可用性レポート。2023年2月"
subtitle: "2月には、GitHubの各サービスにおいてパフォーマンス低下を引き起こす3つのインシデントが発生しました。このレポートでは、GitHub PackagesとGitHub Pagesのパフォーマンスを低下させた1月のインシデントと、Gitユーザーに影響を与えた1月の別のインシデントについても明らかにしています。"
englishsubtitle: "In February, we experienced three incidents that resulted in degraded performance across GitHub services. This report also sheds light into a January incident that resulted in degraded performance for GitHub Packages and GitHub Pages and another January incident that impacted Git users."
englishtitle: "GitHub Availability Report: February 2023"
date: "2023-03-01"
cardurl: "https://github.blog/2023-03-01-github-availability-report-february-2023/"
author: "Jakub Oleksy"
description: " In February, we experienced three incidents that resulted in degraded performance across GitHub services. This report also sheds light into a January incident that resulted in degraded performance for GitHub Packages and GitHub Pages and another January incident that impacted Git users.  January 30 21:31 UTC (lasting 35 minutes)  On January 30 at 21:36 UTC, our alerting system detected a 500 error response increase in requests made to the Container registry. As a result, most builds on GitHub Pages and requests to GitHub Packages failed during the incident.  Upon investigation, we found that a change was made to the Container registry Redis configuration at 21:30 UTC to enforce authentication on Redis connections. There was an issue with the Container registry production deployment file where client connections were unable to authenticate due to a hard coded connection string, resulting in errors and preventing successful connections.  At 22:12 UTC, we reverted the configuration change for Redis authentication. Container registry began recovering two minutes later, and GitHub Pages was considered healthy again by 22:21 UTC.  To help prevent future incidents, we improved management of secrets in the Container registry’s Redis deployment configurations and added extra test coverage for authenticated Redis connections.  January 30 18:35 UTC (lasting 7 hours)  On January 30 at 18:"
coverimage: "https://github.blog/wp-content/uploads/2022/02/Engineering-Enterprise@2x.png?resize=1600%2C850"
category: "Engineering,Enterprise,GitHub Availability Report"
englishsummary: "35 UTC, our monitoring system detected a sudden increase in latency and error rates across multiple services. We found that the cause of the incident was a change made to the GitHub Enterprise Cloud (GHC) network configuration.   In January and February"
summary: "35 UTCに、当社の監視システムが複数のサービスにおいて遅延とエラーレートの急激な増加を検出しました。その結果、原因はGitHub Enterprise Cloud（GHC）のネットワーク構成に加えられた変更であることが判明しました。   1月と2月に"
---

<p>2月には、GitHubの各サービスにおいてパフォーマンス低下を引き起こす3つのインシデントが発生しました。また、1月に発生したGitHub PackagesとGitHub Pagesのパフォーマンス低下と、1月に発生したGitユーザーへの影響についても報告します。</p>
<p><strong>1月30日 21:31 UTC (35分継続)</strong></p>
<p>1月30日21:36 UTCに、アラートシステムがコンテナレジストリへのリクエストで500エラーのレスポンス増加を検出しました。その結果、GitHub Pages でのビルドと GitHub Packages へのリクエストのほとんどが、このインシデントの間失敗しました。</p>
<p>調査の結果、21:30UTCにContainer registryのRedis設定に変更が加えられ、Redis接続に認証が適用されたことが判明しました。Container registry の本番用配置ファイルに問題があり、ハードコードされた接続文字列のためにクライアント接続が認証できず、エラーが発生して接続に成功しませんでした。</p>
<p>22:12 UTCに、Redis認証の設定変更を元に戻しました。コンテナレジストリは2分後に回復し始め、22:21 UTCまでにGitHub Pagesは再び正常とみなされるようになりました。</p>
<p>今後のインシデントを防止するため、Container registry の Redis 展開設定における秘密の管理を改善し、認証された Redis 接続に対する追加のテストカバレッジを追加しました。</p>
<p><strong>1月30日 18:35 UTC (7時間継続)</strong></p>
<p>1月30日18:35 UTCに、GitHubはソースコードのダウンロードにおける圧縮設定をわずかに変更する変更をデプロイしました。この変更により、アーカイブファイルのチェックサムが変更され、多くのコミュニティで予期せぬ結果となりました。これらのファイルの内容は変更されませんでしたが、多くのコミュニティは、バイトの正確なレイアウトも変更されないことに依存するようになっていたのです。この影響に気づいたとき、私たちはこの変更を元に戻し、影響を受けるコミュニティと連絡を取り合いました。</p>
<p>私たちは、この変更が多くのコミュニティに広範な影響を与えることを予期しておらず、将来の事故を防ぐために新しい手順を実施しています。これには、GitHub全体におけるGitの展開に関するいくつかの改善や、ワークフローへのチェックサム検証の追加などが含まれます。</p>
<p>今後の計画については、<a href="https://github.blog/2023-02-21-update-on-the-future-stability-of-source-code-archives-and-hashes/">こちらの関連ブログ</a>記事をご覧ください。</p>
<p><strong>2月7日 21:30 UTC (20時間35分継続)</strong></p>
<p>2月7日21:30 UTCに、東南アジア地域でGitHub Codespacesの作成、起動、接続に障害が発生し、クラウドプロバイダーのデータセンターで障害が発生したことを弊社のモニターが検出しました。この間、お客様への影響を軽減するため、コードスペースの作成をセカンダリロケーションにリダイレクトし、新しいコードスペースを使用できるようにしました。データセンターが復旧すると、その地域のコードスペースは自動的に回復し、その地域の既存のコードスペースを再開させることができました。この事故では、他の地域のコードスペースには影響がありませんでした。</p>
<p>この事故から得た教訓をもとに、地域の冗長性を拡大することを検討し、地域やデータセンターの一時的な停止にうまく対処できるようにアーキテクチャの変更を開始しました。</p>
<p><strong>2月18日02:36 UTC (2時間26分継続)</strong></p>
<p>2月18日02:36 UTCに、アプリケーションコードにエラーが発生し、MySQLデータベースへの接続に問題があることが判明しました。調査の結果、これらのエラーは、シャーディングミドルウェアのいくつかの不健全なデプロイメントが原因であると思われました。03:30 UTC に、私たちはデータベース・インフラの再展開を実施し、修復を試みました。しかし、残念ながら、これはすべての Kubernetes ポッドに問題を伝播させ、システム全体のエラーにつながりました。その結果、複数のサービスが 500 エラー応答を返し、GitHub ユーザーが GitHub.com にサインインする際に問題が発生しました。</p>
<p>04:30 UTC に、デプロイメントの 30% でデータベーストポロジーが破損しており、アプリケーションがデータベースに接続できない状態になっていることがわかりました。正しいデータベーストポロジーのコピーをすべての環境に適用し、5:00 UTCまでにサービス全体のエラーを解決しました。その後、ユーザーは GitHub.com にサインインできるようになりました。</p>
<p>今後のインシデントを防ぐため、データベーストポロジーエラーを検出するモニターを追加し、これらの変更が本番システムに影響を与える前に、このエラーを十分に特定できるようにしました。  また、トポロジーの再読み込みについては、成功したものも失敗したものも含めて、観測可能性を向上させました。さらに、この事故の要因をより深く検証し、再発防止のためにアーキテクチャと運用の両方を改善するよう取り組んでいます。</p>
<p><strong>2月28日 16:05 UTC (1時間26分継続)</strong></p>
<p>2月28日16:05 UTCに、GitHub Codespacesのパフォーマンスが低下しているとの報告を受けました。私たちは、17:31 UTCにこのインシデントを解決しました。</p>
<p>この事象は最近発生したものであるため、現在その要因を調査中であり、来月のレポートでより詳細な最新情報を提供する予定です。</p>
<hr />
<p><a href="https://www.githubstatus.com/">状況の</a>変化に関するリアルタイムの最新情報については、当社の<a href="https://www.githubstatus.com/">ステータスページを</a>ご覧ください。私たちが取り組んでいることの詳細については、<a href="https://github.blog/category/engineering/">GitHubエンジニアリングブログを</a>ご覧ください。</p>


