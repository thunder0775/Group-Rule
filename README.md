# Group-Rule

自己的 Shadowrocket 规则中心：自动抓取、独立容错、审计、去重、冲突检测、编译发布。

## 核心原则

1. **规则与代理策略解耦**：`.list` 只包含匹配规则，不包含 `AI / DIRECT / PROXY / REJECT`。
2. **原子规则细分**：AI、流媒体、社交、开发、服务、国内、拦截分别维护。
3. **单源隔离**：某个远程源失败，只保留该原子规则的上一稳定版本，其余规则继续更新。
4. **自动审计**：检查 HTTP、HTML 错误页、空规则、过小文件、规则格式，并生成重复/冲突报告。
5. **自动编译**：同时生成原子规则与分类组合规则。
6. **小火箭只负责分流**：代理策略完全写在自己的 Shadowrocket 配置里。

## 小火箭订阅

使用 `config/shadowrocket.conf.example` 作为配置模板。规则文件中不包含代理策略；`AI / 🤖️ 优选 / DIRECT / REJECT` 全部由 Shadowrocket 配置定义。

## 自动更新

GitHub Actions 每天自动更新，也支持手动 `workflow_dispatch`。配置、脚本或规则源变更时会自动运行；生成内容无变化则不提交。

## 输出

- `rules/atomic/**`：细粒度规则
- `rules/compiled/**`：按类别合并后的规则
- `reports/latest.md`：人类可读审计报告
- `reports/latest.json`：机器可读审计数据

## 可靠性

更新采用“逐源、逐原子规则”容错机制。异常上游不会覆盖已知稳定文件；同一原子规则存在多个来源时，任一健康来源即可参与构建。

## 首次部署

仓库部署完成后，在 GitHub Actions 页面手动运行一次 **Update Shadowrocket Rules**，生成第一批远程规则文件。
