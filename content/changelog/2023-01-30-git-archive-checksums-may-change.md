---
title: "Git Archive のチェックサムが変更される可能性があります"
englishtitle: "Git archive checksums may change"
date: "2023-01-30"
cardurl: "https://github.blog/changelog/2023-01-30-git-archive-checksums-may-change"
author: "Kevin Duck"
description: "The default compression for Git archives has recently changed ."
coverimage: ""
---

<p><a href="https://github.com/git/git/commit/4f4be00d302bc52d0d9d5a3d4738bb525066c710">最近</a>、Git アーカイブのデフォルト圧縮が<a href="https://github.com/git/git/commit/4f4be00d302bc52d0d9d5a3d4738bb525066c710">変更</a>されました。<br />
そのため、GitHub からダウンロードしたアーカイブは、中身が全く変わらないにもかかわらず、チェックサムが異なる場合があります。</p>
<p>GitHubは、自動生成されたアーカイブのチェックサムの安定性を保証していません。<br />
これらは、リリースタブにある「ソースコード（zip）」や「ソースコード（tar.gz）」という言葉でマークされています。<br />
一貫したチェックサムに依存する必要がある場合は、アーカイブを直接GitHub Releasesにアップロードすることができます。<br />
これらは変更されないことが保証されています。</p>


