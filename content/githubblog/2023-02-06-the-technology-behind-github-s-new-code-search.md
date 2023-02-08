---
title: "GitHubの新しいコード検索を支える技術"
subtitle: "世界最大の公開コード検索インデックスを構築するために何が行われたかをご紹介します。"
englishsubtitle: "A look at what went into building the world's largest public code search index."
englishtitle: "The technology behind GitHub’s new code search"
date: "2023-02-06"
cardurl: "https://github.blog/2023-02-06-the-technology-behind-githubs-new-code-search/"
author: "Timothy Clem"
description: " From launching our technology preview of the new and improved code search experience a year ago, to the public beta we released at GitHub Universe last November, there’s been a flurry of innovation and dramatic changes to some of the core GitHub product experiences around how we, as developers, find, read, and navigate code.  One question we hear about the new code search experience is, “How does it work?” And to complement a talk I gave at GitHub Universe , this post gives a high-level answer to that question and provides a small window into the system architecture and technical underpinnings of the product.  So, how does it work? The short answer is that we built our own search engine from scratch, in Rust, specifically for the domain of code search. We call this search engine Blackbird, but before I explain how it works, I think it helps to understand our motivation a little bit. At first glance, building a search engine from scratch seems like a questionable decision. Why would you do that? Aren’t there plenty of existing, open source solutions out there already? Why build something new?  To be fair, we’ve tried and have been trying, for almost the entire history of GitHub, to use existing solutions for this problem. You can read a bit more about our journey in Pavel Avgustinov’s post, A brief history of code search at GitHub , but one thing sticks out: we haven’t had a lo"
coverimage: "https://github.blog/wp-content/uploads/2023/02/code-search-header.png?resize=1600%2C736"
category: "Engineering,code search,Core productivity"
englishsummary: "  GitHub has built its own search engine from scratch, in Rust, to answer the question of "How does code search work?", and this post provides an overview of the system architecture and technical underpinnings of the product."
summary: "GitHubは、「コード検索はどのように機能するのか」という疑問に答えるために、Rustでゼロから独自の検索エンジンを構築しました。この記事では、この製品のシステムアーキテクチャと技術的基盤の概要について説明します。"
---

<p>1年前に新しいコード検索エクスペリエンスの<a href="https://github.blog/2021-12-08-improving-github-code-search/">テクノロジープレビューを</a>発表してから、昨年11月のGitHub Universeで<a href="https://github.blog/2022-11-15-a-better-way-to-search-navigate-and-understand-code-on-github/">パブリックベータ</a>版をリリースするまで、私たち開発者がコードを見つけ、読み、ナビゲートする方法に関する革新とGitHub製品のコア体験への劇的変化が相次いでいます。</p>
<p>新しいコード検索エクスペリエンスについてよく聞かれる質問のひとつに、"どのように動作するのか "というものがあります。この記事では、<a href="https://www.youtube.com/watch?v=QCs76SC1ZZ0">GitHub Universeで</a>行った講演を補足する形で、この質問に対するハイレベルな答えと、この製品のシステムアーキテクチャや技術的基盤についての小さな窓を提供するものです。</p>
<p>では、どのように動作<em>する</em>のでしょうか？簡単に言うと、私たちはコード検索に特化した独自の検索エンジンをRustで一から作り上げました。この検索エンジンをBlackbirdと呼んでいますが、その仕組みを説明する前に、私たちのモチベーションをお伝えします。一見すると、ゼロから検索エンジンを作るというのは疑問のある決断のように思えます。なぜそんなことをするのでしょうか？既存のオープンソースのソリューションはすでにたくさんあります。ではなぜ、新しいものを作るのでしょうか？</p>
<p>公平を期すために、私たちはGitHubの歴史のほとんどすべてにおいて、この問題に対して既存のソリューションを利用することをまず検討し、またそうしてきました。私たちの道のりについては Pavel Avgustinov の投稿「<a href="https://github.blog/2021-12-15-a-brief-history-of-code-search-at-github/">A brief history of code search at GitHub</a>」の中で紹介されています。この中で印象に残っていることは、<strong><em>コード</em></strong>一般的なテキスト検索製品をコード検索のために使うのは、あまり良いことではないということです。ユーザーエクスペリエンスが悪く、インデックス作成に時間がかかり、ホスティングにコストがかかるからです。コードに特化した新しいオープンソースプロジェクトもありますが、GitHubの規模では間違いなく機能しません。このような状況を知っていた私たちは、以下の3つの点に着目し、独自のソリューションを作ることにしました。</p>
<ol>
<li>コードに質問をし、検索、ブラウズ、ナビゲート、読み込みを繰り返しながら答えを得ることができる、全く新しいユーザーエクスペリエンスのビジョン</li>
<li>私たちは<strong><em>コード</em></strong>検索が、一般的なテキスト検索とは明らかに異なるものであると理解しています。コードはすでに機械が理解できるように設計されており、その構造と関連性を利用することができるはずです。コードの検索には、句読点（ピリオドや開カッコなど）を検索したい、ステミングをしたくない、クエリーからストップワードを削除したくない、正規表現で検索したい、などの独自の要件もあります。</li>
<li>GitHubのサービス規模に対しての開発は非常にユニークであり、挑戦でもあります。Elasticsearchを初めて導入した時、GitHub上の全てのコード（当時は約800万リポジトリ）のインデックスを作成するのに数ヶ月かかりました。現在ではその数は2億を超え、しかもそのコードは静的なものではなく、常に変化しており、検索エンジンが扱うにはかなり困難なものです。ベータ版では、現在約4500万のリポジトリを検索することができ、これは115TBのコードと155億のドキュメントに相当します。 </li>
</ol>
<p>結局、既成のものでは我々のニーズを満たせなかったので、ゼロから何かを作り上げたのです。</p>
<h2 id="just-use-grep">grepを使うだけでいいのか？<a href="#just-use-grep" class="heading-link pl-2 text-italic text-bold" aria-label="Just use grep?"></a></h2>
<p>まず、この問題に対するブルートフォース・アプローチについて説明します。よくこんな質問を受けます。"なぜgrepを使わないのですか？"その答えとして、115TBのコンテンツに対して<a href="https://github.com/BurntSushi/ripgrep">ripgrepを</a>使った計算を少ししてみましょう。8コアのIntel CPUを持つマシンで、ripgrepはメモリにキャッシュされた13GBのファイルに対して、<a href="https://github.com/BurntSushi/ripgrep#quick-examples-comparing-tools">網羅的な正規表現クエリを</a>2.769秒、つまり約0.6GB/秒/コアで実行することができます。</p>
<p>これでは、大量のデータを処理することができないことがすぐにわかります。コード検索は64コア、32マシンのクラスターで実行されます。仮に115TBのコードをメモリに格納し、完璧に並列化できたとしても、1つのクエリを実行するために2,048個のCPUコアを96秒間飽和させることになります！そうすると1つのクエリしか実行できません。他のクエリーは順番に実行しなければなりません。これは、1 秒あたりのクエリ数 (QPS) が 0.01 という驚異的な数字であり、うまくいけば QPS が 2 倍になります。これでは、インフラストラクチャの請求について経営陣との楽しい会話をすることになるでしょう。</p>
<p>このアプローチをGitHubの全コードと全ユーザーに適用するには、費用対効果の高い方法はありません。この問題に大量の資金を投入したとしても、ユーザー体験の目標を達成することはできないでしょう。</p>
<p>つまり、インデックスを作成する必要があるのです。</p>
<h2 id="a-search-index-primer">検索インデックス入門<a href="#a-search-index-primer" class="heading-link pl-2 text-italic text-bold" aria-label="A search index primer"></a></h2>
<p>インデックスとは、キーと、そのキーが出現する文書IDのソートされたリスト（「投稿リスト」と呼ばれる）の対応表と考えることができます。例えば、プログラミング言語に関する小さなインデックスがあります。各文書をスキャンしてどのプログラミング言語で書かれているかを検出し、文書IDを割り当てて、言語をキー、文書IDの投稿リストを値とする転置インデックスを作成します。</p>
<h3 id="forward-index">転置インデックス<a href="#forward-index" class="heading-link pl-2 text-italic text-bold" aria-label="Forward index"></a></h3>
<div class="content-table-wrap"><table>
<tr>
<td><strong>文書ID</strong>
   </td>
<td><strong>内容</strong>
   </td>
</tr>
<tr>
<td>1
   </td>
<td>デフ・リム<br />
    puts "mit"<br />
    エンド
   </td>
</tr>
<tr>
<td>2
   </td>
<td>fn limits() {
   </td>
</tr>
<tr>
<td>3
   </td>
<td>function mits() {
   </td>
</tr>
</table></div>
<h3 id="inverted-index">転置インデックス<a href="#inverted-index" class="heading-link pl-2 text-italic text-bold" aria-label="Inverted index"></a></h3>
<div class="content-table-wrap"><table>
<tr>
<td><strong>言語</strong>
   </td>
<td><strong>Doc ID (投稿)</strong>
   </td>
</tr>
<tr>
<td>JavaScript
   </td>
<td>3, 8, 12, ...
   </td>
</tr>
<tr>
<td>ルビー
   </td>
<td>1, 10, 13, ...
   </td>
</tr>
<tr>
<td>ラスト
   </td>
<td>2, 5, 11, ...
   </td>
</tr>
</table></div>
<p>コード検索には、コンテンツの部分文字列を検索するのに便利な、ngram インデックスと呼ばれる特殊な転置インデックスが必要です。例えば、<a href="https://en.wikipedia.org/wiki/N-gram">n</a>=3 (trigrams)とすると、コンテンツ「limit」を構成するngramは<code>lim</code>,<code>imi</code>,<code>mit</code>,<code>itsと</code>なる。上の文書で、これらのtrigramのインデックスは次のようになります。</p>
<div class="content-table-wrap"><table>
<tr>
<td><strong>ngram</strong>
   </td>
<td><strong>ドキュメントID (投稿)</strong>
   </td>
</tr>
<tr>
<td>lim
   </td>
<td>1, 2, ...
   </td>
</tr>
<tr>
<td>imi
   </td>
<td>2, ...
   </td>
</tr>
<tr>
<td>ミット
   </td>
<td>1, 2, 3, ...
   </td>
</tr>
<tr>
<td>その
   </td>
<td>2, 3, ...
   </td>
</tr>
</table></div>
<p>検索を行うには、複数の検索結果を交差させて、その文字列が出現する文書のリストを得ます。トリグラムインデックスの場合、<code>lim</code>、<code>imi</code>、<code>mit</code>、<code>itsの</code>4つの検索が必要です。</p>
<p>しかし、ハッシュマップとは異なり、これらのインデックスは大きすぎてメモリに収まらないので、代わりにアクセスする必要のあるインデックスごとにイテレータを構築します。これらはソートされたドキュメントID（IDは各ドキュメントのランキングに基づいて割り当てられる）を遅延的に返し、イテレータを（特定のクエリの要求に応じて）交差させたり結合したりして、要求された数の結果を取得するのに十分な距離だけ読み取ります。こうすることで、投稿リスト全体をメモリ上に保持する必要がなくなるのです。</p>
<h2 id="indexing-45-million-repositories">4,500万件のリポジトリへのインデックス付け<a href="#indexing-45-million-repositories" class="heading-link pl-2 text-italic text-bold" aria-label="Indexing 45 million repositories"></a></h2>
<p>次の問題は、このインデックスを合理的な時間で構築する方法です（最初の反復作業では数ヶ月かかったことを思い出してください）。よくあることですが、ここでのコツは、作業している特定のデータについて何らかの洞察を得て、アプローチの指針とすることです。私たちの場合、それは2つのことです。Gitが<a href="https://en.wikipedia.org/wiki/K-way_merge_algorithm">Content Addressable Hashingを</a>使用していることと、GitHubに非常に多くの重複コンテンツが存在することです。この二つの洞察から、私たちは次のような決定を下しました。</p>
<ol>
<li><strong>シャードはGit BlobオブジェクトIDで</strong>管理し、重複を避けつつシャード間でドキュメントを均等に分配します。特別なリポジトリが原因でサーバーが熱くなることもありませんし、必要に応じてシャードの数を簡単に拡張することができます。</li>
<li><strong>インデックスをツリーとしてモデル</strong>化し、デルタエンコーディングを使用してクロールの量を減らし、インデックスのメタデータを最適化します。私たちにとってメタデータとは、文書が出現する場所のリスト（どのパス、ブランチ、リポジトリか）や、それらのオブジェクトに関する情報（リポジトリ名、所有者、可視性など）のようなものです。このデータは、人気のあるコンテンツではかなり大きくなることがあります。</li>
</ol>
<p>また、クエリの結果がコミットレベルで一貫しているように設計されています。チームメイトがコードをプッシュしている間にリポジトリを検索した場合、システムで完全に処理されるまで、新しいコミットからのドキュメントが結果に含まれないはずです。実際、あなたがリポジトリを対象としたクエリから結果を得ている間、他の誰かがグローバルな結果をページングして、別の、より前の、しかし依然として一貫した <strong><em>一貫性のある</em></strong>の状態を見ることができます。これは、他の検索エンジンでは難しいことです。Blackbirdはこのレベルのクエリの一貫性を設計の中核部分として提供しています。</p>
<h2 id="lets-build-an-index">インデックスを構築しよう<a href="#lets-build-an-index" class="heading-link pl-2 text-italic text-bold" aria-label="Let’s build an index"></a></h2>
<p>これらの洞察を得た上で、Blackbirdでインデックスを構築することに目を向けてみましょう。この図は、システムのインジェストとインデックス作成側のハイレベルな概観を表しています。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/Canvas_1-1.png?w=1024&#038;resize=1024%2C692" alt="a high level overview of the ingest and indexing side of the system" width="1024" height="692" class="aligncenter size-large wp-image-69988 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/Canvas_1-1.png?w=1376 1376w, https://github.blog/wp-content/uploads/2023/02/Canvas_1-1.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/Canvas_1-1.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/Canvas_1-1.png?w=1024&#038;resize=1024%2C692 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<p>Kafkaは私たちにインデックスを作成するように指示するイベントを提供します。Gitやコードからシンボルを抽出するサービスとやり取りするクローラーがたくさんあり、それからKafkaを使って、各シャードが自分のペースでインデックスのためのドキュメントを消費できるようにしています。</p>
<p>システムは通常、<code>git pushの</code>ようなイベントに反応して変更されたコンテンツをクロールするだけですが、初めてすべてのリポジトリを取り込むために、いくつかの作業を行いました。このシステムの重要な特性の一つは、デルタエンコーディングを最大限に活用するために、この最初のインジェストを行う順番を最適化することです。これは、リポジトリの類似性を表す新しい確率的データ構造と、リポジトリの類似性を表すグラフの<a href="https://en.wikipedia.org/wiki/Minimum_spanning_tree">最小スパニングツリーの</a>レベルオーダーのトラバーサルからインジェスト順序を駆動することによって実現されています。<sup id="fnref-69904-1"><a href="#fn-69904-1" class="jetpack-footnote" title="Read footnote.">1</a></sup>.</p>
<p>最適化された取り込み順序を使用して、各リポジトリは、構築したデルタツリー内の親に対して差分を取ることでクロールされます。つまり、（リポジトリ全体ではなく）そのリポジトリに固有のBlobのみをクロールする必要があります。クロールでは、GitからBlobの内容を取得し、それを解析してシンボルを抽出し、インデックス作成のための入力となるドキュメントを作成します。</p>
<p>これらのドキュメントは、別のKafkaトピックにパブリッシュされます。ここでパーティション<sup id="fnref-69904-2"><a href="#fn-69904-2" class="jetpack-footnote" title="Read footnote.">2</a></sup>のデータをシャード間で分割します。各シャードは、トピック内の1つのKafkaパーティションを消費します。インデックス作成は、Kafkaを使用することでクロールから切り離され、Kafka内のメッセージの順序がクエリの一貫性を得る方法となります。</p>
<p>インデックス作成用シャードは、これらのドキュメントを受け取り、インデックスを作成します：トークン化により、ngramインデックスを作成します。<sup id="fnref-69904-bignote"><a href="#fn-69904-bignote" class="jetpack-footnote" title="Read footnote.">3</a></sup>(トークン化し、ngramインデックス3（コンテンツ、シンボル、パス）やその他の有用なインデックス（言語、所有者、リポジトリなど）を構築し、十分な作業が蓄積されたらシリアライズしてディスクにフラッシングします。</p>
<p>最後に、シャードはコンパクションを実行し、小さなインデックスをクエリの効率がよく、移動しやすい大きなインデックスにまとめます（たとえば、読み込みレプリカやバックアップのためなど）。コンパクションはまた、投稿リストをスコアで<a href="https://en.wikipedia.org/wiki/Content-addressable_storage">kマージ</a>し、関連文書がより低いIDを持ち、遅延イテレータによって最初に返されるようにします。最初のインジェストではコンパクションを遅らせ、最後に大きなコンパクションを実行します。しかし、インデックスが逐次変更されるにつれて、より短い間隔でコンパクションを実行し、ドキュメントの削除などを処理します。</p>
<h2 id="life-of-a-query">クエリの寿命<a href="#life-of-a-query" class="heading-link pl-2 text-italic text-bold" aria-label="Life of a query"></a></h2>
<p>インデックスができたので、システムを通してクエリを追跡してみるのも面白いでしょう。これから追うクエリは、<a href="https://github.com/rails">Ruby</a>プログラミング言語で書かれたコードを探している<a href="https://github.com/rails">Rails</a>組織に適格な正規表現です。<code>/arguments?/ org:rails lang:Ruby</code>。クエリパスの高レベルなアーキテクチャは、次のようなものです。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/code-search.png?w=1024&#038;resize=1024%2C508" alt="Architecture diagram of a query path." width="1024" height="508" class="aligncenter size-large wp-image-69989 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/code-search.png?w=1376 1376w, https://github.blog/wp-content/uploads/2023/02/code-search.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/code-search.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/code-search.png?w=1024&#038;resize=1024%2C508 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<p>GitHub.com とシャードの間には、ユーザーのクエリを受け取り、検索クラスタの各ホストにリクエストを分散させるサービスを配置しています。Redis を使ってクォータを管理し、アクセス制御データをキャッシュしています。</p>
<p>フロントエンドはユーザーのクエリを受け取り、それをBlackbirdクエリサービスに渡します。クエリは抽象的な構文ツリーに解析され、言語などを正規の<a href="https://github.com/github/linguist">Linguist</a>言語IDに解決し、パーミッションやスコープのための追加の句をタグ付けして、書き直されます。この場合、パブリック・リポジトリや、私がアクセスできるプライベート・リポジトリからの結果が、どのように書き換えられるかがわかると思います。</p>
<pre><code>
And(
    Owner("rails"),
    LanguageID(326),
    Regex("arguments?"),
    Or(
        RepoIDs(...),
        PublicRepo(),
    ),
)
</code></pre>
<p>次に、検索クラスタの各シャードに1つずつ、ファンアウトして<em>n個の</em>同時リクエストを送信します。シャーディング戦略のため、クエリーリクエストはクラスタ内の各シャードに送信されなければなりません。</p>
<p>各シャードでは、インデックスの情報を検索するために、さらにクエリの変換を行います。ここでは、正規表現がngramインデックスに対する一連の部分文字列クエリに変換されていることがわかります。</p>
<pre><code>
and(
  owners_iter("rails"),
  languages_iter(326),
  or(
    and(
      content_grams_iter("arg"),
      content_grams_iter("rgu"),
      content_grams_iter("gum"),
      or(
        and(
         content_grams_iter("ume"),
         content_grams_iter("ment")
        )
        content_grams_iter("uments"),
      )
    ),
    or(paths_grams_iter…)
    or(symbols_grams_iter…)
  ), 
  …
)
</code></pre>
<p>正規表現を部分文字列クエリにする方法についてもっと知りたい場合は、Russ Coxの記事「<a href="https://swtch.com/~rsc/regexp/regexp4.html">Regular Expression Matching with a Trigram Index</a>」を参照してください。私たちは異なるアルゴリズムと、trigramの代わりに動的なグラムサイズを使っています(<sup id="fnref2:69904-bignote"><a href="#fn-69904-bignote" class="jetpack-footnote" title="Read footnote.">3</a></sup>).この場合、エンジンは次のグラムを使います：<code>arg</code><code>, rgu</code>,<code>gum</code>、そして<code>umeと</code> <code>ment</code>、または6グラムの<code>umentsの</code>いずれかです。</p>
<p>各節のイテレータは、<em>andは</em>交差を意味し、<em>unionは</em>結合を意味します。その結果、文書のリストが得られます。各文書をダブルチェックし（マッチの検証や範囲の検出）、スコアリング、ソート、そして要求された数の結果を返さなければならなりません。</p>
<p>クエリサービスに戻ると、すべてのシャードの結果を集約し、スコアで再ソートし、フィルタリングして (パーミッションを再確認して) 上位 100 件を返します。GitHub.com のフロントエンドでは、構文強調や用語強調、ページ送りを行い、最後に結果をページにレンダリングします。</p>
<p>個々のシャードからのp99のレスポンスタイムは100ミリ秒程度ですが、レスポンスの集約やパーミッションのチェック、シンタックスハイライトなどのため、全体のレスポンスタイムはもう少し長くなっています。クエリはインデックスサーバーの1CPUコアを100ミリ秒拘束するので、64コアのホストでは1秒あたり640クエリ程度が上限となります。grepのアプローチ（0.01QPS）と比較すると、これは非常に高速で、同時ユーザクエリや将来の拡張にも十分対応できるものです。</p>
<h2 id="in-summary">まとめ<a href="#in-summary" class="heading-link pl-2 text-italic text-bold" aria-label="In summary"></a></h2>
<p>システム全体を見たところで、問題の規模を再確認してみましょう。我々のインジェストパイプラインは、1秒間に約12万文書を公開できるので、155億文書を処理するのに約36時間かかるはずです。しかし、デルタインデックスにより、クロールしなければならない文書数が50%以上削減され、コーパス全体のインデックスを約18時間で再作成することができます。</p>
<p>インデックスのサイズに関しても、大きな成果があります。私たちは115TBの検索対象コンテンツからスタートしたことを思い出してください。コンテンツの重複排除とデルタインデックスにより、<strong>ユニークな</strong>コンテンツは約28TBに減少しました。インデックス自体は25TBで、これにはすべてのインデックス（ngramを含む）だけでなく、すべてのユニークコンテンツの圧縮コピーも含まれています。つまり、コンテンツを含むインデックスの総容量は、元データのおよそ4分の1ということになります。</p>
<p>まだサインアップしていない方は、ぜひ<a href="https://github.com/features/code-search">ベータ</a>版に参加して、新しいコード検索体験を試してみてください。ご感想をお聞かせください。私たちは積極的にリポジトリを追加し、あなたのような人々からのフィードバックに基づいて、ラフエッジを修正します。</p>

<h3 id="notes">ノート<a href="#notes" class="heading-link pl-2 text-italic text-bold" aria-label="Notes"></a></h3>
<div class="footnotes">
<hr />
<ol>
<li id="fn-69904-1">
最適な取り込み順序を決定するために、あるリポジトリが他のリポジトリとどれくらい似ているか（コンテンツの点で似ているか）を知る方法が必要です。そこで、<a href="https://en.wikipedia.org/wiki/MinHash">MinHash</a>や<a href="https://en.wikipedia.org/wiki/HyperLogLog">HyperLogLog</a> と同じクラスのデータ構造で、これを行うための新しい確率的データ構造を考案しました。このデータ構造を幾何学的フィルタと呼び、対数空間を持つ集合の類似性と集合間の対称的な差を計算することができます。この場合、比較するセットは、(path, blob_sha)タプルで表される各リポジトリのコンテンツです。この知識をもとに、頂点をリポジトリ、辺をこの類似度メトリックで重み付けしたグラフを作成します。このグラフの最小スパニングツリー（類似度をコストとする）を計算し、ツリーをレベルオーダーでトラバースすると、デルタエンコーディングを最大限に活用できるインジェストオーダーが得られます。しかし、このグラフは膨大な数（数百万のノード、数兆のエッジ）なので、MSTアルゴリズムは数分で計算できる近似値を計算し、私たちが目指しているデルタ圧縮の効果の90%を提供<a href="#fnref-69904-1" title="Return to main content.">します</a>。
</li>
<li id="fn-69904-2">
インデックスはGit Blob SHAでシャーディングされます。シャーディングとは、インデックスを作成したデータを複数のサーバーに分散させることです。これは、読み込み（QPSが重要）、ストレージ（ディスク容量が重要）、インデックス作成時間（各ホストのCPUとメモリに制約される）を簡単に水平方向に拡張するために必要なこと<a href="#fnref-69904-2" title="Return to main content.">です</a>。
</li>
<li id="fn-69904-bignote">
特に、我々が使用しているngramインデックスが興味深い。<a href="https://swtch.com/~rsc/regexp/regexp4.html">Russ Coxや他の</a>研究者が指摘するように、trigramは設計空間のスイートスポットとして知られていますが、私たちのスケールではいくつかの問題を引き起こします。</p>
<p> <code>トリグラムの</code>ような一般的な文法は、十分に選択的ではありません。誤検出が多すぎて、クエリーが遅くなります。誤検出の例としては、個々の三文型を含むが、隣り合っていない文書を見つけるようなことがあります。この場合、そのドキュメントのコンテンツを取得し、ダブルチェックするまでは分かりません。この問題を解決するために、私たちはフォローマスクを追加したり、トリグラムの次の文字にビットマスクを使用する（基本的に4分音符の半分）など、いくつかの戦略を試みましたが、すぐに飽和してしまい役に立ちません。</p>
<p>私たちはこの解決策を「スパースグラム」と呼んでおり、次のように動作します。ビッグラムを与えて重みを与える関数があるとします。  例として、<code>チェスターという</code>文字列を考えます。ch "は9、"he "は6、"es "は3、というように各ビグラムに重みを与えます。</p>
<a href="https://github.blog/2023-02-06-the-technology-behind-githubs-new-code-search/#gallery-69904-1-slideshow">クリックするとスライドショーが表示されます。</a>
<p>これらの重みを用いて、内側の重みが境界の重みよりも厳密に小さくなる区間を選んでトークン化します。その区間に含まれる文字がngramを構成し、このアルゴリズムをトリグラムで自然消滅するまで再帰的に適用します。クエリー時には、全く同じアルゴリズムを使用するが、他のものは<a href="#fnref-69904-bignote" title="Return to main content.">冗長</a>であるため、カバーするngramのみを保持する<a href="#fnref2:69904-bignote" title="Return to main content.">。</a>
</li>
</ol>
</div>


