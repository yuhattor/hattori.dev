---
title: "GitHub 課題とプロジェクト - 2月23日更新"
englishtitle: "GitHub Issues & Projects – February 23rd update"
date: "2023-02-23"
cardurl: "https://github.blog/changelog/2023-02-23-github-issues-projects-february-23rd-update"
author: "Kevin Duck"
description: " Today's Changelog brings you updates to workflows, roadmaps, our API and makes cross organization projects a breeze!  Automatically add items from multiple repositories  Last month, we shared the latest automation to help you automatically add relevant items to your project! However, if your project pulls from multiple repositories, this wasn't enough. Today, we're shipping the ability to create up to 3 copies of the auto-add workflow.  After configuring and enabling the initial auto-add workflow, open the context menu in the workflow list and select Duplicate workflow to create a new auto-add workflow.  Note Multi-repository auto-add is currently only shipped to Enterprise users  🗺 Reordering roadmap items  Alongside sorting your roadmap items by a field to organize your view, you can now reorder your items by dragging and dropping them in the table. Quickly make adjustments to the ordering of your items or move them to a different group altogether with the new drag-and-drop functionality.  Add cross-organization issues and pull requests to Projects  We've made it easier to use Projects across different organizations, previously this required pasting URLs to a project directly. With this improvement you can:  Search within different organizations for issues or pull requests directly from the omnibar. Just hit # followed by the organization name and a / to start searching with"
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/7584089/220968252-ab56cf88-b42f-4d14-a44b-b84e645d6262.png?ssl=1"
englishsummary: " the omnibar. Today's Changelog brings updates to workflows, roadmaps, the API, and the ability to add cross-organization issues and pull requests to Projects, making cross organization projects easier."
summary: "本日のChangelogでは、ワークフロー、ロードマップ、APIのアップデートと、Projectsに組織横断的な課題やプルリクエストを追加できるようになり、組織横断的なプロジェクトをより簡単に行えるようになりました。"
---

<p>本日のChangelogでは、ワークフロー、ロードマップ、APIのアップデートをお届けし、組織横断的なプロジェクトを円滑に進めます。</p>
<h2 id="&#x2795;-automatically-add-items-from-multiple-repositories" id="&#x2795;-automatically-add-items-from-multiple-repositories" ><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/2795.png" alt="➕" class="wp-smiley" style="height: 1em; max-height: 1em;" /> 複数のリポジトリからアイテムを自動で追加する<a href="#&#x2795;-automatically-add-items-from-multiple-repositories" class="heading-link pl-2 text-italic text-bold" aria-label="&#x2795; Automatically add items from multiple repositories"></a></h2>
<p>先月、プロジェクトに<a href="https://github.blog/changelog/2023-01-19-github-issues-january-19th-update/#%F0%9F%A4%96-automatically-add-project-items-enterprise-accounts-only">関連するアイテムを自動的に</a>追加するための最新の自動化をご紹介しました。しかし、プロジェクトが複数のリポジトリから取得する場合、これだけでは十分ではありません。本日、自動追加ワークフローのコピーを3つまで作成する機能をリリースしました。</p>
<p>最初の自動追加ワークフローを設定し有効にした後、ワークフローリストのコンテキストメニューを開き、<code>ワークフローの複製を</code>選択して新しい自動追加ワークフローを作成します。</p>
<p><code>注記</code> <em>複数リポジトリの自動追加機能は、現在 Enterprise ユーザーのみに提供され ています。</em></p>

<h2 id="world_map-reordering-roadmap-items" id="world_map-reordering-roadmap-items" ><g-emoji fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f5fa.png?v8" alias="world_map">🗺</g-emoji>ロードマップの項目の並べ替え<a href="#world_map-reordering-roadmap-items" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;g-emoji fallback-src=&quot;https://github.githubassets.com/images/icons/emoji/unicode/1f5fa.png?v8&quot; alias=&quot;world_map&quot;&gt;&#128506;&lt;/g-emoji&gt; Reordering roadmap items"></a></h2>
<p>ロードマップの項目をフィールドでソートしてビューを整理するのと同時に、テーブル内で項目をドラッグ＆ドロップして順序を変更できるようになりました。ドラッグ＆ドロップで、項目の順番を変更したり、別のグループに移動させることができます。</p>

<h2 id="&#x2194;-add-cross-organization-issues-and-pull-requests-to-projects" id="&#x2194;-add-cross-organization-issues-and-pull-requests-to-projects" ><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/2194.png" alt="↔" class="wp-smiley" style="height: 1em; max-height: 1em;" /> プロジェクトに組織横断的な課題、プルリクエストを追加<a href="#&#x2194;-add-cross-organization-issues-and-pull-requests-to-projects" class="heading-link pl-2 text-italic text-bold" aria-label="&#x2194; Add cross-organization issues and pull requests to Projects"></a></h2>
<p>以前は、プロジェクトに直接URLを貼り付ける必要がありましたが、異なる組織間でプロジェクトを使用することが容易になりました。この改善により、次のことが可能になります。</p>
<ul>
<li>異なる組織内の課題やプルリクエストをオムニバーから直接検索することができます。組織内の検索を開始するには、<code>#の</code>後に組織名と<code>/を</code>入力します。 </li>
<li>既存の GraphQL API エンドポイントである<code>addProjectV2ItemById</code> を使ってアイテムを追加することができ、プロジェクトに追加する際に異なる組織からの Issue や Pull Request を受け入れるようになりました。 </li>
</ul>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/7584089/220968252-ab56cf88-b42f-4d14-a44b-b84e645d6262.png?ssl=1" alt="a user searches for issues across organizations using the syntax org-name/repo-name" data-recalc-dims="1"></p>
<h2 id="&#x1f4ca;-projects-graphql-api-improvements" id="&#x1f4ca;-projects-graphql-api-improvements" ><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4ca.png" alt="📊" class="wp-smiley" style="height: 1em; max-height: 1em;" /> プロジェクトの GraphQL API の改善<a href="#&#x1f4ca;-projects-graphql-api-improvements" class="heading-link pl-2 text-italic text-bold" aria-label="&#x1f4ca; Projects GraphQL API improvements"></a></h2>
<p>Projects GraphQL API に新しいエンドポイントが追加され、新規プロジェクトの作成、プロジェクトフィールドの作成、プロジェクトフィールドの削除ができるようになりました。詳細は以下のドキュメントをご覧ください。</p>
<ul>
<li><code>createProjectV2Field:</code> <a href="https://docs.github.com/en/graphql/reference/mutations#createprojectv2field">https://docs.github.com/en/graphql/reference/mutations#createprojectv2field</a></li>
<li><code>deleteProjectV2Field:</code> <a href="https://docs.github.com/en/graphql/reference/mutations#deleteprojectv2field">https://docs.github.com/en/graphql/reference/mutations#deleteprojectv2field</a></li>
<li><code>deleteProjectV2:</code> https:<a href="https://docs.github.com/en/graphql/reference/mutations#deleteprojectv2">//docs.github.com/en/graphql/reference/mutations#deleteprojectv2</a></li>
</ul>
<h2 id="sparkles-bug-fixes-and-improvements" id="sparkles-bug-fixes-and-improvements" >バグフィックスと改善<a href="#sparkles-bug-fixes-and-improvements" class="heading-link pl-2 text-italic text-bold" aria-label="&lt;g-emoji fallback-src=&quot;https://github.githubassets.com/images/icons/emoji/unicode/2728.png?v8&quot; alias=&quot;sparkles&quot;&gt;&#10024;&lt;/g-emoji&gt; Bug fixes and improvements"></a></h2>
<ul>
<li>課題コメント投稿直後にスクロールするとページが「ジャンプ」してしまうフォーカスの問題を修正しました。 </li>
<li>Safari と Firefox で<code>TGZ</code>ファイルのアップロードが機能しない問題を解決しました。 </li>
<li>マークダウンエディタ間でフォーカスを素早く切り替えると、Issue Forms でファイルのアップロードに失敗する問題を解決しました。 </li>
<li>閉じたイテレーションの日付を未来に変更できないバグを修正しました。</li>
<li>ズームインしたときに表示タブの幅が正しくなかったバグを修正 </li>
<li>ベータ版ワークフローで、ピルが中央からずれて表示されることがあったバグを修正</li>
</ul>
<p>GitHub<a href="http://github.com/features/issues">issues</a> でプロジェクト計画に GitHub を活用する方法、<a href="https://github.com/orgs/github/projects/4247/views/7">ロードマップを</a>確認し、<a href="https://docs.github.com/issues">docs</a> でさらに詳しく学びましょう。</p>


