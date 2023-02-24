---
title: "二要素認証の望ましい方法と設定の改善"
englishtitle: "Preferred 2FA methods and settings improvements"
date: "2023-02-22"
cardurl: "https://github.blog/changelog/2023-02-22-preferred-2fa-methods-and-settings-improvements"
author: "Kevin Duck"
description: " The Primary field on two-factor authentication methods has been removed, and replaced with a Preferred option. This new option sets your preferred 2FA method for account login and use of the sudo prompt. You can choose between TOTP, SMS, security keys, or GitHub Mobile as your preferred 2FA method.  Additionally, you can now update your 2FA methods inline at https://github.com/settings/security , rather than going through the initial 2FA setup flow again.  With this change, device-specific preferences for 2FA have been removed – each login will always default to your preferred method. If you previously set a default on one of your devices, your most recent choice has been copied to your account-wide preference. Otherwise, no preference will be set, and GitHub will select from your available second factors in this order: security keys, GitHub Mobile, TOTP, and then SMS.  To learn more, see "Changing your preferred two-factor authentication method" and "Configuring two-factor authentication" .  "
coverimage: "https://i0.wp.com/user-images.githubusercontent.com/1666363/219820201-6fe7f80a-cb6b-4bb9-bd56-984ed917e6a5.png?ssl=1"
englishsummary: ""
summary: ""
---

<p>2要素認証方法の<code>プライマリ</code>フィールドが削除され、<code>プリファレンス</code>オプションに置き換えられました。この新しいオプションは、アカウントへのログインと sudo プロンプトの使用について、優先する 2FA メソッドを設定します。優先する2FA方式は、TOTP、SMS、セキュリティキー、GitHub Mobileから選択することができます。</p>
<p>さらに、最初の二要素認証設定フローを再度通過するのではなく、<a href="https://github.com/settings/security">https://github.com/settings/security</a>、インラインで二要素認証方式を更新することができるようになりました。</p>
<p><img decoding="async" src="https://i0.wp.com/user-images.githubusercontent.com/1666363/219820201-6fe7f80a-cb6b-4bb9-bd56-984ed917e6a5.png?ssl=1" alt="image" data-recalc-dims="1"></p>
<p>この変更により、デバイスごとに設定されていた2FAの設定は削除され、各ログインは常にお好みの方法がデフォルトで使用されます。以前、デバイスの1つにデフォルトを設定した場合、その最新の設定がアカウント全体の設定にコピーされます。そうでない場合は、設定されず、GitHub は利用可能な 2 つ目の要素から、セキュリティキー、GitHub Mobile、TOTP、SMS の順に選択します。</p>
<p>詳しくは、<a href="https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/changing-your-preferred-two-factor-authentication-method">&quot;二要素認証の優先方法を変更する&quot;</a>と<a href="https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication">&quot;二要素認証を設定する&quot;</a> をご覧ください。</p>


