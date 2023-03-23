---
title: "GitHub CLIの拡張機能「GitHub Classroom CLI」をご紹介します。"
englishtitle: "Introducing the GitHub Classroom CLI extension for the GitHub CLI"
date: "2023-03-23"
cardurl: "https://github.blog/changelog/2023-03-23-introducing-the-github-classroom-cli-extension-for-the-github-cli"
author: "Kevin Duck"
description: " We're thrilled to introduce the GitHub Classroom CLI extension for the GitHub CLI, designed to simplify the lives of teachers everywhere. With this powerful new tooling, teachers can create their own personalized workflows, as well as streamline any custom solutions they've already built.  To get started, ensure you have the GitHub CLI installed, then install the extension with the following command:  gh extension install github/gh-classroom  Command your Classroom  The GitHub Classroom CLI extension provides a suite of commands to help you navigate your classrooms and assignments with ease. Here's a quick overview of its capabilities:  gh classroom list : List all your unarchived classrooms  gh classroom view : Show the details of a classroom, such as its name, description, URL, and roster  gh classroom assignments : Display a list of assignments for a classroom  gh classroom assignment : Show the details of an assignment, such as its title, type, deadline, starter code URL, and number of submissions  gh classroom accepted-assignments : List your students' accepted assignments  gh classroom clone starter-repo : Clone the starter code for an assignment  gh classroom clone student-repos : Clone all your students' submissions for an assignment (a scriptable alternative to the Classroom Assistant desktop application)  To target a specific classroom, use the -c flag with each subc"
coverimage: ""
englishsummary: "mmand.  The GitHub Classroom CLI extension provides teachers with powerful new tooling to create personalized workflows and streamline custom solutions, enabling them to easily manage classrooms and assignments."
summary: "mmandです。  GitHub Classroom CLIエクステンションは、パーソナライズされたワークフローを作成し、カスタムソリューションを合理化するための強力な新しいツールを教師に提供し、教室や課題を容易に管理することを可能にします。"
---

<p>私たちは、GitHub<strong>CLI用のGitHub Classroom CLIエクステンションを</strong>紹介できることを嬉しく思っています。この強力なツールにより、教師は自分だけのワークフローを作成したり、すでに構築したカスタムソリューションを合理化したりすることができます。</p>
<p>まず、<a href="https://cli.github.com/">GitHub CLIが</a>インストールされていることを確認し、次のコマンドでエクステンションをインストールします：<br />
<code>gh extension install github/gh-classroom</code></p>
<h2 id="command-your-classroom" id="command-your-classroom" >教室を支配する<a href="#command-your-classroom" class="heading-link pl-2 text-italic text-bold" aria-label="Command your Classroom"></a></h2>
<p>GitHub Classroom CLI エクステンションは、教室や課題を簡単に操作するためのコマンド群を提供します。ここでは、その機能を簡単に説明します：</p>
<ul>
<li><code>gh classroom list</code>：アーカイブされていない教室をすべてリストアップする</li>
<li><code>gh 教室ビュー</code>：教室名、説明、URL、名簿など、教室の詳細を表示する</li>
<li><code>gh 教室の課題</code>教室の課題の一覧を表示する</li>
<li><code>gh教室の課題</code>です：課題のタイトル、種類、期限、スターターコードのURL、提出数など、課題の詳細を表示する</li>
<li><code>GH CLASSIC ACCEPTED-ASSIGNSIONS</code>：生徒が受理した課題をリストアップする</li>
<li><code>gh classroom clone starter-repo</code>：課題用のスターターコードをクローンする</li>
<li><code>gh classroom clone student-repos</code>：課題に対するすべての学生の提出物をクローンする（Classroom Assistantデスクトップアプリケーションのスクリプトによる代替手段）</li>
</ul>
<p>特定の教室を対象とするには、各サブコマンドで<code>-c</code>フラグを使用します（教室のIDは、<code>gh classroom lsや</code> <code>gh classroom viewで</code>選択することで取得します）。<code>c</code>フラグがない場合は、矢印キーで移動できるインタラクティブなピッカーが対象の教室を選択するのに役立ちます。</p>
<p>このサブコマンドのコレクションは、あなたの時間を節約し、ワークフローを向上させる強力な機能を提供するための私たちの旅の始まりを意味します。</p>
<p>私<a href="https://github.com/github/gh-classroom/issues">たちの公開リポジトリ</a>では、問題を報告したり、機能をリクエストしたりすることができます。</p>
<p>GitHub Classroom CLI を使って作ったものは、<a href="https://github.com/community/Global-Campus-Teachers/discussions">Global Campus for Teachers Discussions フォーラム</a>で共有してください！</p>


