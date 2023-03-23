---
title: "GitHub Secure Code Gameでセキュアなコードマインドセットを構築する。"
subtitle: "セキュアなコードを書くことは、機能的なコードを書くのと同じくらい芸術であり、質の高いコードを書くための唯一の方法です。セキュアコードゲームでは、セキュアコードマインドセットを構築できるように、コードのセキュリティ問題を発見し修正するための実践的なトレーニングを提供します。"
englishsubtitle: "Writing secure code is as much of an art as writing functional code, and it is the only way to write quality code. Learn how our Secure Code Game can provide you with hands-on training to spot and fix security issues in your code so that you can build a secure code mindset."
englishtitle: "Build a secure code mindset with the GitHub Secure Code Game"
date: "2023-03-23"
cardurl: "https://github.blog/2023-03-23-build-a-secure-code-mindset-with-the-github-secure-code-game/"
author: "Joseph Katsioloudes"
description: " Fixing security-related issues in code is a different kind of problem solving, and we often see developers introducing more problems as they try to fix these issues. I understand this because I was once one of those developers.  When I started to learn how to write functional code, I was asked to write a form that accepts user input. So, I made a form that accepts user input. I later learned that it was not enough for the code to be functional, it also needed to be secure–like adding user input validation. It was learning about this, and the attacks that could occur without this type of validation, that got me thinking about security as a developer. I learned that I didn’t always need to reinvent the wheel, and that I could instead rely on the best practices, approaches, and code from the people and communities that came before me.  It’s because of my own experiences, and helping others through my work on the GitHub Security Lab team, that I created the Secure Code Game . This hands-on secure coding training is now generally available for all GitHub users via GitHub Skills . The Secure Code Game is perfect for developers and students getting started in their coding careers, or anyone who wants to sharpen their secure-coding abilities.  The game assumes a beginner or intermediate-level of knowledge, and gets more challenging as you complete each level. To meet the needs of open"
coverimage: "https://github.blog/wp-content/uploads/2022/01/Security-Community.png?resize=1200%2C630"
category: "Education,Security,GitHub Security Lab,GitHub Skills"
englishsummary: " source developers, the game is free and open source.  Fixing security-related issues in code is a different kind of problem solving, and the Secure Code Game was created to help developers and students learn best practices and approaches to do this more"
summary: "のソース開発者であれば、このゲームは無料でオープンソースで提供されます。  セキュアコードゲームは、開発者や学生がベストプラクティスやアプローチを学ぶのを助けるために作られたものです。"
---

<p>コードに含まれるセキュリティ関連の問題を修正することは、問題解決とは異なる種類のものであり、開発者がこれらの問題を修正しようとするあまり、さらなる問題を引き起こしているのをしばしば目にします。私もかつてそのような開発者の一人だったため、このことがよくわかります。</p>
<p>関数型コードの書き方を学び始めた頃、ユーザー入力を受け付けるフォームを書くように言われました。そこで、私はユーザー入力を受け付けるフォームを作りました。しかし、機能的なコードだけでは不十分で、ユーザー入力の検証を行うなど、安全なコードであることが必要であることを、後になって知りました。このような検証を行わないと攻撃される可能性があることを知り、開発者としてのセキュリティについて考えるようになったのです。私は、常に車輪の再発明をする必要はなく、先人たちのベストプラクティスやアプローチ、コードを頼りにすることができるのだと学びました。</p>
<p>私自身の経験と、<a href="https://securitylab.github.com/">GitHub Security Lab</a>チームでの仕事を通じて他の人を助けたことが、<a href="https://github.com/skills/secure-code-game">Secure Code Gameを</a>作った理由です。この実践的なセキュアコーディングトレーニングは、GitHub<a href="https://skills.github.com/">Skillsを通じて</a>、すべてのGitHubユーザーが一般に利用できるようになりました。セキュアコードゲームは、これからコーディングを始める開発者や学生、あるいはセキュアコーディングの能力を磨きたい人に最適です。</p>
<p>このゲームは、初級または中級レベルの知識を想定しており、各レベルをクリアするごとに難易度が上がっていきます。オープンソース開発者のニーズに応え、最も人気のある2つの言語から始めるため、このゲームは現在、PythonとCの学習をサポートしています。ゲームをクリアしてフィードバックをいただくことで、このゲームを次にどのように進めていけばよいかを理解することができます。将来的には、新しいレベルを作るために、コミュニティからの貢献を歓迎することをすでに計画しています。</p>
<h2 id="the-art-of-secure-code">セキュアコードの技術<a href="#the-art-of-secure-code" class="heading-link pl-2 text-italic text-bold" aria-label="The art of secure code"></a></h2>
<p>セキュアコーディングに関しては、トレーニングギャップがあることはかなり一般的な知識であり、これにはいくつかの理由があります。1つは、一部の大学では強く推奨されているにもかかわらず、セキュアコード教育がコンピュータサイエンスの学位取得の必須条件になっていないことです。もう一つの理由は、組織内でセキュアコーディングの実践とトレーニングが十分に強調されていないため、開発者がコードを開発する際にセキュリティを優先していない可能性があることです。第三の理由は、脅威の状況が急速に変化し、脆弱性が常に進化していることです。最新の脅威とベストプラクティスを常に把握することは難しいことです。</p>
<p>また、開発者は必ずしもセキュアコーディングに興味を持たないという意見もあります。コードを書くことでクリエイティブになり、機能的なコードでセキュリティの問題を修正することは、同じ場所に留まって進歩がないように感じられます。機能的なコードを書くことで、自分が取り組んでいるプロジェクトや、自分の組織が販売している製品の問題を解決し、うまく動作することに本質的な満足感があるのです。</p>
<p>しかし、私は認識を改めたいと思います。安全なコードを書かずに品質の高いコードを書くことはできませんし、安全なコードを書くことは別の形の問題解決なのです。ハッカーやセキュリティ研究者は、自分たちをコードの問題を見つけるクリエイターだと考えています。なぜなら、問題を見つけ、それを悪用し、その影響を理解するためには、創造的思考と実験が必要だからです。もちろん、悪意を持ったハッカーもいますが、自分たちのコードという芸術を次のレベルに引き上げると考える人も少なくありません。開発者として、高品質のコードを確実に出荷したいのであれば、セキュアコードのアートの基本を学ぶ必要があるのです。</p>
<h2 id="gamification-for-a-secure-code-mindset">セキュアコードマインドセットのためのゲーミフィケーション<a href="#gamification-for-a-secure-code-mindset" class="heading-link pl-2 text-italic text-bold" aria-label="Gamification for a secure code mindset"></a></h2>
<p>セキュアコーディングの基本を学ぶことは、完璧を目指すことではなく、自分のコードにセキュリティ上の問題やバグがないかどうかを確認する際の意識付けをすることなのです。GitHubのハンズオン型セキュアコードゲームは、まさにこれを実現するために作られたものです。このゲームでは、セキュアコードのベストプラクティスと理論を学び、学びながら実践できるようにします。</p>
<p>このゲームでは、意図的に脆弱なコードを提供し、その中の問題を発見して修正するよう求めます。そのコードを実行することで、修正したコードが正しく機能しているか、安全な方法で機能しているかを評価することができます。ここから、脆弱なコードに組み込まれたエクスプロイトに対して、あなたの修正を評価することができます。事前に書き込まれた脆弱性が悪用できなくなれば、次のレベルに進む準備が整ったことになります。レベルは、ゲームが進むにつれて、クリアするのが難しくなります。<a href="https://codeql.github.com/">CodeQLの</a>ようなアプリケーションセキュリティテストツールを使用して、ゲームの後半の段階ですべての脆弱性を見つけ、それらの問題の場所と修正方法について役立つヒントを受け取ることをお勧めします。</p>
<p>GitHub Skills 内の Secure Code Game を始めるには、<a href="https://github.com/skills/secure-code-game">ここをクリックして</a>ください。ゲームに貢献することに興味がある方は、<a href="mailto:securitylab-social@github.com">ぜひ</a>ご連絡をお待ちしています。</p>


