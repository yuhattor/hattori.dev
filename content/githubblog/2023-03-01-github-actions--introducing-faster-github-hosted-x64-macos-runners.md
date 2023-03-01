---
title: "GitHub Actions。GitHubでホストされるx64 macOSランナーの高速化の紹介"
subtitle: "GitHubがホストするmacOSランナー（x64版）を使って、macOS上のGitHub Actionsのジョブを高速化します。"
englishsubtitle: "Speed up your GitHub Actions jobs on macOS with all new, faster GitHub-hosted macOS runners for x64."
englishtitle: "GitHub Actions: Introducing faster GitHub-hosted x64 macOS runners"
date: "2023-03-01"
cardurl: "https://github.blog/2023-03-01-github-actions-introducing-faster-github-hosted-x64-macos-runners/"
author: "Stephen Glass"
description: " Today, GitHub is releasing a public beta for all new, more powerful hosted macOS runners for GitHub Actions. Teams who are looking to speed up their macOS jobs now have new options to meet their needs.  Faster GitHub-hosted macOS runners  When developers use GitHub-hosted runners for GitHub Actions, GitHub is always working to give teams performance and flexibility to quickly build for different platforms. The new GitHub-hosted macOS runners are based on the most current x64 Apple hardware and reduce the time it takes to run your jobs. This means less time waiting on your CI and more time building and rapidly testing code.  In addition to the existing 3-core macOS hosted runners, we are also introducing a new “XL” size, 12-core macOS runner to allow you to pay for that extra performance when you need it. Increasing your runner size is as simple as changing a single line in your workflow file, making it super easy to speed up lagging builds, and with on-demand availability when you want it, you only pay for what you use.  PyTorch, the open source machine learning framework, has used the new runner to improve build times from 1.5 hours to 30 minutes!  If you’re already using the 3-core macOS runners, simply request to join the beta , and we’ll give you access to the hardware to our new fleet. To try the new 12-core runner runner, update the runs-on: key in your GitHub Actions wo"
coverimage: "https://github.blog/wp-content/uploads/2022/06/Engineering-Product@2x.png?resize=1600%2C850"
category: "Engineering,Product,GitHub Actions"
englishsummary: "  GitHub is releasing a public beta for new, faster hosted macOS runners for GitHub Actions, with an additional "XL" size, 12-core runner, to reduce job running time and improve build times."
summary: "  GitHubは、GitHub Actionsのための新しい高速なホスト型macOSランナーのパブリックベータをリリースし、ジョブの実行時間を短縮しビルド時間を改善するために、12コアのランナー「XL」サイズを追加しています。"
---

<p>本日、GitHubはGitHub Actionsのための、より強力な新しいホスト型macOSランナーすべてのパブリックベータ版をリリースします。macOSのジョブを高速化したいチームのニーズに応える、新しいオプションが登場しました。</p>
<h2 id="faster-github-hosted-macos-runners">より高速なGitHub-hosted macOSランナー<a href="#faster-github-hosted-macos-runners" class="heading-link pl-2 text-italic text-bold" aria-label="Faster GitHub-hosted macOS runners"></a></h2>
<p>GitHubは、開発者がGitHub ActionsのGitHubホストランナーを使用する際、異なるプラットフォーム向けに素早くビルドできるパフォーマンスと柔軟性をチームに提供できるよう常に努力しています。新しいGitHub-hosted macOSランナーは最新のx64 Appleハードウェアに基づいており、ジョブの実行にかかる時間を短縮します。つまり、CIで待つ時間を減らし、コードのビルドと迅速なテストに時間を割くことができます。</p>
<p>既存の3コアmacOSホストランナーに加え、新たに「XL」サイズ、12コアmacOSランナーを導入し、必要なときに追加パフォーマンスを支払うことができるようにしました。ランナーサイズの増加は、ワークフローファイルの1行を変更するのと同じくらい簡単で、遅れているビルドを高速化するのがとても簡単になります。</p>
<blockquote><p>
  オープンソースの機械学習フレームワークであるPyTorchは、新しいランナーを使用して、<a href="https://github.com/pytorch/pytorch/pull/81874#issue-1313214360">ビルド時間を</a>1.5時間から30分に<a href="https://github.com/pytorch/pytorch/pull/81874#issue-1313214360">改善</a>しました!
</p></blockquote>
<p>すでに3コアのmacOSランナーを使っている方は、<a href="https://gh.io/preview/macos-xl">ベータ版</a>への参加をリクエストしていただければ、新しいフリートへのハードウェアのアクセス権を差し上げます。新しい12コアランナーを試すには、ベータ版に参加したら、GitHub ActionsのワークフローYAMLの<code>runs-on:</code>キーを更新して、<code>macos-12-xl</code>または<code>macos-latest-xl</code>ランナーイメージをターゲットにするようにしてください。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/221970481-8265a068-3ffa-4950-8636-7b5904f9f104.png?w=841&#038;resize=841%2C278" alt="" width="841" height="278" class="aligncenter size-large wp-image-70373 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/221970481-8265a068-3ffa-4950-8636-7b5904f9f104.png?w=841&#038;resize=841%2C278 841w, https://github.blog/wp-content/uploads/2023/02/221970481-8265a068-3ffa-4950-8636-7b5904f9f104.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/221970481-8265a068-3ffa-4950-8636-7b5904f9f104.png?w=768 768w" sizes="(max-width: 841px) 100vw, 841px" data-recalc-dims="1" /></p>
<p>新しい macOS XL ランナーは、プライベートとパブリックの両方のリポジトリで常に課金されるため、無料で含まれている GitHub Action 分を消費することはありません。ランナーのジョブ分数ごとの価格設定について詳しくは、<a href="https://docs.github.com/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources">ドキュメントを</a>ご覧ください。</p>
<h2 id="learn-more-and-join-the-beta">詳細とベータ版への参加<a href="#learn-more-and-join-the-beta" class="heading-link pl-2 text-italic text-bold" aria-label="Learn more and join the beta"></a></h2>
<p>新しい macOS ランナーの使用に関する詳細は、<a href="https://docs.github.com/actions/using-github-hosted-runners/about-github-hosted-runners#supported-runners-and-hardware-resources">ホストされたランナーのドキュメント</a>をご覧ください。</p>
<div class="content-button-wrap text-left"><a href="https://gh.io/preview/macos-xl" target="_self" class="btn-mktg arrow-target-mktg">ベータ版へのサインアップはこちらから。<svg xmlns="http://www.w3.org/2000/svg" class="octicon arrow-symbol-mktg" width="24" height="24" viewBox="0 0 16 16" fill="none"><path fill="currentColor" d="M7.28033 3.21967C6.98744 2.92678 6.51256 2.92678 6.21967 3.21967C5.92678 3.51256 5.92678 3.98744 6.21967 4.28033L7.28033 3.21967ZM11 8L11.5303 8.53033C11.8232 8.23744 11.8232 7.76256 11.5303 7.46967L11 8ZM6.21967 11.7197C5.92678 12.0126 5.92678 12.4874 6.21967 12.7803C6.51256 13.0732 6.98744 13.0732 7.28033 12.7803L6.21967 11.7197ZM6.21967 4.28033L10.4697 8.53033L11.5303 7.46967L7.28033 3.21967L6.21967 4.28033ZM10.4697 7.46967L6.21967 11.7197L7.28033 12.7803L11.5303 8.53033L10.4697 7.46967Z"></path><path class="octicon-chevrow-stem" stroke="currentColor" d="M1.75 8H11" stroke-width="1.5" stroke-linecap="round"></path></svg></a></div>
<h2 id="apple-silicon-is-on-the-way">Apple シリコンが登場<a href="#apple-silicon-is-on-the-way" class="heading-link pl-2 text-italic text-bold" aria-label="Apple silicon is on the way!"></a></h2>
<p>ホスト型ランナーのデータセンターで、Apple 製シリコンベースのマシンのラックアップとテストを開始しました。この<a href="https://github.com/github/roadmap/issues/528">ロードマップの項目に従って</a>、進捗を確認してください。ハードウェアの入手状況に応じて、CY2023年に限定的なベータ版を提供したいと考えています。</p>


