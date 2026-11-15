# 笔记仓库项目约定

## 修改后的提交与同步

用户要求：每次对笔记仓库做修改，都必须先提交并推送至远端，再通过拉取远端的方式同步到 iCloud。该流程适用于笔记、图片、索引和项目约定等仓库内容；日常提交、推送和拉取已获用户授权，无需逐次重复确认。

每次完成修改后，依次执行：

1. 检查修改内容，只暂存和提交本次任务相关文件，遵守已有忽略规则，保留其他未提交改动。
2. 在工作仓库创建说明清楚的 Git 提交，推送至远端 `origin`。默认分支为 `main`，用户另有指定时按其要求执行。
3. 推送成功后，进入 iCloud 仓库执行 `git pull --ff-only origin main`，通过远端同步本次提交；不以直接复制文件代替拉取。
4. 核对工作仓库、远端和 iCloud 仓库的提交是否一致，并检查两个本地仓库的状态。
5. 在最终回复中简要报告提交、推送及 iCloud 拉取的结果。某一步失败时继续处理能安全解决的问题，并明确说明尚未完成的环节，不把未推送或未拉取的修改报告为同步完成。

遇到远端新增提交、分叉、冲突或本地未提交改动时，先检查并保留已有内容，再采用安全方式整合；不得用强制推送、硬重置或清理命令覆盖用户改动。

## 仓库位置

- 工作仓库：`/Users/andyue/Library/CloudStorage/OneDrive-个人/文档/obsidian`
- 远端：`https://github.com/KayeAdams515/ClaudeNotes.git`
- 默认分支：`main`
- iCloud 仓库：`/Users/andyue/Library/Mobile Documents/iCloud~md~obsidian/Documents/ClaudeNotes`
