# Group-Rule 审计报告

生成时间：`2026-09-05T04:42:56+00:00`
发布闸门：**PASS**

## 审计等级

- `BLOCK`：禁止本次生成结果进入 Git 提交。
- `ERROR`：严重运行异常。
- `WARNING`：记录并继续，异常原子规则使用 Last Known Good。
- `INFO`：信息类质量提示。

## 总体质量

- 精确重复出现次数：`114642`
- 同分类重复规则：`110515`
- 跨分类重复规则：`3265`
- DOMAIN 语义冗余：`13615`
- CIDR 语义冗余：`3747`
- 无效 DOMAIN：`0`
- 无效 CIDR：`0`
- 高风险 DOMAIN-KEYWORD：`0`

## 分类统计

- `ai`：67 条
- `streaming`：1596 条
- `social`：672 条
- `developer`：70 条
- `service`：1983 条
- `global`：24958 条
- `china`：125227 条
- `reject`：190335 条

## 闸门结果

- `INFO`：`2`
- `WARNING`：`2`

### Findings

- **WARNING** `using_last_known_good` — `china/domains`
- **WARNING** `using_last_known_good` — `china/rules`
- **INFO** `semantic_domain_redundancy`
- **INFO** `semantic_cidr_redundancy`

## 语义冗余

DOMAIN 父子覆盖：`13615`（排除裸 TLD）
CIDR 父网覆盖子网：`3747`

### DOMAIN 示例

- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc31.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc31.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3s.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3s.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3z.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrc3z.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrctt.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrctt.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrctu.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjsgrzdrctu.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjz8yzdnc31.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjz8yzdnc31.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjz8yzdnc3t.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjz8yzdnc3t.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpba.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpba.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpbz.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpbz.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpjt.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr4uqmtt8y41hcjzgazdrpjt.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr5dgmttgha1hcj38yzdncb3.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,0gr5dgmttgha1hcj38yzdncb3.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,112-81-125-43.dhost.00cdn.com` ← `DOMAIN-SUFFIX,00cdn.com`
- `DOMAIN,112-81-125-43.dhost.00cdn.com` ← `DOMAIN-SUFFIX,00cdn.com`
- `DOMAIN,113-219-145-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,113-219-145-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,114-236-92-129.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,114-236-92-129.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,180-101-74-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,180-101-74-1.ksyungslb.com` ← `DOMAIN-SUFFIX,ksyungslb.com`
- `DOMAIN,1geadrmttge3nhcjwgazdope.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1geadrmttge3nhcjwgazdope.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1geadrmttge3nhcjwgwzdqqe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1geadrmttge3nhcjwgwzdqqe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjo8yzdnco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjo8yzdnco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjo8yzdnpy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjo8yzdnpy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjtgezdkcy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr3uomttgr31hcjtgezdkcy.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqca.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqca.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqce.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqce.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqco.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqpo.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjigazdqpo.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjzgwzdkqe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`
- `DOMAIN,1gr4uqmtt8y41hcjzgwzdkqe.ourdvsss.com` ← `DOMAIN-SUFFIX,ourdvsss.com`

### CIDR 示例

- `IP-CIDR,0.0.0.0/24` ← `china/rules`
- `IP-CIDR,0.0.0.0/32` ← `china/rules`
- `IP-CIDR,0.0.0.0/32` ← `reject/advertising`
- `IP-CIDR,0.0.0.1/32` ← `china/rules`
- `IP-CIDR,0.0.0.1/32` ← `reject/advertising`
- `IP-CIDR,1.116.0.0/15` ← `china/rules`
- `IP-CIDR,1.118.0.0/23` ← `china/rules`
- `IP-CIDR,1.118.128.0/17` ← `china/rules`
- `IP-CIDR,1.118.16.0/20` ← `china/rules`
- `IP-CIDR,1.118.37.0/24` ← `china/rules`
- `IP-CIDR,1.118.38.0/23` ← `china/rules`
- `IP-CIDR,1.118.4.0/22` ← `china/rules`
- `IP-CIDR,1.118.40.0/21` ← `china/rules`
- `IP-CIDR,1.118.56.0/21` ← `china/rules`
- `IP-CIDR,1.118.8.0/21` ← `china/rules`
- `IP-CIDR,1.118.96.0/19` ← `china/rules`
- `IP-CIDR,1.119.0.0/16` ← `china/rules`
- `IP-CIDR,1.3.0.10/32` ← `china/rules`
- `IP-CIDR,10.0.0.0/8` ← `china/domains`
- `IP-CIDR,10.255.128.136/32` ← `china/domains`
- `IP-CIDR,10.255.128.136/32` ← `china/rules`
- `IP-CIDR,10.72.25.0/24` ← `china/domains`
- `IP-CIDR,10.72.25.0/24` ← `china/rules`
- `IP-CIDR,100.64.0.0/10` ← `china/domains`
- `IP-CIDR,101.124.19.122/32` ← `china/rules`
- `IP-CIDR,101.192.0.0/18` ← `china/rules`
- `IP-CIDR,101.192.132.0/22` ← `china/rules`
- `IP-CIDR,101.192.164.0/22` ← `china/rules`
- `IP-CIDR,101.192.168.0/21` ← `china/rules`
- `IP-CIDR,101.192.176.0/20` ← `china/rules`
- `IP-CIDR,101.192.192.0/19` ← `china/rules`
- `IP-CIDR,101.192.68.0/22` ← `china/rules`
- `IP-CIDR,101.192.84.0/22` ← `china/rules`
- `IP-CIDR,101.192.88.0/21` ← `china/rules`
- `IP-CIDR,101.193.0.0/18` ← `china/rules`
- `IP-CIDR,101.193.100.0/22` ← `china/rules`
- `IP-CIDR,101.193.108.0/22` ← `china/rules`
- `IP-CIDR,101.193.112.0/22` ← `china/rules`
- `IP-CIDR,101.193.120.0/21` ← `china/rules`
- `IP-CIDR,101.193.132.0/22` ← `china/rules`
- `IP-CIDR,101.193.164.0/22` ← `china/rules`
- `IP-CIDR,101.193.168.0/21` ← `china/rules`
- `IP-CIDR,101.193.176.0/20` ← `china/rules`
- `IP-CIDR,101.193.192.0/19` ← `china/rules`
- `IP-CIDR,101.194.0.0/15` ← `china/rules`
- `IP-CIDR,101.196.0.0/14` ← `china/rules`
- `IP-CIDR,101.201.29.182/32` ← `china/rules`
- `IP-CIDR,101.226.10.8/32` ← `china/rules`
- `IP-CIDR,101.227.200.0/24` ← `china/rules`
- `IP-CIDR,101.227.97.240/32` ← `china/rules`

## 跨分类冲突（最多 100 条）

- `DOMAIN,ai.google.dev` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,alkalimakersuite-pa.clients6.google.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,api.msn.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,api.statsig.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,assets.msn.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,audio4-ak-spotify-com.akamaized.net` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,browser-intake-datadoghq.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,cdn-spotify-experiments.conductrics.com` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,cdn.usefathom.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,copilot.microsoft.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,developer.microsoft.com` → 胜出 `global`；涉及 china, global
- `DOMAIN,gateway.bingviz.microsoft.net` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,gateway.bingviz.microsoftapp.net` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,heads-ak-spotify-com.akamaized.net` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,in.appcenter.ms` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,lf16-effectcdn.byteeffecttos-g.com` → 胜出 `social`；涉及 global, social
- `DOMAIN,lf16-pkgcdn.pitaya-clientai.com` → 胜出 `social`；涉及 global, social
- `DOMAIN,location.microsoft.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,makersuite.google.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,netflix.com.edgesuite.net` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,np-edge.itunes.apple.com` → 胜出 `global`；涉及 china, global
- `DOMAIN,odc.officeapps.live.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,openai-api.arkoselabs.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,openaicom-api-bdcpf8c6d2e9atf6.z01.azurefd.net` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,openaicomproductionae4b.blob.core.windows.net` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,p16-tiktokcdn-com.akamaized.net` → 胜出 `social`；涉及 global, social
- `DOMAIN,play-edge.itunes.apple.com` → 胜出 `global`；涉及 china, global
- `DOMAIN,production-openaicom-storage.azureedge.net` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,r.bing.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,self.events.data.microsoft.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,services.bingapis.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,spotify.com.edgesuite.net` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,spotify.map.fastly.net` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,spotify.map.fastlylb.net` → 胜出 `streaming`；涉及 global, streaming
- `DOMAIN,static.cloudflareinsights.com` → 胜出 `ai`；涉及 ai, global
- `DOMAIN,vsmarketplacebadge.apphb.com` → 胜出 `service`；涉及 global, service
- `DOMAIN,www.bing.com` → 胜出 `ai`；涉及 ai, global
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
- `DOMAIN-SUFFIX,0emm.com` → 胜出 `reject`；涉及 global, reject, service
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
- `DOMAIN-SUFFIX,265.com` → 胜出 `service`；涉及 china, global, service
- `DOMAIN-SUFFIX,2mdn-cn.net` → 胜出 `reject`；涉及 global, reject, service
- `DOMAIN-SUFFIX,2mdn.net` → 胜出 `reject`；涉及 global, reject, service
- `DOMAIN-SUFFIX,2o7.net` → 胜出 `reject`；涉及 global, reject
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
- `DOMAIN-SUFFIX,52av.be` → 胜出 `reject`；涉及 global, reject
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

## 编译输出校验

- 状态：**PASS**
- 问题数：`0`
