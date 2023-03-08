---
title: "Slackで特定のDiscussionカテゴリーを購読する機能を導入しました。"
englishtitle: "Introducing the ability to subscribe to specific Discussion categories on Slack"
date: "2023-03-08"
cardurl: "https://github.blog/changelog/2023-03-08-introducing-the-ability-to-subscribe-to-specific-discussion-categories-on-slack"
author: "Kevin Duck"
description: " Many users use our Slack integration to know what’s new in their repo’s Discussion. However, for large repos, these notifications can get overwhelming. Today, we’re introducing the ability to subscribe to specific Discussion categories in Slack. By default, when users subscribe to a Discussion, they subscribe to all categories. With the new command, we’re introducing a way to add category filters:  /github subscribe <org_name>/<repo_name> discussions:{category:"<category1>","<category2>"}  Users can also unsubscribe a Slack channel from previously set category filters with a similar command:  /github unsubscribe <org_name>/<repo_name> discussions:{category:"<category1>"}  Note: By default, if no category filters were added, the app will subscribe to all categories in the Discussion. Similarly, if you remove all category filters, the app will return to its default state of being subscribed to all categories. To unsubscribe from Discussions entirely, users can continue to use the unsubscribe command on Discussions, as shown below:  /github unsubscribe <org_name>/<repo_name> discussions  "
coverimage: ""
englishsummary: ""
summary: ""
---

<p>多くのユーザーは、自分のレポのディスカッションの新着情報を知るために、私たちのSlack統合を利用しています。しかし、大規模なレポの場合、これらの通知に圧倒されることがあります。今日、私たちはSlackで特定のディスカッション・カテゴリーを購読する機能を導入します。デフォルトでは、ユーザーがディスカッションに登録すると、すべてのカテゴリーに登録されます。新しいコマンドでは、カテゴリーフィルターを追加する方法を導入しています。</p>
<p><code>/github subscribe &lt;org_name&gt;/&lt;repo_name&gt; discussions:{category:&quot;&lt;category1&gt;&quot;,&quot;&lt;category2&gt;&quot;}.</code></p>
<p>また、同様のコマンドで、以前に設定したカテゴリーフィルターからSlackチャンネルの登録を解除することもできます。</p>
<p><code>/github unsubscribe &lt;org_name&gt;/&lt;repo_name&gt;ディスカッション:{category:&quot;&lt;category1&gt;&quot;}。</code></p>
<p>注：デフォルトでは、カテゴリーフィルターが追加されていない場合、アプリはディスカッションのすべてのカテゴリーにサブスクライブされます。同様に、すべてのカテゴリーフィルターを削除すると、アプリはすべてのカテゴリーに登録されるデフォルトの状態に戻ります。Discussionから完全に購読を解除するには、ユーザーは引き続き、以下のようにDiscussionのunsubscribeコマンドを使用することができます。</p>
<p><code>/github unsubscribe &lt;org_name&gt;/&lt;repo_name&gt;ディスカッション</code></p>


