---
title: "GitHub Discussionsを閉じる機能を追加する。"
englishtitle: "Adding the ability to close GitHub Discussions"
date: "2023-03-14"
cardurl: "https://github.blog/changelog/2023-03-14-adding-the-ability-to-close-github-discussions"
author: "Kevin Duck"
description: " GitHub Discussions now supports the ability to close a Discussion. Discussions can be closed for one of three reasons: Resolved, Outdated, or Duplicate. Closing a Discussion is much like closing an Issue or a Pull Request. Users can select a reason for closing in the dropdown. A screenshot of the dropdown is shown below:  The reason for closing is visible to users in two places on the page.  First, in the icon at the top of the Discussion:  Second, on the events timeline:  Besides the state of the Discussion being visible on the page, we're also now surfacing the state of a Discussion in search. We're adding three new filters:  is:<closed/opened>  filters out open/closed discussions  reason:<resolved/outdated/duplicate>  returns closed discussions that were closed with the provided reason  closed:<date>  returns discussions closed on a certain date. Supports < and > operators to get discussions closed before or after the date.  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/3157267/224842821-c451b3b9-9cb0-427b-81af-1dddd3935bc9.png?ssl=1"
englishsummary: " GitHub Discussions now supports the ability to close a Discussion with a reason visible to users in two places on the page, and the state of the Discussion is now also being surfaced in search."
summary: "GitHub Discussionsでは、ページの2箇所でユーザーに見える理由をつけてDiscussionを閉じる機能に対応し、Discussionの状態も検索で表面化されるようになりました。"
---

<p>GitHub Discussionsでは、Discussionをクローズする機能が追加されました。ディスカッションは、3つの理由のうち1つで閉じることができます。解決済み」、「古い」、「重複」の3つの理由です。ディスカッションを閉じるのは、IssueやPull Requestを閉じるのと同じです。ユーザーは、ドロップダウンで閉じる理由を選択することができます。ドロップダウンのスクリーンショットを以下に示します。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/3157267/224842821-c451b3b9-9cb0-427b-81af-1dddd3935bc9.png?ssl=1" alt="Dropdown showing Close Discussion options" data-recalc-dims="1"></p>
<p>終了の理由は、ページ上の2つの場所でユーザーに表示されます。</p>
<p>まず、ディスカッションの上部にあるアイコンに表示されます。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/3157267/224843498-f5aa49d4-fd3a-4a30-bdcc-bd7954ec2537.png?ssl=1" alt="Icon at the top of Discussions showing that it is closed" data-recalc-dims="1"></p>
<p>2つ目は、イベントのタイムライン上です。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/3157267/224843530-66bb8bf5-bf3a-4410-87ef-6657ec7d2b20.png?ssl=1" alt="The event timeline showing a Discussion being closed" data-recalc-dims="1"></p>
<p>ディスカッションの状態がページ上で見えるだけでなく、検索でもディスカッションの状態を表示するようになりました。3つの新しいフィルタを追加しました。</p>
<p><code>is:&lt;closed/opened&gt;</code><br />
オープン/クローズドな議論をフィルタリングする</p>
<p><code>reason:&lt;resolved/outdated/duplicate&gt; (解決済み/古い/重複)</code><br />
終了したディスカッションのうち、終了した理由が記載されているものを返却します。</p>
<p><code>休館日：&lt;日付</code><br />
特定の日付に閉じたディスカッションを返します。日付の前後で終了したディスカッションを取得するための<code>&lt;と</code> <code>&gt;</code>演算子をサポートします。</p>


