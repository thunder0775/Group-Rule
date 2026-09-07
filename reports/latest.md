# Group-Rule 审计报告

生成时间：`2026-09-07T07:24:49+00:00`
发布闸门：**PASS**

## 审计等级

- `BLOCK`：禁止本次生成结果进入 Git 提交。
- `ERROR`：严重运行异常。
- `WARNING`：记录并继续，异常原子规则使用 Last Known Good。
- `INFO`：信息类质量提示。

## 总体质量

- 精确重复出现次数：`3225`
- 同分类重复规则：`61`
- 跨分类重复规则：`3121`
- DOMAIN 语义冗余：`3055`
- CIDR 语义冗余：`434`
- 无效 DOMAIN：`0`
- 无效 CIDR：`0`
- 高风险 DOMAIN-KEYWORD：`0`
- reject 与代理域重叠已剔除：`5709`
- 父子策略分裂（跨代理分类）：`313`
- 子域并入父分类：`326`

## 分类统计

- `ai`：43 条
- `streaming`：1565 条
- `social`：676 条
- `developer`：71 条
- `service`：1843 条
- `global`：25289 条
- `china`：119628 条
- `reject`：185293 条

## 闸门结果

- `INFO`：`4`
- `WARNING`：`2`

### Findings

- **WARNING** `too_few_rules` — `china/domains`
- **INFO** `semantic_domain_redundancy`
- **INFO** `semantic_cidr_redundancy`
- **INFO** `reject_proxy_overlap_sanitized`
- **INFO** `child_collapsed_to_parent_category`
- **WARNING** `child_policy_split`

## 语义冗余

DOMAIN 父子覆盖：`3055`（排除裸 TLD）
CIDR 父网覆盖子网：`434`

### DOMAIN 示例

- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc31.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3s.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3z.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrctt.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrctu.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjz8yzdnc31.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjz8yzdnc3t.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpba.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpbz.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpjt.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr5dgmttgha1hcj38yzdncb3.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,112-81-125-43.dhost.00cdn.com` ← `DOMAIN-SUFFIX,00cdn.com`
- `DOMAIN,113-219-145-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,114-236-92-129.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,180-101-74-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,1geadrmttge3nhcjwgazdope.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1geadrmttge3nhcjwgwzdqqe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjo8yzdnco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjo8yzdnpy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjtgezdkcy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqca.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqce.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqpo.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjzgwzdkqe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdcca.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdcco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdkca.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdkco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdkpe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdkpy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj38yzdkqy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj3gczdcpa.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj3gczdcpe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj3gczdcpo.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcj3gczdcqy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr5dgmttgha1hcttgrzdnpo.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1graukmttga4nhcjtgozdgce.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,218-91-225-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,219-155-150-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,222-188-6-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,36-104-134-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,36-25-252-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,3dns-1.adobe.com` ← `DOMAIN-SUFFIX,adobe.com`
- `DOMAIN,3dns-2.adobe.com` ← `DOMAIN-SUFFIX,adobe.com`
- `DOMAIN,3dns-3.adobe.com` ← `DOMAIN-SUFFIX,adobe.com`
- `DOMAIN,3dns-4.adobe.com` ← `DOMAIN-SUFFIX,adobe.com`
- `DOMAIN,3dns-5.adobe.com` ← `DOMAIN-SUFFIX,adobe.com`
- `DOMAIN,3dns.adobe.com` ← `DOMAIN-SUFFIX,adobe.com`
- `DOMAIN,3ge3drmttga5nhcbqge3ur.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`

### CIDR 示例

- `IP-CIDR,0.0.0.1/32` ← `reject/advertising`
- `IP-CIDR,1.3.0.10/32` ← `china/domains`
- `IP-CIDR,101.124.19.122/32` ← `china/domains`
- `IP-CIDR,101.201.29.182/32` ← `china/domains`
- `IP-CIDR,101.226.10.8/32` ← `china/domains`
- `IP-CIDR,101.227.200.0/24` ← `china/domains`
- `IP-CIDR,101.227.97.240/32` ← `china/domains`
- `IP-CIDR,101.251.211.235/32` ← `china/domains`
- `IP-CIDR,101.35.204.35/32` ← `china/domains`
- `IP-CIDR,101.36.166.16/32` ← `china/domains`
- `IP-CIDR,103.224.222.208/32` ← `china/domains`
- `IP-CIDR,103.249.254.113/32` ← `china/domains`
- `IP-CIDR,103.37.152.97/32` ← `china/domains`
- `IP-CIDR,103.41.167.226/32` ← `china/domains`
- `IP-CIDR,103.41.167.234/31` ← `china/domains`
- `IP-CIDR,103.41.167.236/32` ← `china/domains`
- `IP-CIDR,103.49.209.27/32` ← `reject/advertising`
- `IP-CIDR,103.75.152.210/32` ← `china/domains`
- `IP-CIDR,103.75.153.3/32` ← `china/domains`
- `IP-CIDR,106.11.25.31/32` ← `china/domains`
- `IP-CIDR,106.75.231.48/32` ← `china/domains`
- `IP-CIDR,106.75.231.48/32` ← `china/domains`
- `IP-CIDR,106.75.231.48/32` ← `reject/advertising`
- `IP-CIDR,106.75.65.90/32` ← `china/domains`
- `IP-CIDR,106.75.65.92/32` ← `china/domains`
- `IP-CIDR,106.75.74.76/32` ← `china/domains`
- `IP-CIDR,109.123.233.251/32` ← `reject/advertising`
- `IP-CIDR,109.239.140.0/24` ← `global/proxy`
- `IP-CIDR,111.11.208.2/32` ← `china/domains`
- `IP-CIDR,111.175.220.160/29` ← `china/domains`
- `IP-CIDR,111.175.220.163/32` ← `china/domains`
- `IP-CIDR,111.175.220.163/32` ← `reject/advertising`
- `IP-CIDR,111.175.220.164/32` ← `china/domains`
- `IP-CIDR,111.175.220.164/32` ← `reject/advertising`
- `IP-CIDR,111.175.221.58/32` ← `china/domains`
- `IP-CIDR,111.206.22.0/24` ← `china/domains`
- `IP-CIDR,111.206.25.147/32` ← `china/domains`
- `IP-CIDR,111.30.135.167/32` ← `china/domains`
- `IP-CIDR,111.30.159.168/32` ← `china/domains`
- `IP-CIDR,111.30.176.111/32` ← `china/domains`
- `IP-CIDR,111.63.135.0/24` ← `china/domains`
- `IP-CIDR,111.73.45.147/32` ← `china/domains`
- `IP-CIDR,112.124.115.215/32` ← `china/domains`
- `IP-CIDR,112.132.230.179/32` ← `china/domains`
- `IP-CIDR,112.29.211.120/32` ← `china/domains`
- `IP-CIDR,112.74.95.46/32` ← `china/domains`
- `IP-CIDR,113.12.83.4/31` ← `china/domains`
- `IP-CIDR,113.207.57.24/32` ← `china/domains`
- `IP-CIDR,113.57.230.88/32` ← `china/domains`
- `IP-CIDR,114.110.97.97/32` ← `china/domains`

## reject 代理域重叠清理

剔除条数：`5709`（父域已在代理分类中的子域不再 REJECT）

- `DOMAIN-SUFFIX,0emm.com` ← covered by `0emm.com`
- `DOMAIN-SUFFIX,1.hao123.com` ← covered by `hao123.com`
- `DOMAIN-SUFFIX,104231.dtiblog.com` ← covered by `dtiblog.com`
- `DOMAIN-SUFFIX,1080872514.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1097834592.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1187531871.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1208344341.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1437953666.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1529462937.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1548164934.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1675450967.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1991482557.rsc.cdn77.org` ← covered by `cdn77.org`
- `DOMAIN-SUFFIX,1l-hit.mail.ru` ← covered by `mail.ru`
- `DOMAIN-SUFFIX,1l-hit.vkplay.ru` ← covered by `vkplay.ru`
- `DOMAIN-SUFFIX,1l-view.mail.ru` ← covered by `mail.ru`
- `DOMAIN-SUFFIX,1l-view.my.games` ← covered by `my.games`
- `DOMAIN-SUFFIX,1wincdn.b-cdn.net` ← covered by `b-cdn.net`
- `DOMAIN-SUFFIX,2006mindfreaklike.blogspot.com` ← covered by `blogspot.com`
- `DOMAIN-SUFFIX,24hmoneygram.weebly.com` ← covered by `weebly.com`
- `DOMAIN-SUFFIX,25serve.yourporngod.com` ← covered by `yourporngod.com`
- `DOMAIN-SUFFIX,2mdn-cn.net` ← covered by `2mdn-cn.net`
- `DOMAIN-SUFFIX,2mdn.net` ← covered by `2mdn.net`
- `DOMAIN-SUFFIX,2o7.net` ← covered by `2o7.net`
- `DOMAIN-SUFFIX,3dns-1.adobe.com` ← covered by `adobe.com`
- `DOMAIN-SUFFIX,3dns-2.adobe.com` ← covered by `adobe.com`
- `DOMAIN-SUFFIX,3dns-3.adobe.com` ← covered by `adobe.com`
- `DOMAIN-SUFFIX,3dns-4.adobe.com` ← covered by `adobe.com`
- `DOMAIN-SUFFIX,3dns.adobe.com` ← covered by `adobe.com`
- `DOMAIN-SUFFIX,3j0pw4ed7uac-a.akamaihd.net` ← covered by `akamaihd.net`
- `DOMAIN-SUFFIX,3p-geo.yahoo.com` ← covered by `yahoo.com`
- `DOMAIN-SUFFIX,3p-udc.yahoo.com` ← covered by `yahoo.com`
- `DOMAIN-SUFFIX,450a.feet9.com` ← covered by `feet9.com`
- `DOMAIN-SUFFIX,478789.everydayporn.co` ← covered by `everydayporn.co`
- `DOMAIN-SUFFIX,4hfvbao1ea.execute-api.ap-northeast-2.amazonaws.com` ← covered by `amazonaws.com`
- `DOMAIN-SUFFIX,51tongji.trafficmanager.net` ← covered by `trafficmanager.net`
- `DOMAIN-SUFFIX,52av.be` ← covered by `52av.be`
- `DOMAIN-SUFFIX,61serve.everydayporn.co` ← covered by `everydayporn.co`
- `DOMAIN-SUFFIX,682a5845.b-cdn.net` ← covered by `b-cdn.net`
- `DOMAIN-SUFFIX,6969.javher.com` ← covered by `javher.com`
- `DOMAIN-SUFFIX,7ng6v3lu3c.execute-api.us-east-1.amazonaws.com` ← covered by `execute-api.us-east-1.amazonaws.com`
- `DOMAIN-SUFFIX,7q1z79gxsi.global.ssl.fastly.net` ← covered by `fastly.net`
- `DOMAIN-SUFFIX,9w2zed1szg.execute-api.us-east-1.amazonaws.com` ← covered by `execute-api.us-east-1.amazonaws.com`
- `DOMAIN-SUFFIX,a-delivery.rmbl.ws` ← covered by `rmbl.ws`
- `DOMAIN-SUFFIX,a-reporting.nytimes.com` ← covered by `nytimes.com`
- `DOMAIN-SUFFIX,a.ad.playstation.net` ← covered by `playstation.net`
- `DOMAIN-SUFFIX,a.apkpures.xyz` ← covered by `apkpures.xyz`
- `DOMAIN-SUFFIX,a.baidu.com` ← covered by `baidu.com`
- `DOMAIN-SUFFIX,a.fox.com` ← covered by `fox.com`
- `DOMAIN-SUFFIX,a.foxsports.com` ← covered by `foxsports.com`
- `DOMAIN-SUFFIX,a.foxsportsflorida.com` ← covered by `foxsportsflorida.com`

## 父子策略分裂（跨代理分类）

数量：`313`（同一站点子域与父域落在不同代理策略组，易导致 SSL/拆隧道问题）

- 子 `DOMAIN,ai.google.dev` @`global` ← 父 `DOMAIN-SUFFIX,google.dev` @`service`
- 子 `DOMAIN,alkalicore-pa.clients6.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alkalimakersuite-pa.clients6.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt1-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt2-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt3-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt4-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt5-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt6-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt7-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,alt8-mtalk.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,android.googlesource.com` @`global` ← 父 `DOMAIN-SUFFIX,googlesource.com` @`service`
- 子 `DOMAIN,antigravity-pa.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,antigravity.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,api.msn.com` @`global` ← 父 `DOMAIN-SUFFIX,msn.com` @`service`
- 子 `DOMAIN,api.statsig.com` @`ai` ← 父 `DOMAIN-SUFFIX,api.statsig.com` @`global`
- 子 `DOMAIN,api.viu.now.com` @`global` ← 父 `DOMAIN-SUFFIX,now.com` @`streaming`
- 子 `DOMAIN,apple.com.akadns.net` @`global` ← 父 `DOMAIN-SUFFIX,akadns.net` @`service`
- 子 `DOMAIN,assets.msn.com` @`global` ← 父 `DOMAIN-SUFFIX,msn.com` @`service`
- 子 `DOMAIN,audio-ak-spotify-com.akamaized.net` @`streaming` ← 父 `DOMAIN-SUFFIX,audio-ak-spotify-com.akamaized.net` @`global`
- 子 `DOMAIN,az764295.vo.msecnd.net` @`global` ← 父 `DOMAIN-SUFFIX,msecnd.net` @`service`
- 子 `DOMAIN,azure.microsoft.com` @`global` ← 父 `DOMAIN-SUFFIX,microsoft.com` @`service`
- 子 `DOMAIN,azuremarketplace.microsoft.com` @`global` ← 父 `DOMAIN-SUFFIX,microsoft.com` @`service`
- 子 `DOMAIN,bingsettingssearch.trafficmanager.net` @`global` ← 父 `DOMAIN-SUFFIX,trafficmanager.net` @`service`
- 子 `DOMAIN,bybit-exchange.github.io` @`developer` ← 父 `DOMAIN-SUFFIX,github.io` @`global`
- 子 `DOMAIN,client-teamviewer-com.trafficmanager.net` @`global` ← 父 `DOMAIN-SUFFIX,trafficmanager.net` @`service`
- 子 `DOMAIN,clients1.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,cloudaicompanion.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,cloudcode-pa.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,configuration-lb.ls-apple.com.akadns.net` @`global` ← 父 `DOMAIN-SUFFIX,akadns.net` @`service`
- 子 `DOMAIN,copilot-proxy.githubusercontent.com` @`developer` ← 父 `DOMAIN-SUFFIX,githubusercontent.com` @`global`
- 子 `DOMAIN,copilot-workspace.githubnext.com` @`developer` ← 父 `DOMAIN-SUFFIX,githubnext.com` @`global`
- 子 `DOMAIN,copilot.microsoft.com` @`global` ← 父 `DOMAIN-SUFFIX,microsoft.com` @`service`
- 子 `DOMAIN,copilotprodattachments.blob.core.windows.net` @`global` ← 父 `DOMAIN-SUFFIX,windows.net` @`service`
- 子 `DOMAIN,crl.microsoft.com` @`global` ← 父 `DOMAIN-SUFFIX,microsoft.com` @`service`
- 子 `DOMAIN,daily-cloudcode-pa.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,default.exp-tas.com` @`global` ← 父 `DOMAIN-SUFFIX,exp-tas.com` @`service`
- 子 `DOMAIN,developer.microsoft.com` @`global` ← 父 `DOMAIN-SUFFIX,microsoft.com` @`service`
- 子 `DOMAIN,developers.facebook.com` @`global` ← 父 `DOMAIN-SUFFIX,facebook.com` @`social`
- 子 `DOMAIN,discord-attachments-uploads-prd.storage.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,disneyplus.com.ssl.sc.omtrdc.net` @`streaming` ← 父 `DOMAIN-SUFFIX,disneyplus.com.ssl.sc.omtrdc.net` @`global`
- 子 `DOMAIN,dtlgalleryint.cloudapp.net` @`global` ← 父 `DOMAIN-SUFFIX,cloudapp.net` @`service`
- 子 `DOMAIN,epc-de-agent-proxy.germanywestcentral.cloudapp.azure.com` @`global` ← 父 `DOMAIN-SUFFIX,azure.com` @`service`
- 子 `DOMAIN,espn.api.edge.bamgrid.com` @`global` ← 父 `DOMAIN-SUFFIX,bamgrid.com` @`streaming`
- 子 `DOMAIN,espn.hb.omtrdc.net` @`streaming` ← 父 `DOMAIN-SUFFIX,espn.hb.omtrdc.net` @`global`
- 子 `DOMAIN,espndotcom.tt.omtrdc.net` @`streaming` ← 父 `DOMAIN-SUFFIX,espndotcom.tt.omtrdc.net` @`global`
- 子 `DOMAIN,fbcdn-a.akamaihd.net` @`social` ← 父 `DOMAIN-SUFFIX,fbcdn-a.akamaihd.net` @`global`
- 子 `DOMAIN,firebase.google.com` @`global` ← 父 `DOMAIN-SUFFIX,google.com` @`service`
- 子 `DOMAIN,firebase.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`
- 子 `DOMAIN,firebaseappcheck.googleapis.com` @`global` ← 父 `DOMAIN-SUFFIX,googleapis.com` @`service`

## 子域并入父分类

移动条数：`326`

- `DOMAIN,chat.openai.com.cdn.cloudflare.net`：`ai/openai` → `global/proxy`
- `DOMAIN,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net`：`ai/openai` → `global/proxy`
- `DOMAIN,openaicomproductionae4b.blob.core.windows.net`：`ai/openai` → `global/proxy`
- `DOMAIN,production-openaicom-storage.azureedge.net`：`ai/openai` → `global/proxy`
- `DOMAIN,static.cloudflareinsights.com`：`ai/openai` → `global/proxy`
- `DOMAIN-SUFFIX,openaiapi-site.azureedge.net`：`ai/openai` → `global/proxy`
- `DOMAIN-SUFFIX,openaicom.imgix.net`：`ai/openai` → `global/proxy`
- `DOMAIN,ai.google.dev`：`ai/gemini` → `global/proxy`
- `DOMAIN,alkalimakersuite-pa.clients6.google.com`：`ai/gemini` → `global/proxy`
- `DOMAIN,makersuite.google.com`：`ai/gemini` → `global/proxy`
- `DOMAIN-SUFFIX,bard.google.com`：`ai/gemini` → `global/proxy`
- `DOMAIN-SUFFIX,gemini.google.com`：`ai/gemini` → `global/proxy`
- `DOMAIN-SUFFIX,proactivebackend-pa.googleapis.com`：`ai/gemini` → `global/proxy`
- `DOMAIN-SUFFIX,apis.google.com`：`ai/gemini` → `global/proxy`
- `DOMAIN,api.msn.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,assets.msn.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,chat.openai.com.cdn.cloudflare.net`：`ai/copilot` → `global/proxy`
- `DOMAIN,copilot.microsoft.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,gateway.bingviz.microsoft.net`：`ai/copilot` → `global/proxy`
- `DOMAIN,gateway.bingviz.microsoftapp.net`：`ai/copilot` → `global/proxy`
- `DOMAIN,in.appcenter.ms`：`ai/copilot` → `global/proxy`
- `DOMAIN,location.microsoft.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,odc.officeapps.live.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,openaicomproductionae4b.blob.core.windows.net`：`ai/copilot` → `global/proxy`
- `DOMAIN,production-openaicom-storage.azureedge.net`：`ai/copilot` → `global/proxy`
- `DOMAIN,r.bing.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,self.events.data.microsoft.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,services.bingapis.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,static.cloudflareinsights.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,sydney.bing.com`：`ai/copilot` → `global/proxy`
- `DOMAIN,www.bing.com`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,api.microsoftapp.net`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,bing-shopping.microsoft-falcon.io`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,challenges.cloudflare.com`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,edgeservices.bing.com`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,openaiapi-site.azureedge.net`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,openaicom.imgix.net`：`ai/copilot` → `global/proxy`
- `DOMAIN-SUFFIX,video.google.com`：`streaming/youtube` → `global/proxy`
- `DOMAIN-SUFFIX,wide-youtube.l.google.com`：`streaming/youtube` → `global/proxy`
- `DOMAIN-SUFFIX,youtube-ui.l.google.com`：`streaming/youtube` → `global/proxy`
- `DOMAIN-SUFFIX,youtube.googleapis.com`：`streaming/youtube` → `global/proxy`
- `DOMAIN-SUFFIX,youtubeembeddedplayer.googleapis.com`：`streaming/youtube` → `global/proxy`
- `DOMAIN-SUFFIX,youtubei.googleapis.com`：`streaming/youtube` → `global/proxy`
- `DOMAIN,e13252.dscg.akamaiedge.net`：`streaming/netflix` → `global/proxy`
- `DOMAIN-SUFFIX,netflix.com.edgesuite.net`：`streaming/netflix` → `global/proxy`
- `DOMAIN-SUFFIX,us-west-2.amazonaws.com`：`streaming/netflix` → `global/proxy`
- `DOMAIN-SUFFIX,abcnews.edgesuite.net`：`streaming/disney` → `global/proxy`
- `DOMAIN-SUFFIX,cdn.optimizely.com`：`streaming/disney` → `service/microsoft`
- `DOMAIN-SUFFIX,disney-portal.my.onetrust.com`：`streaming/disney` → `global/proxy`
- `DOMAIN-SUFFIX,disney.my.sentry.io`：`streaming/disney` → `ai/copilot`

## 跨分类冲突（最多 100 条）

- `DOMAIN,browser-intake-datadoghq.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,cdn-spotify-experiments.conductrics.com` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,cdn.usefathom.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,lf16-effectcdn.byteeffecttos-g.com` → 胜出 `social`；涉及 global, social
- `DOMAIN,lf16-pkgcdn.pitaya-clientai.com` → 胜出 `social`；涉及 global, social
- `DOMAIN,openai-api.arkoselabs.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,vsmarketplacebadge.apphb.com` → 胜出 `service`；涉及 global, service
- `DOMAIN-KEYWORD,1drv` → 胜出 `developer`；涉及 developer, global, service
- `DOMAIN-KEYWORD,colab` → 胜出 `ai`；涉及 ai, global
- `DOMAIN-KEYWORD,developerprofiles` → 胜出 `ai`；涉及 ai, global
- `DOMAIN-KEYWORD,generativelanguage` → 胜出 `ai`；涉及 ai, global
- `DOMAIN-KEYWORD,musical.ly` → 胜出 `social`；涉及 global, social
- `DOMAIN-KEYWORD,onedrive` → 胜出 `developer`；涉及 developer, global, service
- `DOMAIN-KEYWORD,openai` → 胜出 `ai`；涉及 ai, global
- `DOMAIN-KEYWORD,openaicom-api` → 胜出 `ai`；涉及 ai, global
- `DOMAIN-KEYWORD,skydrive` → 胜出 `developer`；涉及 developer, global, service
- `DOMAIN-KEYWORD,tiktok` → 胜出 `social`；涉及 global, social
- `DOMAIN-SUFFIX,003store.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,0emm.com` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,165tchuang.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,17gouwuba.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,17swan.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,1drv.com` → 胜出 `developer`；涉及 developer, global, service
- `DOMAIN-SUFFIX,1drv.ms` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,1e100.net` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,1l1.cc` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,1sapp.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,1ucrs.com` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,20thcenturystudios.com.au` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN-SUFFIX,20thcenturystudios.com.br` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN-SUFFIX,20thcenturystudios.jp` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN-SUFFIX,21vbc.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,21vbluecloud.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,21vbluecloud.net` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,2481e.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,25662zubo23739.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,265.com` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,2girls1finger.org` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,2mdn-cn.net` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,2mdn.net` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,3337723.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3337738.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,360ads.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,365dmp.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3721zh.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,37swan.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,39jz.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3p8801.co` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,4009997658.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,466453.com` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,50bang.org` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,51.la` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,518ad.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,54kefu.net` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,55726zubo56686.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,57573zubo36833.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,595image.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,5hffr1p22j.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,609999.xyz` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,644446.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,68287zubo85737.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,693836.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,6d63d3.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,6fm4dcpj31.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,6pctuhriw.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,73336zubo25326.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,876920.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,88362zubo95838.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,8k69vb6421.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,8x5vviy4r2.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,91.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,91cy.app` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,91short.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,93692zubo66936.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,961.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,96382zubo66756.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,99thz.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,9cao9.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,a-msedge.net` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,a1.mzstatic.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,a2.mzstatic.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,a3.mzstatic.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,a4.mzstatic.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,a4xvv2g18l.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,a5.mzstatic.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,aa77kk.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,aadrm.com` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,abbyychina.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,abc-studios.com` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN-SUFFIX,abc.com` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN-SUFFIX,abc.xyz` → 胜出 `service`；涉及 global, service
- `DOMAIN-SUFFIX,abcnews.com` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN-SUFFIX,aboutfacebook.com` → 胜出 `social`；涉及 global, social
- `DOMAIN-SUFFIX,accessfacebookfromschool.com` → 胜出 `social`；涉及 global, social
- `DOMAIN-SUFFIX,accountkit.com` → 胜出 `social`；涉及 global, social
- `DOMAIN-SUFFIX,acebooik.com` → 胜出 `social`；涉及 global, social
- `DOMAIN-SUFFIX,acebook.com` → 胜出 `social`；涉及 global, social
- `DOMAIN-SUFFIX,acg.tv` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,acgvideo.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,achat-followers-instagram.com` → 胜出 `social`；涉及 global, social

## 编译输出校验

- 状态：**PASS**
- 问题数：`0`

## 中国直连安全过滤

- 原始中国规则：`120528`
- 发布中国域名规则：`110952`
- 移除非域名/关键词/IP规则：`8065`
- 移除非 CN TLD：`841`
- 移除显式海外回归域名：`2`
- 移除与海外高优先级分类重叠：`626`
