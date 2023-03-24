---
title: "GitHubのアクション：SBOMがmacOS用のホストされたランナーイメージリリースに添付されるようになりました。"
englishtitle: "GitHub Actions: SBOMs are now attached to hosted runner image releases for macOS"
date: "2023-03-24"
cardurl: "https://github.blog/changelog/2023-03-24-github-actions-sboms-are-now-attached-to-hosted-runner-image-releases-for-macos"
author: "Kevin Duck"
description: " In addition to Ubuntu & Windows , GitHub Actions now attaches a SBOM (Software Bill of Materials) to hosted runner image releases for macOS. In the context of GitHub Actions hosted runners, an SBOM details the software pre-installed on the virtual machine that is running your Actions workflows. This is useful in the situation where there is a vulnerability detected, you will be able to quickly tell if you are affected or not. If you are building artifacts, you can include this SBOM in your bill of materials for a comprehensive list of everything that went into creating your software.  To check out the new files, head over to the runner-images repository release page now or check out our docs for more information.  "
coverimage: ""
englishsummary: "  GitHub Actions now attaches a SBOM (Software Bill of Materials) to hosted runner image releases for macOS, which is useful for quickly determining if a vulnerability is present and for creating a comprehensive bill of materials for artifacts."
summary: "  GitHub Actionsでは、macOS向けのホスト型ランナーイメージリリースにSBOM（ソフトウェア部品表）を添付するようになりました。これは、脆弱性の有無を迅速に判断し、成果物の包括的な部品表を作成するために便利です。"
---

<p><a href="https://github.blog/changelog/2022-12-16-github-actions-sboms-now-attached-to-hosted-runner-image-releases-for-ubuntu-windows/">UbuntuとWindowsに</a>加え、GitHub ActionsはmacOS用のホステッドランナーイメージリリースにSBOM（Software Bill of Materials）を添付するようになりました。GitHub Actionsのホストランナーのコンテキストでは、SBOMは、Actionsワークフローを実行している仮想マシンにプリインストールされているソフトウェアの詳細を示します。これは、脆弱性が検出された状況で、影響を受けるかどうかがすぐに分かるようになるため、便利です。アーティファクトを構築する場合、このSBOMを部品表に含めると、ソフトウェアを作成するために必要なすべてのものの包括的なリストが作成できます。</p>
<p>新しいファイルをチェックするには、今すぐ<a href="https://github.com/actions/runner-images/releases">runner-images</a>リポジトリのリリースページにアクセスするか、詳細については私たちの<a href="https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions">ドキュメントを</a>チェックしてください。</p>


