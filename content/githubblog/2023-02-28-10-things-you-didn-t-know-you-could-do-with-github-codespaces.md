---
title: "意外と知らない、GitHub Codespacesでできる10のこと！"
subtitle: "GitHub Codespacesの可能性を最大限に引き出す10のヒントとトリックをご紹介します。AIイメージの生成から、セルフガイドのコーディングワークショップの運営まで、このパワフルなツールを使ってソフトウェア開発のワークフローを最適化する方法を発見してください。"
englishsubtitle: "Unlock the full potential of GitHub Codespaces with these 10 tips and tricks! From generating AI images to running self-guided coding workshops, discover how to optimize your software development workflow with this powerful tool."
englishtitle: "10 things you didn’t know you could do with GitHub Codespaces"
date: "2023-02-28"
cardurl: "https://github.blog/2023-02-28-10-things-you-didnt-know-you-could-do-with-github-codespaces/"
author: "Rizel Scarlett"
description: " Ever feel like you’re coding on a plane mid-flight? When I first learned to code about five years ago, my laptop was painstakingly slow, but I couldn’t afford a better one. That’s why I relied on browser-based IDEs like jsbin.com to run my code.  Now fast forward to today, where GitHub Codespaces provides a fully-fledged, browser-based Integrated Development Environment (IDE) on a virtual machine. This means you can code without draining your local machine’s resources. Cloud-powered development is a game-changer for folks with less powerful machines, but that barely scratches the surface of GitHub Codespaces’ versatility.  In this blog post, we’ll discuss a few ways that you can get the most out of GitHub Codespaces!  Generate AI images  You can run Stable Diffusion with GitHub Codespaces. Like DALL-E and Midjourney, Stable Diffusion is one of many machine-learning models using deep learning to convert text into art.  Stable Diffusion takes the following steps to convert text into art:  AI receives an image  AI adds noise to the image until the image becomes completely unrecognizable. (Noise is another way of saying pixelated dots.)  AI removes the noise until it produces a clear, high-quality image  AI learns from a database called LAION-Aesthetics. The database has image-text pairs to learn to convert text into images.  This entire process is resource-intensive! Experts reco"
coverimage: "https://github.blog/wp-content/uploads/2023/02/221670941-4fc6bc8d-d6dc-4701-8cd3-92d4d8d78908.png?resize=1600%2C850"
category: "Engineering,Product,Codespaces"
englishsummary: "  GitHub Codespaces provides a powerful Integrated Development Environment (IDE) on a virtual machine, allowing developers with less powerful machines to code without draining their local resources, and can be used for a variety of tasks such as generating AI images."
summary: "GitHub Codespacesは、仮想マシン上に強力な統合開発環境（IDE）を提供し、性能の低いマシンを持つ開発者がローカルリソースを消耗せずにコーディングできるようにし、AI画像の生成など様々なタスクに利用することが可能です。"
---

<p>飛行中の飛行機でコーディングしているような気分になったことはありませんか？私が初めてコードを学んだ5年ほど前、私のノートパソコンは苦痛を感じるほど遅かったのですが、もっと良いものを買う余裕はありませんでした。そのため、私はコードを実行するために<a href="https://jsbin.com/">jsbin.com</a>のようなブラウザベースの IDE に頼っていました。</p>
<p>GitHub Codespaces は、仮想マシン上で本格的なブラウザベースの統合開発環境 (IDE) を提供します。つまり、ローカルマシンのリソースを消費することなく、コードを書くことができるのです。クラウドパワーによる開発は、マシン性能の低いユーザーにとっては画期的なことですが、GitHub Codespacesの多機能性についてはまだほんの少ししか触れていないのが現状です。</p>
<p>このブログでは、GitHub Codespacesを最大限に活用するための方法をいくつか紹介します。</p>
<h2 id="generate-ai-images-%f0%9f%8e%a8">AI画像の生成<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f3a8.png" alt="🎨" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#generate-ai-images-%f0%9f%8e%a8" class="heading-link pl-2 text-italic text-bold" aria-label="Generate AI images &#x1f3a8;"></a></h2>
<p>GitHub Codespacesで<a href="https://github.com/CompVis/stable-diffusion">Stable Diffusionを</a>実行することができます。DALL-EやMidjourneyのように、Stable Diffusionはディープラーニングを使ってテキストをアートに変換する数多くの機械学習モデルの1つです。</p>
<p>Stable Diffusionは、以下の手順でテキストをアートに変換します。</p>
<ul>
<li>AIが画像を受け取る</li>
<li>AIは、画像が全く認識できなくなるまで、画像にノイズを加える。(ノイズは、ピクセル化されたドットの別の言い方です）。</li>
<li>AIがノイズを除去し、クリアで高品質な画像を生成する</li>
<li>AIは「LAION-Aesthetics」と呼ばれるデータベースから学習する。このデータベースには画像とテキストのペアがあり、テキストを画像に変換するための学習を行っています。</li>
</ul>
<p>このプロセス全体は、リソースを大量に消費します専門家は、Stable Diffusionのようなデータの多いタスクを実行するには、強力なグラフィック・プロセッシング・ユニット（GPU）を搭載したコンピュータを使用することを推奨しています。しかし、誰もがそのような計算能力を持つコンピューターを持っているわけではないので（私も含めて）、私は代わりにGitHub Codespacesを使用しています。</p>
<p>コードスペースは仮想マシン上でホストされるので、マシンの種類を2コアから32コアまで設定することができます。より強力なマシンが必要な場合は、GPUを搭載したコードスペースへのアクセスをリクエストすることができます。つまり、機械学習エンジニアがiPadやChromebookを使って、GitHub Codespaces経由でデータ量の多い深層学習の計算を行うことができるのです。</p>
<p>私がどのようにコードスペース内でアートを生成したかについては、私の<a href="https://dev.to/github/generate-ai-art-with-github-codespaces-59fc">DEV</a>投稿と<a href="https://github.com/galaxy-bytes/codespaces-jupyter">リポジトリを</a>チェックしてみてください。</p>
<p>以下では、GitHub Codespacesで生成したコードとAI画像をご覧いただけます。</p>
<pre><code class="language-python"><br />from torch import autocast

# 画像のプロンプトをここで変更しましょう
prompt = "綿菓子の髪とピンクのドレスを着た漫画の黒人の女の子が、綿菓子の雲があるピンクの空の前に立っている"
with autocast(device):
  image = pipe(prompt, height=768, width=768).images[0].
イメージ
</code></pre>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/02/221672299-cda9af56-d8b6-4833-aed4-56ee2367edd9.png?w=880&#038;resize=880%2C791" alt="Computer-generated drawing-style image of a Black woman wearing a pink t-shirt, standing in front of a green field and some trees, with a pink cloud floating above her in the blue sky." width="880" height="791" class="aligncenter size-large wp-image-70334 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/221672299-cda9af56-d8b6-4833-aed4-56ee2367edd9.png?w=880&#038;resize=880%2C791 880w, https://github.blog/wp-content/uploads/2023/02/221672299-cda9af56-d8b6-4833-aed4-56ee2367edd9.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/221672299-cda9af56-d8b6-4833-aed4-56ee2367edd9.png?w=768 768w" sizes="(max-width: 880px) 100vw, 880px" data-recalc-dims="1" /></p>
<h2 id="manage-github-codespaces-from-the-command-line-%f0%9f%a7%91%f0%9f%92%bb">GitHub のコード空間をコマンドラインから管理する<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f9d1-200d-1f4bb.png" alt="🧑‍💻" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#manage-github-codespaces-from-the-command-line-%f0%9f%a7%91%f0%9f%92%bb" class="heading-link pl-2 text-italic text-bold" aria-label="Manage GitHub Codespaces from the command line &#x1f9d1;&#x200d;&#x1f4bb;"></a></h2>
<p>2000年代には、うっかりドキュメントを閉じてしまったり、コンピュータが突然シャットダウンしてしまったりして、せっかく作った作品が永遠に失われてしまうことがありました。幸いなことに、今は2023年、GitHub Codespacesを含め、多くのエディターがそのような事態を防いでくれています。コードスペースを閉じれば、たとえ変更をコミットし忘れたとしても作業内容が保存されます。</p>
<p>しかし、コードをリポジトリにプッシュしたからといって、コードスペースが終了したのであれば、遠慮なく削除してしまってかまいません。GitHub のコードスペース管理は、次のような理由から重要です。</p>
<ul>
<li>GitHub Codespace がたくさんあって混乱して、誤って間違ったものを削除してしまわないように。</li>
<li>デフォルトでは、アクティブでないGitHub Codespacesは30日ごとに自動的に削除されます。</li>
</ul>
<p>GitHub Codespacesは<a href="https://github.com/">GitHub UI</a>または<a href="https://cli.github.com/">GitHub CLIで</a>管理することができます。GitHub CLIでは、以下のようなことができます。</p>
<p><strong>コードスペースの作成</strong></p>
<pre><code class="language-bash">gh codespace create -r OWNER/REPO_NAME [-b BRANCH] (コードスペースの作成)
</code></pre>
<p><strong>自分のコードスペースをすべてリストアップする</strong></p>
<pre><code class="language-bash">gh コードスペースの一覧
</code></pre>
<p><strong>コードスペースを削除する</strong></p>
<pre><code class="language-bash">gh コードスペースの削除 -c CODESPACE-NAME
</code></pre>
<p><strong>コードスペースの名前を変更する</strong></p>
<pre><code class="language-bash">gh コードスペース編集 -c CODESPACE-NAME -d DISPLAY-NAME
</code></pre>
<p><strong>コードスペースのマシンタイプを変更</strong></p>
<pre><code class="language-bash">gh コード空間の編集 -m MACHINE-TYPE-NAME
</code></pre>
<p>GitHub コードスペースを CLI で管理する方法については、これですべてを網羅したわけではありません。コマンドラインからコードスペースを管理する方法については、<a href="https://docs.github.com/en/codespaces/developing-in-codespaces/using-github-codespaces-with-github-cli">こちらで</a>詳しく説明しています。</p>
<h2 id="pair-program-with-a-teammate-%f0%9f%91%a5">チームメイトとのペアプログラミング<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f465.png" alt="👥" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#pair-program-with-a-teammate-%f0%9f%91%a5" class="heading-link pl-2 text-italic text-bold" aria-label="Pair program with a teammate &#x1f465;"></a></h2>
<p>リモートで作業しているときのペアプログラミングは、なかなか難しいものです。チームメイトの隣に座っていないと、画面やコードを共有するのが難しくなります。しかし、それがうまくいけば、双方のコミュニケーションと技術的なスキルの向上につながるので、価値があるのです。Live Share エクステンションをインストールしてポートを転送すれば、GitHub Codespaces でのリモートペアプログラミングをより簡単に行えるようになります。</p>
<h3 id="share-your-forwarded-ports">転送したポートの共有<a href="#share-your-forwarded-ports" class="heading-link pl-2 text-italic text-bold" aria-label="Share your forwarded ports"></a></h3>
<p>ローカルでホストしているウェブアプリの URL を共有し、チームメイトや共同作業者がそれを使えるようにすることができます。共有したいポートを右クリックすると、ポートの可視性を "Private" から "Public" に切り替えるオプションが表示されます。ローカルアドレスの値をコピーして必要な共同作業者に共有すれば、あなたとは別の部屋にいてもローカルでホストされているウェブアプリを閲覧したりテストやデバッグをしたりすることができるようになります。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/221672569-897a86c3-4db8-4c6d-8411-af808f509162.png?w=1000&#038;resize=1000%2C512" alt="Screenshot of how to share the URL of your locally hosted web app by setting its port to public." width="1000" height="512" class="aligncenter size-large wp-image-70335 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/221672569-897a86c3-4db8-4c6d-8411-af808f509162.png?w=1000&#038;resize=1000%2C512 1000w, https://github.blog/wp-content/uploads/2023/02/221672569-897a86c3-4db8-4c6d-8411-af808f509162.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/221672569-897a86c3-4db8-4c6d-8411-af808f509162.png?w=768 768w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<h3 id="live-share">ライブシェア<a href="#live-share" class="heading-link pl-2 text-italic text-bold" aria-label="Live Share"></a></h3>
<p>Live Shareエクステンションを使えば、あなたとあなたのチームメイトが同時に同じプロジェクトに入力することができます。チームメイトのカーソルとあなたのカーソルがハイライトされるので、誰がタイピングしているのかを簡単に識別することができます。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/221673035-87e02ecf-0aad-4a86-bfe5-f8f291088ffa.png?w=1024&#038;resize=1024%2C391" alt="Screenshot of code in an editor showing sections highlighted and labeled with the names of users currently working on those lines." width="1024" height="391" class="aligncenter size-large wp-image-70336 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/221673035-87e02ecf-0aad-4a86-bfe5-f8f291088ffa.png?w=1300 1300w, https://github.blog/wp-content/uploads/2023/02/221673035-87e02ecf-0aad-4a86-bfe5-f8f291088ffa.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/221673035-87e02ecf-0aad-4a86-bfe5-f8f291088ffa.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/221673035-87e02ecf-0aad-4a86-bfe5-f8f291088ffa.png?w=1024&#038;resize=1024%2C391 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<h2 id="pair-program-with-ai-%f0%9f%a4%96">AIとのペアプログラム<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f916.png" alt="🤖" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#pair-program-with-ai-%f0%9f%a4%96" class="heading-link pl-2 text-italic text-bold" aria-label="Pair program with AI &#x1f916;"></a></h2>
<p>Visual Studio Codeのマーケットプレイスでは、GitHub<a href="https://github.com/features/copilot">Copilotを</a>はじめ、GitHub Codespacesと互換性のあるさまざまな拡張機能が提供されています。コードを書きながらアイデアを交換したいけれど、周りに誰もいないという場合は、GitHub Copilotという拡張機能をインストールして、AIとペアプログラミングをしてみてはいかがでしょうか。GitHub CopilotはAIを搭載したコード補完ツールで、コードスニペットを提案したり、コードを補完したりして、より速くコードを書くことを支援します。</p>
<p>コード補完による生産性向上だけでなく、GitHub Copilotは様々なバックグラウンドを持つ開発者に力を与えてくれます。私のお気に入りのGitHub Copilotツールの1つは、ハンズフリーで音声起動するAIプログラマーの「<a href="https://githubnext.com/projects/hey-github/">Hey, GitHub</a>」です。以下の<a href="https://youtu.be/rwN7bYhF2_Q">ビデオで</a>、"Hey, GitHub "が手先が不自由な人や視覚障害者の開発者体験をどのように向上させるかをご覧ください。</p>
<hr>
<div class="mod-vh position-relative" style="height: 0; padding-bottom: calc((9 / 16)*100%);">
			<iframe loading="lazy" class="position-absolute top-0 left-0 width-full height-full" src="https://www.youtube.com/embed/rwN7bYhF2_Q?version=3&#038;rel=1&#038;showsearch=0&#038;showinfo=1&#038;iv_load_policy=1&#038;fs=1&#038;hl=en-US&#038;autohide=2&#038;wmode=transparent" title="YouTube video player" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0"></iframe>
		</div>
<hr>
<p>GitHub Copilotのその他の使用例については、<a href="https://github.blog/2022-09-14-8-things-you-didnt-know-you-could-do-with-github-copilot/">こちらを</a>ご覧ください。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/221673157-4f0854b8-8425-42d2-b46c-0ec29da644ed.gif?w=1024&#038;resize=1024%2C600" alt="Gif demonstrating how Copilot can recommend lines of code." width="1024" height="600" class="aligncenter size-large wp-image-70337 width-fit" data-recalc-dims="1" /></p>
<h2 id="teach-people-to-code-%f0%9f%91%a9%f0%9f%8f%ab">コーディングを教える<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f469-200d-1f3eb.png" alt="👩‍🏫" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#teach-people-to-code-%f0%9f%91%a9%f0%9f%8f%ab" class="heading-link pl-2 text-italic text-bold" aria-label="Teach people to code &#x1f469;&#x200d;&#x1f3eb;"></a></h2>
<p>ブートキャンプ、教室、ミートアップ、カンファレンスなどを通じてコーディングについて教育する中で、私は、人々にコードを教えることは難しいということを学びました。ワークショップでは、参加者がフォローできるように環境を整えることにほとんどの時間を費やしてしまうこともあります。しかし、GitHub Codespacesでコーディングを教えたり、ワークショップを運営したりすることは、参加者全員にとってより良い経験を生み出します。初心者の開発者に、テンプレートを使って作業するためにリポジトリをクローンする方法を理解することを期待するのではなく、コードスペースを開いて、設定した開発環境で作業することができるのです。これで、誰もがあなたと同じ環境を持っていて、簡単にフォローできるという安心感を得ることができます。これにより、多くの時間、ストレス、混乱が軽減されます。</p>
<p>GitHub Codespaces を<a href="https://docs.github.com/en/education/manage-coursework-with-github-classroom/integrate-github-classroom-with-an-ide/using-github-codespaces-with-github-classroom">教師や学生にとって</a>より利用しやすくするために、180時間の無料利用（50人のクラスで月5回分の課題に相当）を提供しました。GitHub Codespacesの設定と、<a href="https://marketplace.visualstudio.com/items?itemName=vsls-contrib.codetour">CodeTourなどの</a>拡張機能を活用したセルフガイドのワークショップの運営に関する<a href="https://dev.to/github/how-to-run-a-frontend-workshop-in-codespaces-2ede">チュートリアルを</a>ご覧ください。</p>
<p>ハーバード大学最大のクラスであるCS50が、どのように<a href="https://www.youtube.com/watch?v=LuiqVZnOaVk">GitHub Codespacesを使って</a>学生にコードを教えているのか、ご覧ください。</p>
<h2 id="learn-a-new-framework-%f0%9f%93%9d">新しいフレームワークを学ぶ<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4dd.png" alt="📝" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#learn-a-new-framework-%f0%9f%93%9d" class="heading-link pl-2 text-italic text-bold" aria-label="Learn a new framework &#x1f4dd;"></a></h2>
<p>コードを学ぶとき、チュートリアルを追うことに時間をかけすぎてしまいがちです。チュートリアルの消費とプロジェクトの構築のバランスをとることで、学習はより効果的になることが多いのです。GitHub Codespaces のクイックスタート・テンプレートは、フレームワークを学ぶための迅速かつ効率的な方法です。</p>
<p><a href="https://github.com/codespaces/templates">クイックスタートテンプレート</a>には、Next.js, React.js, Django, Express, Ruby on Rails, Preact, Flask, Jupyter Notebookといった最も一般的なアプリケーションフレームワークの定型コード、転送ポート、設定済み開発コンテナなどが含まれています。テンプレートは、開発者に、コードスペースでアプリケーションを構築、テスト、デバッグするためのサンドボックスを提供します。ワンクリックでテンプレートを開き、新しいフレームワークで実験することができます。</p>
<p>コードスペースでフレームワークを試すことで、開発者はフレームワークの構造と機能をよりよく理解し、よりよい定着と習得につなげることができます。たとえば、私は Jupyter Notebook にはなじみがありませんが、GitHub Codespaces の Jupyter Notebook テンプレートを使ったことがあります。この定型文のおかげで、Jupyter Notebookの構造を実験し、よりよく理解することができました。このテンプレートを使って、小さな<a href="https://github.com/galaxy-bytes/codespaces-jupyter">プロジェクトも</a>作りました。</p>
<p>この<a href="https://github.blog/2023-02-22-a-beginners-guide-to-learning-to-code-with-github-codespaces/">ブログ記事と</a> <a href="https://github.com/codespaces/new?template_repository=github/codespaces-learn-with-me">テンプレートは</a>、GitHub Codespacesを使って、開発者がReactの最初の行を書くのをガイドするもので、チェックしてみてください。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=1024&#038;resize=1024%2C474" alt="Screenshot showing a list of available codespace templates." width="1024" height="474" class="aligncenter size-large wp-image-70338 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=2354 2354w, https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=1024&#038;resize=1024%2C474 1024w, https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=1536 1536w, https://github.blog/wp-content/uploads/2023/02/221677283-4458b3b7-a9e8-45b6-b7ce-508d10ed127c.png?w=2048 2048w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<h2 id="store-environment-variables-%f0%9f%94%90">環境変数の保存<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f510.png" alt="🔐" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#store-environment-variables-%f0%9f%94%90" class="heading-link pl-2 text-italic text-bold" aria-label="Store environment variables &#x1f510;"></a></h2>
<p>過去に何度か、環境変数を誤って共有したり誤操作したりしたことがありました。ここでは、私が環境変数を誤って扱ってしまった、ぞっとするような瞬間をいくつか紹介します。</p>
<ul>
<li>ライブデモで聴衆に見せてしまった。</li>
<li>環境変数をGitHubにアップロードしてしまった。</li>
<li>チームメイトと値を共有する良い方法が見つからなかった。</li>
</ul>
<p>このような事態を避けるために、GitHub の Codespaces シークレットを使うことができました。GitHub Codespaces の secret には、API Key や環境変数、秘密の認証情報などを GitHub Codespaces ごとに保存しておくことができます。</p>
<p>GitHub Codespaces secret に保存した後は、コード内で<code>process.env.{SUPER_SECRET_API_KEY}</code> のように環境変数を参照することができるようになります。</p>
<p>GitHub Codespaces で環境変数を安全に保存する方法については、こちらの<a href="https://dev.to/github/securely-store-environment-variables-with-github-codespaces-3dgc">チュートリアルを</a>参照ください。</p>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/02/221677059-55c4b91d-613b-40f4-98a7-4981d88936be.png?w=1024&#038;resize=1024%2C576" alt="Screenshot showing how to securely store your environment variables with GitHub Codespaces." width="1024" height="576" class="aligncenter size-large wp-image-70339 width-fit" srcset="https://github.blog/wp-content/uploads/2023/02/221677059-55c4b91d-613b-40f4-98a7-4981d88936be.png?w=1632 1632w, https://github.blog/wp-content/uploads/2023/02/221677059-55c4b91d-613b-40f4-98a7-4981d88936be.png?w=300 300w, https://github.blog/wp-content/uploads/2023/02/221677059-55c4b91d-613b-40f4-98a7-4981d88936be.png?w=768 768w, https://github.blog/wp-content/uploads/2023/02/221677059-55c4b91d-613b-40f4-98a7-4981d88936be.png?w=1024&#038;resize=1024%2C576 1024w, https://github.blog/wp-content/uploads/2023/02/221677059-55c4b91d-613b-40f4-98a7-4981d88936be.png?w=1536 1536w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /></p>
<h2 id="onboard-developers-faster-%f0%9f%8f%83%f0%9f%92%a8">開発者をより早く取り込む<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f3c3.png" alt="🏃" class="wp-smiley" style="height: 1em; max-height: 1em;" /><img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4a8.png" alt="💨" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#onboard-developers-faster-%f0%9f%8f%83%f0%9f%92%a8" class="heading-link pl-2 text-italic text-bold" aria-label="Onboard developers faster &#x1f3c3;&#x1f4a8;"></a></h2>
<p>一般に、ソフトウェアエンジニアはチームに参加したときに自分のローカル環境をセットアップする責任があります。ローカル環境のセットアップには、ドキュメントの質にもよりますが一日から一週間かかることもあります。幸いなことに、組織は GitHub Codespaces を使ってカスタム環境を設定し、オンボーディングプロセスを自動化することができます。新しいエンジニアがチームに参加する際、コードスペースを開くと、必要な拡張機能、依存関係、環境変数がコードスペース内に存在するため、ローカル環境のセットアップを省略することができるのです。</p>
<p>2021年、GitHubエンジニアリングチームは、GitHub.comの開発において、<a href="https://github.blog/2021-08-11-githubs-engineering-team-moved-codespaces/">macOSモデルからGitHubコードスペースに </a>移行しました。14年以上経過し、私たちのリポジトリはディスク上に約13GBを蓄積していました。リポジトリのクローン、依存関係のセットアップ、ブートストラップに約45分かかりました。GitHub Codespacesに完全に移行した後は、事前に設定された信頼性の高いコードスペースでGitHub.comを起動するのに10秒しかかかりません。</p>
<p>しかし、私たちの言葉を鵜呑みにする必要はありません。通信会社TELUSの情報サービス担当マネージャーであるKetan Shah氏は、「GitHubは新入社員のオンボーディングプロセスを丸々一日短縮してくれるんだ」と証言しています。新しい開発者は、すべてが一カ所に集まっているため、数分で作業を開始することができます」。</p>
<p>GitHub Codespacesによる開発者の迅速なオンボーディングについて、詳しくはこちらをご覧ください。</p>
<ul>
<li><a href="https://github.com/customer-stories/telus">TELUS社によるGitHub Codespacesの</a>活用方法</li>
<li><a href="https://github.com/customer-stories/elanco">Elanco社によるGitHub Codespacesの</a>利用方法</li>
<li>GitHub Codespace を使って、開発コンテナでポジティブなオンボーディング体験を構成する方法</li>
</ul>
<h2 id="conduct-technical-interviews-%f0%9f%92%bc">技術面接の実施<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/1f4bc.png" alt="💼" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#conduct-technical-interviews-%f0%9f%92%bc" class="heading-link pl-2 text-italic text-bold" aria-label="Conduct technical interviews &#x1f4bc;"></a></h2>
<p>持ち帰りのプロジェクトやテクニカルスクリーン、ライブコーディングは、ソフトウェア開発者にとって苦痛でありながらも必要な面接体験の一部となります。候補者にきちんと設定された信頼性の高い環境を提供することで、面接官は不安を軽減し、パフォーマンスを向上させることができるのです。GitHub Codespacesを使えば、候補者はもう環境のセットアップを心配する必要はありません。面接官はGitHub Codespacesを使ってリアルタイムにフィードバックを行い、Visual Studio Code Live Shareなどの組み込みツールを使ってコラボレーションを行うことができます。さらに、GitHub Codespacesは面接プロセスにおいて安全で隔離された環境を提供し、機密情報やデータの保護を保証します。</p>
<p>GitHubの様々なエンジニアリングチームが<a href="https://github.blog/2021-12-16-technical-interviews-via-codespaces/">GitHub Codespacesを使用して</a>どのように<a href="https://github.blog/2021-12-16-technical-interviews-via-codespaces/">インタビューを</a>実施しているかをご覧ください。</p>
<h2 id="code-in-the-cloud-with-your-preferred-editor-%e2%98%81%ef%b8%8f">クラウド上で好きなエディターでコーディング<img src="https://s.w.org/images/core/emoji/14.0.0/72x72/2601.png" alt="☁" class="wp-smiley" style="height: 1em; max-height: 1em;" /><a href="#code-in-the-cloud-with-your-preferred-editor-%e2%98%81%ef%b8%8f" class="heading-link pl-2 text-italic text-bold" aria-label="Code in the cloud with your preferred editor &#x2601;"></a></h2>
<p>私はVisual Studio Codeが大好きで、メインエディターとして使っています。しかし、あなたの役割や他の要因によって、異なる好みがあるかもしれません。  GitHub Codespaces は Visual Studio Code 以外にも、以下のエディタをサポートしています。</p>
<ul>
<li>Jupyter Notebook</li>
<li>IntelliJ IDEA </li>
<li>RubyMine</li>
<li>GoLand </li>
<li>PyCharm </li>
<li>PhpStorm</li>
<li>WebStorm</li>
</ul>
<h2 id="but-wait-theres-more">でも、まだあるんです<a href="#but-wait-theres-more" class="heading-link pl-2 text-italic text-bold" aria-label="But, wait, there’s more!"></a></h2>
<p>GitHub Codespacesの超能力は、どんなデバイスからでもコーディングができ、インターネットさえあれば標準化された環境を手に入れることができることです。しかし、ソフトウェア開発のワークフローをより簡単にする機能も搭載されています。GitHubユーザーは月60時間、GitHub Proユーザーは月90時間無料で利用できるので、実際に試してその良さを体験しない手はない。さあ、<a href="https://github.com/codespaces/templates">今</a>すぐ試してみませんか？</p>


