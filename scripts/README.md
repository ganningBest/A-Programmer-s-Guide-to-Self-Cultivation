# 脚本工具说明

## 🛠️ 可用脚本

### 1. `add_payment_qr.py` - 快速收款码设置 ⭐ 推荐

**功能：** 一键添加收款码并自动更新README

**使用方法：**
```bash
python scripts/add_payment_qr.py
```

**操作步骤：**
1. 运行脚本
2. 输入收款码图片路径
3. 脚本自动复制图片并更新README

### 2. `setup_payment.py` - 收款码设置助手

**功能：** 手动设置和检查收款码

**使用方法：**
```bash
python scripts/setup_payment.py
```

## 📋 收款码设置说明

### 准备工作
1. 获取您的支付宝收款码图片
2. 确保图片清晰可扫描
3. 建议图片大小 < 500KB

### 快速设置（推荐）
```bash
# 运行快速设置脚本
python scripts/add_payment_qr.py

# 按提示输入图片路径
# 脚本会自动完成所有设置
```

### 手动设置
1. 将收款码图片重命名为 `alipay-qr.jpg`
2. 放入 `assets/images/` 目录
3. 在README.md中替换占位符为：
   ```markdown
   ![支付宝收款码](assets/images/alipay-qr.jpg)
   ```

## ✅ 验证设置

设置完成后：
1. 检查 `assets/images/alipay-qr.jpg` 文件存在
2. 在README.md中查看收款码显示
3. 提交到Git并在GitHub上验证

## 🆘 常见问题

**Q: 图片不显示怎么办？**
A: 检查文件路径和文件名是否正确

**Q: 支持其他格式吗？**
A: 建议使用JPG格式，PNG也支持

**Q: 如何添加微信收款码？**
A: 类似步骤，文件名改为 `wechat-qr.jpg`
