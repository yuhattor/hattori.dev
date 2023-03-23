---
title: "あいまいなブランチ名やタグ名をブロックする"
englishtitle: "Block ambiguous branch and tag names"
date: "2023-03-23"
cardurl: "https://github.blog/changelog/2023-03-23-block-ambiguous-branch-and-tag-names"
author: "Kevin Duck"
description: " GitHub blocks branch and tag names which begin with refs/ .  Under the hood, all Git refs begin with a prefix (refs/heads/ for branches and refs/tags/ for tags).  In typical use, though, users rarely see these prefixes, so they're silently handled by GitHub, the Git client, and other tools.  When a similar string is used as the beginning of the visible part of the branch or tag name, this results in ambiguity:  did the user intend refs/heads/feature or refs/heads/refs/heads/feature ?  In nearly all cases, refs/ in front of a branch or tag name is accidental and becomes a problematic surprise later.  This change blocks new introductions of such names.  Repositories with existing branches named this way can still push updates to those branches.  "
coverimage: ""
englishsummary: "  GitHub blocks branch and tag names which begin with "refs/" to avoid ambiguity and potential issues with accidental naming."
summary: "  GitHubでは、曖昧さや誤った命名による潜在的な問題を避けるため、「refs/」で始まるブランチ名やタグ名をブロックしています。"
---

<p>GitHub は<code>refs/</code> で始まるブランチ名やタグ名をブロックしています。</p>
<p>内部では、すべての Git refs はプレフィックスで始まります<code>(</code>ブランチは<code>refs/heads/</code>、タグは<code>refs/tags/</code>です)。<br />
しかし、一般的な使用では、ユーザーがこれらの接頭辞を目にすることはほとんどありません。そのため、GitHubやGitクライアント、その他のツールによって黙って処理されます。<br />
似たような文字列がブランチやタグの名前の先頭に使われると、あいまいな表現になってしまいます：<br />
ユーザーは<code>refs/heads/featureを</code>意図したのでしょうか、それとも<code>refs/heads/refs/heads/featureを</code>意図したのでしょうか？<br />
ほとんどすべての場合、ブランチ名やタグ名の前に<code>refs/が</code>あるのは偶然であり、後で問題となるサプライズとなるのです。</p>
<p>この変更により、このような名前の新規導入がブロックされます。<br />
このような名前のブランチを持つリポジトリは、そのブランチへの更新をプッシュすることができます。</p>


