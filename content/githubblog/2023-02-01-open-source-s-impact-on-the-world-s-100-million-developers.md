---
title: "オープンソースがもたらす、世界の1億人の開発者へのインパクト"
subtitle: "今回は、GitHub上でオープンソースソフトウェアがどのように進化してきたか、また、オープンソースソフトウェアの大規模な成長とともに、メンテナやコントリビューターの役割がどのように変化してきたかをご紹介します。"
englishsubtitle: "We’re taking a look at how open source software has evolved on GitHub, and how the role of a maintainer and contributor has changed alongside the massive growth in open source software."
englishtitle: "Open source’s impact on the world’s 100 million developers"
date: "2023-02-01"
cardurl: "https://github.blog/2023-02-01-open-sources-impact-on-the-worlds-100-million-developers/"
author: "Abby Cabunoc Mayes"
description: "The open source movement quietly underpins all of the technology we use to live and work. Open source is about more than just technology or a license—it’s about creating a culture of participation and collaboration, where anyone can contribute to making the world a better place."
coverimage: "https://github.blog/wp-content/uploads/2023/01/100MDevs_Blog_1200x627_v3.gif?resize=1200%2C627"
category: "Open Source"
---

<p>オープンソースムーブメントは、私たちが生活や仕事に使用するすべてのテクノロジーを静かに支えています。オープンソースは、単なる技術やライセンス以上のものであり、誰もが世界をより良くするために貢献できる、参加と協力の文化を創造するものです。</p>
<p>オープンソースソフトウェアはGitHubよりずっと以前から存在していました。しかし今日、GitHubはオープンソースコミュニティの多くの人々が出会い、他の人々を刺激し、プロジェクトを成長させ、その仕事を評価される場所となっています。<a href="https://github.blog/2023-01-25-100-million-developers-and-counting/">GitHubの開発者数が1億</a>人を突破したことを発表したとき、開発者の定義がテクノロジー企業のためにソフトウェアを作る人たちだけでなく、どのように進化してきたかを見てきました。しかし、それだけではありません。オープンソースで働く、あるいはオープンソースで働くという旅も進化しています。今回は、GitHub でオープンソースプロジェクトのお気に入りのメンテナを紹介し、彼らの経験談を聞いてみたいと思います。</p>
<h2 id="an-idea-takes-off-%f0%9f%9a%80">あるアイデアが軌道に乗る<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f680.png" alt="🚀" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#an-idea-takes-off-%f0%9f%9a%80" class="heading-link pl-2 text-italic text-bold" aria-label="An idea takes off &#x1f680;"></a></h2>
<p>ある開発者の個人的なプロジェクトが GitHub 上で広がり、世界中の開発者に影響を与えたという話を聞くのはとても楽しいものです。PSSendGrid のメンテナであり GitHub のスターでもある<a href="https://github.com/Ba4bes">Barbara Forbes</a> さんは、まさにこのような体験をしました。GitHub Universe で、<a href="https://youtu.be/oNVei5QR8Zk">彼女の話を聞いて</a>みました。</p>
<blockquote><p>私は日々の仕事をこなしながら、仕事で遭遇する問題に対して自分なりの解決策を考えていました。突然、人々がリポジトリにスターを追加し、イシューを作成していることを発見したのです全く期待していなかったのに、本当に流行ったモジュールのひとつが、SendGrid APIに関するラッパーでした。これはもしかしたらみんな使えるかもしれない、だからこれをオンラインに置いておこうと思ったんです。そうしたら、なんと<strong>4万件もダウンロード</strong>されていたんです。</p></blockquote>
<p>自分の趣味のプロジェクトが世界中の開発者に利用されていることもそうですが、開発者が自分のプロジェクトに貢献し、みんなのためにより良いものにしようと興奮していることも、また別の話です。この感覚は、プロジェクトを超えた何かを作り上げたとき、つまりコミュニティを作り上げたときに、特別なものとなりますオープンソースプロジェクトは、一人の開発者から、一緒に素晴らしいものを作ろうとする熱心なコミュニティへと急速に成長することができます。<a href="https://github.com/readme/stories/evan-you">Vueのメンテナであるエヴァン・ユーの</a>話を聞いてください。</p>
<blockquote><p>ユーザー数が一定量に達したとき、Vueはコミュニティになりました。突然、貢献者、教育者、学生など、すべての人々が私を頼りにするようになったのです。Vueのコアメンバーは、本当に情熱を持って取り組んでいました。ユーザーが面白いものを作っている。Vueは、私が想像していた以上に大きな存在になりました。</p></blockquote>
<h2 id="maintaining-with-others-%f0%9f%91%a5">他の人と一緒にメンテナンスする<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f465.png" alt="👥" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#maintaining-with-others-%f0%9f%91%a5" class="heading-link pl-2 text-italic text-bold" aria-label="Maintaining with others &#x1f465;"></a></h2>
<p>プロジェクトが成熟するにつれ、多くのメンテナは新しいリーダーや貢献者を受け入れる余裕を持つようになります。メンターシップ、ガバナンスの構築、ミートアップの開催など、持続可能なコミュニティとコードベースを構築するためには、目に見えない多くの作業が必要です。オープンソースでは、多様な人々との円滑なコラボレーションを可能にするために、ガバナンスが重要な鍵を握っています。ロリーナ・メサが、Python Software Foundation の理事会での<a href="https://github.com/readme/stories/lorena-mesa">経験の一部を</a>紹介します。</p>
<blockquote><p>オープンソースについて考えるとき、人々は技術的な要素に焦点を当てます。しかし、それはまた、コラボレーションについてです。このことを行うには村が必要です。</p></blockquote>
<p>コードだけでなく、あらゆる種類のコントリビューションを募ることが、メンテナにとって重要なのです。<a href="https://github.com/electron/electron">Electronの</a>メンテナである<a href="https://github.com/VerteDinde">Keeley Hammondは</a>、新しい貢献者、特に非技術的な貢献のためのスペースを作るためにどのように働いて<a href="https://github.com/readme/stories/keeley-hammond">いるかを話して</a>くれました。</p>
<blockquote><p>私たちは新しいコントリビューターを歓迎し、アクセスしやすくするために努力しています。しかしElectronは、たとえ経験豊富な開発者であっても、入り込むのに躊躇するコードベースです。私がプロジェクトに貢献しようとしたとき、最初は技術的な仕事ではなく、メンテナサミットの運営を手伝ったり、リリースノートを集めたり、ブログ記事を書いたりすることを志願していました。</p></blockquote>
<h2 id="getting-paid-%f0%9f%92%b0">報酬を得る<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4b0.png" alt="💰" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#getting-paid-%f0%9f%92%b0" class="heading-link pl-2 text-italic text-bold" aria-label="Getting paid &#x1f4b0;"></a></h2>
<p>何千ものソフトウェア会社や組織が、オープンソースプロジェクトの拡張や保守のためにチームを作っています。Metaによる<a href="https://github.com/facebook/react">Reactの</a>メンテナンス、<a href="https://youtu.be/qDyAWtlpqUA?t=1829">PickNikによるRobot Operating SystemのMoveItプロジェクトの運営</a>、Quansight Labsによる<a href="https://github.com/numpy/numpy">NumPy</a>、<a href="https://github.com/scipy/scipy">SciPy</a>、<a href="https://github.com/scikit-learn/scikit-learn">scikit-learnでの</a>作業はすべて、雇用と寄付を通じて基礎となるオープンソースプロジェクトに影響を与える組織の例となります。Metaのオープンソースプログラムオフィスの<a href="https://www.youtube.com/watch?v=pqj-0FvapKE">Dmitry Vinnikから話を聞いて</a>みましょう。</p>
<blockquote><p>Meta は、Meta のオープンソース プロジェクトでさえも、すべてスケールについて考えています。毎年、私たちは1年分のレビューを発表しています。前回のレビューでは、800以上のアクティブなオープンソースリポジトリがありました。</p></blockquote>
<p>他のプロジェクトは、<a href="https://github.com/sponsors">GitHub Sponsorsの</a>ようなツールを使って、寄付によって維持することができます。GitHub Universeでは、<a href="https://github.com/kovidgoyal/calibre">Calibreの</a>メンテナである<a href="https://www.youtube.com/watch?v=5l0bVoQ4jN8">Kovid Goyal</a>氏に、オープンソースでフルタイムに働くためにスポンサーを得た経験について<a href="https://www.youtube.com/watch?v=5l0bVoQ4jN8">話を</a>聞きました。</p>
<blockquote><p>Calibreは、私が予想していたよりもずっと大きくなりました。寄付のボタンを設置したら、ピザよりも多くのお金をもらうようになりました...私は妻と話し合い、これをフルタイムでやっていこうと決めました。それ以来、ずっとうまくいっていますよ。</p></blockquote>
<h2 id="keep-contributing">貢献し続ける<a href="#keep-contributing" class="heading-link pl-2 text-italic text-bold" aria-label="Keep contributing"></a></h2>
<p>オープンソースは、私たちのテクノロジーの世界の基礎的な岩盤であり続けるでしょう。オープンソースコミュニティーを発展させ、私たちが信頼するプロジェクトに恩返しをするのは、私たち全員にかかっているのです。私たちは、オープンソースのサポートを継続し、次の1億人の開発者（アーティスト、オーガナイザー、コーダーなど）にツールを提供できることに興奮しています。</p>
<p><strong>最初の寄付をすることに興味がありますか？</strong><br />
<a href="https://opensource.guide/how-to-contribute/">オープンソースに貢献する方法</a>」をご覧ください。</p>
<p><strong>次に貢献できる最高のプロジェクトを見つけたいですか？</strong><br />
<a href="https://github.com/explore/">GitHub Explore</a> をご覧ください。</p>


