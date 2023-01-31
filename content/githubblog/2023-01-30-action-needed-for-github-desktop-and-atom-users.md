---
title: "GitHub DesktopとAtomをご利用の方に必要な対応について"
subtitle: "2月2日までに GitHub DesktopとAtomのバージョンをアップデートしてください。"
englishsubtitle: "Update to the latest version of Desktop and previous version of Atom before February 2."
englishtitle: "Action needed for GitHub Desktop and Atom users"
date: "2023-01-30"
cardurl: "https://github.blog/2023-01-30-action-needed-for-github-desktop-and-atom-users/"
author: "Alexis Wales"
description: "On December 7, 2022, GitHub detected unauthorized access to a set of repositories used in the planning and development of GitHub Desktop and Atom . After a thorough investigation, we have concluded there was no risk to GitHub.com services as a result of this unauthorized access and no unauthorized changes were made to these projects."
coverimage: "https://github.blog/wp-content/uploads/2022/08/Security-Product@2x.png?resize=1600%2C850"
category: "Security,Atom,GitHub Desktop"
---

<p>2022年12月7日、GitHubは<a href="https://desktop.github.com/">GitHub Desktop</a>および<a href="https://github.blog/2022-06-08-sunsetting-atom/">Atomの</a>企画・開発で使用されている一連のリポジトリへの不正アクセスを検知しました。徹底的な調査の結果、この不正アクセスによるGitHub.comのサービスへのリスクはなく、これらのプロジェクトに不正な変更は加えられていないと結論付けました。</p>
<p>暗号化されたコード署名証明書一式が流出しましたが、この証明書はパスワードで保護されており、悪意を持って使用された形跡はありません。予防措置として、GitHub Desktop および Atom アプリケーションで使用されている公開された証明書を失効させます。これらの証明書を取り消すことにより、GitHub Desktop for MacおよびAtomの一部のバージョンが無効になります。</p>
<p>これらのバージョンのGitHub Desktop for Macは、2月2日に動作しなくなります。<a href="https://docs.github.com/en/desktop/installing-and-configuring-github-desktop/installing-and-authenticating-to-github-desktop/updating-github-desktop">最新バージョンの Desktop にアップデートして</a>ください。</p>
<ul>
<li>3.1.2</li>
<li>3.1.1</li>
<li>3.1.0</li>
<li>3.0.8</li>
<li>3.0.7</li>
<li>3.0.6</li>
<li>3.0.5</li>
<li>3.0.4</li>
<li>3.0.3</li>
<li>3.0.2</li>
</ul>
<p>GitHub Desktop for Windows への影響はございません。</p>
<p>これらのバージョンのAtomも2月2日に動作が停止します。Atom を使い続けるには、ユーザーは<a href="https://github.com/atom/atom/releases/tag/v1.60.0">以前の Atom バージョンをダウンロード</a>する必要があります。</p>
<ul>
<li>1.63.1</li>
<li>1.63.0</li>
</ul>
<h2 id="what-happened">何が起こったか<a href="#what-happened" class="heading-link pl-2 text-italic text-bold" aria-label="What happened"></a></h2>
<p>2022年12月6日、私たちの<code>atom</code>、<code>desktop</code>、およびその他の非推奨のGithub所有組織のリポジトリが、マシンアカウントに関連する漏洩したPAT (Personal Access Token)によってクローンされました。2022年12月7日に発見されると、当社チームは直ちに漏洩した認証情報を失効させ、顧客および内部システムへの潜在的な影響の調査を開始しました。影響を受けたリポジトリには、お客様のデータは含まれていませんでした。</p>
<p>しかし、これらのリポジトリには、当社のGitHub DesktopおよびAtomリリースのワークフローでActionを介して使用するための暗号化されたコードサイニング証明書が複数保管されていました。脅威者がこれらの証明書を解読または使用できたという証拠はありません。</p>
<p>証明書は、コードがリストされた作者によって作成されたことを確認するために使用され、<a href="https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits">GitHub上のコミットに署名</a>するのと非常によく似ています。これらの証明書は、既存の Desktop および Atom アプリのインストールを危険にさらすものではありません。しかし、復号化されると、脅威者はこれらの証明書で非公式なアプリケーションに署名し、それらがGitHubによって公式に作成されたように装うことができるようになります。</p>
<p>2022年12月6日時点でも有効な証明書は、Windowsで使用されているDigicertコードサイニング証明書2枚と、Apple Developer ID証明書1枚の計3枚でした。<strong>GitHubは2023年2月2日に3つの証明書をすべて失効</strong>させる予定です。</p>
<ul>
<li>1つのDigicert証明書は2023年1月4日に期限切れとなり、2つ目の証明書は2023年2月1日に期限切れとなる予定です。有効期限が切れると、これらの証明書はコードの署名に使用できなくなります。これらは継続的なリスクにはなりませんが、予防措置として、2月2日に失効させる予定です。</li>
<li>Apple Developer ID証明書は、2027年まで有効です。私たちはAppleと協力して、2月2日に証明書が失効されるまで、公開された証明書で署名された新しい実行ファイル（アプリケーションなど）がないか監視しています。</li>
</ul>
<p>2023年1月4日、私たちはDesktopアプリの新バージョンを公開しました。このバージョンは、脅威者に公開されていない新しい証明書で署名されています。</p>
<h2 id="impact-to-github-com">GitHub.comへの影響<a href="#impact-to-github-com" class="heading-link pl-2 text-italic text-bold" aria-label="Impact to GitHub.com"></a></h2>
<p>漏洩したリポジトリの内容を調査した結果、上記の特定の証明書以外、GitHub.comやその他の提供物への影響は認められませんでした。また、これらのリポジトリにあるコードに不正な変更は加えられていません。</p>
<h2 id="how-github-responded-to-protect-our-users">ユーザー保護のためのGitHubの対応について<a href="#how-github-responded-to-protect-our-users" class="heading-link pl-2 text-italic text-bold" aria-label="How GitHub responded to protect our users"></a></h2>
<p>本日、<strong>Atom アプリ 1.63.0-1.63.1 の最新 2 バージョンをリリースページより削除</strong>しました。証明書が失効されると、これらのバージョンは機能しなくなります。<a href="https://github.com/atom/atom/releases/tag/v1.60.0">以前のAtomリリースは</a>、<a href="https://github.blog/2022-06-08-sunsetting-atom/#if-im-using-atom-what-changes-can-i-expect-after-the-sunset">日没のガイダンスに従って</a> <a href="https://github.com/atom/atom/releases/tag/v1.60.0">ダウンロード</a>することができます。</p>
<p>2023年2月2日（木）に、<strong>Desktop app バージョン 3.0.2-3.1.2 および Atom バージョン 1.63.0-1.63.1 に署名するために使用された Mac および Windows 署名証明書を失効</strong>させます。これらの証明書が無効になると、これらの証明書で署名されたすべてのバージョンは機能しなくなります。ワークフローの中断を避けるため、2月2日までに<a href="https://desktop.github.com/">Desktop のアップデートと</a> <a href="https://github.com/atom/atom/releases/tag/v1.60.0">Atom のダウングレードを</a>行うことを強くお勧めします。</p>
<p>GitHubと広範な開発者エコシステムのセキュリティと信頼性は、私たちの最優先事項です。GitHub DesktopとAtomの使用を継続するために、ユーザーの皆様には上記の推奨事項を実行されることをお勧めします。</p>


