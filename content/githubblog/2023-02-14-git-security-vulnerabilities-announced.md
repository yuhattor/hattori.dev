---
title: "Gitのセキュリティ脆弱性を発表"
subtitle: "特に、信頼できないパッチやリポジトリに対して `git apply` や `git clone` を使っている場合は、最新のバージョンにアップグレードすることが推奨されます。"
englishsubtitle: "Git users are encouraged to upgrade to the latest version, especially if they use `git apply` or `git clone` against untrusted patches or repositories."
englishtitle: "Git security vulnerabilities announced"
date: "2023-02-14"
cardurl: "https://github.blog/2023-02-14-git-security-vulnerabilities-announced-3/"
author: "Taylor Blau"
description: " Today, the Git project released new versions to address a pair of security vulnerabilities, (CVE-2023-22490 and CVE-2023-23946 ) that affect versions 2.39.1 and older. These affect Git’s local clone optimization, as well as git apply , respectively.  CVE-2023-22490  When cloning a repository, Git selects and uses a transport mechanism appropriate for the URL scheme of your clone. When cloning a local repository, however, Git instead uses a separate local clone optimization copying files directly from the source to destination.  A specially-crafted repository can trick Git into using its local clone optimization when using a non-local transport. Git will abort clones from repositories whose $GIT_DIR/objects directory contains a symbolic link. However, the top-level $GIT_DIR/objects directory may itself be a symbolic link.  These two may be combined to include arbitrary files based on known paths from a victim’s filesystem into the clone’s working copy, allowing for data exfiltration in a similar manner as CVE-2022-39253 .  [source ]  CVE-2023-23946  Git allows for applying arbitrary patches to your repository’s history with git apply . In order to prevent malicious patches from creating files outside of the working copy, git apply rejects patches which attempt to write a file beyond a symbolic link.  However, this mechanism can be tricked when the malicious patch creates that s"
coverimage: "https://github.blog/wp-content/uploads/2022/01/Security-Open-Source-Product.png?resize=1200%2C630"
category: "Open Source,Security,Git"
englishsummary: " ymbolic link, allowing the patch to write a file outside the working copy.  The Git project released new versions to address two security vulnerabilities, CVE-2023-22490 and CVE-2023-23946, which affect versions"
summary: "ymbolic link を使用し、パッチが作業コピーの外部にファイルを書き込むことを可能にします。  Gitプロジェクトは、2つのセキュリティ脆弱性、CVE-2023-22490とCVE-2023-23946に対応する新しいバージョンをリリースし、その影響はバージョン"
---

<p>本日、Git プロジェクトは、バージョン 2.39.1 以降に存在するセキュリティ脆弱性<a href="https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q">(CVE-2023-22490</a>および<a href="https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh">CVE-2023-23946</a>) に対応した新バージョンを<a href="https://lore.kernel.org/git/xmqqr0us5dio.fsf@gitster.g/T/#u">リリース</a>しました。それぞれ、Gitのローカルクローンの最適化、および<code>git applyに</code>影響を及ぼします。</p>
<h2 id="cve-2023-22490">CVE-2023-22490<a href="#cve-2023-22490" class="heading-link pl-2 text-italic text-bold" aria-label="CVE-2023-22490"></a></h2>
<p>リポジトリをクローンするとき、Git はクローンの URL スキームに適した<a href="https://git-scm.com/docs/gitcore-tutorial#_merging_external_work">トランスポート機構を</a>選択して使用します。しかし、ローカルリポジトリをクローンする場合、Git は代わりに別の<a href="https://git-scm.com/docs/git-clone/2.39.1#Documentation/git-clone.txt---local">ローカルクローン</a>最適化を使い、コピー元からコピー先まで直接ファイルをコピーします。</p>
<p>特別に作られたリポジトリは、ローカルでないトランスポートを使うときにローカルクローン最適化を使うようにGitをだますことができます。Gitは、<code>$GIT_DIR/objects</code>ディレクトリにシンボリックリンクが含まれるリポジトリからのクローンを中断します。しかし、トップレベルの<code>$GIT_DIR/objects</code>ディレクトリは、それ自体がシンボリックリンクである可能性があります。</p>
<p>この2つを組み合わせることで、被害者のファイルシステムから既知のパスに基づいた任意のファイルをクローンの作業コピーに含めることができ、<a href="https://github.com/git/git/security/advisories/GHSA-3wp6-j8xr-qw85">CVE-2022-39253</a> と同様の方法でデータを流出させることが可能です。</p>
<p><a href="https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q">[ソース］</a></p>
<h2 id="cve-2023-23946">CVE-2023-23946<a href="#cve-2023-23946" class="heading-link pl-2 text-italic text-bold" aria-label="CVE-2023-23946"></a></h2>
<p>Git では、<code>git apply</code> でリポジトリの履歴に任意のパッチを適用することができます。悪意のあるパッチが作業コピーの外にファイルを作成するのを防ぐために、<code>git apply</code>はシンボリックリンクを越えてファイルを書き込もうとするパッチを拒否します。</p>
<p>しかし、悪意のあるパッチがそのシンボリックリンクを最初に作ってしまうと、この仕組みがだまされてしまうことがあります。これを利用して、信頼できないソースから悪意のあるパッチを適用すると、被害者のファイルシステム上に任意のファイルを書き込むことができます。</p>
<p><a href="https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh">[ソース］</a></p>
<h2 id="upgrade-to-the-latest-git-version">Gitの最新バージョンにアップグレードする<a href="#upgrade-to-the-latest-git-version" class="heading-link pl-2 text-italic text-bold" aria-label="Upgrade to the latest Git version"></a></h2>
<p>これらの脆弱性から保護する最も効果的な方法は、Git 2.39.2 にアップグレードすることです。すぐにアップデートできない場合は、以下のステップを踏んでリスクを減らしてください。</p>
<ul>
<li>信頼できないリポジトリに対して<code>git clone</code>を<code>--recurse-submodules</code>付きで実行しないようにする。</li>
<li>信頼できないリポジトリからの入力に対して<code>git apply</code>/<code>git am</code>を実行しないようにします。 </li>
</ul>
<p>ワークフローでサブモジュールが必要な場合は、各<code>.gitmodules</code>ファイルに疑わしいモジュールの URL が含まれていないことを確認した上で、サブモジュールの各レイヤーを繰り返しクローンすることができます。</p>
<p>パッチを適用しても安全かどうかわからない場合は、<code>git apply --stat</code> でパッチの内容を調べます。シンボリックリンクとその先にあるファイルを作成するようなパッチを適用するのは避けましょう。</p>
<p>これらの攻撃からユーザーを守るために、GitHubは積極的な措置をとっています。具体的には、以下の通りです。</p>
<ul>
<li><a href="https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q">CVE-2023-22490</a>および<a href="https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh">CVE-2023-23946において</a>、GitHub.comが攻撃のベクトルとして使用されることを防ぐための緩和策を実施しました。</li>
<li>本脆弱性の悪用を防止するGitHub Desktopのリリースを本日2月14日以降に予定しています。</li>
<li>GitHub CodespacesとGitHub Actionsに、Gitのバージョンをアップするためのアップデートを予定。</li>
<li>GitHub Enterprise Serverに、パッチを適用したバージョンのGitのアップデートを予定しています。</li>
</ul>
<p><a href="https://github.com/git/git/security/advisories/GHSA-gw92-x3fm-3g3q">CVE-2023-22490</a>のクレジットは yvvdwf に、<a href="https://github.com/git/git/security/advisories/GHSA-r87m-v37r-cwfh">CVE-2023-23946</a>のクレジットは GitLab の Joern Schneeweisz に帰属します。この修正は、GitHub の Taylor Blau 氏と GitLab の Patrick Steinhardt 氏がそれぞれ行い、さらに git-security メンバがフィードバックとレビューを行っています。</p>
<div class="post-content-cta"><p><a href="https://git-scm.com/">Git 2.39.2 のダウンロード</a></p>
</div>


