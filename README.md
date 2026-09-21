# Music Show Title Design

一个面向中文音综、MV 歌名和节目标题的 Codex Skill。它根据参考图生成多种字体方向、分层排版和真实透明背景的 PNG 标题素材。

## 安装

将整个仓库复制到个人 Skill 目录：

```bash
mkdir -p "$HOME/.agents/skills"
cp -R music-show-title-design "$HOME/.agents/skills/"
```

也可以在 Codex 中调用 `$skill-installer`，让它从本 GitHub 仓库安装。

如果安装后没有立即出现，请重启 Codex。

## 使用

在 Codex 中输入 `$music-show-title-design`，并提供：

- 中文标题；
- 英文标题（可选）；
- 艺人或署名（可选）；
- 一张或多张排版参考图；
- 需要的版本数量、画面比例和配色。

示例：

```text
$music-show-title-design
参考这张图的层次和节奏，为“夏夜未眠 / Sleepless Summer”设计六版 16:9 透明音综标题。
```

## 脚本依赖

`scripts/black_to_alpha.py` 用于把纯黑技术背景转换为真实透明通道，需要 Python 3、NumPy 和 Pillow：

```bash
python3 -m pip install -r requirements.txt
```

## 内容说明

- `SKILL.md`：Skill 的核心工作流与质量要求
- `references/style-directions.md`：字体与构图方向库
- `scripts/black_to_alpha.py`：透明通道转换脚本
- `agents/openai.yaml`：显示名称、简介与默认提示词

