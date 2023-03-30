---
title: "CodeQLのC++用データフローライブラリの改善点"
subtitle: "これらの変更により、カスタムクエリ作成者のエクスペリエンスが向上し、一部の標準クエリでより高い精度が得られるようになります。カスタムクエリでこれらを有効にする方法については、こちらをご覧ください。"
englishsubtitle: "These changes will improve the experience for custom query authors and enable better precision in some of our standard queries. Learn how to enable them for your custom queries."
englishtitle: "Improvements to CodeQL’s data flow library for C++"
date: "2023-03-30"
cardurl: "https://github.blog/2023-03-30-improvements-to-codeqls-data-flow-library-for-c/"
author: "Robert Marsh"
description: " We’ve recently made some changes to CodeQL’s data flow and taint tracking libraries for C++, which will improve the experience for custom query authors and enable better precision in some of our standard queries. While these changes are included in the standard queries already, you can also enable them for custom queries. We’ll show you how in this blog post.  CodeQL  CodeQL is the static analysis engine behind code scanning. CodeQL works by constructing a database of your code, and then running queries against that database. These queries depend on a variety of shared libraries that perform specific analyses, such as taint tracking and range analysis.  Dataflow  CodeQL’s dataflow library performs an analysis of what expressions may have their value copied to which other expressions, across the entire program. The taint tracking library generalizes this to what expressions may influence the value of which other expressions. Because this is potentially a very large relation, we use a query-specific configuration to restrict the analysis to a set of interesting sources and sinks for a given query before performing any interprocedural analysis. This allows the dataflow or taint tracking configuration to also include query-specific sanitizers and guards that prevent dangerous data from flowing.  Def-use vs use-use  Historically, the C++ dataflow library has followed a “def-use” pa"
coverimage: "https://github.blog/wp-content/uploads/2021/12/github-security_orange-banner.png?resize=1200%2C630"
category: "Security,CodeQL"
englishsummary: "  CodeQL has recently made changes to its data flow and taint tracking libraries for C++ which will improve the experience for custom query authors and enable better precision in some of the standard queries."
summary: "  CodeQLは最近、C++用のデータフローとテイント追跡ライブラリに変更を加え、カスタムクエリ作成者のエクスペリエンスを向上させ、一部の標準クエリでより精度の高い処理を可能にしました。"
---

<p>最近、CodeQL の C++ 用データフローおよびテイント追跡ライブラリにいくつかの変更を加え、カスタム クエリ作成者のエクスペリエンスを向上させ、一部の標準クエリでより優れた精度を実現するようにしました。これらの変更はすでに標準クエリに含まれていますが、カスタムクエリで有効にすることもできます。このブログ記事でその方法を紹介します。</p>
<h2 id="codeql">CodeQL<a href="#codeql" class="heading-link pl-2 text-italic text-bold" aria-label="CodeQL"></a></h2>
<p><a href="https://codeql.github.com/">CodeQLは</a>、コードスキャンを支える静的解析エンジンです。CodeQLは、コードのデータベースを構築し、そのデータベースに対してクエリーを実行することで動作します。これらのクエリーは、テイント追跡や範囲分析など、特定の分析を行うさまざまな共有ライブラリに依存しています。</p>
<h2 id="dataflow">データフロー<a href="#dataflow" class="heading-link pl-2 text-italic text-bold" aria-label="Dataflow"></a></h2>
<p>CodeQLのデータフローライブラリは、プログラム全体にわたって、どの式が他のどの式に値をコピーされる可能性があるかという分析を実行します。テイント追跡ライブラリーはこれを、どの式がどの他の式の値に影響を与える可能性があるかに一般化します。これは非常に大きな関係になる可能性があるため、手続き間解析を行う前に、クエリ固有の設定を使用して、与えられたクエリの興味深いソースとシンクのセットに解析を制限しています。これにより、データフローやテイントトラッキングの構成に、危険なデータが流れるのを防ぐクエリ固有のサニタイザーやガードも含めることができます。</p>
<h2 id="def-use-vs-use-use">デフユースとユースユースの比較<a href="#def-use-vs-use-use" class="heading-link pl-2 text-italic text-bold" aria-label="Def-use vs use-use"></a></h2>
<p>歴史的に、C++データフローライブラリは「def-use」パターンに従っており、変数からの読み取りは「定義」（変数への代入）から「使用」（その変数からの読み取り）までのステップとしてモデル化され、同じ定義の2つの後続使用は直接接続しない。他の言語の分析では、「use-use」パターンに従っており、変数からの読み出しは、前の読み出し（前の読み出しがない場合は定義）からのステップとしてモデル化されます。</p>
<p>クエリ作成者にとってuse-useパターンの大きな利点は、条件付きサニタイザーを考慮したクエリの実装がよりシンプルになることです。次のようなコードを考えてみましょう：</p>
<pre><code>char *str = source()；
if (isSafe(str)) { (isSafe(str))
    シンク(str)
}
</code></pre>
<p>以前は、この結果を除外するために、クエリは別の制御フロー分析を使用して、値の危険な使用へのすべてのパスでチェックが行われることを示す必要がありました。ユースユースフローでは、この解析がデータフロー・グラフに組み込まれ、エンドユーザーのクエリーを簡素化することができます。</p>
<h2 id="pointers-and-indirections">ポインタと間接関数<a href="#pointers-and-indirections" class="heading-link pl-2 text-italic text-bold" aria-label="Pointers and indirections"></a></h2>
<p>ポインターの値とそれが指す値を分離して分析するようになり、関数境界で渡される値と汚染されたデータの間に複数レベルのポインターを含めることができるようになりました。これにより、特に文字列の値について、特定のフローをより正確に追跡することができるようになりました。</p>
<pre><code>char *str = source()；
sqlEscape(&amp;str)；
sink(str)；
</code></pre>
<p>上記の例では、ユーザが制御する値は<code>argv</code>そのものではなく、2回再参照された後にargvが指し示す値である。以前は、コマンドライン入力を危険視するクエリでは、<code>argvを</code>汚染された値としてマークし、それへのアクセスも汚染されたものとみなされていました。つまり、ポインタの値が安全であっても、<code>argvを</code>再参照することが危険とみなされるクエリもあったのです。新しいシステムでは、汚染されたデータは<code>argvを</code>2回再参照することによってのみアクセスされることを表現できるため、これらのクエリは最初の再参照を安全でないものとして扱わなくなりました。</p>
<h2 id="how-to-adopt-it-for-custom-queries">カスタムクエリに採用する方法<a href="#how-to-adopt-it-for-custom-queries" class="heading-link pl-2 text-italic text-bold" aria-label="How to adopt it for custom queries"></a></h2>
<p>新しいライブラリは標準的なクエリで使用されていますが、インダイレクト処理の変更に伴いクエリの変更が必要になる場合があるため、カスタムクエリではオプトインとなっています。一般的に、新しいライブラリは古いライブラリとほぼ同じ動作をします。しかし、新しいライブラリはポインタとそのインダイレクトの区別をより正確に処理するため、いくつかの違いがあります。例えば，次の例では，argvは一連の文字へのポインタであり，fopenの第1引数は一連の文字へのポインタである．</p>
<pre><code>int main (int argc, char **argv) { 。
    if(argc &gt;= 2) {。
        fopen(argv[1])
    }
}
</code></pre>
<p>argvからその引数への流れを見つけるために、以前は次のようなクエリを書いていました：</p>
<pre><code>インポート cpp
インポート semmle.code.cpp.dataflow.TaintTracking

class ArgvTaintedFopenConfig extends TaintTracking::Configuration {.
  ArgvTaintedFopenConfig() { this = "ArgvTaintedFopenConfig" } 。

  override predicate isSource(DataFlow::Node node) {。
    exists(パラメータargv |)
      node.asParameter() = argv とする。
      argv.hasName("argv")かつ
      argv.getFunction().hasGlobalName("main")
    )
  }

  override predicate isSink(DataFlow::Node node) {。
    exists(FunctionCall fopenCall |)
      node.asExpr() = fopenCall.getArgument(0) とする。
      fopenCall.getTarget().hasGlobalOrStdName("fopen")
    )
  }
}
</code></pre>
<p>新しいシステムでは、代わりに<code>node.asParameter(2)</code>を使って、<code>argv の</code>値そのものではなく、2回再参照された後に指す一連の文字に関心があることを指定することができます。同様に、<code>node.asIndirectArgument(1)</code>を使って、<code>fopenに</code>入る潜在的に危険なデータはポインタではなく、1回の再参照の後にそれが指す値であることを指定することができる。</p>
<pre><code>インポート cpp
インポート semmle.code.cpp.dataflow.new.TaintTracking

class ArgvTaintedFopenConfig extends TaintTracking::Configuration {.
  ArgvTaintedFopenConfig() { this = "ArgvTaintedFopenConfig" } 。

  override predicate isSource(DataFlow::Node node) {。
    exists(パラメータargv |)
      node.asParameter(2) = argv とする。
      argv.hasName("argv")かつ
      argv.getFunction().hasGlobalName("main")
    )
  }

  override predicate isSink(DataFlow::Node node) {。
    exists(FunctionCall fopenCall |)
      node.asIndirectArgument(1) = fopenCall.getArgument(0) とする。
      fopenCall.getTarget().hasGlobalOrStdName("fopen")
    )
  }
}
</code></pre>
<p>あるいは、より一般的な述語<code>node.asIndirectExpr(int)</code>があり、プログラム中のポインタ型の任意の式の間接の値を記述するために使用することができます。</p>
<p>新しいライブラリにオプトインするには、<code>import semmle.code.cpp.dataflow.DataFlow</code>を<code>import semmle.code.cpp.dataflow.new.DataFlow</code> と置き換えてください。次に、<code>node.asExpr()</code>や<code>node.asParameter()</code>を使った<code>isSource()</code>や<code>isSink() の</code>定義が、追跡したい値を指定しているのか、その値への単なるポインタや参照なのかを考えてみます。後者の場合は、新しい<code>node.asIndirectArgument(int)</code>,<code>node.asIndirectExpr(int)</code>,<code>node.asDefiningArgument(int)</code>,<code>node.asParameter(int)</code> に置き換えてください。既存の<code>node.asParameter()</code>と<code>node.asExpr()</code>はまだ存在しますが、ノードの再参照ではなく、ノード自体の値を参照するようになったことに注意してください。</p>
<h3 id="learn-more-about-github-security-solutions">GitHubのセキュリティソリューションについてもっと知る<a href="#learn-more-about-github-security-solutions" class="heading-link pl-2 text-italic text-bold" aria-label="Learn more about GitHub security solutions"></a></h3>
<p>GitHubは、開発者の体験を損なうことなく、より安全でセキュアなソフトウェアの構築を支援することを約束します。コードスキャンなどのGitHubのセキュリティ機能の詳細や有効化については、GitHubの<a href="https://docs.github.com/en/enterprise-cloud@latest/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning">ドキュメントを</a>ご覧ください。</p>


