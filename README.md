# Embedded Map File Analyzer 📊

**一个轻量级 Python 工具，用于解析嵌入式 C 程序的 `.map` 文件，快速定位内存占用瓶颈，助力资源优化！**

---

## 🚀 功能特性
- **自动化解析**：提取 `.text`、`.data`、`.bss` 等关键段的内存使用数据
- **多编译器支持**：适配 GCC / IAR / Keil 等主流嵌入式工具链（需简单配置正则表达式）
- **模块级统计**：按代码模块（`.o` 文件）排序内存占用，快速定位"内存大户"
- **可视化报告**：支持生成终端表格或导出为 CSV/HTML（需安装 `matplotlib` 或 `pandas`）
- **轻量无依赖**：仅需 Python 3.6+，核心代码不足 100 行！

---

## 🛠️ 使用场景
- 嵌入式开发中排查 **Flash/RAM 溢出** 问题
- 评估代码优化（如函数内联、编译器选项调整）后的内存变化
- 开源项目或团队协作时，生成标准化内存报告

---

## 📥 安装与使用
```bash
# 1. 克隆仓库
git clone https://github.com/your_username/EmbMapAnalyzer.git

# 2. 运行脚本（示例）
python map_analyzer.py --input firmware.map --format console

# 📋输出示例

# 🔌支持编译器

# 🤝贡献指南
欢迎提交 Issue 或 PR：

适配新编译器：修改 regex_patterns.json 中的正则规则
扩展输出格式：添加 exporter_csv.py 或 exporter_html.py
优化性能：用 lark / pyparsing 重构解析逻辑

# 📜开源协议
MIT License - 自由使用，保留作者信息即可

立即尝试 → 让 .map 文件分析变得像 print("Hello World!") 一样简单！ 🚀
