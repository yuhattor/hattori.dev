---
title: "WindowsとLinux の Larger Hosted Runner におけるハードウェアアクセラレーションをしたAndroidの仮想化"
englishtitle: "Hardware accelerated Android virtualization on Actions Windows and Linux larger hosted runners"
date: "2023-02-23"
cardurl: "https://github.blog/changelog/2023-02-23-hardware-accelerated-android-virtualization-on-actions-windows-and-linux-larger-hosted-runners"
author: "Kevin Duck"
description: ""
coverimage: ""
englishsummary: ""
summary: ""
---

<p>2023年2月23日より、GitHubがホストする<a href="https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners">大規模Linuxランナー</a>のActionsユーザーは、Androidのテストにハードウェアアクセラレーションを利用することができるようになる予定です。ハードウェアアクセラレーションを利用した4コアマシンでのテストは、ハードウェアアクセラレーションを利用しない場合に比べて約2〜3倍、MacOSを利用した場合に比べて約2倍高速になります。</p>
<p>Linuxでこれを利用するには、ActionsユーザがrunnerユーザをKVMユーザグループに追加する必要があります。</p>

```yaml
- name: Enable KVM group perms
  run: |
    echo 'KERNEL=="kvm", GROUP="kvm", MODE="0666", OPTIONS+="static_node=kvm"' | sudo tee /etc/udev/rules.d/99-kvm4all.rules
    sudo udevadm control --reload-rules
    sudo udevadm trigger --name-match=kvm
```

<p>(これについてのフィードバックをくれた<a href="https://github.com/gsauthof">gsauthof</a>に感謝します!)</p>
<p>これで、<a href="http://github.com/reactivecircus/android-emulator-runner">reactivecircus/android-emulator-runner</a>のようなAndroidエミュレータアクションを利用する際に、ハードウェアアクセラレーションを利用することができるようになります。</p>
