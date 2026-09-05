# Group-Rule

自己的 Shadowrocket 规则中心：自动抓取、独立容错、审计、去重、冲突检测、语义检查、编译发布。

## 核心原则

1. **规则与代理策略解耦**：`.list` 只包含匹配规则，不包含 `AI / DIRECT / PROXY / REJECT`。
2. **原子规则细分**：AI、流媒体、社交、开发、服务、国内、拦截分别维护。
3. **单源隔离**：某个远程源失败，只保留该原子规则的上一稳定版本，其余规则继续更新。
4. **多源冗余**：同一原子规则可以配置多个上游；健康源并集进入原子规则，单个上游故障不会拖垮整体。
5. **自动健康审计**：检查 HTTP、HTML 错误页、规则数量骤降/暴增、无效规则比例、重定向主机变化。
6. **规则质量审计**：检查 DOMAIN、DOMAIN-SUFFIX、CIDR 的格式与语义，识别危险的短 `DOMAIN-KEYWORD`。
7. **跨分类裁决**：完全相同规则按 `config/priority.json` 自动保留最高优先级分类；原子文件不被改写。
8. **语义冗余只审计不盲删**：父域覆盖子域、父 CIDR 覆盖子网等情况进入报告，避免因为自动清理造成分流范围变化。
9. **编译输出自检**：生成后再次检查规则格式、策略泄漏、DOMAIN/CIDR 合法性。
10. **小火箭只负责分流**：代理策略完全写在自己的 Shadowrocket 配置里。

## 审计层级

`上游可用性 → 内容完整性 → 规则结构 → 规则语义 → 跨分类冲突 → 编译输出`

其中“源异常”会触发该原子规则的 Last Known Good；语义冗余目前只记录，不直接修改原子规则。

## 小火箭订阅

使用 `config/shadowrocket.conf.example` 作为配置模板。规则文件中不包含代理策略；`AI / ⚡ 优选 / DIRECT / REJECT` 全部由 Shadowrocket 配置定义。

## 自动更新

GitHub Actions 每天自动更新，也支持手动 `workflow_dispatch`。配置、脚本或规则源变更时会自动运行；生成内容无变化则不提交，并通过并发控制避免多个构建同时推送。

## 输出

- `rules/atomic/**`：细粒度、可独立审计的规则
- `rules/compiled/**`：按类别合并并完成精确冲突裁决的规则
- `reports/latest.md`：人类可读审计报告
- `reports/latest.json`：机器可读审计结果
- `reports/source-history.json`：上游 SHA/规则数历史，用于异常变化检测

## 健康阈值

在 `config/sources.json` 的 `health` 中统一控制：

- `min_rules`：单源最低有效规则数
- `min_rule_ratio`：相对历史规则数的最低保留比例
- `max_rule_ratio`：相对历史规则数的最高增长比例
- `max_invalid_ratio`：允许的无效行比例
- `max_audit_samples`：报告中保留的详细样本数量

单个源也可以覆盖这些阈值，不需要修改引擎代码。

## 首次部署

仓库部署完成后，在 GitHub Actions 页面手动运行一次 **Update Shadowrocket Rules**，生成第一批远程规则文件。
