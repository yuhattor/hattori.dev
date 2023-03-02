---
title: "GitHub 課題とプロジェクト - 3月2日更新"
englishtitle: "GitHub Issues & Projects – March 2nd update"
date: "2023-03-02"
cardurl: "https://github.blog/changelog/2023-03-02-github-issues-projects-march-2nd-update"
author: "Kevin Duck"
description: " Today's Changelog brings you roadmap markers and command line support for Projects!  📍 Markers on roadmaps  Keep track of upcoming dates in your roadmap by visualizing the due dates of your milestones, iteration durations and breaks, and additional date fields as vertical markers. Configure these from the Markers menu to display them on the view.  💻 Manage projects from the command line  Interact with projects, items, and fields from your favorite terminal with the GitHub CLI projects extension.  To install the extension in gh :  $ gh extension install github/gh-projects  Usage:  $ gh projects -h  Work with GitHub Projects. Note that the token you are using must have 'project' scope, which is not set by default. You can verify your token scope by running 'gh auth status' and add the project scope by running 'gh auth refresh -s project'.  Usage:  projects [command]  Available Commands:  close Close a project  copy Copy a project  create Create a project  delete Delete a project  edit Edit a project  field-create Create a field in a project  field-delete Delete a field in a project  field-list List the fields in a project  help Help about any command  item-add Add a pull request or an issue to a project  item-archive Archive an item in a project  item-create Create a draft issue item in a project  item-delete Delete an item from a project  item-edit Edit a draft issue in a proje"
coverimage: ""
englishsummary: "  GitHub CLI projects extension now provides roadmap markers and command line support for Projects."
summary: "  GitHub CLI projects extensionで、Projectsのロードマップマーカーとコマンドラインのサポートが追加されました。"
---

<p>本日の Changelog では、Projects のロードマップマーカーとコマンドラインのサポートをお届けします!</p>
<h2 id="round_pushpin-markers-on-roadmaps" id="round_pushpin-markers-on-roadmaps" ><g-emoji fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4cd.png?v8" alias="round_pushpin">📍</g-emoji>ロードマップにマーカーを付ける<a href="#round_pushpin-markers-on-roadmaps" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;g-emoji fallback-src=&quot;https://github.githubassets.com/images/icons/emoji/unicode/1f4cd.png?v8&quot; alias=&quot;round_pushpin&quot;&gt;&#128205;&lt;/g-emoji&gt; Markers on roadmaps"></a></h2>
<p>マイルストーンの期日、イテレーションの期間と区切り、追加の日付フィールドを垂直マーカーとして視覚化することで、ロードマップの今後の日付を追跡します。<code>マーカー</code>メニューからこれらを設定し、ビューに表示します。</p>

<h2 id="computer-manage-projects-from-the-command-line" id="computer-manage-projects-from-the-command-line" ><g-emoji fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4bb.png?v8" alias="computer">💻</g-emoji>コマンドラインからのプロジェクト管理<a href="#computer-manage-projects-from-the-command-line" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;g-emoji fallback-src=&quot;https://github.githubassets.com/images/icons/emoji/unicode/1f4bb.png?v8&quot; alias=&quot;computer&quot;&gt;&#128187;&lt;/g-emoji&gt; Manage projects from the command line"></a></h2>
<p>GitHub<a href="https://cli.github.com/">CLI</a> <code>projects</code>拡張を使えば、お気に入りのターミナルからプロジェクト、アイテム、フィールドを操作することができます。</p>
<p><code>gh</code> に拡張機能をインストールするには、以下のようにします。</p>
<pre><code>gh 拡張インストール github/gh-projects</code></pre>
<p>使い方は</p>
<pre><code>$ gh projects -h
GitHub のプロジェクトで作業する。使用するトークンには 'project' スコープが必要で、デフォルトでは設定されていないことに注意しましょう。トークンのスコープを確認するには 'gh auth status' を実行し、プロジェクトのスコープを追加するには 'gh auth refresh -s project' を実行します。

使い方は
  projects [コマンド].

利用可能なコマンド
  close プロジェクトを閉じる
  copy プロジェクトをコピーする
  create プロジェクトを作成する
  delete プロジェクトを削除する
  edit プロジェクトを編集する
  field-create プロジェクト内にフィールドを作成する
  field-delete プロジェクト内のフィールドを削除します。
  field-list プロジェクト内のフィールドをリストアップします
  help コマンドに関するヘルプ
  item-add プルリクエストや課題をプロジェクトに追加する
  item-archive プロジェクト内のアイテムをアーカイブします
  item-create プロジェクト内に課題のドラフトを作成
  item-delete プロジェクトからアイテムの削除
  item-edit プロジェクト内のドラフト課題の編集
  item-list プロジェクト内のアイテムをリストアップ
  リスト ユーザーまたは組織のプロジェクトをリストアップします
  表示 プロジェクトを表示します。

フラグ
  -h, --help プロジェクトに関するヘルプ

コマンドの詳細については、&quot;projects [command] --help &quot;を使ってください。</code></pre>
<p>フィードバックは<a href="https://github.com/github/gh-projects/issues">リポジトリで</a>共有しましょう。</p>
<p>拡張機能については、こちらのGitHub<a href="https://github.blog/2023-01-13-new-github-cli-extension-tools/">ブログで</a>詳しく解説しています（自分で構築する方法もあります！）。</p>
<h2 id="sparkles-bug-fixes-and-improvements" id="sparkles-bug-fixes-and-improvements" ><g-emoji fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/2728.png?v8" alias="sparkles">✨</g-emoji>バグ修正と改善<a href="#sparkles-bug-fixes-and-improvements" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;g-emoji fallback-src=&quot;https://github.githubassets.com/images/icons/emoji/unicode/2728.png?v8&quot; alias=&quot;sparkles&quot;&gt;&#10024;&lt;/g-emoji&gt; Bug fixes and improvements"></a></h2>
<ul>
<li>ボードのカラムでアイテムを並べ替えるときに自動スクロールするようにした</li>
<li>既存のワークフローをリネームできない不具合を修正</li>
<li>ロードマップビューのトップアイテムのツールチップが切れていたバグを修正</li>
<li>名前に<code>/が</code>含まれる自動追加ワークフローが複製できない不具合を修正（Enterpriseユーザーのみ）</li>
<li>自動追加ワークフローを追加削除する際に確認ダイアログを追加（Enterpriseユーザーのみ）</li>
</ul>
<p>GitHub<a href="http://github.com/features/issues">Issues</a> を使って GitHub をプロジェクト計画に利用する方法、<a href="https://github.com/orgs/github/projects/4247/views/7">ロードマップを</a>確認し、<a href="https://docs.github.com/issues">ドキュメントで</a>さらに詳しく学びましょう。</p>


