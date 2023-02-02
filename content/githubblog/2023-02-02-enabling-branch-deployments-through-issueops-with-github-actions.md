---
title: "GitHub ActionsでIssueOpsによるブランチデプロイメントを可能にする。"
subtitle: "もし開発者がブランチデプロイを活用したいが、ChatOpsのフルスタックをリポジトリに統合していない場合はどうすればいいでしょうか？私たちは、すべての開発者がGitHubリポジトリから簡単にブランチデプロイを利用できる方法を見つけたいと思い、branch-deploy Actionが生まれました!"
englishsubtitle: "What if developers want to leverage branch deployments but don't have a full ChatOps stack integrated with their repositories? We wanted to set out to find a way for all developers to be able to take advantage of branch deployments with ease, right from their GitHub repository, and so the branch-deploy Action was born!"
englishtitle: "Enabling branch deployments through IssueOps with GitHub Actions"
date: "2023-02-02"
cardurl: "https://github.blog/2023-02-02-enabling-branch-deployments-through-issueops-with-github-actions/"
author: "Grant Birkinbine"
description: "At GitHub, the branch deploy model is ubiquitous and it is the standard way we ship code to production, and it has been for years. We released details about how we perform branch deployments with ChatOps all the way back in 2015 ."
coverimage: "https://github.blog/wp-content/uploads/2022/09/Open-Source-Engineering@2x.png?resize=1600%2C850"
category: "Engineering,Open Source,automation,Deployment,GitHub Actions"
---

<p>GitHubでは、ブランチ・デプロイ・モデルはどこにでもあり、私たちがコードをプロダクションに出荷する標準的な方法であり、それは何年も前からそうでした。私たちは、<a href="https://github.blog/2015-06-02-deploying-branches-to-github-com/">2015</a>年にChatOpsでブランチデプロイを行う方法の詳細を公開しました。</p>
<p>私たちはほとんどのリポジトリでChatOpsを使用してブランチデプロイメントを実行することができますが、ChatOpsが単にうまくいかない状況もいくつかあります。もし開発者がブランチデプロイを活用したいが、リポジトリにChatOpsのフルスタックを統合していない場合はどうすればいいのでしょうか？私たちは、すべての開発者がGitHubのリポジトリから簡単にブランチ・デプロイを利用できる方法を見つけたいと思い、branch-deploy Actionが生まれました!</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/usage.gif" alt="Gif demonstrating how to us the branch-deploy Action."/></p>
<h2 id="how-does-github-use-this-action">GitHubはこのアクションをどのように使っているのか？<a href="#how-does-github-use-this-action" class="heading-link pl-2 text-italic text-bold" aria-label="How Does GitHub use this Action?"></a></h2>
<p>GitHubは主にChatOpsと<a href="https://hubot.github.com/">Hubot</a>)を使って、可能な限りブランチデプロイを促進するようにしています。ChatOpsが使えない場合は、このbranch-deploy Actionで代用しています。私たちのユースケースの大半は、インフラストラクチャー・アズ・コード（IaC）リポジトリで、インフラの変更をTerraformを使ってデプロイしています。GitHubはこのActionを多くの内部リポジトリで使っていますし、<a href="https://www.npmjs.com/">npmも</a>そうです。他にも多くの公共、オープンソース、企業組織がこのActionを採用し、コードを本番環境に出荷するのに役立っています。</p>
<h2 id="understanding-the-branch-deploy-model">ブランチ・デプロイ・モデルを理解する<a href="#understanding-the-branch-deploy-model" class="heading-link pl-2 text-italic text-bold" aria-label="Understanding the branch deploy model"></a></h2>
<p>branch-deploy アクションを理解する前に、まずブランチデプロイモデルとは何か、そしてなぜそれが有用なのかを理解しましょう。</p>
<p>ブランチデプロイモデルを理解するために、まず伝統的な<strong>デプロイ → マージ</strong>モデルを見てみましょう。それは次のようなものです。</p>
<ol>
<li>ブランチを作成する。</li>
<li>ブランチにコミットを追加する。</li>
<li>プルリクエストを発行する。</li>
<li>フィードバックやピアレビューを収集する</li>
<li>ブランチをマージする。</li>
<li>デプロイは<code>メイン</code>ブランチから開始されます。</li>
</ol>
<div class="image-frame image-frame-full border rounded-2 overflow-hidden d-flex flex-row flex-justify-center" style="background: #EAEEF2"><br />
<img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/merge-deploy.jpg?w=720&#038;resize=720%2C237" alt="Diagram outlining the steps of the traditional deploy model, enumerated in the numbered list above." width="720" height="237" class="aligncenter size-large wp-image-69854 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/merge-deploy.jpg?w=720&#038;resize=720%2C237 720w, https://github.blog/wp-content/uploads/2023/02/merge-deploy.jpg?w=300 300w" sizes="(max-width: 720px) 100vw, 720px" data-recalc-dims="1" /><br /></div>
<p>では、<strong>ブランチのデプロイモデルを見て</strong>いきましょう。</p>
<ol>
<li>ブランチを作成する。</li>
<li>ブランチにコミットを追加する。</li>
<li>プルリクエストを作成する。</li>
<li>フィードバックとピアレビューを収集する</li>
<li>変更をデプロイする</li>
<li>検証する</li>
<li>あなたのブランチを<code>main</code>/<code>master</code>ブランチにマージする。 </li>
</ol>
<div class="image-frame image-frame-full border rounded-2 overflow-hidden d-flex flex-row flex-justify-center" style="background: #EAEEF2"><br />
<img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/branch-deploy.jpg?w=720&#038;resize=720%2C244" alt="Diagram outlining the steps of the branch deploy model, enumerated in the list above." width="720" height="244" class="aligncenter size-large wp-image-69855 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/branch-deploy.jpg?w=720&#038;resize=720%2C244 720w, https://github.blog/wp-content/uploads/2023/02/branch-deploy.jpg?w=300 300w" sizes="(max-width: 720px) 100vw, 720px" data-recalc-dims="1" /><br /></div>
<p><code>メイン</code>ブランチが本当に安定したブランチになることはないため、マージデプロイモデルは本質的にリスクが高いです。デプロイに失敗したり、ロールバックが必要になったりした場合は、もう一度すべてのプロセスをたどって変更をロールバックすることになります。しかし、ブランチデプロイモデルでは、<code>メイン</code>ブランチは常に「良い」状態であり、いつでもブランチデプロイからデプロイを元に戻すことができます。ブランチデプロイモデルでは、ブランチが正常にデプロイされ、検証された時点で初めて変更を<code>メイン</code>ブランチにマージします。</p>
<p><em>注：これは、<a href="https://docs.github.com/en/get-started/quickstart/github-flow">GitHubフローと</a>呼ばれることもあります。</em></p>
<h3 id="key-concepts">主要な概念<a href="#key-concepts" class="heading-link pl-2 text-italic text-bold" aria-label="Key concepts"></a></h3>
<p>ブランチ・デプロイ・モデルの主要な概念です。</p>
<ul>
<li><code>main</code>ブランチは、常に安定したデプロイ可能なブランチであるとみなされます。</li>
<li>すべての変更は、<code>メイン</code>ブランチにマージされる前に本番環境にデプロイされます。</li>
<li>ブランチデプロイメントをロールバックするには、<code>メイン</code>ブランチをデプロイします。</li>
</ul>
<p>ここまでで、ブランチ配備の方法論に納得していただけたのではないでしょうか。では、どのように実装すればいいのでしょうか?GitHub Actions を使った IssueOps の紹介です。</p>
<h2 id="issueops">IssueOps (課題処理)<a href="#issueops" class="heading-link pl-2 text-italic text-bold" aria-label="IssueOps"></a></h2>
<p>IssueOps を定義するには、似たようなものである<strong>ChatOps</strong> と比較するのが一番わかりやすいでしょう。ChatOps という概念はすでにご存知かもしれませんが、そうでない場合はここで簡単に定義しておきましょう。</p>
<blockquote><p>
  ChatOpsとは、チャットボットと対話し、チャットプラットフォームで直接コマンドを実行するプロセスのことです。例えば、ChatOpsでは、ウェブサイトの状態を確認するために、<code>.ping example.orgの</code>ようなことを行うことができます。
</p></blockquote>
<p>IssueOpsは、同じ考え方を採用していますが、媒体が異なります。コマンドを実行するためにチャットサービス（DiscordやSlackなど）を使うのではなく、GitHub Issueやプルリクエストのコメントを利用するのです。<a href="https://github.com/features/actions">GitHub Actions</a>は、IssueOps コマンドが呼び出されたときに、私たちが望むロジックを実行するランタイムです。</p>
<h2 id="github-actions">GitHub Actions<a href="#github-actions" class="heading-link pl-2 text-italic text-bold" aria-label="GitHub Actions"></a></h2>
<p>どのように動作するのでしょうか？このセクションでは、この Action がどのように動作するのかを詳しく説明し、あなたのプロジェクトで活用するきっかけになればと思います。完全なソースコードと詳細なドキュメントは<a href="https://github.com/github/branch-deploy">GitHubで</a>見ることができます。</p>
<p>以下、branch-deploy Actionのデモ設定を使って、その手順を説明します。</p>
<h4 id="1-create-this-file-under-github-workflows-branch-deploy-yml-in-your-github-repository">1.1. GitHub リポジトリの<code>.github/workflows/branch-deploy.yml</code>の下に、以下のファイルを作成します。<a href="#1-create-this-file-under-github-workflows-branch-deploy-yml-in-your-github-repository" class="heading-link pl-2 text-italic text-bold" aria-label="1. Create this file under &lt;code&gt;.github/workflows/branch-deploy.yml&lt;/code&gt; in your GitHub repository:"></a></h4>
<pre><code class="language-yaml">名前: "ブランチデプロイデモ"

# このワークフローは、プルリクエストの新しいコメントに対して実行されます - 例。コメントとして ".deploy" を指定
を実行します。
  issue_comment:
    タイプ[作成済み］

ジョブズ
  demo:
    もし${{ github.event.issue.pull_request }} を実行します。# pull requestのコメントに対してのみ実行 (issueのコメントに対しては実行する必要なし)
    実行環境: ubuntu-latest
    の手順で実行します。
      # IssueOps のブランチデプロイメントロジックを実行する、ばんざーい!
      # これは以下の全てのステップの "ゲート "として使われ、条件付きでステップ/デプロイメントを起動します。
      - uses: github/branch-deploy@vX.X.X # X.X.X を使いたいバージョンに置き換えてください。
        id: branch-deploy # このステップのアウトプットを参照できるように、ここに id をつけることが重要です。
        を使っています。
          trigger:".deploy" # プルリクエストのコメントで探したいトリガーフレーズ

      # プロジェクトのデプロイメントロジックをここで実行します - 例は以下の通りです。

      # branch-deploy ステップで提供された ref に基づいて、プロジェクトのリポジトリをチェックアウトします。
      - uses: actions/checkout@3.0.2
        もし${{ steps.branch-deploy.outputs.continue == 'true' }} # トリガーとなるフレーズが見つからない場合はスキップします。# トリガーとなるフレーズが見つからなかったらスキップする
        を使っています。
          ref: ${{ steps.branch-deploy.outputs.ref }} # トリガーとなるフレーズが見つからない場合はスキップする。# branch-deploy ステップから検出されたブランチを使用する

      # ここで偽の "noop" デプロイメントロジックを実行する
      # 条件付きで noop のデプロイを実行する
      - name: 偽の noop デプロイ
        もし${{ steps.branch-deploy.outputs.continue == 'true' &amp;&amp; steps.branch-deploy.outputs.noop == 'true' }} # トリガーとなるフレーズが見つかり、branch-deploy ステップで noop デプロイが検出された場合のみ実行されます。# トリガーフレーズが見つかり、branch-deploy ステップが noop デプロイを検出した場合のみ実行される
        run: echo "I am doing a fake noop deploy" （偽の noop デプロイをしています。

      # ここで、偽の "通常の" デプロイメントロジックを実行します。
      # 条件付きで通常のデプロイを実行する
      - name: 偽の通常のデプロイ
        もし${{ steps.branch-deploy.outputs.continue == 'true' &amp;&amp; steps.branch-deploy.outputs.noop != 'true' }} # トリガーとなるフレーズが見つかり、branch-deploy ステップが通常のデプロイを検出した場合のみ実行されます。# トリガーフレーズが見つかり、branch-deploy ステップが通常のデプロイを検出した場合のみ実行される
        run: echo "私は偽の通常のデプロイを行っています"
</code></pre>
<h4 id="2-trigger-a-noop-deploy-by-commenting-deploy-noop-on-a-pull-request">2.プルリクエストに<code>.deploy noop</code>とコメントすることで noop デプロイをトリガーします。<a href="#2-trigger-a-noop-deploy-by-commenting-deploy-noop-on-a-pull-request" class="heading-link pl-2 text-italic text-bold" aria-label="2. Trigger a noop deploy by commenting &lt;code&gt;.deploy noop&lt;/code&gt; on a pull request."></a></h4>
<p>noopデプロイが検出されたので、このアクションは<code>noop</code>変数を<code>trueに</code>出力します。IssueOpsコマンドを実行する正しい権限がある場合、このアクションは<code>continue</code>変数も<code>trueに</code>出力します。<code>fake noop deployという</code>名前のステップが実行され、<code>fake regular deployの</code>ステップはスキップされます。</p>
<h4 id="3-after-your-noop-deploy-completes-you-would-typically-run-deploy-to-execute-the-actual-deployment-fake-regular-deploy">3.3. noop deployが完了したら、通常、<code>.deployを</code>実行して、実際のデプロイメント、<code>偽の通常のデプロイメントを</code>実行することになります。<a href="#3-after-your-noop-deploy-completes-you-would-typically-run-deploy-to-execute-the-actual-deployment-fake-regular-deploy" class="heading-link pl-2 text-italic text-bold" aria-label="3. After your noop deploy completes, you would typically run &lt;code&gt;.deploy&lt;/code&gt; to execute the actual deployment, &lt;code&gt;fake regular deploy&lt;/code&gt;."></a></h4>
<h2 id="features">特徴<a href="#features" class="heading-link pl-2 text-italic text-bold" aria-label="Features"></a></h2>
<p>branch-deploy Action の最も優れた点は、あらゆるデプロイメントターゲットやユースケースに対して<strong>高度に</strong>カスタマイズ可能であることです。以下は、このActionに搭載されている機能の一部です。</p>
<ul>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f50d.png" alt="🔍" class="wp-smiley" style="height: 1em; max-height: 1em;" /> IssueOpsコマンドがプルリクエストで使用されると検出します。 </li>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4dd.png" alt="📝" class="wp-smiley" style="height: 1em; max-height: 1em;" /> 設定可能：コマンドの構文、環境、noopトリガー、ベースブランチ、反応などを選択できます。</li>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/2705.png" alt="✅" class="wp-smiley" style="height: 1em; max-height: 1em;" /> リポジトリに設定されたブランチ保護設定を尊重します。</li>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4ac.png" alt="💬" class="wp-smiley" style="height: 1em; max-height: 1em;" /> IssueOps コマンドにコメントし、反応します。</li>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f680.png" alt="🚀" class="wp-smiley" style="height: 1em; max-height: 1em;" /> 簡単な設定でGitHubデプロイメントをトリガーします。</li>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f513.png" alt="🔓" class="wp-smiley" style="height: 1em; max-height: 1em;" /> デプロイロックにより、複数のデプロイの衝突を防止します。</li>
<li><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f30e.png" alt="🌎" class="wp-smiley" style="height: 1em; max-height: 1em;" /> 設定可能な環境ターゲット</li>
</ul>
<p>また、リポジトリには<a href="https://github.com/github/branch-deploy/blob/main/docs/usage.md">使用ガイドが</a>付属しており、利用可能な IssueOps コマンドとその動作に素早く慣れるために、あなたとあなたのチームが参照することができます。</p>
<h2 id="examples">例<a href="#examples" class="heading-link pl-2 text-italic text-bold" aria-label="Examples"></a></h2>
<p>branch-deploy アクションはカスタマイズ可能で、さまざまなプロジェクトに適しています。ここでは、branch-deployアクションを使用して、さまざまなサービスにデプロイする方法をいくつか例として紹介します。</p>
<ul>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#simple-example">簡単な例</a></li>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#terraform">テラフォーム</a></li>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#heroku">Heroku</a></li>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#railway">鉄道</a></li>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#ssh">SSHデプロイメント</a></li>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#cloudflare-pages">Cloudflareページ</a></li>
<li><a href="https://github.com/github/branch-deploy/blob/main/docs/examples.md#cloudflare-workers">Cloudflare ワーカー</a></li>
</ul>
<h2 id="conclusion">まとめ<a href="#conclusion" class="heading-link pl-2 text-italic text-bold" aria-label="Conclusion"></a></h2>
<p>もしあなたがDevOpsの経験を高めたい、デプロイの信頼性を高めたい、あるいは変更をより速く出荷したいと考えているなら、ブランチデプロイはあなたのためにあります!</p>
<p>ブランチ・デプロイ・モデルがなぜ本番環境へのコード配布に最適なのか、ご理解いただけたでしょうか。</p>
<p>GitHub + Actions + IssueOps を使えば、どんなリポジトリでもブランチ・デプロイ・モデルを利用することができるのです!</p>
<p><small>ソースコード<a href="https://github.com/marketplace/actions/branch-deploy">GitHub</a></small></p>


