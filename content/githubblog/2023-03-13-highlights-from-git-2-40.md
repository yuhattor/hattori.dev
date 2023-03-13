---
title: "Git 2.40のハイライト"
subtitle: "今年最初のGitリリースがやってきました。Git 2.40の新機能のハイライトをご覧ください。"
englishsubtitle: "The first Git release of the year is here! Take a look at some of our highlights on what's new in Git 2.40."
englishtitle: "Highlights from Git 2.40"
date: "2023-03-13"
cardurl: "https://github.blog/2023-03-13-highlights-from-git-2-40/"
author: "Taylor Blau"
description: " The open source Git project just released Git 2.40 with features and bug fixes from over 88 contributors, 30 of them new.  We last caught up with you on the latest in Git when 2.39 was released . To celebrate this most recent release, here’s GitHub’s look at some of the most interesting features and changes introduced since last time.  Longtime readers will recall our coverage of git jump from way back in our Highlights from Git 2.19 post. If you’re new around here, don’t worry: here’s a brief refresher.  git jump is an optional tool that ships with Git in its contrib directory . git jump wraps other Git commands, like git grep and feeds their results into Vim’s quickfix list. This makes it possible to write something like git jump grep foo and have Vim be able to quickly navigate between all matches of “foo” in your project.  git jump also works with diff and merge . When invoked in diff mode, the quickfix list is populated with the beginning of each changed hunk in your repository, allowing you to quickly scan your changes in your editor before committing them. git jump merge , on the other hand, opens Vim to the list of merge conflicts.  In Git 2.40, git jump now supports Emacs in addition to Vim, allowing you to use git jump to populate a list of locations to your Emacs client. If you’re an Emacs user, you can try out git jump by running:  M-x grepgit jump --stdout grep fo"
coverimage: "https://github.blog/wp-content/uploads/2023/03/git-240-2.png?resize=1600%2C850"
category: "Engineering,Open Source,Git"
englishsummary: "  Git 2.40 has been released with features and bug fixes from 88 contributors, including a new tool called git jump, which allows users to quickly navigate between matches and conflicts in Vim and Emacs."
summary: "  Git 2.40がリリースされ、88人のコントリビューターによる機能とバグ修正が行われました。この中には、VimとEmacsでマッチとコンフリクトの間を素早く移動できる新しいツール「git jump」が含まれています。"
---

<p>オープンソースのGitプロジェクトは、88以上のコントリビューター（うち30人は新規参加）による機能とバグフィックスを含む<a href="https://lore.kernel.org/git/xmqqjzzkv8xz.fsf@gitster.g/T/#u">Git 2.40をリリース</a>しました。</p>
<p>前回、Gitの最新情報をお伝えしたのは<a href="https://github.blog/2022-12-12-highlights-from-git-2-39/">2.39のリリース</a>時でした。この最新のリリースを記念して、前回から導入された最も興味深い機能や変更点をGitHubが紹介します。</p>
<hr />
<ul>
<li>長年の読者の皆さんは、<code>Git</code> <a href="https://github.blog/2018-09-10-highlights-from-git-2-19/">2.19のハイライトで</a>紹介した<code>gitジャンプの</code>記事を思い出してください。もしあなたがこのページを初めてご覧になるのなら、ご心配なく。ここで簡単におさらいしておきましょう。
<p><code><a href="https://github.com/git/git/tree/v2.40.0/contrib/git-jump">git jump</a></code>は、Git の<code><a href="https://github.com/git/git/tree/v2.40.0/contrib">contrib</a></code> ディレクトリに同梱されているオプションのツールです。<code>git jump</code>は、<code>git grep</code>のような他の Git コマンドをラップして、その結果を Vim の<a href="https://vimdoc.sourceforge.net/htmldoc/quickfix.html">quickfix</a>リストにフィードします。このため、<code>git jump grep foo</code>のように書くと、Vim でプロジェクト内の "foo" にマッチするすべての箇所をすばやく表示することができます。</p>
<p><code>git jump</code>は<code>diff</code>や<code>merge</code> でも動作します。<code>diff</code>モードで実行すると、リポジトリの各変更ハンクの先頭がクイックフィクスリストに表示され、コミットする前にエディタで変更点をすばやく確認することができます。</p>
<p>Git 2.40 では、<code>git jump</code>が Vim に加えて Emacs もサポートするようになり、<code>git jump</code>を使って Emacs クライアントに場所のリストを入力することができるようになりました。Emacsユーザーであれば、<code>git jumpを</code>実行して試してみることができます。</p>
<p><code>M-x grep<RET>git jump --stdout grep foo<RET></code></p>
<p>[<a href="https://github.com/git/git/compare/9ea1378d046d764642718f1b070689072bde4601...9508dfd9f553019c2e3b2869926a0dcaed7a498f">出典</a>]</p>
</li>
<li>
<p>Git リポジトリでスクリプトを書いたことがある人なら、Git の<code>cat-file</code>ツールをご存知でしょう。このツールを使えば、任意のオブジェクトの内容を出力することができます。</p>
<p>v2.38.0<a href="https://github.blog/2022-10-03-highlights-from-git-2-38/">がリリース</a>されたときに、cat<code>-fileが</code>コミットの内容を出力するときにGitの<a href="https://git-scm.com/docs/gitmailmap">メールマップルールを</a>適用するようになったという話をしました。要約すると、Gitはリポジトリのメールマップに従って名前と電子メールのペアを書き換えることができます。v2.38.0 では、<code>git cat-file</code>は新しい<code>--use-mailmap</code>オプションで、オブジェクトの内容を印刷する前にそれらの変換を適用する方法を学びました。</p>
<p>しかし、特定のオブジェクトの内容には興味がなく、代わりにサイズを知りたい場合はどうすればいいのでしょうか。その場合、<code>-batch-check=%(objectsize)</code>や、1つのオブジェクトをチェックするだけなら<code>-sを</code>使うことになるかもしれません。</p>
<p>しかし、それは間違いです。以前のバージョンの Git では、<code>git cat-file</code>の<code>--batch-check</code>と<code>-s</code>オプションは<code>--use-mailmap</code> の存在を無視していたため、mailmap の書き換えの両側の名前とメールのペアが異なる長さだった場合に誤った結果になる可能性がありました。</p>
<p>Git 2.40 ではこれが修正され、<code>git cat-file -s</code>と<code>--batch-check</code>with は<code>--use-mailmap</code> とともに実行されたときに、あたかも置換IDを使って書かれたかのようにオブジェクトのサイズを忠実に報告するようになりました。</p>
<p><a href="https://github.com/git/git/compare/2b4f5a4e4bb102ac8d967cea653ed753b608193c...a797c0ea042af697d82ad475b9f354c4a33a9047">[ソース］</a></p>
</li>
<li>
<p>スクリプトの話をしている間に、あまり知られていない Git コマンドを紹介しましょう。 <code><a href="https://git-scm.com/docs/git-check-attr/2.40.0">git check-attr</a></code>.<code>check-attrを</code>使用して、どの <code><a href="https://git-scm.com/docs/gitattributes/2.40.0">ギットアタビュート</a></code>は、与えられたパスに対して設定されます。</p>
<p>これらの属性は、リポジトリ内の<code>.gitattributes</code>ファイルによって定義され、設定されます。単純な例では、次のように<code>.gitattributes</code>ファイルから読み取るのが簡単です。</p>
<pre><code>&lt;code&gt;$ head -n 2 .gitattributes 
* ホワイトスペース＝！インデント、トレール、スペース 
*.[ch] whitespace=indent,trail,space diff=cpp
</code></pre>
<p>ここでは、<code>*.c</code>や<code>*.h</code>で終わるファイルには上記の属性が設定されていることを比較的簡単に確認できます。しかし、もっと複雑なルールがある場合や、プロジェクトで複数の<code>.gitattributes</code>ファイルを使用している場合はどうすればいいのでしょうか。そんなときは<code>check-attrを</code>使いましょう。</p>
<pre><code>$ git check-attr -a git.c 
git.c: diff: cpp 
git.c: 空白文字: インデント、トレイル、スペース
</code></pre>
<p>以前は、<code>check-attrの</code>決定的な制限として、<a href="https://git-scm.com/docs/gitformat-index/2.40.0">インデックスが</a>必要だったため、<a href="https://git-scm.com/docs/gitglossary/2.40.0#Documentation/gitglossary.txt-aiddefbarerepositoryabarerepository">ベアリポジトリで</a> <code>check-attrを</code>使用したい場合、以下のようにインデックスを一時的に読み込む必要がありました。</p>
<pre><code>TEMP_INDEX="$(mktemp ...)" のように。 

git read-tree --index-output="$TEMP_INDEX" HEAD 
GIT_INDEX_FILE="$TEMP_INDEX" git check-attr ... 
</code></pre>
<p>この種の回避策は、Git 2.40 以降ではもはや必要ありません。Git 2.40 では、<code>check-attr</code>は新たに<code>--source=<tree-ish></code>で<code>.gitattributes</code>をスキャンするようになりました。つまり、ベアリポジトリであっても、上記の代わりに以下のようにすればうまくいくでしょう。</p>
<pre><code>$ git check-attr -a --source=HEAD^{tree} git.c 
git.c: diff: cpp 
git.c: 空白文字: インデント、トレイル、スペース
</code></pre>
<p><a href="https://github.com/git/git/compare/8a40af9cabe2efbb830bf90c864ffda3136926ba...47cfc9bd7d0add617cf6d928e96b7d207be614f1">[出典</a>]</p>
</li>
<li>
<p>何年も前から、Gitの古い部分をPerlやShellの実装から、より現代的なCの同等物に書き換えるという努力が続けられています。Git自身のAPIをネイティブに使えるようになったことはもちろんですが、Gitコマンドを単一のプロセスに統合することは、Windowsのようなプロセスの起動コストが高いプラットフォームでも、より迅速に実行できるようになることを意味します。</p>
<p>その点で、このリリースには特筆すべきいくつかのハイライトがあります。</p>
<p>Git 2.40では、<code>git bisectが</code>ネイティブのビルトインとしてC言語で完全に実装されました。これは、Google Summer of Code の学生を含む多くの Git 貢献者の長年の努力の結果です。<br />
同様に、Git 2.40 では<code>git add --interactive</code> のレガシーな実装が廃止されました。これはシェルスクリプトとして始まり、バージョン 2.26 でネイティブの組み込み機能として再導入されたもので、実験的に<code>add.interactive.useBuiltin</code>という設定の下で新旧両方の実装をサポートしています。</p>
<p>バージョン2.37からこのデフォルトが「true」になっているため、Gitプロジェクトは、今やレガシーな実装を完全に取り除く時が来たと判断し、Gitのパフォーマンスを向上させレガシースクリプトのフットプリントを減らすための長年の努力に終止符を打つことにしました。</p>
<p><a href="https://github.com/git/git/compare/c48035d29b4e524aed3a32f0403676f0d9128863...049141dce971bdbb85b3c6d12aae7254e7ddbe68">[ソース</a>、<a href="https://github.com/git/git/compare/c5f7b2a6fe34bbdd4453be6620e08dbcf1b695fb...5a7d41d849290ceadb02487ec962c5a040391535">ソース］</a></p>
</li>
<li>
<p>最後になりましたが、Git の CI インフラストラクチャには、ちょっとした改良が加えられています。Gitには、Windows特有の長時間のCIビルドがいくつかありますが、このリリースでは（<code>git-for-windows</code>リポジトリ以外では）無効化されています。Git の開発者であれば、CI の実行がより速く完了し、プッシュごとのリソース消費も少なくなるはずです。</p>
<p>同じように、すでにアクティブなCIジョブが実行されているブランチへのプッシュで、それらのジョブをキャンセルするかどうかを設定することができるようになりました。これは、あるトピックに取り組んでいるときに同じブランチに何度もプッシュする場合に便利でしょう。</p>
<p>この設定は、Git の<code>ci-config を</code>使って行います。<code>ci-config</code> というブランチに<code>skip-concurrent</code>という特別なスクリプトを追加します。Gitのフォークにそのブランチがあれば、Gitはそこにある関連スクリプトを参照して、どのブランチで作業しているかに基づいてCIを同時に実行するかどうかを決定します。</p>
<p><a href="https://github.com/git/git/compare/4dbebc36b0893f5094668ddea077d0e235560b16...a0da6deeec16e3a141476dd63d644ed2428476d8">[ソース</a>、<a href="https://github.com/git/git/compare/42f9a60013bd30ed6aee1a5002c26f58a1531f95...eb5b03a9c0a0c8b4d82ece6069821de41b06722b">ソース</a>]。</p>
</li>
</ul>
<h2 id="the-rest-of-the-iceberg">残りの氷山<a href="#the-rest-of-the-iceberg" class="heading-link pl-2 text-italic text-bold" aria-label="The rest of the iceberg"></a></h2>
<p>これは、最新リリースからの変更点のほんの一例です。詳しくは、<a href="https://github.com/git/git/blob/v2.40.0/Documentation/RelNotes/2.40.0.txt">2.40の</a>リリースノート、またはGitリポジトリにある<a href="https://github.com/git/git/tree/v2.40.0/Documentation/RelNotes">以前のバージョンの</a>リリースノートをご覧ください。</p>


