---
title: "古くなったコードスキャン設定を削除して、古いアラートを閉じる"
englishtitle: "Delete stale code scanning configurations to close outdated alerts"
date: "2023-03-10"
cardurl: "https://github.blog/changelog/2023-03-10-delete-stale-code-scanning-configurations-to-close-outdated-alerts"
author: "Kevin Duck"
description: " Code scanning configurations can now be deleted from the code scanning alert page. This could be used to delete stale configurations causing alerts to remain open, or delete old configurations which are no longer used.  Code scanning can be configured to use different tools, target different languages, or even analyze different parts of the codebase in the same repository. In certain circumstances more than one of these configurations may produce the same alert. However, if one of the configurations is no longer used and becomes 'stale' you may find that the alert is fixed in one configuration but not in the stale configuration, which is potentially confusing. Today we are releasing a new feature that allows you to easily delete stale configurations which cause alerts to remain open after they've been fixed.  In the code scanning alert page, the counter in the 'Affected branches' sidebar shows the number of configurations for the branch. Click a branch to view the configuration details, and delete configurations as required. A configuration is deleted for a branch, so may have an impact on the status of other alerts on the same branch. When a configuration is deleted, a timeline entry is recorded on the alert, and repositories in an organization also record an audit log entry. If a configuration is deleted by mistake, re-run the analysis to update the alert and reinstate the c"
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/19343236/223517268-8f0be686-e61e-4615-9e86-ddb259293001.png?ssl=1"
englishsummary: "  Today, a new feature has been released that enables users to delete code scanning configurations from the code scanning alert page, which can help resolve issues caused by stale configurations and delete old configurations that are no longer used."
summary: "  本日、コードスキャン警告ページからコードスキャン設定を削除できる新機能がリリースされ、古くなった設定に起因する問題の解決や、使わなくなった古い設定を削除することができるようになりました。"
---

<p>コードスキャン警告ページでコードスキャン設定を削除できるようになりました。これは、アラートが開いたままになっている古い設定を削除したり、使われなくなった古い設定を削除したりするために使用されます。</p>
<p>コードスキャンは、異なるツールの使用、異なる言語のターゲット、あるいは同じリポジトリ内のコードベースの異なる部分を分析するように設定することができます。特定の状況下では、これらの構成のうち2つ以上が同じアラートを生成することがあります。  しかし、ある構成が使用されなくなり「古くなった」場合、ある構成ではアラートが修正され、古くなった構成では修正されないということがあり、混乱を招く可能性があります。今日、私たちは、アラートが修正された後に開かれたままになる原因となる「古い設定」を簡単に削除できる新機能をリリースします。</p>
<p>コードスキャンアラートページの「影響を受けるブランチ」サイドバーのカウンターは、ブランチのコンフィギュレーション数を表示します。ブランチをクリックすると、構成の詳細が表示され、必要に応じて構成が削除されます。ブランチの構成が削除されると、同じブランチの他のアラートのステータスに影響を与える可能性があります。構成が削除されると、アラートにタイムラインエントリーが記録され、組織内のリポジトリにも監査ログエントリーが記録されます。構成が誤って削除された場合、分析を再実行してアラートを更新し、構成を復活させます。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/19343236/223517268-8f0be686-e61e-4615-9e86-ddb259293001.png?ssl=1" alt="Delete code scanning configurations" data-recalc-dims="1"></p>
<p><a href="https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/managing-code-scanning-alerts-for-your-repository#removing-stale-configurations-and-alerts-from-a-branch">古くなったコードスキャンの構成とアラートを削除</a>する方法について、詳しくはこちらをご覧ください。</p>


