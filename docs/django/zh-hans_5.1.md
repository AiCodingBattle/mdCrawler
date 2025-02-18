Django
The web framework for perfectionists with deadlines.
切换主题（当前主题：自动）
切换主题（当前主题：浅色）
切换主题（当前主题：深色）
Toggle Light / Dark / Auto color theme
Menu
  * Overview
  * Download
  * Documentation
  * News
  * Community
  * Code
  * Issues
  * About
  * ♥ Donate
  * 切换主题（当前主题：自动）
切换主题（当前主题：浅色）
切换主题（当前主题：深色）
Toggle Light / Dark / Auto color theme


# 文档
Search: 搜索
  * Getting Help


  * el
  * en
  * es
  * fr
  * id
  * it
  * ja
  * ko
  * pl
  * pt-br
  * 语言： **zh-hans**


  * 2.0
  * 2.1
  * 2.2
  * 3.0
  * 3.1
  * 3.2
  * 4.0
  * 4.1
  * 4.2
  * 5.0
  * dev
  * 文档版本： **5.1**


  * 

# Django 文档¶
你所需要知道的关于 Django 的一切。
## 快速入门¶
你是刚学 Django 或是初学编程？ 这就是你开始学习的地方！
  * **从零开始：** 概要 | 安装
  * **入门教程：** 第 1 节：请求和响应 | 第 2 节：模型和管理站点 | 第 3 节：视图和模板 | 第 4 节：表单和通用视图 | 第 5 节：测试 | 第 6 节：静态文件 | 第 7 节：自定义管理站点 | 第 8 节：添加第三方包
  * **进阶教程：** 如何编写可复用的应用 | 提交你的第一个 Django 贡献


## 获取帮助¶
遇到问题？我们可以帮你！
  * 试试 FAQ —— 这里有很多常见问题的解答。
  * 正在寻找特定的信息？试试 Index，Module Index 或者 详细内容目录。
  * 找不到解决方案？去 FAQ：获取帮助 找找更多的帮助信息，也可以向社区寻求帮助。
  * 在我们的 ticket tracker 报告关于 Django 的 Bug。


## 这份文档是如何组织的¶
Django 有丰富的文档。一份高度概述的文档会告诉你在哪里找到特定的东西：
  * 教程 通过一系列的步骤来带领你创建一个网页应用程序。如果你是 Django 或网页应用开发的新手，可以从这里开始。也可以看一下 “ 快速入门 ”。
  * 专题指南 在相当高的层次上介绍关键主题和概念，并提供有用的背景信息和解释。
  * 参考指南 包含 API 和 Django 各个工作机制方面的技术参考。它们介绍了 Django 是如何工作，如何被使用的。不过，你得先对关键字的概念有一定理解。
  * 操作指南 是一份目录。它们以排列好的关键问题和用例的方式指导你。它们比教程更加深入，且需要你先了解一些关于 Django 是如何工作的知识。


## 模型层¶
Django 提供了一个抽象的模型（“models”）层，用于结构化和操作你的网页应用程序的数据。阅读下面内容了解更多：
  * **模型：** 模型介绍 | 字段类型 | 索引 | Meta 选项 | Model 类
  * **QuerySet：** 执行查询 | QuerySet 方法参考 | 查询表达式
  * **模型实例：** 实例方法 | 访问关联的对象
  * **迁移：** 迁移概述 | 操作参考 | SchemaEditor | 编写迁移
  * **高级：** 管理器 | 原始 SQL | 事务 | 聚合 | 搜索 | 自定义字段 | 多个数据库 | 自定义查询 | 查询表达式 | 条件表达式 | 数据库函数
  * **其它：** 支持的数据库 | 旧数据库 | 提供初始化数据 | 优化数据库访问 | PostgreSQL 的特有功能


## 视图层¶
Django 具有 “视图” 的概念，负责处理用户的请求并返回响应。通过以下链接查找所有你需要知道的有关视图的信息：
  * **基础：** URL 配置 | 视图函数 | 便捷工具 | 装饰器 | 异步支持
  * **参考：** 内置视图 | 请求／响应对象 | TemplateResponse 对象
  * **文件上传：** 概览 | 文件对象 | 存储 API | 管理文件 | 自定义存储
  * **基于类的视图：** 概览 | 内置显示视图 | 内置编辑视图 | 使用混入 | API 参考 | 扁平化索引
  * **高级：** 生成 CSV | 生成 PDF
  * **中间件：** 概览 | 内建的中间件类


## 模板层¶
模板层提供了一个对设计者友好的语法用于渲染向用户呈现的信息。学习如何使用语法（面向设计者）以及如何扩展（面向程序员）：
  * **基础：** 概述
  * **对于设计者：** 语法概述 | 内建标签及过滤器 | 人性化
  * **对于开发者：** 模板 API | 自定义标签和过滤器 | 自定义模板后端


## 表单¶
Django 提供了一个丰富的框架来帮助创建表单和处理表单数据。
  * **基础：** 概览 | 表单 API | 内建字段 | 内建部件
  * **进阶：** 针对模型的表单 | 整合媒体 | 表单集 | 自定义验证


## 开发进程¶
学习众多的组件及工具，来帮助你开发和测试 Django 应用：
  * **设置：** 概览 | 完整的设置列表
  * **应用程序：** 概览
  * **异常：** 概览
  * **django-admin.py 和 manage.py：** 概览 | 添加自定义命令
  * **测试：** 介绍 | 书写并运行测试 | 包含的测试工具 | 高级主题
  * **部署：** 概述 | WSGI 服务器 | ASGI 服务器 | 部署静态文件 | 使用 email 追踪代码错误 | 部署检查清单


## 管理¶
找到所有你想知道的，关于自动化管理界面的知识，Django 最受欢迎的特性之一：
  * 管理站点
  * 管理动作
  * 管理文档生成器


## 安全¶
安全是网络应用程序开发中最重要的一个话题，Django 提供了多种保护工具和机制。
  * 安全概览
  * 在 Django 中披露的安全问题
  * 点击劫持保护
  * 跨站请求伪造 CSRF 保护
  * 登录加密
  * 安全中间件


## 国际化和本地化¶
Django 提供了一个强大的国际化和本地化的框架, 以帮助您在多语言和世界各地区进行应用程序的开发：
  * 概览 | 国际化 | 本地化 | 本地化的网页用户界面格式和表单输入
  * 时区


## 性能和优化¶
有各种各样的技术和工具，可以帮助你的代码的运行更高效，更快和使用更少的系统资源.
  * 性能和优化概述


## 地理框架¶
GeoDjango 旨在成为一个世界级的地理网络框架。它的目标是使建立 GIS 网页应用尽可能容易，并利用空间数据的力量。
## 常见的网络应用工具¶
Django 提供了网络应用程序开发中普遍需要的多种工具：
  * **认证：** 概述 | 使用认证系统 | 密码管理 | 自定义认证 | API 参考
  * 缓存
  * 日志
  * 发送邮件
  * 资讯聚合 (RSS/Atom)
  * 分页
  * 消息框架
  * 序列化
  * 会话
  * 站点地图
  * 静态文件管理
  * 数据验证


## 其它核心功能¶
了解更多 Django 框架的其他核心功能 :
  * 有条件的内容处理
  * 内容类型和通用关系
  * 简单页面
  * 重定向
  * 信号
  * 系统检查框架
  * 站点框架
  * Django 中的 Unicode


## Django 开源项目¶
了解 Django 项目本身的开发进程以及你如何为 Django 做贡献：
  * **社区：** 为 Django 做出贡献 | 发布进程 | 团队组织 | Django 源代码仓库 | 安全政策 | 邮件列表和论坛
  * **设计哲学：** 概览
  * **文档：** 关于本文档
  * **第三方发行：** 概览
  * **Django 时间线：** API 稳定性 | 发行说明和升级说明 | 过时时间表


Django 文档内容
开始 
Back to Top
# 附加信息
## Support Django!
![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)
  * South Shore Acupunture donated to the Django Software Foundation to support Django development. Donate today! 


## 浏览
  * 上一个： Django 文档内容
  * 下一个： 开始
  * 目录
  * General Index
  * Python Module Index


## 当前位置
  * Django 5.1 文档
    * Django 文档


## 获取帮助
FAQ
    尝试查看 FAQ — 它包括了很多常见问题的答案
索引, 模块索引, or 目录
    查找特定信息时比较容易
Django Discord Server
    Join the Django Discord Community.
Official Django Forum
    Join the community on the Django Forum.
Ticket tracker
    在我们的 `ticket tracker`_ 中报告 Django 或 Django 文档的 Bug。
## 下载：
离线 (Django 5.1): HTML | PDF | ePub 由 Read the Docs 提供。 
# Django Links
## Learn More
  * About Django
  * Getting Started with Django
  * Team Organization
  * Django Software Foundation
  * Code of Conduct
  * Diversity Statement


## Get Involved
  * Join a Group
  * Contribute to Django
  * Submit a Bug
  * Report a Security Issue
  * Individual membership


## Get Help
  * Getting Help FAQ
  * Django Discord
  * Official Django Forum


## Follow Us
  * GitHub
  * Twitter
  * Fediverse (Mastodon)
  * News RSS


## Support Us
  * Sponsor Django
  * Corporate membership
  * Official merchandise store
  * Benevity Workplace Giving Program


Django
  * Hosting by In-kind donors
  * Design by Threespot & andrevv


© 2005-2025  Django Software Foundation and individual contributors. Django is a registered trademark of the Django Software Foundation. 
