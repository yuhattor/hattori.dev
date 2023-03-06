---
title: "devコンテナとGitHub Codespacesで開発環境を自動化する方法"
subtitle: "GitHub Codespacesは、devコンテナと組み合わせることで、より早くコーディングを開始することができます。GitHub Codespacesを使ってオープンソースプロジェクトにdevコンテナを追加し、開発環境の一部を自動化する方法をご紹介します。"
englishsubtitle: "GitHub Codespaces enables you to start coding faster when coupled with dev containers. Learn how to automate a portion of your development environment by adding a dev container to an open source project using GitHub Codespaces."
englishtitle: "How to automate your dev environment with dev containers and GitHub Codespaces"
date: "2023-03-06"
cardurl: "https://github.blog/2023-03-06-how-to-automate-your-dev-environment-with-dev-containers-and-github-codespaces/"
author: "Kedasha Kerr"
description: " When I started my first role as a software engineer, I remember taking about four days to set up my local development environment. I had so many issues with missing dependencies, incorrect versions, and failed installations. When I finally finished setting up all the tools and software I needed to be a productive member of the team, I cloned one of our repositories to my machine, set up my environment variables, ran npm run dev and received so many errors because I forgot to install the dependencies (and read the README) or switch to the right node version. Ugh! I can’t tell you how many times this happened to me in my first year!  Back then, I wished I had a way that was streamlined—something I set up only once, that just worked every time I accessed the repository. Although I did learn how to automate my computer setup with a Brewfile, I wish I could just get to coding in a repository without thinking about configuration.  source  When I think about how we work on projects in a repository, I realize that many of the processes we need to get started on that project can be automated with the help of dev containers, in this case, by using a devcontainer.json file and Codespaces.  Let’s take a look at how we can automate our dev environment by adding a dev container to this open source project—Tech is Hiring in GitHub Codespaces.  For a TLDR of this post, GitHub Codespaces enabl"
coverimage: "https://github.blog/wp-content/uploads/2023/03/automate-header.png?resize=1200%2C630"
category: "Engineering,Product,Codespaces"
englishsummary: "se users to automate their dev environment set up with the help of dev containers."
summary: "は、devコンテナの助けを借りて、開発環境のセットアップを自動化することができます。"
---

<p>ソフトウェアエンジニアとして最初の仕事を始めたとき、ローカル開発環境のセットアップに4日ほどかかったのを覚えています。依存関係の欠如、不正確なバージョン、インストールの失敗など、多くの問題がありました。チームの生産的なメンバーになるために必要なツールやソフトウェアのセットアップがようやく終わったとき、私たちのリポジトリの1つを自分のマシンにクローンして環境変数を設定し、<code>npm run devを</code>実行すると、依存関係のインストール（およびREADMEを読む）または正しいnodeバージョンへの切り替えを忘れていたために多くのエラーを受け取りました。うっ!このようなことが1年目に何度あったことか!</p>
<p>当時は、合理的な方法、つまり、一度セットアップするだけで、リポジトリにアクセスするたびに動作するような方法があればいいなと思いました。Brewfileで<a href="https://gh.io/automate-with-brewfile">コンピュータのセットアップを自動化 </a>する方法を学びましたが、設定を考えずにリポジトリでコーディングできるようになればと思います。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/image2.gif" alt="Gif from the animated show Spongebob Squarepants of a character picking up a computer as if to toss it away, saying &quot;I&#039;ll show you automated.&quot;"><br />
<small><em><a href="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTEyZThjNjUzNTYyNzZkOGFjMGIyOWQ0ODA4YjU0MzQyZTBlOGYyNCZjdD1n/l1KtYG8BndKBmWrM4/giphy.gif">ソース</a></em></small></p>
<p>リポジトリにあるプロジェクトにどのように取り組むかを考えると、そのプロジェクトを始めるために必要なプロセスの多くは、devコンテナ、この場合はdevcontainer.jsonファイルとCodespacesの助けを借りて自動化できることに気づきます。</p>
<p>それでは、このオープンソースプロジェクト「Tech<a href="https://github.com/TechIsHiring/techishiring-website">is Hiring</a>in GitHub Codespaces」にdevコンテナを追加することで、開発環境を自動化する方法を見てみましょう。</p>
<blockquote><p>
  GitHubのCodespacesは、DevContainerと組み合わせることで、より速くコーディングを開始することができるようになります。その概要については、以下の画像をご覧ください。
</p></blockquote>
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image1.png?w=940&#038;resize=940%2C788" alt="Image of a table entitled &quot;Start coding faster with Codespaces.&quot; The left column is labeled &quot;Old Way&quot; and the right column is labeled &quot;New Way.&quot; The rest of this blog post will enumerate the items listed in the image." width="940" height="788" class="aligncenter size-large wp-image-70522 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image1.png?w=940&#038;resize=940%2C788 940w, https://github.blog/wp-content/uploads/2023/03/image1.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/image1.png?w=768 768w" sizes="(max-width: 940px) 100vw, 940px" data-recalc-dims="1" /></p>
<p>さて、定義を整理しておきましょう。</p>
<h3 id="what-is-github-codespaces">GitHub Codespacesとは？<a href="#what-is-github-codespaces" class="heading-link pl-2 text-italic text-bold" aria-label="What is GitHub Codespaces?"></a></h3>
<p>GitHub<a href="https://gh.io/codepaces">Codespacesは</a>、クラウド上の開発環境です。仮想マシン上で動作する隔離された環境（Dockerコンテナ）で、GitHubによってホストされています。仮想マシンやDockerコンテナについてよく知らない方は、以下のビデオを見てください：<a href="https://www.youtube.com/watch?v=N5gworNCJuY">仮想マシンとは</a>何か、<a href="https://www.youtube.com/watch?v=jPdIRX6q4jA">Dockerコンテナとは</a>何か。</p>
<p>現在、個人の開発者は1ヶ月に60時間、コードスペースを無料で使用することができるので、ぜひこの素晴らしさを利用して、どこからでもビルドできるようにしましょう。</p>
<h3 id="what-are-dev-containers">Devコンテナとは何ですか？<a href="#what-are-dev-containers" class="heading-link pl-2 text-italic text-bold" aria-label="What are dev containers?"></a></h3>
<p>開発用<a href="https://containers.dev/">コンテナでは</a>、あらかじめ設定された隔離された環境（コンテナ）でコードを実行することができます。開発環境をリポジトリにあらかじめ定義しておくことで、設定ファイルに悩まされることなく、一貫性のある信頼性の高い環境を利用することができます。</p>
<h3 id="what-is-the-devcontainer-json-file">devcontainer.jsonファイルとは何ですか？<a href="#what-is-the-devcontainer-json-file" class="heading-link pl-2 text-italic text-bold" aria-label="What is the devcontainer.json file?"></a></h3>
<p><code>devcontainer.json</code>ファイルは、プロジェクトのビルド、表示、実行の方法を定義する文書です。簡単に言うと、開発環境に必要な動作を指定することができるのです。例えば、VS CodeでESLint拡張をインストールすることを含む<code>devcontainer.json</code>ファイルがあれば、ワークスペースを開くと、ESLintが自動的にインストールされます。</p>
<h2 id="automating-your-workflow-with-dev-containers-and-github-codespaces">開発コンテナとGitHub Codespacesでワークフローを自動化する<a href="#automating-your-workflow-with-dev-containers-and-github-codespaces" class="heading-link pl-2 text-italic text-bold" aria-label="Automating your workflow with dev containers and GitHub Codespaces"></a></h2>
<p>GitHub Codespacesを使い始めるにあたって、<code>devcontainer.json</code>ファイルをセットアップする必要はありません。GitHub Codespaces のデフォルトでは、膨大な数の言語やツールに対応した<a href="https://github.com/devcontainers/images/blob/main/src/universal/.devcontainer/devcontainer.json">ユニバーサル dev コンテナイメージが</a>使用されています。つまり、<code>devcontainer.json</code>ファイルがない状態で新しいコードスペースを開くと、コードスペースが自動的にロードされ、すぐにコーディングできるようになります。しかし、<code>devcontainer.j</code>sonファイルを追加することで、開発環境のワークフローの多くを自分好みに自動化できるようになります。</p>
<blockquote><p>
  さて、ここまではお喋りでしたが、ここからは皆さんが本当に求めているものをご紹介します。
</p></blockquote>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/image8.gif" alt="Gif of the character Mary Poppins pinching shut the mouth of her talking umbrella handle and telling it, &quot;The will be quite enough of that, thank you.&quot; She then opens the umbrella and floats away."><br />
<small><em><a href="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTA0ZTg4OGZkYjNhYmYyOGU5MjFhZTAzMmNmMTFlM2RhYzQyNTgxZSZjdD1n/bRBufdofrX9e0/giphy-downsized.gif">根源</a></em></small></p>
<p>オープンソースプロジェクト「<em>Tech is Hiring</em>」を使って、ローカルの開発環境を使って、通常どのようにリポジトリを使って作業するのかを説明します。</p>
<h2 id="what-work-typically-looks-like">通常、どのような作業をするのか<a href="#what-work-typically-looks-like" class="heading-link pl-2 text-italic text-bold" aria-label="What work typically looks like"></a></h2>
<p>一見したところ、このプロジェクトでは、Nextjs、Tailwind CSS、Chakra UI、TypeScript、Storybook、Vite、Cypress、Axios、Reactjsが依存関係として使われていることがわかります。このプロジェクトを実行するためには、これらの依存関係をすべてローカルマシンにインストールする必要があります。</p>
<ol>
<li>リポジトリをクローンして、プロジェクトにcdしてみましょう。
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/image5.gif" alt="Gif of the terminal output as the Tech is Hiring repository is cloned." data-recalc-dims="1"></p>
</li>
<li>
<p>次に、ローカルでプロジェクトを実行するための依存関係をインストールしましょう。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/image6.gif" alt="Gif showing terminal output as the necessary dependencies are installed."></p>
</li>
<li>
<p>このプロジェクトはstorybookを使っているので、storybookと実際のアプリの両方をローカルで動かしてみましょう。</p>
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/image7-1.gif" alt="Gif of the user&#039;s desktop with a terminal app running commands."></p>
</li>
</ol>
<p>プロセスはそれほど悪くはないのですが、少し時間がかかりました。また、正しいnodeのバージョンを使っているかどうか、環境変数が必要かどうか、解決すべきランタイムエラーがあるかどうかなどを確認する必要があります。幸いなことに、この作業中にエラーが発生することはありませんでしたが、それでも少し時間がかかりました。</p>
<h2 id="going-faster-with-github-codespaces-and-dev-containers">GitHub Codespacesと開発用コンテナで高速化する<a href="#going-faster-with-github-codespaces-and-dev-containers" class="heading-link pl-2 text-italic text-bold" aria-label="Going faster with GitHub Codespaces and dev containers"></a></h2>
<p>このプロジェクトに<code>devcontainer.json</code>ファイルを追加して GitHub Codespaces で開き、何が起こるか確認することで、プロセスをより良いものにしましょう。</p>
<p>VS Codeのコマンドパレットを使って既存のdevコンテナを追加するか、設定ファイルを自分で書くか（これは後述します）、どちらかです。</p>
<ol>
<li>まず、プロジェクトのルートに<code>.devcontainer</code>フォルダを作成し、新しいフォルダに<code>devcontainer.json</code>ファイルを作成しましょう。
<p><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image3.png?w=612&#038;resize=612%2C142" alt="Creating a a `.devcontainer` folder in the root of the project and a `devcontainer.json` file in the new folder. " width="612" height="142" class="aligncenter size-large wp-image-70528 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image3.png?w=612&#038;resize=612%2C142 612w, https://github.blog/wp-content/uploads/2023/03/image3.png?w=300 300w" sizes="(max-width: 612px) 100vw, 612px" data-recalc-dims="1" /></p>
</li>
<li>
<p>では、依存関係のインストール、開発サーバーの起動、localhost:3000でのアプリのプレビューの開始、vscode拡張のインストールを自動化してみましょう。すべての設定が完了したら、jsonファイルは<a href="https://gh.io/example-devcontainer">次の</a>ようになります。</p>
<pre><code>{
  // 使用されている画像
   "イメージ "です。"mcr.microsoft.com/devcontainers/universal:2" となります。
  // 最小のcpuを設定する
   "hostRequirements "という。{
       "cpus "です。4
   },
   // 依存関係をインストールし、アプリを起動する
   "updateContentCommand "です。"npm install "です。
   "postAttachCommand "です。"npm run dev",
   // コンテナが構築されたらapp.tsxを開く
   "customizations "という。{
       "codespaces "という。{
           "openFiles "です。[
               "src/pages/_app.tsx "とする。
           ]
       },
       // いくつかのvscode拡張をインストールする
       "vscode "という。{
           "エクステンション "です。[
               "dbaeumer.vscode-eslint "です。
               "github.vscode-pull-request-github "です。
               "eamodio.gitlens "です。
               "christian-kohler.npm-intellisense "です。
           ]
       }
   },
   // リモートサーバーに接続する
   "forwardPorts "です。[3000],
   // ポートにラベルを付けて、アプリのプレビューを開きます。
   "portsAttributes "という。{
      "3000":{
         "ラベル "です。"アプリケーション"。
         "onAutoForward "です。"openPreview "の場合
       }
     }
}
</code></pre>
<blockquote><p>
  補足：このファイルでは、各プロパティの前にコメントを付けることで、その目的を分解しています。各プロパティの詳細については、<a href="https://containers.dev/implementors/json_reference/">container.dev</a>.で引き続きお読みください。また、不要な拡張機能をいくつかインストールしましたが、拡張機能のインストールも自動化できることをお見せしたかったのです
</p></blockquote>
</li>
<li>このファイルをコミットしてメインブランチにマージし、GitHub Codespacesでプロジェクトを開いてみましょう。
<p><img decoding="async" src="https://github.blog/wp-content/uploads/2023/03/image4.gif" alt="Committing a file, merging it to the main branch, and then opening GitHub Codespaces."></p>
<p>GitHub Codespaces でアプリケーションを開くと、依存関係がインストールされてサーバーが起動し、プレビューが自動的に開かれます。このリポジトリで作業するために環境変数が必要な場合は、GitHubの<a href="https://docs.github.com/en/codespaces/managing-your-codespaces/managing-encrypted-secrets-for-your-codespaces">リポジトリシークレットとして</a>すでに設定されているはずです。また、私たちのマシンに大量の<code>node_moduleを</code>インストールする必要もありませんでした。</p>
</li>
</ol>
<p>これを勝利と呼ぶ!</p>
<h2 id="comparing-both-ways">両方の方法を比較する<a href="#comparing-both-ways" class="heading-link pl-2 text-italic text-bold" aria-label="Comparing both ways"></a></h2>
<p>開発環境を自動化するために、devコンテナとGitHub Codespacesを使ってできることはまだまだたくさんあります。しかし、GitHub Codespacesとdevコンテナの助けを借りて、今やったことをまとめてみましょう。</p>
<ul>
<li>GitHubのリポジトリでGitHub Codespacesのボタンをクリックしました。</li>
<li>GitHubリポジトリでGitHub Codespacesボタンをクリックしました。</li>
<li>私たちは仕事に取り掛かり、コーディングを開始しました。 </li>
</ul>
<p>さて、これで良いのでしょうか？</p>
<h2 id="wrapping-up">まとめ<a href="#wrapping-up" class="heading-link pl-2 text-italic text-bold" aria-label="Wrapping up"></a></h2>
<p>では、GitHub Codespaces の何が重要で、なぜ開発者として気にする必要があるのでしょうか。ひとつは、リポジトリにアクセスするために必要な起動処理のほとんどを自動化できることです。また、開発用コンテナを使えば、開発環境をより多くカスタマイズすることができます。次回のブログでは、<code>devcontainer.json</code>ファイルの構造について説明しますから<a href="https://containers.dev/implementors/json_reference/">お楽しみに</a>。</p>
<p>2つ目は、どこからでもコーディングができることです。私は、あるサイドプロジェクトに別のマシンでアクセスできないのが嫌なのですが、そのマシンはそのプロジェクトにぴったり合うように設定されているからです。GitHub Codespacesを使えば、<strong>ボタンを</strong>クリックするだけで、モダンなブラウザをサポートする<strong>どのマシンからでも</strong> <strong>コーディングを始める</strong>ことができます。</p>
<p>ぜひ今日<a href="https://gh.io/try-codespaces">からGitHub Codespacesを</a>使い始めて、自分のプロジェクトにdevcontainer.jsonファイルを追加してみてください。きっと後悔はしないはずです。</p>
<p>それではまた次回、ハッピーコーディング</p>


