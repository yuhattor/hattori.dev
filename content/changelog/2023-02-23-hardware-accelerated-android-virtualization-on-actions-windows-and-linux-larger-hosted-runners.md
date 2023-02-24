---
title: "Actions WindowsとLinuxの大規模なホストランナー上でハードウェアアクセラレーションによるAndroidの仮想化"
englishtitle: "Hardware accelerated Android virtualization on Actions Windows and Linux larger hosted runners"
date: "2023-02-23"
cardurl: "https://github.blog/changelog/2023-02-23-hardware-accelerated-android-virtualization-on-actions-windows-and-linux-larger-hosted-runners"
author: "Kevin Duck"
description: " Starting on February 23, 2023, Actions users of GitHub-hosted larger Linux runners will be able to make use of hardware acceleration for Android testing. Testing on a 4-core machine with hardware acceleration is around 2-3 times faster than not using hardware acceleration and around 2 times faster than using MacOS.  To make use of this on Linux, Actions users will need to add the runner user to the KVM user group  - name: Enable KVM group perms  run: |  echo 'KERNEL=="kvm", GROUP="kvm", MODE="0666", OPTIONS+="static_node=kvm"' | sudo tee /etc/udev/rules.d/99-kvm4all.rules  sudo udevadm control --reload-rules  sudo udevadm trigger --name-match=kvm  (Thank you gsauthof for the feedback on this!)  You will then be able to make use of hardware acceleration when making use of Android emulator actions such as reactivecircus/android-emulator-runner .  "
coverimage: ""
englishsummary: ""
summary: ""
---

<p>2023年2月23日より、GitHubがホストする<a href="https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners">大規模Linuxランナー</a>のActionsユーザーは、Androidのテストにハードウェアアクセラレーションを利用することができるようになる予定です。ハードウェアアクセラレーションを利用した4コアマシンでのテストは、ハードウェアアクセラレーションを利用しない場合に比べて約2〜3倍、MacOSを利用した場合に比べて約2倍高速になります。</p>
<p>Linuxでこれを利用するには、ActionsユーザがrunnerユーザをKVMユーザグループに追加する必要があります。</p>
<pre><code>      - name: KVMグループのパーマネントを有効にする
        を実行します。|
            echo 'KERNEL==&quot;kvm&quot;, GROUP=&quot;kvm&quot;, MODE=&quot;0666&quot;, OPTIONS+=&quot;static_node=kvm&quot;'｜すで に tee /etc/udev/rules.d/99-kvm4all.rules を実行します。
            sudo udevadm control --reload-rules
            sudo udevadm trigger --name-match=kvm</code></pre>
<p>(これについてのフィードバックをくれた<a href="https://github.com/gsauthof">gsauthof</a>に感謝します!)</p>
<p>これで、<a href="http://github.com/reactivecircus/android-emulator-runner">reactivecircus/android-emulator-runnerの</a>ようなAndroidエミュレータアクションを利用する際に、ハードウェアアクセラレーションを利用することができるようになります。</p>


