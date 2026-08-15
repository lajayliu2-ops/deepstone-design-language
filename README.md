# Deepstone Design Language

当前团队试用版本：`v1.3.1`

这是 DeepStone 团队共用的 Codex Skill，用于按照统一的品牌设计语言制作或改版：

- HTML 页面
- Word 文档
- PowerPoint 演示文稿
- PDF 文件

## 团队成员如何安装

### 项目内使用（推荐）

1. 使用 GitHub Desktop 克隆本仓库。
2. 在 Codex 中打开克隆后的仓库文件夹。
3. Codex 会自动读取 `.agents/skills/deepstone-design-language/`。
4. 如果暂时没有显示，重新启动 Codex。

### 在所有项目中使用

把 `.agents/skills/deepstone-design-language/` 复制到个人目录：

```text
~/.agents/skills/deepstone-design-language/
```

然后重新启动 Codex。

## 使用示例

在 Codex 中直接描述任务，或者显式输入 `$deepstone-design-language`：

```text
用 $deepstone-design-language 把这份项目资料制作成一份中文客户提案 PPT。
```

```text
用 $deepstone-design-language 把这份 Word 报告改成 DeepStone 风格，并导出 PDF。
```

```text
用 $deepstone-design-language 根据这份自然语言需求制作一个响应式 HTML 页面。
```

HTML 任务会同时保留完整可编辑源文件夹，并生成一个已经内嵌本地字体、Logo、图片、CSS 和 JavaScript 的客户可转发文件，例如：

```text
Paneco_Valuation_Report_2026_DeepStone_Standalone.html
```

对客户或团队发送时优先使用这个命名好的 `*_DeepStone_Standalone.html`；`index.html` 只作为可编辑源文件保留。

## 目录说明

正式 Skill 位于：

```text
.agents/skills/deepstone-design-language/
```

其中包括品牌规则、设计令牌、字体、Logo、模板和辅助脚本。字体各自附带 SIL Open Font License 授权文件。

## 内部资料说明

DeepStone 名称、Logo、品牌模板和设计规范仅供获得授权的 DeepStone 团队成员及合作方使用。未经授权，请勿公开发布、转售或用于其他品牌。
