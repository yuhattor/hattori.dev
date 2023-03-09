---
title: "GitHub Docsの新しい検索方法について"
subtitle: "GitHub Docsは最近、サイトサーチをElasticsearchに変更しました。その時の実装を紹介します。"
englishsubtitle: "GitHub Docs recently changed its site-search to Elasticsearch. Here’s how it was implemented."
englishtitle: "How GitHub Docs’ new search works"
date: "2023-03-09"
cardurl: "https://github.blog/2023-03-09-how-github-docs-new-search-works/"
author: "Peter Bengtsson"
description: " Until recently, the site-search on GitHub Docs was an in-memory solution. While it was a great starting point, we ultimately needed a solution that would scale with our growing needs, so we rewrote it in Elasticsearch. In this blog post, we share how the implementation works and how you can impress users with your site-search by doing the same.  How it started  Our previous solution couldn’t scale because it required loading all of the records into memory (the Node.js code that Express.js runs). This means that we’d need to scrape all the searchable text—title, headings, breadcrumbs, content, etc.—and store that data somewhere so it could quickly be loaded in the Node process runtime. To store the data, we used the Git repository itself, so when we built the Docker image run in Azure, it would have access to all the searchable text from disk.  It would take a little while to load in all the searchable text, so we generated a serialized index from the searchable text, and stored that on disk too. This solution is OKish if your data is small, but we have eight languages and five different versions per language.  Running Elasticsearch locally  The reason we picked Elasticsearch over other alternatives is a story for another day, but one compelling argument is that it’s possible to run it locally on your laptop. For the majority of contributors who make copy edits, the task of ins"
coverimage: "https://github.blog/wp-content/uploads/2022/09/Open-Source-Engineering@2x.png?resize=1600%2C850"
category: "Engineering,Open Source,Elasticsearch,GitHub Docs"
englishsummary: "uring their changes don’t break the search experience is a daunting one. However, running Elasticsearch locally means they can test their changes before they commit them.   GitHub Docs recently rewrote their site-search solution in"
summary: "その変更が検索エクスペリエンスを壊さないようにすることは、大変なことです。しかし、Elasticsearchをローカルで実行することで、コミットする前に変更をテストすることができます。   GitHub Docsは最近、サイト内検索ソリューションを次のように書き直しました。"
---

<p>最近まで、<a href="https://docs.github.com/">GitHub Docs</a>のサイト内検索はインメモリソリューションでした。これは素晴らしい出発点でしたが、私たちは最終的にニーズの増加に合わせてスケールするソリューションが必要だったため、Elasticsearchで書き直しました。このブログポストでは、この実装がどのように機能するのか、また、同じようにサイト内検索を行うことで、ユーザーに感動を与えることができるのかについて紹介します。</p>
<h2 id="how-it-started">どのように始まったか<a href="#how-it-started" class="heading-link pl-2 text-italic text-bold" aria-label="How it started"></a></h2>
<p>以前のソリューションでは、すべてのレコードをメモリ（Express.jsが実行するNode.jsのコード）に読み込む必要があったため、拡張できませんでした。つまり、検索可能なテキスト（タイトル、見出し、パンくず、コンテンツなど）をすべてスクレイピングし、そのデータをどこかに保存して、Node プロセスのランタイムですぐに読み込めるようにする必要がありました。データを保存するために、Gitリポジトリそのものを使いました。Azureで実行するDockerイメージを構築すると、ディスクからすべての検索可能なテキストにアクセスできるようになります。</p>
<p>検索可能なテキストをすべて読み込むには少し時間がかかるので、検索可能なテキストから<em>シリアライズされた</em> <em>インデックスを</em>生成し、それもディスクに保存しました。データが少なければこの方法でOKなのですが、私たちは8つの言語と言語ごとに5つの異なるバージョンを持っています。</p>
<h2 id="running-elasticsearch-locally">ローカルでElasticsearchを実行する<a href="#running-elasticsearch-locally" class="heading-link pl-2 text-italic text-bold" aria-label="Running Elasticsearch locally"></a></h2>
<p>他の選択肢ではなくElasticsearchを選んだ理由は別の日にお話しますが、説得力のある論拠として、ラップトップ上でローカルに実行することが可能であることがあげられます。コピー編集を行う大多数のコントリビューターにとって、Elasticsearchをローカルにインストールする作業は必要ありません。そのため、デフォルトでは<code>/api/search</code>Express.js のミドルウェアは以下のような感じになっています。</p>
<pre><code>if (process.env.ELASTICSEARCH_URL) { です。
  router.use('/search', search)
} else {
  router.use()
    '/search'です。
    createProxyMiddleware({)
      target: 'https://docs.github.com'。
  ...
</code></pre>
<p>誰かがラップトップ（またはCodespaces）で<code>http://localhost:4000/api/search</code>を使用すると、Elasticsearchのものを私たちのプロダクションサーバに転送するだけです。そうすれば、ローカルで検索エンジンをデバッグしているエンジニア（私のような）は、<code>http://localhost:9200</code>で Elasticsearch を起動し、それを<code>.env</code>ファイルに設定することができます。これで、エンジニアは自分のローカルElasticsearchで、新しい検索クエリのテクニックをすぐに試すことができるようになりました。</p>
<h2 id="the-search-implementation">検索の実装<a href="#the-search-implementation" class="heading-link pl-2 text-italic text-bold" aria-label="The search implementation"></a></h2>
<p>私たちの検索機能のコアとなる考え方は、Elasticsearchに1回だけクエリを送信することです。1つのリクエストを送信するのではなく、より具体的な検索クエリを最初に試して、結果が少なすぎる場合は、2番目の、より定義された検索クエリを試みることができます。</p>
<pre><code>// 注意！これは私たちが行うことではありません。

let result = await client.search({ index, body: searchQueryStrict })
if (result.hits.length === 0) { 。
  // 厳密には何も見つからないので、緩いクエリで再試行する。
  result = await client.search({ index, body: searchQueryLoose })
}
</code></pre>
<p>最も正確な結果を得るために、ブーストと様々なマッチング手法のマトリックスを使用しています。やや擬似的なコードにすると、次のようになります。</p>
<p>クエリが複数の用語である場合<code>（_explicitの</code>意味については後で説明します）。</p>
<pre><code>[
  { match_phrase: { title_explicit:[オブジェクト] }。},
  { match_phrase: { title: [Object] }.},
  { match_phrase: { headings_explicit:[オブジェクト] }。},
  { match_phrase: { headings:[オブジェクト] }。},
  { match_phrase: { content:[オブジェクト] }。},
  { match_phrase: { content_explicit:[オブジェクト] }。},
  { match:{ title_explicit:[オブジェクト] }。},
  { match:{ headings_explicit:[オブジェクト] }。},
  { match:{ content_explicit:[オブジェクト] }。},
  { match:{ title: [オブジェクト] }.},
  { match:{ headings:[オブジェクト] }。},
  { match:{ content:[オブジェクト] }.},
  { match:{ title_explicit:[オブジェクト] }。},
  { match:{ headings_explicit:[オブジェクト] }。},
  { match:{ content_explicit:[オブジェクト] }。},
  { match:{ title: [オブジェクト] }.},
  { match:{ headings:[オブジェクト] }。},
  { match:{ content:[オブジェクト] }.},
  { fuzzy: { title: [Object] }.}
]
</code></pre>
<p>クエリが1つの用語の場合</p>
<pre><code>[
  { match:{ title_explicit:[オブジェクト] }。},
  { match:{ headings_explicit:[オブジェクト] }。},
  { match:{ content_explicit:[オブジェクト] }。},
  { match:{ title: [オブジェクト] }.},
  { match:{ headings:[オブジェクト] }。},
  { match:{ content:[オブジェクト] }.},
  { fuzzy: { title: [Object] }.}
]
</code></pre>
<p>確かに、一握りのクエリに見えることもありますが、Elasticsearchは高速です。全体の時間のほとんどは、クエリを送信して結果を受信するためのネットワーク時間です。実際、私たちのElasticsearchサーバーでは、検索クエリ全体の実行にかかる時間（ネットワークを除く）は20ミリ秒と非常に安定して推移しています。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/31d270ffe9d659a3c0c97ec81da17bd3.png?w=1024&#038;resize=1024%2C554" alt="" width="1024" height="554" class="aligncenter size-large wp-image-70603 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/31d270ffe9d659a3c0c97ec81da17bd3.png?w=1200 1200w, https://github.blog/wp-content/uploads/2023/03/31d270ffe9d659a3c0c97ec81da17bd3.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/31d270ffe9d659a3c0c97ec81da17bd3.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/31d270ffe9d659a3c0c97ec81da17bd3.png?w=1024&#038;resize=1024%2C554 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<p><a href="https://docs.github.com">docs.github.com</a>の全検索の約55%は多項目クエリで、例えば<code>アクションの残り</code>です。つまり、約半数のケースで、クエリ全体のうち<code>match_phrase</code>の部分などを省略することができるので、簡略化したクエリを使うことができるのです。</p>
<p>検索の様々な組み合わせに入る前に、「明示的」の意味について後で説明する部分がある。基本的に、各フィールドは2回インデックスされます。例：<code>titleと</code> <code>title_explicit</code>。同じ内容でもトークン化が異なるため、クエリとのマッチングに影響を及ぼし、その違いを利用してブースティングを変えています。</p>
<p>マトリックスを構成するノードは以下の通りです。</p>
<h3 id="fields">Fields（フィールド<a href="#fields" class="heading-link pl-2 text-italic text-bold" aria-label="Fields:"></a></h3>
<ul>
<li><code>title</code>(<code>&lt;h1&gt;</code>テキスト)</li>
<li><code>みだし</code></li>
<li><code>コンテント</code></li>
</ul>
<h3 id="analyzer">アナライザー<a href="#analyzer" class="heading-link pl-2 text-italic text-bold" aria-label="Analyzer:"></a></h3>
<ul>
<li>explicit (ステミングなし、同義語なし)</li>
<li>regular (Snowballの完全なステミングと、おそらく同義語)</li>
</ul>
<h3 id="matches-on-multi-term-queries">Matches：（多項目クエリについて）<a href="#matches-on-multi-term-queries" class="heading-link pl-2 text-italic text-bold" aria-label="Matches: (on multi-term queries)"></a></h3>
<ul>
<li><code>マッチフレーズ</code></li>
<li><code>ORで</code><code>一致する</code>（"foo" OR "bar "を含むdocs）</li>
<li><code>ANDで</code><code>一致する</code>（「foo」と「bar」を含むドキュメント）</li>
</ul>
<p>これらの組み合わせにはそれぞれ固有のブースト番号があり、マッチした結果のランキングを押し上げる。実際の数値はあまり重要ではありませんが、重要なのはブースト数値が互いに<em>異なるという</em>ことです。例えば、<code>タイトルでの</code>マッチは、<code>コンテンツでの</code>マッチよりもブーストが少し高くなります。また、すべての単語が存在するマッチは、一部の単語だけがマッチする場合よりも、ブーストがわずかに高くなります。別の例として、検索ワードが<code>docker actionの</code>場合、ユーザーは "<em>Docker</em>イメージの公開 "や "GitHub<em>Actionsの</em>メタデータ構文 "よりも "<em>Docker</em>コンテナ<em>アクションの</em>作成 "を見たいはずです。</p>
<p>上記の各ノードには、次のようなブースト計算があります。</p>
<pre><code>const BOOST_PHRASE = 10.0
const BOOST_TITLE = 4.0
const BOOST_HEADINGS = 3.0
コンスタントBOOST_CONTENT = 1.0
const BOOST_AND = 2.5
const BOOST_EXPLICIT = 3.5

...
match_phrase: { title_explicit:{ boost:BOOST_EXPLICIT * BOOST_PHRASE * BOOST_TITLE, クエリ }.},
をマッチさせます。{ headings:{ boost:BOOST_HEADINGS * BOOST_AND, query, operator: 'AND' }.},
...
</code></pre>
<p>行列の各ノードについて、<code>ブースト</code>値がどうなるかを排他的にプリントすると、次のようになります。</p>
<pre><code>[
  { match_phrase: { title_explicit: 140 }.},
  { match_phrase: { title: 40 }.},
  { match_phrase: { headings_explicit: 105 }.},
  { match_phrase: { headings:30 }},
  { match_phrase: { content:10 }},
  { match_phrase: { content_explicit:35 }},
  { match:{ title_explicit:35, 演算子: 'AND' }.},
  { match:{ headings_explicit: 26.25, operator: 'AND' }.},
  { match:{ content_explicit: 8.75, operator: 'AND' }.},
  { match:{ title: 10, operator: 'AND' }.},
  { match:{ headings:7.5, operator: 'AND' }.},
  { match:{ content:2.5, operator: 'AND' }.},
  { match:{ title_explicit: 14 }.},
  { match:{ headings_explicit: 10.5 }.},
  { match:{ content_explicit:3.5 }},
  { match:{ title: 4 }.},
  { match:{ headings:3 }},
  { match:{ content:1 }},
  { fuzzy: { title: 0.1 }.}
]
</code></pre>
<p>それがElasticsearchに送られるわけです。複雑なウィッシュリストのようなもので、「クリスマスに自転車が欲しい。でも、ピンクの自転車があったらもっといい。ピンクにブルーのストライプがあればなお良し。本当は、青いストライプと真鍮のベルが付いたピンクの自転車が一番いいのですが......」。</p>
<p>ユーザーにとって理想的な実装と検索結果という意味で重要なのは、人間と文脈のインテリジェンスを用いてこれらのパラメーターを定義することです。その中には、かなり明白なものもあれば、もっと微妙なものもあります。たとえば、ステミングを必要としない<code>タイトルの</code>フレーズマッチは、可能な限り最高のマッチングであると考え、最高のブーストを得ることができます。</p>
<h2 id="why-explicit-boost-is-important">明示的なブーストが重要な理由<a href="#why-explicit-boost-is-important" class="heading-link pl-2 text-italic text-bold" aria-label="Why explicit boost is important"></a></h2>
<p>誰かが「creating repositories」と入力すると、「Create a private GitHub repository」のようなタイトルに間違いなく<em>マッチ</em>するはずです。これは、<code>creating =&gt; creat &lt;= create</code>と<code>repositories =&gt; repository &lt;= repository</code> というステムがあるからです。ステミングを考慮したマッチングをぜひ含めるべきでしょう。しかし、「Creating private GitHub repositories」のように、ユーザーが入力した単語と一致する単語を明示的に使用している記事があれば、その記事のランキングを上げたい。それは、その記事が検索者にもっと関連していると考えられるからです。</p>
<p>また、特殊なキーワードである<code>working-directoryは</code>、<a href="https://docs.github.com/actions/creating-actions/metadata-syntax-for-github-actions#runsstepsworking-directory">コンテンツ内に出現する可能性のある</a>正確な用語です。誰かが<code>working-directoryを</code>検索した場合、<code>working-directoryと</code>Directories that workが同じ2つのステム<code>（「work」「directori」</code>）に分解されるのに、「Directories that work」のようなタイトル（例）ではランキングを圧倒できないようにしたいです。</p>
<p>私たちが頼りにしている解決策は、2つのマッチングを行うことです。1つはステミングあり、もう1つはステミングなしです。それぞれ異なるブーストがあります。これは、「『Peter』を探しているが、『Petter』や『Pierre』、『Piotr』もあれば、それもいい。でも、理想を言えば、まず第一に『ピーター』です。実際には、すべての結果を表示させるのではなく、『Peter』を最初に表示させるのです」。ステミングは素晴らしいですが、検索結果を「圧倒」してしまう可能性があります。これは、英語の散文に見えるような特定のキーワードに役立ちます。例えば、「working-directory」は通常の英語表現に見えますが、実はハードコードされた特定のキーワードなのです。</p>
<p>コードにすると、次のようになります。</p>
<pre><code class="language-js">// インデックスを作成する...
await client.indices.create({)
  をマッピングします。{
    プロパティを使用します。{
      url:{ type: 'keyword' },
      のタイトルが表示されます。{ type: 'text', analyzer: 'text_analyzer', norms: false },
      title_explicit:{ type: 'text', analyzer: 'text_analyzer_explicit', norms: false },
      のコンテンツになります。{type: 'text', analyzer: 'text_analyzer' },
      content_explicit:{ type: 'text', analyzer: 'text_analyzer_explicit' },
      // ...スニップ...
      },
    },
    // ...スニップ...
  })
// 検索中...
matchQueries.push(
  ...[
    { match:{ title_explicit:{ boost:BOOST_EXPLICIT * BOOST_TITLE, クエリ }.}},
    { match:{ content_explicit:{ boost:BOOST_EXPLICIT * BOOST_CONTENT, クエリ }.}},
    { match:{ title:{ boost:BOOST_TITLE, クエリ }.}},
    { match:{ content:{ boost:BOOST_CONTENT, クエリ }.}},
    // ...スニップ...
])
</code></pre>
<h2 id="ranking-is-not-that-easy">ランキングはそんなに簡単ではありません<a href="#ranking-is-not-that-easy" class="heading-link pl-2 text-italic text-bold" aria-label="Ranking is not that easy"></a></h2>
<p>検索は、急速にアートになってきています。ただ用語を照合して、入力された用語に一致する文書のリストを表示するだけでは不十分です。まず、ランキングは決定的に重要である。特に、ある検索語から数十、数百の一致する文書が得られる場合には、その傾向が顕著です。Googleに長年依存してきた私たちは、最初の検索結果が自分の望むものであることを期待するようになりました。</p>
<p>これを素晴らしい体験にするために、私たちは、どのページが最も人気があるかを判断する方法として<strong>ページビューメトリクスを</strong>使用することで、ユーザーが純粋に探しているドキュメントを推測するようにしています。もちろん、一番人気のあるものを最初に提供してクリックされれば、さらに人気が出るだけですが、これはスタートラインです。私たちは、ユーザーが何かをググることで多くのページビューを獲得しています。しかし、ユーザーが自分にとって最適な情報を持っていると判断したページに移動することで、定期的にページビューの指標を得ることもできます。</p>
<p>現時点では、最も人気のある上位1,000のURLのページビューメトリクスを収集しています。そして、それらをランク付けし、0.0から1.0の間（を含む）の数値に正規化します。その数値が何であれ、私たちは+1.0を加え、Elasticsearchでこの数値にマッチスコアを掛け合わせます。</p>
<p>ある検索クエリで一致する2つのドキュメントが見つかり、そのマッチスコアが前述の検索実装に基づき15.6と13.2であったとします。ここで、13.2のマッチが人気のあるページにあったとすると、その人気度は0.75かもしれないので、13.2 * (1 + 0.75) = 23.1 となる。そして、もう一つの少し良くマッチしたものは、人気度が0.44なので、最終的な数字は15.6 * (1 + 0.44) = 22.5となり、少なくなっています。結論から言うと、用語と用語が一致しないような文書にも、上位に食い込むチャンスを与えることができるのです。また、内容的に曖昧にしかマッチしていない大人気の文書が、タイトルでマッチしていたかもしれない他のマッチを「圧倒」することがないようにすることができます。</p>
<p>難しい課題ですが、だからこそ楽しいのです。ユーザーと同じように考えるという意味で、コードに人間味を持たせる必要があるのです。というのも、より多くの優れた指標を用いても、ユーザーの状況や出身地は常に変化しているため、アルゴリズムが完璧になることはありません。しかし、私たちはそれについていけるように努力します。</p>
<h2 id="whats-next">次はどうする？<a href="#whats-next" class="heading-link pl-2 text-italic text-bold" aria-label="What&#8217;s next?"></a></h2>
<p>Elasticsearch には、同義語と呼ばれる単語の別名を定義できる機能があります。(例えば、repo = リポジトリ。) この機能の課題は、ライターがどのように便利で保守的な方法で管理・維持するかということです。</p>
<p>現在GitHubでは、ページビューメトリクスによって人気度を算出しています。ユーザーがどのページにたどり着いたかをもっと深く掘り下げると面白いかもしれません。例えば、読者が必要なものをどうやって探せばいいのかわからず、製品のランディングページ（私たちには約20のページがあります）から始めて、徐々にコンテンツの奥へと進み、最終的に欲しい知識や答えを提供するページにたどり着いたとしましょう。このプロセスは、各ページに等しい尺度を与えることになり、それは素晴らしいことではありません。</p>
<p>もう一つのエキサイティングなアイデアは、検索結果のURLがクリックさ<em>れなかった</em>時、特にランキングで上位に表示された時に、そのURLをすべて記録することです。そうすれば、人気のあるリスティングがさらに人気を集めるだけのリスクを減らすことができる。また、人間による「修正」を記録すれば、非常に強力なシグナルになり得ます。</p>
<p>また、他の文脈上の変数に基づいて、基礎となる検索を調整することも可能です。例えば、ユーザーが現在<a href="https://docs.github.com/rest">REST APIのドキュメントに</a>いる場合、「課金」のような曖昧なものを検索するときは、REST API関連のドキュメントが少し好まれると推測できます（例えば、<a href="https://docs.github.com/en/billing/managing-your-github-billing-settings/setting-your-billing-email">Billing and payments "Setting your billing email."</a> ではなく<a href="https://docs.github.com/en/rest/billing">REST API "About billing"</a>を好む<a href="https://docs.github.com/en/billing/managing-your-github-billing-settings/setting-your-billing-email">）</a>。</p>
<p>次に何をお探しですか？最近、<a href="https://docs.github.com/">https://docs.github.com</a>の検索を試してみて、最適な検索結果を得られなかったと感じたことはありませんか？<a href="https://github.com/github/docs/issues/new/choose">ぜひお知らせいただき、</a>ご連絡ください。</p>


