---
title: "Grafana AlertingチームがGitHub Projectsで課題管理をスケールアップする方法"
subtitle: "GrafanaのArmand Grilletから、彼のチームがGitHub Projectsをどのように利用しているかを聞くことができます。"
englishsubtitle: "Hear from Grafana’s Armand Grillet about how his team uses GitHub Projects."
englishtitle: "How the Grafana Alerting team scales their issue management with GitHub Projects"
date: "2023-03-15"
cardurl: "https://github.blog/2023-03-15-how-the-grafana-alerting-team-scales-their-issue-management-with-github-projects/"
author: "Mario Rodriguez"
description: " At GitHub you’ve heard us talk about how we are using GitHub Projects and GitHub Actions to plan and track our work and now we’ve asked one of our customers, Grafana Labs, to share how their teams are approaching work in a new way. Whether they are managing open source requests, operational tasks, or escalations, the Grafana Labs Alerting team uses GitHub Projects to manage all these issues efficiently.  Let’s hear more from Armand Grillet , Senior Engineering Manager at Grafana Labs, including how his teams use tasklists to break work into manageable tasks, use a common set of labels to filter tasks, create multiple views on a single project to meet the needs of different teams and stakeholders, and use automation to enable engineers to stay focused on the code.  Grafana is a leading open source platform for monitoring and observability, which is why the Grafana Labs GitHub organization is the center of our engineering efforts with nearly 1,000 repositories, including six having more than 2,000 stars. In addition to this open source work, Grafana Labs engineers take care of the Grafana Cloud observability platform and its customers’ escalations.  As the manager of the Grafana Alerting and service-level objectives (SLOs) backend teams at Grafana Labs it was essential to have one project board that benefited our multiple stakeholders: team members, other employees, and the open"
coverimage: "https://github.blog/wp-content/uploads/2022/06/Engineering-Product@2x.png?resize=1600%2C850"
category: "Engineering,Product,GitHub Actions,GitHub Issues,GitHub Projects"
englishsummary: " source community.  Grafana Labs uses GitHub Projects to manage open source requests, operational tasks, and escalations efficiently, with tasklists, labels, multiple views, and automation to meet the needs of different stakeholders."
summary: "ソースコミュニティです。  Grafana Labsは、GitHub Projectsを利用して、オープンソースのリクエスト、運用タスク、エスカレーションを効率的に管理し、タスクリスト、ラベル、複数のビュー、自動化により、さまざまな関係者のニーズに対応します。"
---

<div class="content-table-wrap"><table style="border: 1px black">
<tbody>
<tr>
<td>GitHubでは、GitHub ProjectsとGitHub Actionsを使ってどのように仕事を計画し追跡しているかという話を聞いたことがあると思いますが、今回は私たちの顧客の1つであるGrafana Labsに、彼らのチームが新しい方法で仕事に取り組んでいる様子を紹介してもらいました。オープンソースのリクエスト、運用タスク、エスカレーションなど、Grafana LabsのアラートチームはGitHub Projectsを使ってこれらの問題をすべて効率的に管理しています。
</td>
</tr>
</tbody>
</table></div>
<p style="margin: 20px; min-height: 175px;"><img decoding="async" class="width-fit alignright wp-image-64708 size-thumbnail" style="border-radius: 50%;" src="https://github.blog/wp-content/uploads/2023/03/armand.jpeg?resize=150%2C150" alt="Headshot photograph of Armand Grillet, a white male with short brownish hair and a short beard wearing round tortoise shell glasses." width="150" height="150" align="left" data-recalc-dims="1" /> から詳しく聞いてみましょう。 <a href="https://github.com/armandgrillet"><strong>アルマン・グリレ</strong></em></a>彼のチームがどのように<strong>タスクリストを</strong>使用して作業を管理可能なタスクに分割し、<strong>共通のラベルセットを</strong>使用してタスクをフィルタリングし、異なるチームや利害関係者のニーズを満たすために単一のプロジェクトで<strong>複数のビューを</strong>作成し、エンジニアがコードに集中できるように<strong>自動化を</strong>使用しているのか、Grafana Labsのシニアエンジニアリングマネージャーが紹介しました。</p>
<hr>
<p>Grafanaはモニタリングと観測性のための主要なオープンソースプラットフォームです。そのため、<a href="https://github.com/grafana">Grafana Labs GitHub組織は</a>、2,000以上のスターを持つ6つを含む約1,000のリポジトリで私たちのエンジニアリング活動の中心となっています。このオープンソースの仕事に加えて、Grafana Labsのエンジニアは、<a href="https://grafana.com/products/cloud/">Grafana Cloudの</a>観測可能なプラットフォームとその顧客のエスカレーションを担当しています。</p>
<p>Grafana Labsの<a href="https://grafana.com/products/alerting/">Grafana Alertingと</a>サービスレベル目標（SLO）バックエンドチームのマネージャーとして、チームメンバー、他の従業員、オープンソースコミュニティといった複数のステークホルダーに利益をもたらす1つのプロジェクトボードを持つことが不可欠でした。<a href="https://github.com/orgs/grafana/projects/52">私たちのGitHubプロジェクトは</a>、まさにそれを実現する機会を提供してくれました。また、「<a href="https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/copying-an-existing-project">コピーを</a>作成する」機能を使えば、<strong> <a href="https://github.com/orgs/grafana/projects/52">私たちのボードの</a>コピーを作成</strong>し、自分のプロジェクトのニーズに合わせてアレンジすることもできます。</p>
<h2 id="one-view-for-each-team-assembled-around-task-lists">タスクリストを中心に組み立てられた各チームの1つのビュー<a href="#one-view-for-each-team-assembled-around-task-lists" class="heading-link pl-2 text-italic text-bold" aria-label="One view for each team, assembled around task lists"></a></h2>
<figure id="attachment_70749"  class="wp-caption aligncenter mx-0"><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image1-6.png?w=1024&#038;fit=1024%2C1024" alt="" class="width-fit size-large wp-image-70749 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image1-6.png?w=1999 1999w, https://github.blog/wp-content/uploads/2023/03/image1-6.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/image1-6.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/image1-6.png?w=1024&#038;fit=1024%2C1024 1024w, https://github.blog/wp-content/uploads/2023/03/image1-6.png?w=1536 1536w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /><figcaption class="text-mono color-fg-muted mt-14px f5-mktg">Grafana Alertingプロジェクトでは、"バックエンド"、"フロントエンド"、"UX"、"ドキュメント "という4つのチームがそれぞれビューを持っています。</figcaption></figure>
<p>Grafana Alertingには、バックエンド、フロントエンド、UX、docsという4つのチームにまたがって働く貢献者がいます。これらの貢献者タイプはそれぞれ、私たちのプロジェクトで独自のビューを持っています。フィールドのオプション（したがってカラム）は、これらのビューのそれぞれで同じです。</p>
<ul>
<li><strong>Inbox-</strong>レビューされて<strong>いません</strong></li>
<li><strong>入力待ち-</strong>詳細が必要な<strong>オープン</strong>ソースの課題 </li>
<li><strong>バックログレビュー済み</strong>、設定されたマイルストーンに応じた優先度</li>
<li><strong>進行中</strong></li>
<li><strong>レビューで</strong></li>
<li><strong>完了</strong></li>
</ul>
<p>これらのカラム（カスタムフィールド）は、意図的に汎用的なものです。課題がコミュニティの誰かによって書かれたのか、社内の誰かによって書かれたのかに関係なく、すべてのチームで使用することができます。私たちは、「area/frontend」のようなラベルに基づくプロジェクトフィルターを使用して、課題がプロジェクトに追加されると自動的に正しいビューに追加されるようにしています。</p>
<figure id="attachment_70750"  class="wp-caption aligncenter mx-0"><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image2-6.png?w=1024&#038;fit=1024%2C1024" alt="Big issues that we work on over a quarter use tasklists to breakdown the main pieces of work." class="width-fit size-large wp-image-70750 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image2-6.png?w=1999 1999w, https://github.blog/wp-content/uploads/2023/03/image2-6.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/image2-6.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/image2-6.png?w=1024&#038;fit=1024%2C1024 1024w, https://github.blog/wp-content/uploads/2023/03/image2-6.png?w=1536 1536w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /><figcaption class="text-mono color-fg-muted mt-14px f5-mktg">四半期に渡って取り組む大きな課題では、タスクリストを使用して、主な作業内容を細分化しています。</figcaption></figure>
<div class="content-table-wrap"><table style="border: 1px black">
<tbody>
<tr>
<td><em>注：タスクリストは現在プライベートベータ版です。<a href="https://github.com/features/preview">GitHubの機能プレビューポータルから</a>アクセスできるように組織にサインアップすることができます。</em>
</td>
</tr>
</tbody>
</table></div>
<p>大きな課題については、<a href="https://docs.github.com/en/issues/tracking-your-work-with-issues/about-tasklists">GitHubのタスクリスト</a>機能を利用して、作業をタスクに分解しています。ラベルを使って、関連するチームのビューに含まれるようにタスクをフィルタリングしています。こうすることで、2つの異なる、しかし有用な情報を提供するビューができあがります。例えば、docsチームの場合。</p>
<ul>
<li><em>type</em>/docs "というラベルが付いた小さな課題は、docsチームが取り組むべき課題です。</li>
<li>type/docs "のラベルと<em>追加</em>領域のラベル（例えば "area/frontend"）が付いたタスクリストを含む大きな課題は、docsチームに依存している課題ですが、そのアイテムは "docs "が所有しているわけではありません。このような大きな問題については、ステータスが「進行中」であれば、docsチームの誰かが、自分たちがどのように手助けできるかを確認し始めるべきです。 </li>
</ul>
<p>バックエンドチームのマネージャーであり、Grafana Alertingのプロジェクトリーダーである私にとって、このワークフローは安心感を与えてくれるものです。ドキュメントチームのメンバーがミーティングを欠席しても、エンジニアが課題のステータスを管理しているので、プロジェクトのドキュメントビューは常に正確です。</p>
<p>4つのチームビューと、四半期全体の大きな課題を一覧表示する「Epics」ビュー（ボードの最初のビュー）を組み合わせることで、誰もがGrafana Alertingで私たちの進捗を確認することができます。Grafana Labsの組織の一員であるGitHubユーザーはすべての課題を見ることができますが、私たちのコミュニティ内のGithubユーザーは公開リポジトリにある課題しか見ることができません。私たちの課題のほとんどは<a href="https://github.com/grafana/grafana">Grafanaのパブリックリポジトリに</a>あるので<a href="https://github.com/grafana/grafana">、これは</a>デフォルトで透明であることを可能にします。</p>
<p>運用業務に関連する課題にはプライベートリポジトリを使用していますが、プロジェクトフィルターを簡単に使用できるように、アラート関連の<em>すべての</em>リポジトリで同じラベルを使用しています。多くのリポジトリで共通のラベルを持つことで、他のリポジトリ、特に新しいリポジトリでも、たとえそれがアラートに関係なくても、同じラベルを持つ動機付けになります。このように共通性が高まることで、複数のリポジトリにまたがる課題の検索が容易になり、特に当社のプロダクトマネージャーにとって有用です。</p>
<h2 id="custom-fields-to-create-tailored-views">カスタムフィールドでカスタマイズされたビューを作成<a href="#custom-fields-to-create-tailored-views" class="heading-link pl-2 text-italic text-bold" aria-label="Custom fields to create tailored views"></a></h2>
<p>GitHub Projectsの貴重な機能は、ビューごとに異なるカラム<a href="https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields">（カスタムフィールド</a>）を持つことができることです。これにより、小さな課題だけでなく、四半期全体をカバーする大きな課題も表示することができるようになりました。私たちのチームは、通常の課題と比較して速いペースで作業されるエンジニアリングのエスカレーションも扱っています。</p>
<p>チームとして、私たちは3つのカスタムフィールドを用意しています。</p>
<ul>
<li><strong>ステータス</strong>：エスカレーションを除くすべての課題のデフォルトフィールドです（前述のとおり）。</li>
<li><strong>クォーター</strong>：タスクリストを含む大きな課題に使用します。</li>
<li><strong>エスカレーション</strong>：各エスカレーションの詳細なステータスを取得するために使用します。</li>
</ul>
<p>これらのカスタムフィールドを使用すると、四半期ごとの目標を俯瞰できるエピックビューや、エンジニアリング作業が必要なエスカレーションの状態を確認できるエスカレーションビューなど、カスタムビューを作成することができます。</p>
<figure id="attachment_70751"  class="wp-caption aligncenter mx-0"><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image4-6.png?w=1024&#038;fit=1024%2C1024" alt="" class="width-fit size-large wp-image-70751 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image4-6.png?w=1999 1999w, https://github.blog/wp-content/uploads/2023/03/image4-6.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/image4-6.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/image4-6.png?w=1024&#038;fit=1024%2C1024 1024w, https://github.blog/wp-content/uploads/2023/03/image4-6.png?w=1536 1536w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /><figcaption class="text-mono color-fg-muted mt-14px f5-mktg">エスカレーションビューでは、エスカレーションステータスのカスタムフィールドに "Waiting for release" などの特別な値を設定して使用しています。</figcaption></figure>
<p>GitHub Projects の適応性のおかげで、通常の課題、大きな課題、エスカレーションを参照するための「真実の情報源」がようやくひとつになりました。</p>
<h2 id="enhancing-projects-with-github-actions">GitHub Actionsでプロジェクトを強化する<a href="#enhancing-projects-with-github-actions" class="heading-link pl-2 text-italic text-bold" aria-label="Enhancing projects with GitHub Actions"></a></h2>
<p>また、解決が急がれるエスカレーションについては、<a href="https://github.com/features/actions">GitHub Actionsを使って</a>Slackで通知したり、優先度の高いエスカレーションであれば<a href="https://grafana.com/products/oncall/">Grafana OnCallを</a>使ったりしています。</p>
<p><a href="https://github.blog/2023-01-19-how-github-coordinates-product-releases-with-github-projects-and-github-actions/">GitHub ProjectsとGitHub Actionsを組み合わせると</a>、無限の可能性が広がります。<a href="https://github.com/github/issue-labeler">github/issue-labeler</a>のようなアクションでは、異なるチームが共有するリポジトリに、課題で使用されるキーワードに応じて自動的にラベルが付けられる課題を置くことができます。これらのラベルは、他のアクションによって、課題を正しいビューに追加したり、外部システムに通知を送信するために使用されます。プロジェクトを開いて、新しい関連する課題が自動的に追加され、トリアージの準備が整っているのを見ると、まるで魔法のようだと感じます。</p>
<figure id="attachment_70752"  class="wp-caption aligncenter mx-0"><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image3-4.png?w=1024&#038;fit=1024%2C1024" alt="" class="width-fit size-large wp-image-70752 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image3-4.png?w=1462 1462w, https://github.blog/wp-content/uploads/2023/03/image3-4.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/image3-4.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/image3-4.png?w=1024&#038;fit=1024%2C1024 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /><figcaption class="text-mono color-fg-muted mt-14px f5-mktg">grafana/support-escalations "に、"alerting "と "prio/3 "というラベルの課題がサポートによって作成されています。これにより、適切なプロジェクトに課題が追加され、GitHub Actionsを介してSlackの現在のオンコールに通知されます。</figcaption></figure>
<p>お客様からリクエストされた機能に関連するエスカレーションがよく発生します。オープンソースの課題からエスカレーションにリンクさせることで、エンジニアとプロダクトマネージャーが一つのプラットフォームで一緒に優先順位を決めることができ、この情報は社外のGitHubユーザーには秘密にすることができます。</p>
<p>これらの自動化は、エンジニアのモチベーションや私たちの生産性の面でも重要な役割を担っています。例えば、Grafana Alertingチームには、サポートから1週間に5件程度のエスカレーションに関する問題が寄せられます。2022年の最後の四半期には、自動化によってエンジニアがこの作業の優先順位を決める動機付けがなされたため、どの時間帯でも、チームの未解決のエスカレーションは平均で4件しかありませんでした。これは、GitHub ProjectsとGitHub Actionsに移行する前の平均20件のオープンエスカレーションから大幅に減少しています。</p>
<figure id="attachment_70753"  class="wp-caption aligncenter mx-0"><img decoding="async" loading="lazy" src="https://github.blog/wp-content/uploads/2023/03/image5-3.png?w=1024&#038;fit=1024%2C1024" alt="Flow chart showing the origins and routes that an item can take on its way to ending up in a GitHub project." class="width-fit size-large wp-image-70753 width-fit" srcset="https://github.blog/wp-content/uploads/2023/03/image5-3.png?w=1200 1200w, https://github.blog/wp-content/uploads/2023/03/image5-3.png?w=300 300w, https://github.blog/wp-content/uploads/2023/03/image5-3.png?w=768 768w, https://github.blog/wp-content/uploads/2023/03/image5-3.png?w=1024&#038;fit=1024%2C1024 1024w" sizes="(max-width: 1000px) 100vw, 1000px" data-recalc-dims="1" /><figcaption class="text-mono color-fg-muted mt-14px f5-mktg">GitHub ProjectsとGitHub Actionsを組み合わせることで、さまざまなソースからのフィードバックを、最も関連性の高いリポジトリを通して、1つのプロジェクトにルーティングすることができるようになりました。</figcaption></figure>
<h2 id="github-projects-at-scale">GitHub Projectsのスケール<a href="#github-projects-at-scale" class="heading-link pl-2 text-italic text-bold" aria-label="GitHub Projects at scale"></a></h2>
<p>GitHub Projectsを使い始めてから、私たちのチームはどんどん大きくなっています。私たちのスケーリングにおいて重要な出来事は、SLOに取り組むチームのために新しいプロジェクトを作ったことです。もともとこのチームにはエスカレーションがなく、エンジニアの数も少なかった。アラート」プロジェクトの<a href="https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/copying-an-existing-project">コピーを</a>簡単に作ることができ、新しいチームのリポジトリに対応するためにフィルターも変更しました。重要なのは、大きなチームのために用意したワークフローが、このような新しいチームにとって過大なものにならないかということでした。答えは「はい」でした。ビューの数が多すぎて、不要なオーバーヘッドが発生していましたが、新しいチームのニーズに合わせてビューの数を減らすことは非常に簡単でした。SLOチームの出発点として既存のプロジェクトを使用することで、新しいプロジェクトを素早く立ち上げることができました。</p>
<p>GitHub Projectsを1年間使ってみて、Grafana Labsのさまざまなタイプの問題に対応し、さまざまなチームのニーズに適応する能力があることがわかりました。GitHub Projectsは、エンジニアがコードに集中できるようにし、課題をより可視化する柔軟な計画・追跡ソリューションであることがわかりました。GitHub Projectsは、貢献者の負担を低く抑える一方で、管理者がチームの取り組みを理解し計画するために必要なビューを提供します。GitHub Projects は、Grafana Alerting チームがプロジェクト計画を立てるために必要な唯一のツールです。</p>


