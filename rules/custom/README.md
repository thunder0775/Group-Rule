# 自定义规则

这里用于放你自己的规则。

原则：

- 只写匹配规则，不写代理策略。
- 代理策略统一由 Shadowrocket `.conf` 决定。
- 推荐使用 `DOMAIN-SUFFIX`、`DOMAIN`、`DOMAIN-KEYWORD`、`IP-CIDR` 等。
- Actions 编译时会自动去重并合并到对应原子规则。
