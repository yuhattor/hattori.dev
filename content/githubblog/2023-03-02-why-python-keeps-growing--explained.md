---
title: "Pythonが成長し続ける理由、解説"
subtitle: "Pythonがこれまで以上に多くの人に使われるようになった理由、その主な使用例、そしてリリースから30年以上経った今でもこれほど人気がある理由を深く掘り下げて解説します。"
englishsubtitle: "A deep dive into why more people are using Python than ever, its key use cases, and why it’s still so popular 30-plus years after it was first released."
englishtitle: "Why Python keeps growing, explained"
date: "2023-03-02"
cardurl: "https://github.blog/2023-03-02-why-python-keeps-growing-explained/"
author: "Rizel Scarlett"
description: " Which programming language has been around for more than three decades and continues to grow in popularity each year?  If you guessed Python, you nailed it. In the 2022 Octoverse report , we found that Python remains the second most-used programming language on GitHub. Interestingly, Python’s use grew more than 22 percent year over year with more than four million developers on GitHub using it at some point in 2022.  In this article, we’ll dive into a brief history of Python, its benefits, its use cases, and seek to answer why a program language conceived in the 1980s continues to dominate development. And, since this is GitHub, we’ll also offer a few useful tips and tricks for developers new to—and experienced in—Python.  So, what is Python?  Python is a high-level, interpreted programming language with a simple syntax, which makes it easily readable and extremely user- and beginner-friendly. Originally built to satisfy Guido Van Rossum’s desire for a programming language that was simple to use and beautiful to look at, Python was first released to the world in 1991.  Fun Fact: Python was named after the BBC TV show , “Monty Python’s Flying Circus.”  Since its development, it has grown to have widespread applicability for developers, data scientists, researchers, and more. But how, you may ask, can a coding language be simple and beautiful to look at? Here’s some proof:  Pyth"
coverimage: "https://github.blog/wp-content/uploads/2023/02/python-growing.png?resize=1600%2C850"
category: "Engineering,Open Source,Octoverse,python"
englishsummary: "ons popularity has continued to grow for more than three decades, and is currently the second most-used programming language on GitHub."
summary: "onsの人気は30年以上続いており、現在GitHubで2番目に使用されているプログラミング言語です。"
---

<p>30年以上の歴史があり、年々人気が高まっているプログラミング言語はどれでしょう？</p>
<p>Pythonと答えた方は大正解でした。<a href="https://octoverse.github.com/2022/top-programming-languages">2022年のOctoverseレポートでは</a>、Pythonは依然としてGitHubで2番目に多く使われているプログラミング言語であることがわかりました。興味深いことに、Pythonの使用率は前年比で22%以上増加し、2022年のある時点でGitHub上の400万人以上の開発者がPythonを使用しています。</p>
<p>この記事では、Pythonの歴史、利点、ユースケースを簡単に説明し、1980年代に考案されたプログラム言語がなぜ開発を支配し続けるのか、その答えを探っていきます。また、ここはGitHubなので、Pythonを初めて使う開発者や経験豊富な開発者に役立つヒントやコツも紹介します。</p>
<h2 id="so-what-is-python-%f0%9f%a4%94">Pythonとは？<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f914.png" alt="🤔" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#so-what-is-python-%f0%9f%a4%94" class="heading-link pl-2 text-italic text-bold" aria-label="So, what is Python? &#x1f914;"></a></h2>
<p>Pythonは高水準のインタープリタ型プログラミング言語で、シンプルな構文で読みやすく、ユーザーや初心者に非常に優しい言語です。Pythonは元々、<a href="https://docs.python.org/3/faq/general.html#why-was-python-created-in-the-first-place">Guido Van Rossumの</a>「使いやすく、見た目も美しい<a href="https://docs.python.org/3/faq/general.html#why-was-python-created-in-the-first-place">プログラミング言語</a>が欲しい」という要望を満たすために作られ、1991年に初めて世に送り出されました。</p>
<blockquote><p>
  Pythonは、<a href="https://docs.python.org/3/faq/general.html#why-is-it-called-python">BBCのテレビ番組</a>「Monty Python's Flying Circus」にちなんで名づけられました<strong>。</strong>
</p></blockquote>
<p>開発以来、開発者、データサイエンティスト、研究者などに広く適用されるまでに成長しました。しかし、どうしてコーディング言語がシンプルで見た目も美しいのか、疑問に思われるかもしれません。それを証明するのが、こちらです。</p>
<h3 id="python">Python<a href="#python" class="heading-link pl-2 text-italic text-bold" aria-label="Python"></a></h3>
<pre><code class="language-python">print("Hello world.")
</code></pre>
<p>vs.</p>
<h3 id="java">Java<a href="#java" class="heading-link pl-2 text-italic text-bold" aria-label="Java"></a></h3>
<pre><code class="language-java">public class HelloWorld {
    public static void main (String[]args) {
      System.out.println.("Hello world");
    }
}
</code></pre>
<p>Pythonは汎用言語であるため、様々な用途で使用することができ、そのシンプルさから、作業の自動化、Webサイトやソフトウェアの構築、データ分析などに最適な言語です。</p>
<p>また、Pythonは開発者やエンジニアの間で人気がある他のいくつかの特徴を持っています。これらは以下の通りです。</p>
<ul>
<li><strong>読みやすい。</strong>Pythonのコードは、句読点ではなく英語のキーワードを使用し、改行によってコードブロックが定義されます。つまり、コードを見るだけで、そのコードが何をするために設計されているのかがわかるのです。</p>
</li>
<li>
<p><strong>オープンソースです。</strong> <a href="https://www.python.org/downloads/">ソースコードを</a>ダウンロードして、自由に改変して使うことができます。</p>
</li>
<li>
<p><strong>移植性がある</strong>Pythonはクロスプラットフォーム言語です。つまり、Pythonインタプリタがあれば、どのOS上でも<strong>同じ</strong>コードを実行できます。</p>
</li>
<li>
<p><strong>拡張可能です。</strong>Pythonのコードは他の言語（C++など）で書くことができ、ユーザーはPythonインタープリタに低レベルモジュールを追加して、ツールをカスタマイズしたり最適化したりすることができます。</p>
</li>
<li>
<p><strong>幅広い標準ライブラリがあります。</strong>この<a href="https://docs.python.org/3/library/">ライブラリは</a>誰でも利用することができ、ユーザは一つ一つの関数についてコードを書く必要がなく、日常的なプログラミングの問題などに役立つ組み込みモジュールにアクセスすることができます。</p>
</li>
</ul>
<h2 id="what-is-python-commonly-used-for-%f0%9f%92%bb">Pythonはどんなことに使われるの？<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4bb.png" alt="💻" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#what-is-python-commonly-used-for-%f0%9f%92%bb" class="heading-link pl-2 text-italic text-bold" aria-label="What is Python commonly used for? &#x1f4bb;"></a></h2>
<p>Pythonは、Webやソフトウェア開発、機械学習や人工知能（AI）など、あらゆることに利用することができます。その代表的な使用例をいくつか見てみましょう。</p>
<pre><code class="language-python">インポート・アンチグラビティ

def main():
    antigravity.fly()

if __name__ == '__main__':
    main()
</code></pre>
<p><strong><em>このコマンドを実行すると、Python開発者の間の内輪のジョークをチェックすることができます。</em></strong></p>
<h3 id="using-python-for-web-and-software-development">PythonをWebやソフトウェア開発に利用する<a href="#using-python-for-web-and-software-development" class="heading-link pl-2 text-italic text-bold" aria-label="Using Python for web and software development"></a></h3>
<p>Pythonは、簡潔で読みやすい構文を維持しながら、複雑なマルチプロトコルのアプリケーションを作成できるため、Webやソフトウェア開発で人気のある言語です。実際、最も人気のあるアプリケーションのいくつかは、Pythonで構築されています。さらに、Pythonのオープンソースコミュニティは、開発者に再利用可能なコード、フレームワーク、サポートを大量に提供します。その一例です。<a href="https://www.djangoproject.com/">Djangoは</a>、経験豊富な開発者によって設計された、最も使用されているPythonフレームワークの1つで、他の人がアプリケーションの構築時間を短縮し、進捗を妨げるかもしれない問題を回避するのに役立ちます。</p>
<h3 id="using-python-for-task-automation">タスクの自動化のためのPythonの使用<a href="#using-python-for-task-automation" class="heading-link pl-2 text-italic text-bold" aria-label="Using Python for task automation"></a></h3>
<p>Pythonの主な利点の1つは、手作業や繰り返しの作業を自動化できることです。Pythonでは、組み込みモジュールや堅牢なライブラリにある書きかけのコードを使用して、あらゆるものを自動化する方法を学ぶことができます。また、特定のアクションを実行するための独自のカスタムスクリプトを作成することもできます。例えば、<a href="https://docs.python.org/3/library/smtplib.html">「smtplib」モジュールで</a>電子メールを自動化したり、<a href="https://docs.python.org/3/library/shutil.html">「shutil」モジュールで</a>ファイルをコピーしたりすることが簡単にできます。Pythonはまた、テストフレームワークの堅牢なセットを持っており、テストの自動化のための優れた言語となっています。<a href="https://docs.pytest.org/en/7.2.x/">Pytest</a>、<a href="https://behave.readthedocs.io/en/stable/">Behave</a>、<a href="https://robotframework.org/">Robotなどの</a>フレームワークにより、開発者はビルドの品質を保証するためのシンプルかつ効果的なテストを書くことができます。</p>
<h3 id="using-python-for-machine-learning-and-data-science">Pythonの機械学習とデータサイエンスへの利用<a href="#using-python-for-machine-learning-and-data-science" class="heading-link pl-2 text-italic text-bold" aria-label="Using Python for machine learning and data science"></a></h3>
<p>Pythonは、データサイエンスや研究で最も好まれる言語です。Pythonの構文は理解しやすく、適応性が高いため、開発経験がほとんどない人でも簡単にPythonを習得し、研究、レポート、予測分析、回帰分析などのデータ操作に使用することができます。データの収集と解析は、データサイエンティストにとって時間のかかる作業です。Pythonはまた、機械学習（ML）モデルのトレーニングに最適な言語の1つです。これらのモデルは、特定のアルゴリズムを通じて、データのパターンを分析・識別し、そのデータに基づいて予測や意思決定を行うことができます。また、過去のデータセットの出力に基づいて常に進化し、新たな変数に立ち向かいます。データ科学者やMLモデルの開発者は、<a href="https://numpy.org/">NumPy</a>、<a href="https://pandas.pydata.org/">Pandas</a>、<a href="https://matplotlib.org/">Matplotlibなどの</a>ライブラリを利用して、クリーニング、データ変換、可視化などの機能を自動化することがよくあります。</p>
<h3 id="using-python-for-financial-analysis">Pythonの金融分析への活用<a href="#using-python-for-financial-analysis" class="heading-link pl-2 text-italic text-bold" aria-label="Using Python for financial analysis"></a></h3>
<p>Pythonが大規模なデータセットを扱うデータサイエンティストを支援するのと同様に、Pythonは複雑な計算を迅速に実行するために金融業界で広く使用されています。株式市場では膨大な量のデータが生成されますが、Pythonは株価に関するデータをインポートし、アルゴリズムによって戦略を生成して取引機会を特定するために使用することができます。また、ポートフォリオの最適化、リスク管理、金融モデリングと可視化、暗号通貨分析、さらには詐欺の検出などにも使用できます。</p>
<h3 id="using-python-for-and-artificial-intelligence">Pythonの用途と人工知能<a href="#using-python-for-and-artificial-intelligence" class="heading-link pl-2 text-italic text-bold" aria-label="Using Python for and artificial intelligence"></a></h3>
<p>Pythonは、最も複雑な人工知能（AI）技術の一部にも使用されており、実際にAIに適した言語の1つとなっています。Pythonの簡潔で読みやすいコードにより、開発者は一貫性のある信頼性の高いシステムを作成できます。また、その膨大なライブラリには、開発者に機械学習タスクの強力なアルゴリズムを提供する<a href="http://pybrain.org/">PyBrainなどの</a>フレームワークが多数用意されています。さらに、Pythonの可視化機能は、AIやML用のこれらの大規模なデータセットを、理解しやすいグラフやレポートに変換するのに役立つのです。興味深いことに、人工知能研究所のOpenAIは、AIシステムを訓練する深層学習の標準フレームワークとして、Pythonフレームワークの<a href="https://pytorch.org/">Pytorchを</a>利用しているのだそうです。</p>
<h2 id="why-is-python-so-popular-%f0%9f%99%8c">なぜPythonが人気なのか？<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f64c.png" alt="🙌" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#why-is-python-so-popular-%f0%9f%99%8c" class="heading-link pl-2 text-italic text-bold" aria-label="Why is Python so popular? &#x1f64c;"></a></h2>
<p>Pythonは比較的シンプルに学習できることに加え、一貫して人気を集め続けている理由がいくつかあります。それらは以下の通りです。</p>
<ul>
<li><strong>生産性が高い。</strong>C++のような他の複雑なプログラミング言語と比較して、Pythonの構文は、ユーザーがより少ないものでより多くのことを行うことができ、同じコードの行を書くための時間と労力を削減することができます。</p>
</li>
<li>
<p><strong>Pythonには、ユーザをサポートする広大なコミュニティがあります。</strong>どんなに優れた開発者でも問題にぶつかることがあります。このようなとき、ユーザーコミュニティが貴重なリソースとなります。Pythonには、ドキュメント、チュートリアル、ヒント、言語をマスターするためのトリックを集めた巨大なコミュニティがあります。例えば、<a href="https://github.com/python/cpython">GitHubのPythonコミュニティでは</a>、言語の最新バージョンに関する情報からバグレポートやアップデートノートまで、あらゆる情報を提供しています。</p>
</li>
<li>
<p><strong>学術的である。</strong>Pythonは学問の世界でよく使われる言語となっており、小学生でもPythonに出会うことがあります（信じられないかもしれませんが、<a href="https://pythonbooks.org/for-kids/">Python専用の絵本</a>もあります）。コンピュータサイエンスの学生はPythonを学ぶことが多いですが、その用途はその分野を超えて、STEMや学術研究の他の分野にも及んでいます。例えば、微分方程式の解法、統計解析、粒子拡散のシミュレーションや追跡などにPythonを使用することができます。</p>
</li>
<li>
<p><strong>企業需要も高い。</strong>開発やデータ分析業務に幅広く応用できるため、Pythonの学習や知識は、求職者の間でトップスキルとみなされることが多いようです。<a href="https://www.statista.com/statistics/1296727/programming-languages-demanded-by-recruiters/">Statistaに</a>よると、Pythonは2022年に世界中の採用担当者が最も要求する言語の第3位となっています。</p>
</li>
</ul>
<h2 id="the-bottom-line">最重要課題<a href="#the-bottom-line" class="heading-link pl-2 text-italic text-bold" aria-label="The bottom line"></a></h2>
<p>Pythonはどこにでもあり、多くの人が日常的に遭遇する技術、Webサイト、そしてシステムの構築に使用されています。Pythonは、お気に入りのビデオストリーミングサービスから、次の暗号通貨取引を支援するMLアルゴリズムまで、あらゆるものを動かしています。さらに、<a href="https://github.com/readme/featured/webb-telescope-astropy">NASAがJames Webb宇宙望遠鏡のデータ解析にPythonを</a>使用しているように、Pythonは文字通り、この世に存在しないプログラミング言語の1つなのです。<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f680.png" alt="🚀" class="wp-smiley" style="height: 1em; max-height: 1em;" /></p>
<h2 id="how-to-get-started-with-python-%f0%9f%93%93">Pythonを始めるには<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4d3.png" alt="📓" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#how-to-get-started-with-python-%f0%9f%93%93" class="heading-link pl-2 text-italic text-bold" aria-label="How to get started with Python &#x1f4d3;"></a></h2>
<p>Googleで検索すると、Pythonの旅を始めるためのリソースが何百と出てきますが、すぐに圧倒されてしまうかもしれません。ここでは、Pythonを使い始めるために役立つGitHubリポジトリをいくつか紹介します。</p>
<ul>
<li><strong><a href="https://github.com/TheAlgorithms/Python">ビルド済みのPythonアルゴリズムを見る</a></strong>:ネットワークフローから物理、ニューラルネットワークまで、このリポジトリはPythonでアルゴリズムを構築するための素晴らしいガイドです。</li>
<li><strong><a href="https://github.com/Asabeneh/30-Days-Of-Python">30日でPythonを学ぶ</a></strong>:このステップバイステップガイドは、30日間でPythonの基本を学ぶことができます。 </li>
<li><strong><a href="https://github.com/trekhleb/learn-python">このチートシートからいくつかのヒントを得てください。</a></strong>:Pythonスクリプトのコード例と解説をまとめた、Python学習用のチートシートをご覧ください。</li>
<li><strong><a href="https://github.com/huangsam/ultimate-python">Pythonのスキルを磨く</a></strong>:Pythonのスーパーファンによって作られた、初心者から熟練者までのための学習ガイドからヒントを得てください。 </li>
</ul>
<p><a href="https://www.python.org/downloads/">Python</a> の最新バージョンをダウンロードしましょう。</p>
<h3 id="start-building-on-github-today">GitHub で今すぐビルドを始めよう<a href="#start-building-on-github-today" class="heading-link pl-2 text-italic text-bold" aria-label="Start building on GitHub today"></a></h3>
<p>GitHubは、Pythonを使い始めるための2つの簡単な方法を提供しています。GitHub Codespaces と GitHub Copilot です。</p>
<p>GitH<a href="https://github.com/features/codespaces">ub Codespacesは</a>、GitHubのすべての開発者が毎月60時間無料で利用でき、どのデバイスからでもクラウド上の開発環境を高速にスピンアップすることができます。Django の<a href="https://github.com/codespaces/templates">クイックスタート</a>・テンプレートをチェックして、ブラウザですぐにコーディングを始めましょう!</p>
<p>また、GitHubのAIペアプログラマーであるGitHub<a href="https://github.com/features/copilot">Copilotを使って</a>、Pythonの最初の行を書くことができます。その方法は以下の通りです。</p>
<ol>
<li>GitHub Copilot エクステンションをコードエディタにインストールします。 </li>
<li>コメントでプロジェクトの目的を記述します。</li>
<li>どのライブラリが必要かをコメントで記述する。</li>
<li>タブをクリックすると、GitHub Copilot が新しいテクニックやメソッドを学ぶのに役立つコード行を提案してくれます。</li>
</ol>
<div style="width: 3024px;" class="wp-video"><!--[if lt IE 9]><script>document.createElement('video');</script><![endif]-->
<video class="wp-video-shortcode" id="video-70321-1" width="3024" height="1922" preload="metadata" controls="controls"><source type="video/mp4" src="https://github.blog/wp-content/uploads/2023/03/rock_paper_scissors_AdobeExpress.mp4?_=1" /><a href="https://github.blog/wp-content/uploads/2023/03/rock_paper_scissors_AdobeExpress.mp4">https://github.blog/wp-content/uploads/2023/03/rock_paper_scissors_AdobeExpress.mp4</a></video></div>
<p>機械学習からデータ分析まで、Pythonの多用途性により、開発者だけでなく非開発者にも爆発的な成長を続けています。GitHubやローカルマシンでPythonを試して、この成長の一翼を担い、今すぐ始めましょう!</p>


