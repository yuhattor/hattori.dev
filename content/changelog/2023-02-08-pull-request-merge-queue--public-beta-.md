---
title: "プルリクエスト・マージキュー（パブリックベータ版）"
englishtitle: "Pull request merge queue (public beta)"
date: "2023-02-08"
cardurl: "https://github.blog/changelog/2023-02-08-pull-request-merge-queue-public-beta"
author: "Kevin Duck"
description: " Today we are announcing the public beta of pull request merge queue for repos on GitHub Enterprise Cloud and open source organizations! 🎉  Merge queue helps increase velocity in software delivery by automating pull request merges into your busiest branches.  Before merge queue, developers were often required to update their pull request branches prior to merging to ensure their changes wouldn't break the main branch when merged. Each update resulted in a fresh round of continuous integration (CI) checks that would have to finish before the developer could attempt to merge. If another pull request got merged, every developer would have to go through the process again.  Merge queue automates this process by ensuring each pull request queued for merging is built with the pull requests ahead of it in the queue.  Queueing a pull request to merge  If your pull request targets a branch that uses merge queue, instead of merging your pull request directly when it meets the requirements to merge, you will add it to the queue by clicking Merge when ready from the pull request page or from GitHub Mobile.  The queue then creates a temporary branch that contains the latest changes from the base branch, the changes from other pull requests already in the queue, and the changes from your pull request. CI then starts, with the expectation that all required status checks must pass before the br"
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/2503052/217027654-f570fb25-092d-476e-b6f5-0b31b8514662.png?ssl=1"
englishsummary: "anched merge is merged back into the base branch.  GitHub's Merge Queue automates the process of merging pull requests by queuing them and running continuous integration checks to ensure that changes won't break the main branch."
summary: "を実行すると、その変更がベースブランチにマージされます。  GitHub の Merge Queue は、プルリクエストをキューに入れ、継続的インテグレーションチェックを行い、変更がメインブランチを壊さないようにすることで、プルリクエストのマージ処理を自動化します。"
---

<p>本日、GitHub Enterprise Cloud上のレポとオープンソース組織向けのプルリクエスト・マージキューのパブリックベータを発表します！<g-emoji fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f389.png?v8" alias="tada">🎉</g-emoji>。</p>
<p>マージキューは、最も忙しいブランチへのプルリクエストのマージを自動化することで、ソフトウェアのデリバリー速度を向上させるのに役立ちます。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/2503052/217027654-f570fb25-092d-476e-b6f5-0b31b8514662.png?ssl=1" alt="Pull request merge queue" data-recalc-dims="1"></p>
<p>マージキュー以前は、開発者はマージする前にプルリクエストブランチを更新して、マージ時に自分の変更がメインブランチを壊さないようにする必要があることがよくありました。更新するたびに継続的インテグレーション (CI) のチェックが繰り返され、それが終わらないと開発者はマージすることができませんでした。別のプルリクエストがマージされると、すべての開発者がこのプロセスを再度行う必要がありました。</p>
<p>Merge queue は、マージのためにキューに入れられた各プルリクエストが、キューの中でその前にあるプルリクエストと一緒にビルドされるようにすることで、このプロセスを自動化します。</p>
<h2 id="queueing-a-pull-request-to-merge" id="queueing-a-pull-request-to-merge" >プルリクエストをマージするためにキューに入れる<a href="#queueing-a-pull-request-to-merge" class="heading-link pl-2 text-italic text-bold" aria-label="Queueing a pull request to merge"></a></h2>
<p>マージキューを使うブランチを対象とするプルリクエストの場合は、マージ要件を満たしたときに直接マージするのではなく、プルリクエストページや GitHub Mobile から<strong>Merge when ready</strong>をクリックしてキューに追加することになります。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/2503052/217023882-cf4bf568-af5d-469e-882a-14f1837add72.gif?ssl=1" alt="Queue to merge" data-recalc-dims="1"></p>
<p>すると、キューは一時ブランチを作成し、ベースブランチからの最新の変更点、すでにキューにある他のプルリクエストからの変更点、そしてあなたのプルリクエストからの変更点が含まれるようになります。そして、ブランチ（とそれを表すプルリクエスト）がマージされる前に、必要なすべてのステータスチェックが通過することを想定して CI が開始されます。</p>
<p>キューに入れられたプルリクエストにマージの競合があったり、必要なステータスチェックに失敗したりすると、それが最前面に達した時点で自動的にキューから削除され、通知が送信されます。問題が解決されると、再びキューに追加されます。</p>
<p><a href="https://docs.github.com/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue">マージキューによるプルリクエストのマージについては</a>、プルリクエストのページで詳しく説明しています。<a href="https://testflight.apple.com/join/NLskzwi5">iOS TestFlight</a>または<a href="https://play.google.com/apps/testing/com.github.android">Google Play (Beta)</a> から GitHub Mobile のベータ版を使って、外出先からプルリクエストをキューに入れることもできますよ。</p>
<h2 id="viewing-the-queue" id="viewing-the-queue" >キューの表示<a href="#viewing-the-queue" class="heading-link pl-2 text-italic text-bold" aria-label="Viewing the queue"></a></h2>
<p>自分がキューのどこにいるのか、常に把握することができます。</p>
<p>ブランチページやプルリクエストページからアクセスできるキューの詳細ページには、キュー内のプルリクエストとそれぞれのステータス、必要なステータスチェックやマージまでの推定時間などが表示されます。また、マージされたプルリクエストの数や過去 30 日間の傾向も表示されます。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/2503052/217023511-13c729f7-7458-4ee3-8f7c-be5a7cf06f99.png?ssl=1" alt="Merge queue details page" data-recalc-dims="1"></p>
<p>権限によっては、このページからプルリクエストをキューから削除したり、キューをクリアしたりすることもできます。</p>
<h2 id="getting-started" id="getting-started" >はじめに<a href="#getting-started" class="heading-link pl-2 text-italic text-bold" aria-label="Getting started"></a></h2>
<p>マージキューは、全体のベロシティを向上させ、開発者の生産性に影響を与える手動でのブランチ更新を回避するのに役立ちます。最も忙しいブランチでマージキューを<a href="https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/managing-a-merge-queue">有効に</a>する方法について、詳しくはこちらをご覧ください。</p>
<p>マージキューをどのように改善したらよいか、皆さんのご意見をお聞かせください。マージ<a href="https://github.com/community/community/discussions/46757">キューのパブリックベータディスカッションに</a>参加してください。</p>


