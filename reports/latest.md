# Group-Rule 审计报告

生成时间：`2026-09-07T08:19:35+00:00`
发布闸门：**PASS**

## 审计等级

- `BLOCK`：禁止本次生成结果进入 Git 提交。
- `ERROR`：严重运行异常。
- `WARNING`：记录并继续，异常原子规则使用 Last Known Good。
- `INFO`：信息类质量提示。

## 总体质量

- 精确重复出现次数：`993`
- 同分类重复规则：`91`
- 跨分类重复规则：`901`
- DOMAIN 语义冗余：`2682`
- CIDR 语义冗余：`420`
- 无效 DOMAIN：`0`
- 无效 CIDR：`0`
- 高风险 DOMAIN-KEYWORD：`0`
- reject 与代理域重叠已剔除：`5709`
- 父子策略分裂（跨代理分类）：`0`
- 子域并入父分类：`235`

## 分类统计

- `ai`：74 条
- `streaming`：1617 条
- `social`：685 条
- `developer`：82 条
- `service`：2202 条
- `global`：24827 条
- `china`：119628 条
- `reject`：185293 条

## 闸门结果

- `INFO`：`4`
- `WARNING`：`1`

### Findings

- **WARNING** `too_few_rules` — `china/domains`
- **INFO** `semantic_domain_redundancy`
- **INFO** `semantic_cidr_redundancy`
- **INFO** `reject_proxy_overlap_sanitized`
- **INFO** `child_collapsed_to_parent_category`

## 语义冗余

DOMAIN 父子覆盖：`2682`（排除裸 TLD）
CIDR 父网覆盖子网：`420`

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
- `IP-CIDR,114.112.163.232/32` ← `china/domains`

## reject 代理域重叠清理

剔除条数：`5709`（父域已在代理分类中的子域不再 REJECT）

- `DOMAIN-SUFFIX,0emm.com` ← covered by `None`
- `DOMAIN-SUFFIX,1.hao123.com` ← covered by `None`
- `DOMAIN-SUFFIX,104231.dtiblog.com` ← covered by `None`
- `DOMAIN-SUFFIX,1080872514.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1097834592.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1187531871.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1208344341.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1437953666.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1529462937.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1548164934.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1675450967.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1991482557.rsc.cdn77.org` ← covered by `None`
- `DOMAIN-SUFFIX,1l-hit.mail.ru` ← covered by `None`
- `DOMAIN-SUFFIX,1l-hit.vkplay.ru` ← covered by `None`
- `DOMAIN-SUFFIX,1l-view.mail.ru` ← covered by `None`
- `DOMAIN-SUFFIX,1l-view.my.games` ← covered by `None`
- `DOMAIN-SUFFIX,1wincdn.b-cdn.net` ← covered by `None`
- `DOMAIN-SUFFIX,2006mindfreaklike.blogspot.com` ← covered by `None`
- `DOMAIN-SUFFIX,24hmoneygram.weebly.com` ← covered by `None`
- `DOMAIN-SUFFIX,25serve.yourporngod.com` ← covered by `None`
- `DOMAIN-SUFFIX,2mdn-cn.net` ← covered by `None`
- `DOMAIN-SUFFIX,2mdn.net` ← covered by `None`
- `DOMAIN-SUFFIX,2o7.net` ← covered by `None`
- `DOMAIN-SUFFIX,3dns-1.adobe.com` ← covered by `None`
- `DOMAIN-SUFFIX,3dns-2.adobe.com` ← covered by `None`
- `DOMAIN-SUFFIX,3dns-3.adobe.com` ← covered by `None`
- `DOMAIN-SUFFIX,3dns-4.adobe.com` ← covered by `None`
- `DOMAIN-SUFFIX,3dns.adobe.com` ← covered by `None`
- `DOMAIN-SUFFIX,3j0pw4ed7uac-a.akamaihd.net` ← covered by `None`
- `DOMAIN-SUFFIX,3p-geo.yahoo.com` ← covered by `None`
- `DOMAIN-SUFFIX,3p-udc.yahoo.com` ← covered by `None`
- `DOMAIN-SUFFIX,450a.feet9.com` ← covered by `None`
- `DOMAIN-SUFFIX,478789.everydayporn.co` ← covered by `None`
- `DOMAIN-SUFFIX,4hfvbao1ea.execute-api.ap-northeast-2.amazonaws.com` ← covered by `None`
- `DOMAIN-SUFFIX,51tongji.trafficmanager.net` ← covered by `None`
- `DOMAIN-SUFFIX,52av.be` ← covered by `None`
- `DOMAIN-SUFFIX,61serve.everydayporn.co` ← covered by `None`
- `DOMAIN-SUFFIX,682a5845.b-cdn.net` ← covered by `None`
- `DOMAIN-SUFFIX,6969.javher.com` ← covered by `None`
- `DOMAIN-SUFFIX,7ng6v3lu3c.execute-api.us-east-1.amazonaws.com` ← covered by `None`
- `DOMAIN-SUFFIX,7q1z79gxsi.global.ssl.fastly.net` ← covered by `None`
- `DOMAIN-SUFFIX,9w2zed1szg.execute-api.us-east-1.amazonaws.com` ← covered by `None`
- `DOMAIN-SUFFIX,a-delivery.rmbl.ws` ← covered by `None`
- `DOMAIN-SUFFIX,a-reporting.nytimes.com` ← covered by `None`
- `DOMAIN-SUFFIX,a.ad.playstation.net` ← covered by `None`
- `DOMAIN-SUFFIX,a.apkpures.xyz` ← covered by `None`
- `DOMAIN-SUFFIX,a.baidu.com` ← covered by `None`
- `DOMAIN-SUFFIX,a.fox.com` ← covered by `None`
- `DOMAIN-SUFFIX,a.foxsports.com` ← covered by `None`
- `DOMAIN-SUFFIX,a.foxsportsflorida.com` ← covered by `None`

## 子域并入父分类

移动条数：`235`

- `DOMAIN-SUFFIX,disney.my.sentry.io`：`streaming/disney` → `ai/copilot`
- `DOMAIN-SUFFIX,beacons.gvt2.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,beacons2.gvt2.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,beacons3.gvt2.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,gcp.gvt2.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,redirector.gcpcdn.gvt1.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,redirector.gvt1.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,redirector.offline-maps.gvt1.com`：`service/google` → `streaming/youtube`
- `DOMAIN-SUFFIX,redirector.snap.gvt1.com`：`service/google` → `streaming/youtube`
- `DOMAIN,alkalicore-pa.clients6.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt1-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt2-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt3-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt4-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt5-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt6-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt7-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,alt8-mtalk.google.com`：`global/proxy` → `service/google`
- `DOMAIN,android.googlesource.com`：`global/proxy` → `service/google`
- `DOMAIN,antigravity-pa.googleapis.com`：`global/proxy` → `service/google`
- `DOMAIN,antigravity.googleapis.com`：`global/proxy` → `service/google`
- `DOMAIN,api.viu.now.com`：`global/proxy` → `streaming/max`
- `DOMAIN,apple.com.akadns.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,audio-ak-spotify-com.akamaized.net`：`global/proxy` → `streaming/spotify`
- `DOMAIN,az764295.vo.msecnd.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,azure.microsoft.com`：`global/proxy` → `service/microsoft`
- `DOMAIN,azuremarketplace.microsoft.com`：`global/proxy` → `service/microsoft`
- `DOMAIN,bingsettingssearch.trafficmanager.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,bybit-exchange.github.io`：`global/proxy` → `developer/github`
- `DOMAIN,client-teamviewer-com.trafficmanager.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,clients1.google.com`：`global/proxy` → `service/google`
- `DOMAIN,cloudaicompanion.googleapis.com`：`global/proxy` → `service/google`
- `DOMAIN,cloudcode-pa.googleapis.com`：`global/proxy` → `service/google`
- `DOMAIN,configuration-lb.ls-apple.com.akadns.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,copilot-proxy.githubusercontent.com`：`global/proxy` → `developer/github`
- `DOMAIN,copilot-workspace.githubnext.com`：`global/proxy` → `developer/github`
- `DOMAIN,copilotprodattachments.blob.core.windows.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,crl.microsoft.com`：`global/proxy` → `service/microsoft`
- `DOMAIN,daily-cloudcode-pa.googleapis.com`：`global/proxy` → `service/google`
- `DOMAIN,default.exp-tas.com`：`global/proxy` → `service/microsoft`
- `DOMAIN,developer.microsoft.com`：`global/proxy` → `service/microsoft`
- `DOMAIN,developers.facebook.com`：`global/proxy` → `social/facebook`
- `DOMAIN,discord-attachments-uploads-prd.storage.googleapis.com`：`global/proxy` → `service/google`
- `DOMAIN,disneyplus.com.ssl.sc.omtrdc.net`：`global/proxy` → `streaming/disney`
- `DOMAIN,dtlgalleryint.cloudapp.net`：`global/proxy` → `service/microsoft`
- `DOMAIN,epc-de-agent-proxy.germanywestcentral.cloudapp.azure.com`：`global/proxy` → `service/microsoft`
- `DOMAIN,espn.api.edge.bamgrid.com`：`global/proxy` → `streaming/disney`
- `DOMAIN,espn.hb.omtrdc.net`：`global/proxy` → `streaming/disney`
- `DOMAIN,espndotcom.tt.omtrdc.net`：`global/proxy` → `streaming/disney`
- `DOMAIN,fbcdn-a.akamaihd.net`：`global/proxy` → `social/facebook`

## 跨分类冲突（最多 100 条）

- `DOMAIN-SUFFIX,003store.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,165tchuang.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,17gouwuba.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,17swan.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,1l1.cc` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,1sapp.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,21vbc.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,21vbluecloud.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,21vbluecloud.net` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,2481e.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,25662zubo23739.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,2girls1finger.org` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3337723.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3337738.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,360ads.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,365dmp.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3721zh.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,37swan.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,39jz.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,3p8801.co` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,4009997658.com` → 胜出 `reject`；涉及 china, reject
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
- `DOMAIN-SUFFIX,a1.mzstatic.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,a2.mzstatic.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,a3.mzstatic.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,a4.mzstatic.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,a4xvv2g18l.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,a5.mzstatic.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,aa77kk.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,abbyychina.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,acg.tv` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,acgvideo.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,acobt.tech` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,acs.org` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,ad7.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adcdownload.apple.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,adcdownload.apple.com.akadns.net` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,adkwai.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,ads8.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adsame.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adsmogo.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adsmogo.mobi` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adsmogo.net` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adukwai.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adview.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adwangmai.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,adxvip.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,aeqfuyc.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,age.tv` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,agedm.app` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,agefans.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,aggresmart.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,aicdn.work` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,aiclk.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,ainb01010zh.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,ainb12251zh.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,aipage.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,aiqicha.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,aivaylaco.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,aiwanma99.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,aizhantj.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,alibabacloud.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,alicloud.com` → 胜出 `global`；涉及 china, global
- `DOMAIN-SUFFIX,allyes.com` → 胜出 `reject`；涉及 china, reject
- `DOMAIN-SUFFIX,amemv.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,amp-api.media.apple.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,animetamashi.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,anitama.net` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,apollo-platform.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,apollo-share.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,apollo.auto` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,app-site-association.cdn-apple.com` → 胜出 `service`；涉及 china, service
- `DOMAIN-SUFFIX,appldnld.apple.com` → 胜出 `service`；涉及 china, service

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
