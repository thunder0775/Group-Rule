# Group-Rule 审计报告

生成时间：`2026-09-05T03:17:51+00:00`
跨分类重复规则：`23`

## 分类统计

- `ai`：71 条
- `streaming`：1600 条
- `social`：670 条
- `developer`：70 条
- `service`：1814 条
- `china`：12586 条
- `reject`：972 条

## 原子规则状态

- `ai/anthropic`：**updated**，当前 3，历史 3
- `ai/copilot`：**updated**，当前 49，历史 49
- `ai/gemini`：**updated**，当前 13，历史 13
- `ai/openai`：**updated**，当前 34，历史 34
- `ai/xai`：**updated**，当前 2，历史 2
- `china/domains`：**unavailable**，当前 0，历史 0
  - ⚠️ `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Shadowrocket/ChinaMax/ChinaMax_Domain.list` → `rejected` zero_rules
- `china/rules`：**updated**，当前 12586，历史 12586
- `developer/dropbox`：**updated**，当前 17，历史 17
- `developer/github`：**updated**，当前 31，历史 31
- `developer/gitlab`：**updated**，当前 6，历史 6
- `developer/onedrive`：**updated**，当前 16，历史 16
- `reject/advertising`：**updated**，当前 781，历史 781
- `reject/hijacking`：**updated**，当前 228，历史 228
- `reject/privacy`：**updated**，当前 20，历史 20
- `service/apple`：**updated**，当前 43，历史 43
- `service/baidu`：**updated**，当前 251，历史 251
- `service/bilibili`：**updated**，当前 127，历史 127
- `service/douyin`：**updated**，当前 13，历史 13
- `service/google`：**updated**，当前 698，历史 698
- `service/microsoft`：**updated**，当前 671，历史 671
- `service/xiaohongshu`：**updated**，当前 4，历史 4
- `service/zhihu`：**updated**，当前 7，历史 7
- `social/facebook`：**updated**，当前 569，历史 569
- `social/instagram`：**updated**，当前 4，历史 4
- `social/telegram`：**updated**，当前 35，历史 35
- `social/tiktok`：**updated**，当前 32，历史 32
- `social/twitter`：**updated**，当前 33，历史 33
- `streaming/disney`：**updated**，当前 173，历史 173
- `streaming/max`：**updated**，当前 51，历史 51
- `streaming/netflix`：**updated**，当前 1157，历史 1157
- `streaming/spotify`：**updated**，当前 30，历史 30
- `streaming/youtube`：**updated**，当前 190，历史 190

## 冲突示例（最多 100 条）

- `DOMAIN-KEYWORD,1drv` → developer, service
- `DOMAIN-KEYWORD,onedrive` → developer, service
- `DOMAIN-KEYWORD,skydrive` → developer, service
- `DOMAIN-SUFFIX,1drv.com` → developer, service
- `DOMAIN-SUFFIX,deepmind.com` → ai, service
- `DOMAIN-SUFFIX,grok.com` → ai, social
- `DOMAIN-SUFFIX,livefilestore.com` → developer, service
- `DOMAIN-SUFFIX,microsoftpersonalcontent.com` → developer, service
- `DOMAIN-SUFFIX,onedrive.com` → developer, service
- `DOMAIN-SUFFIX,sharepoint.com` → developer, service
- `DOMAIN-SUFFIX,sharepointonline.com` → developer, service
- `DOMAIN-SUFFIX,snssdk.com` → service, social
- `DOMAIN-SUFFIX,spoprod-a.akamaihd.net` → developer, service
- `IP-CIDR,172.110.32.0/21` → service, streaming
- `IP-CIDR,203.107.1.0/24` → reject, service
- `IP-CIDR,216.73.80.0/20` → service, streaming
- `IP-CIDR,2620:120:e000::/40` → service, streaming
- `USER-AGENT,*bili*` → china, service
- `USER-AGENT,Bilibili*` → china, service
- `USER-AGENT,Microsoft*` → china, service
- `USER-AGENT,TikTok*` → china, social
- `USER-AGENT,bili*` → china, service
- `USER-AGENT,bili-inter*` → china, service
