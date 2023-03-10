---
title: "GitHub Actions - 必要なワークフローを改善しました。"
englishtitle: "GitHub Actions – Required workflows improvements"
date: "2023-03-10"
cardurl: "https://github.blog/changelog/2023-03-10-github-actions-required-workflows-improvements"
author: "Kevin Duck"
description: " Today, we are adding a couple of new improvements to required workflows in GitHub Actions.  Blocking direct push: Direct pushes are now blocked on branches of the repositories where required workflows are enforced. To push to a branch where required workflows are enforced at the organizational level, create a pull request to make the necessary changes. If you want to allow direct pushes for a particular repository, you must remove the repository as a target from respective required workflows.  Ability to configure required workflows from refs: Required workflows can now be referenced using any branch, tag, or commit SHA from the repository containing the workflow file, during its configuration. This helps you to freeze your required workflow file to a fully validated golden version and gives you the flexibility to move to latest version after testing it thoroughly. The branch, tag, or commit can be specified in the workflow path text field similar to how it is specified for actions within a workflow yaml.  Link to Documentation  Note: Required workflows is currently in beta.  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/58063491/217733287-c275b763-4980-4545-967c-ff21d132349d.png?ssl=1"
englishsummary: "  GitHub Actions has added new improvements to required workflows that block direct pushes to certain branches and allows users to configure required workflows from refs."
summary: "  GitHub Actionsは、特定のブランチへの直接プッシュをブロックする必須ワークフローに新たな改良を加え、ユーザーがrefsから必須ワークフローを設定できるようにしました。"
---

<p>本日、GitHub Actionsの<a href="https://docs.github.com/en/actions/using-workflows/required-workflows">必須ワークフローに</a>いくつかの新しい改善点を追加します。</p>
<ul>
<li><strong>ダイレクトプッシュをブロックする</strong>必須ワークフローが適用されているリポジトリのブランチでは、ダイレクトプッシュがブロックされるようになりました。組織レベルで必須ワークフローが施行されているブランチにプッシュするには、プルリクエストを作成し、必要な変更を行います。特定のリポジトリに対してダイレクトプッシュを許可したい場合は、それぞれの必須ワークフローからターゲットとしてそのリポジトリを削除する必要があります。
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/58063491/217733287-c275b763-4980-4545-967c-ff21d132349d.png?ssl=1" alt="Block direct push PR" data-recalc-dims="1"></p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/58063491/217755595-9be258c6-9153-4af4-be3c-3074e60e85a0.png?ssl=1" alt="Block direct push CI" data-recalc-dims="1">
</li>
<li><strong>参照元から必要なワークフローを設定できるようになりました。</strong>ワークフローを構成する際に、ワークフローファイルを含むリポジトリから任意のブランチ、タグ、またはコミット SHA を使用して、必要なワークフローを参照できるようになりました。これにより、必要なワークフローファイルを完全に検証されたゴールデンバージョンに固定し、十分にテストした後に最新バージョンに移行する柔軟性を提供することができます。ブランチ、タグ、またはコミットは、ワークフロー yaml 内のアクションに指定される方法と同様に、ワークフロー パス テキスト フィールドに指定できます。
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/17287148/223700823-bc684392-46c9-4859-a50a-704d5342872d.png?ssl=1" alt="Required workflows ref" data-recalc-dims="1">
</li>
</ul>
<p><a href="https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#configuring-a-required-workflow-for-your-organization">ドキュメントへのリンク</a></p>
<p>注）必須ワークフローは現在ベータ版です。</p>


