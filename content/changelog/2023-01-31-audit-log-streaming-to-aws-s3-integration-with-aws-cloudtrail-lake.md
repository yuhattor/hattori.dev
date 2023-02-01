---
title: "AWS CloudTrail Lake を使った監査ログの AWS S3 インテグレーション"
englishtitle: "Audit log streaming to AWS S3 integration with AWS CloudTrail Lake"
date: "2023-01-31"
cardurl: "https://github.blog/changelog/2023-01-31-audit-log-streaming-to-aws-s3-integration-with-aws-cloudtrail-lake"
author: "Kevin Duck"
description: "In January 2022, GitHub announced audit log streaming to AWS is generally available . By streaming the audit log for your enterprise , enterprises benefit from:"
coverimage: ""
---

<p>2022年1月、GitHubは<a href="https://github.blog/changelog/2022-01-20-audit-log-streaming-is-generally-available/">AWSへの監査ログストリーミングが一般に利用可能に</a>なったことを発表しました。<a href="https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise">企業の監査ログをストリーミング</a>することで、企業には以下のようなメリットがあります。</p>
<ul>
<li><strong>データ探索。</strong>大量のデータを照会するための好みのツールを使用して、ストリームされたイベントを調べることができます。ストリームには、企業アカウント全体の監査イベントとGitイベントの両方が含まれます。</li>
<li><strong>データの継続性。</strong>監査データを失うことなく、最大 7 日間ストリームを一時停止できます。</li>
<li><strong>データの保持。</strong>エクスポートされた監査ログと Git イベントのデータは、必要な限り保持されます。</li>
</ul>
<p>このサービスを拡張するために、監査ログをAWS S3にストリーミングしている企業は、AWS CloudTrail Lakeインテグレーションを使用して、GitHub監査ログを自動的に統合し、<a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html">AWS Cloud Trail Lakeに</a>取り込むことができるようになりました。AWS CloudTrail Lakeは、セキュリティと監査のデータレイクとして管理され、イベントの集約、不変的な保存、クエリを可能にします。この統合を自分のAWSアカウントに導入することで、AWS CloudTrail Lakeは、SQLベースのクエリを使用してGitHub監査ログイベントを分析するためのツールを取得し提供します。</p>
<p>詳しくは、AWS<a href="https://docs.github.com/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#integrating-with-aws-cloudtrail-lake">CloudTrail Lakeとの統合</a>に関するドキュメントをご覧ください。</p>


